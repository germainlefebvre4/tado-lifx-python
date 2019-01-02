# Turn off your lights'home when you are away

Objective: Use already apps installed to integrate automation.

Inputs:
* Tado Smart Thermostat
* Lifx Bulbs

Ouputs:
* Turn off the lights

Conditions:
* Your are away (home)

## Getting started
```
pipenv run python3 main.py
```

## Pre-requisite
Python libraries:
```
pipenv install requests yamlsettings six
```
Tado library at [https://github.com/germainlefebvre4/libtado](https://github.com/germainlefebvre4/libtado)

## Configuration
Provides your Tado credentials:
* Username: Usually your email address
* Password: The password matching your email
* Client secret: Value provided at login in headers response (use <F12> to enable developer mode)
and you Lifx credentials:
* Token: Generated token at [https://cloud.lifx.com/settings](https://cloud.lifx.com/settings)
