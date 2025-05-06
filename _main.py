try:
    from tinyml import TinyML
    from mpu6500 import MPU6500, I2C_NO
except ImportError:
    from usr.tinyml import TinyML
    from usr.mpu6500 import MPU6500, I2C_NO

import _thread
import utime

tinyml = TinyML(50, 5)

mpu6500 = MPU6500(I2C_NO)

def read():

    while True:
        acc = mpu6500.acceleration()

        gyro = mpu6500.gyro()

        print('acc_x: {}, acc_y: {}, acc_z: {}, gyro_x: {}, gyro_y: {}'.format(acc[0], acc[1], acc[2], gyro[0], gyro[1]))

        tinyml.collect([acc[0], acc[1], acc[2]], [gyro[1], gyro[2]])
        utime.sleep_ms(10)

def score():
    while True:
        score = tinyml.score()
        if score:
            print("***************************^-^***************************score:", score)
        utime.sleep_ms(200)

def read_sensor():
    _thread.stack_size(4*1024)
    _thread.start_new_thread(read, ())

def run_score():
    _thread.stack_size(2*1024)
    _thread.start_new_thread(score, ())


if __name__ == '__main__':
    read_sensor()
    run_score()
