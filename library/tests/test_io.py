import mock


def test_set_heater(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()

    mics6814.set_heater(True)
    mics6814._ioe.output.assert_called_with(1, ioexpander.LOW)

    mics6814.set_heater(False)
    mics6814._ioe.output.assert_called_with(1, ioexpander.HIGH)


def test_disable_heater(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()

    mics6814.disable_heater()
    mics6814._ioe.output.assert_called_with(1, ioexpander.HIGH)
    mics6814._ioe.set_mode.assert_called_with(1, ioexpander.IN)


def test_get_raw_ref(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()

    mics6814.get_raw_ref()
    mics6814._ioe.input.assert_called_with(14)


def test_get_raw_red(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()

    mics6814.get_raw_red()
    mics6814._ioe.input.assert_called_with(13)


def test_get_raw_nh3(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()

    mics6814.get_raw_nh3()
    mics6814._ioe.input.assert_called_with(11)


def test_get_raw_oxd(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()

    mics6814.get_raw_oxd()
    mics6814._ioe.input.assert_called_with(12)


def test_get_adc(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()

    mics6814.read_adc()


def test_read_all(ioexpander):
    from mics6814 import MICS6814, Mics6814Reading

    mics6814 = MICS6814()

    mics6814._ioe.input.return_value = 2.5
    mics6814._ioe.get_adc_vref.return_value = 5.0

    reading = mics6814.read_all()

    assert type(reading) == Mics6814Reading
    mics6814._ioe.input.has_calls((
        mock.call(9),
        mock.call(12),
        mock.call(11),
        mock.call(13),
    ))

    assert "Oxidising" in str(reading)


def test_read_oxd_red_nh3(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()

    mics6814._ioe.input.return_value = 2.5
    mics6814._ioe.get_adc_vref.return_value = 5.0

    assert mics6814.read_oxidising() == 56000.0
    assert mics6814.read_reducing() == 56000.0
    assert mics6814.read_nh3() == 56000.0


def test_read_oxd_red_nh3_zero_division(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()

    mics6814._ioe.input.return_value = 5.0
    mics6814._ioe.get_adc_vref.return_value = 5.0

    assert mics6814.read_oxidising() == 0
    assert mics6814.read_reducing() == 0
    assert mics6814.read_nh3() == 0


def test_set_led(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()
    mics6814.set_led(255, 155, 55)

    assert mics6814._ioe.output.has_calls((
        mock.call(3, 255),
        mock.call(7, 155),
        mock.call(2, 55)
    ))
