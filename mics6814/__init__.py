import ioexpander as io


__version__ = '0.0.2'

MICS6814_I2C_ADDR = 0x19

MICS6814_LED_R = 3  # P1.2
MICS6814_LED_G = 7  # P1.1
MICS6814_LED_B = 2  # P1.0

MICS6814_VREF = 14  # P1.4 AIN0 - 3v3
MICS6814_RED = 13   # P0.7 AIN2 - Reducing
MICS6814_NH3 = 11   # P0.6 AIN3 - NH3
MICS6814_OX = 12    # P0.5 AIN4 - Oxidizing

MICS6814_HEATER_EN = 1  # P1.5 Heater Enable


class Mics6814Reading(object):
    __slots__ = 'oxidising', 'reducing', 'nh3', 'adc'

    def __init__(self, ox, red, nh3, adc=None):
        self.oxidising = ox
        self.reducing = red
        self.nh3 = nh3
        self.adc = adc

    def __repr__(self):
        fmt = """Oxidising: {ox:05.02f} Ohms
Reducing: {red:05.02f} Ohms
NH3: {nh3:05.02f} Ohms"""
        if self.adc is not None:
            fmt += """
ADC (ref): {adc:05.02f} Volts
"""
        return fmt.format(
            ox=self.oxidising,
            red=self.reducing,
            nh3=self.nh3,
            adc=self.adc)

    __str__ = __repr__


class MICS6814():
    def __init__(self, i2c_addr=MICS6814_I2C_ADDR, interrupt_timeout=1.0, interrupt_pin=None, gpio=None):
        self._ioe = io.IOE(i2c_addr, interrupt_timeout, interrupt_pin, gpio)

        self._chip_id = self._ioe.get_chip_id()

        # TODO - Validate CHIP ID

        self.set_pwm_period(5100)
        self._ioe.set_pwm_control(divider=1)

        self.set_brightness(1.0)
        self._ioe.set_mode(MICS6814_LED_R, io.PWM)   # P1.2 LED Red
        self._ioe.set_mode(MICS6814_LED_G, io.PWM)   # P1.1 LED Green
        self._ioe.set_mode(MICS6814_LED_B, io.PWM)   # P1.0 LED Blue

        self._ioe.set_mode(MICS6814_VREF, io.ADC)    # P1.4 AIN5 - 2v8
        self._ioe.set_mode(MICS6814_RED, io.ADC)     # P0.5 AIN4 - Red
        self._ioe.set_mode(MICS6814_NH3, io.ADC)     # P0.6 AIN3 - NH3
        self._ioe.set_mode(MICS6814_OX, io.ADC)      # P0.7 AIN2 - OX

        self._ioe.set_mode(MICS6814_HEATER_EN, io.OUT)   # P1.5 Heater Enable
        self._ioe.output(MICS6814_HEATER_EN, io.LOW)

    def set_brightness(self, brightness):
        """Set the LED brightness.

        :param brightness: From 0.0 to 1.0

        """
        self.brightness = brightness

    def set_pwm_period(self, value):
        """Set the LED PWM period.

        :param value: PWM period from 255 to 65535

        """
        self.pwm_period = value
        self._ioe.set_pwm_period(value)

    def set_heater(self, value):
        """Set the status of the gas heater.

        :param value: Heater on/off (True/False)

        """
        self._ioe.output(1, io.LOW if value else io.HIGH)

    def disable_heater(self):
        """Disable the gas heater."""
        self._ioe.output(MICS6814_HEATER_EN, io.HIGH)
        self._ioe.set_mode(MICS6814_HEATER_EN, io.IN)

    def get_raw_ref(self):
        """Return raw reference ADC reading."""
        return self._ioe.input(MICS6814_VREF)

    def get_raw_red(self):
        """Return raw Reducing Gasses reading."""
        return self._ioe.input(MICS6814_RED)

    def get_raw_nh3(self):
        """Return raw NH3 ADC reading."""
        return self._ioe.input(MICS6814_NH3)

    def get_raw_oxd(self):
        """Return raw Oxidizing Gasses ADC reading."""
        return self._ioe.input(MICS6814_OX)

    def set_led(self, r, g, b):
        """Set onboard LED to RGB value.

        :param r: Amount of Red (0-255)
        :param g: Amount of Green (0-255)
        :param b: Amount of Blue (0-255)

        """
        r = self.pwm_period - (r * self.pwm_period / 255.0 * self.brightness)
        g = self.pwm_period - (g * self.pwm_period / 255.0 * self.brightness)
        b = self.pwm_period - (b * self.pwm_period / 255.0 * self.brightness)
        self._ioe.output(MICS6814_LED_R, int(r))
        self._ioe.output(MICS6814_LED_G, int(g))
        self._ioe.output(MICS6814_LED_B, int(b))

    def read_all(self):
        """Return gas resistance for oxidising, reducing and NH3"""
        ref = self.get_raw_ref()
        red = self.get_raw_red()
        nh3 = self.get_raw_nh3()
        oxd = self.get_raw_oxd()

        vref = self._ioe.get_adc_vref()

        try:
            red = (red * 56000) / (vref - red)
        except ZeroDivisionError:
            red = 0

        try:
            nh3 = (nh3 * 56000) / (vref - nh3)
        except ZeroDivisionError:
            nh3 = 0

        try:
            oxd = (oxd * 56000) / (vref - oxd)
        except ZeroDivisionError:
            oxd = 0

        return Mics6814Reading(oxd, red, nh3, ref)

    def read_oxidising(self):
        """Return gas resistance for oxidising gases.
        Eg chlorine, nitrous oxide
        """
        return self.read_all().oxidising

    def read_reducing(self):
        """Return gas resistance for reducing gases.
        Eg hydrogen, carbon monoxide
        """
        return self.read_all().reducing

    def read_nh3(self):
        """Return gas resistance for nh3/ammonia"""
        return self.read_all().nh3

    def read_adc(self):
        """Return spare ADC channel value"""
        return self.read_all().adc
