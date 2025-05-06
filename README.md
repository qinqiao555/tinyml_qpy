# TinyML for QuecPython

## Directory Structure

```plaintext
tinyml_qpy/
├── _main.py/
├── mpu6500.py/
├── random_forest.py
├── tinyml.py
└── readme.md
```

`mpu6500.py` -  mpu6500 sensor driver code;

`random_forest.py` - Random Forest Algorithm;

`tinyml.py` - TinyML Utils.

## Current progress

The current program can run normally, but the sensor driver is not adjusted properly or the random forest algorithm is inaccurate, resulting in the acquisition of data into the random forest algorithm can not get the target result. For example: along the X axis of the sensor movement, the program does not return the corresponding result.

You can refer to this documentation: [TinyML: Machine Learning on ESP32 with MicroPython - DEV Communit](https://dev.to/tkeyo/tinyml-machine-learning-on-esp32-with-micropython-38a6) and this github repository: [tkeyo/tinyml-esp: Machine Learning on ESP32 with MicroPython and standard ML algorithms to detect gestures from time-series data.](https://github.com/tkeyo/tinyml-esp)