#include "hardware/i2c.h"

#define I2C_PORT i2c0
#define I2C_SDA 0
#define I2C_SCL 1

// Trecho do sensor mp6050
void mpu6050_reset();
void mpu6050_read_raw(int16_t accel[3], int16_t gyro[3]);
// fim do trecho mppu6050