# MICS6814 Breakout Garden Breakout

[![Build Status](https://shields.io/github/workflow/status/pimoroni/mics6814-python/Python%20Tests)](https://github.com/pimoroni/mics6814-python/actions)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/mics6814-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/mics6814-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/pimoroni-mics6814.svg)](https://pypi.python.org/pypi/pimoroni-mics6814)
[![Python Versions](https://img.shields.io/pypi/pyversions/pimoroni-mics6814.svg)](https://pypi.python.org/pypi/pimoroni-mics6814)

# Pre-requisites

You must enable i2c:

* i2c: `sudo raspi-config nonint do_i2c 0`

You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.

# Installing

Stable library and dependencies from GitHub:

* `git clone https://github.com/pimoroni/mics6814-python`
* `cd mics6814-python`
* `sudo ./install.sh`

Latest/development library and dependencies from GitHub:

* `git clone https://github.com/pimoroni/mics6814-python`
* `cd mics6814-python`
* `sudo ./install.sh --unstable`

Stable (library only) from PyPi:

* Just run `sudo pip3 install pimoroni-mics6814`

# Changelog
0.0.1
-----

* Initial Release
