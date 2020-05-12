# Reference <!-- omit in toc -->

- [Getting Started](#getting-started)
  - [Installing](#installing)
- [Examples](#examples)
  - [Example](#example)
- [Function Reference](#function-reference)
  - [set_header](#set_header)
  - [set_led](#set_led)
  - [set_brightness](#set_brightness)
  - [set_pwm_period](#set_pwm_period)
  - [read_all](#read_all)
  - [read_oxidising](#read_oxidising)
  - [read_reducing](#read_reducing)
  - [read_nh3](#read_nh3)
  - [read_adc](#read_adc)
  - [get_raw_ref](#get_raw_ref)
  - [get_raw_red](#get_raw_red)
  - [get_raw_nh3](#get_raw_nh3)
  - [get_raw_oxd](#get_raw_oxd)
  - [disable_heater](#disable_heater)


## Getting Started

Most people should grab the library from GitHub and run our simple installer:

### Installing

```
git clone https://github.com/pimoroni/mics6814-python
cd mics6814-python
sudo ./install.sh
```

This ensures any dependencies are installed and will copy examples into `~/Pimoroni/mics6814/`

You can install just the mics6814 library by running:

```
sudo pip3 install mics6814
```

## Examples

### Example
[example.py](examples/example.py)

Example description.


## Function Reference

In all cases you'll first need to initialise a MICS6814 library instance with the specific I2C address for each driver you're using.

```python
from mics6814 import MICS6814

mics6814 = MICS6814()
```

### set_header

```python
mics6814.set_heater(value)
```

Turn the gas heater on/off. Heater should be on to take gas measurements.

### set_led

```python
mics6814.set_led(red, green, blue)
```

Set the onboard indicator LED.

Red, green and blue values should be a number from 0-255.

### set_brightness

```python
mics6814.set_brightness(brightness)
```

Set the brightness of the breakout LEDs. This scales the PWM duty cycle for all LED channels (Red, Green & Blue).

Valid values range from 0 (off) to 1.0 (full brightness) and the on period of the LED is equal to:

```python
pwm_period - (colour_brightness * pwm_period / 255.0 * brightness)
```

### set_pwm_period

```python
mics6814.set_pwm_period(value)
```

Set the PWM period of the breakout LEDs.

Valid values range from 255 (the minimum period required for full colour fidelity at full brightness) to 65535 and offer LED PWM frequencies from around 94KHz to 366Hz.

### read_all

```python
readings = mics6814.read_all()
```

Read gas resistances for oxidizing, reducing and NH3. All resistances are scaled against the reference voltage.

Returns a Mics6814Reading namedtuple with ox, red, nh3 and adc properties.

### read_oxidising

```python
ox = mics6814.read_oxidising()
```

Returns the value of ox from `mics6814.read_all()`

### read_reducing

```python
ox = mics6814.read_reducing()
```

Returns the value of red from `mics6814.read_all()`

### read_nh3

```python
ox = mics6814.read_nh3()
```

Returns the value of nh3 from `mics6814.read_all()`

### read_adc

```python
ox = mics6814.read_adc()
```

Returns the value of adc from `mics6814.read_all()`

### get_raw_ref

```python
ref = mics6814.get_raw_ref()
```

Return the raw reference ADC reading.

### get_raw_red

```python
red = mics6814.get_raw_red()
```

Return the raw reducing gasses ADC reading.

### get_raw_nh3

```python
nh3 = mics6814.get_raw_nh3()
```

Return the raw NH3 ADC reading.

### get_raw_oxd

```python
oxd = mics6814.get_raw_oxd()
```

Return the raw oxidizing gasses ADC reading.

### disable_heater

```python
mics6814.disable_heater()
```

Disable the IO pin connected to the heater.
