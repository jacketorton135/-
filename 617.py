import serial
import time

# 设置串口参数
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # 修改为你的串口名称, 如 /dev/ttyUSB0, /dev/ttyACM0 或 COM3

def read_from_arduino():
    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    time.sleep(2)  # 等待串口稳定
    print("Starting to read from Arduino...")
    read_from_arduino()

    ser.close()  # 关闭串口
