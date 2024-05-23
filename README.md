# MICS6814 Breakout Garden Breakout

[![Build Status](https://img.shields.io/github/actions/workflow/status/pimoroni/mics6814-python/test.yml?branch=main)](https://github.com/pimoroni/mics6814-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/mics6814-python/badge.svg?branch=main)](https://coveralls.io/github/pimoroni/mics6814-python?branch=main)
[![PyPi Package](https://img.shields.io/pypi/v/pimoroni-mics6814.svg)](https://pypi.python.org/pypi/pimoroni-mics6814)
[![Python Versions](https://img.shields.io/pypi/pyversions/pimoroni-mics6814.svg)](https://pypi.python.org/pypi/pimoroni-mics6814)

## Installing

### Pre-requisites

You must enable i2c:

* i2c: `sudo raspi-config nonint do_i2c 0`

You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your BH1745
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

Stable library and dependencies from GitHub:

* `git clone https://github.com/pimoroni/mics6814-python`
* `cd mics6814-python`
* `sudo ./install.sh`

Latest/development library and dependencies from GitHub:

* `git clone https://github.com/pimoroni/mics6814-python`
* `cd mics6814-python`
* `sudo ./install.sh --unstable`

**Note** Libraries will be installed in the "pimoroni" virtual environment, you will need to activate it to run examples:

```
source ~/.virtualenvs/pimoroni/bin/activate
```

### Stable (library only) from PyPi:

* In your Python Virtual Environment, run `pip install pimoroni-mics6814`
