Earth Signal Universe Wide - Seismographic Data Client
========================

# Dev Diary:

## obspy
Started from:
`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.
Used this to setup the environment:
[https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/]()

## Data from Ran
82.102.143.63:18000
network: IS
station: DSI
location: 22
Channel: HH[ENZ]

## Debug with slinktool

Ran
`./slinktool -v -S IS_DS
I:22ENZ 82.102.143.63:18000`

## With obspy
* Had to change the requirements.txt to install on debian (scipy was causing issues)
* Used my GsiClient 
* ran `select_stream('IS', 'DSI', 'ENZ')` and after `run()` I got results!


---------------
The original repo format left this here:

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.
