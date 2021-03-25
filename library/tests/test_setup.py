import mock


def test_setup(ioexpander):
    from mics6814 import MICS6814

    mics6814 = MICS6814()

    mics6814._ioe.set_pwm_period.assert_called_once_with(5100)
    mics6814._ioe.set_mode.assert_has_calls((
        mock.call(3, ioexpander.PWM),
        mock.call(7, ioexpander.PWM),
        mock.call(2, ioexpander.PWM),

        mock.call(14, ioexpander.ADC),
        mock.call(12, ioexpander.ADC),
        mock.call(11, ioexpander.ADC),
        mock.call(13, ioexpander.ADC),

        mock.call(1, ioexpander.OUT)
    ))
    mics6814._ioe.output.assert_called_once_with(1, ioexpander.LOW)

    del mics6814
