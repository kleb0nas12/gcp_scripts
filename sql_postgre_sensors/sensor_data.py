from gpiozero import CPUTemperature
from postgre import DbOperations
from datetime import datetime
import Adafruit_DHT
import time
import glob
import os


class MainOperation:
    def __init__(self):
        #self.DB = DbOperations()
        self.cpu_t = CPUTemperature()
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 18

    def _get_cput(self) -> float:
        return round(self.cpu_t.temperature, 1)

    def _get_out_temp_hum(self) -> list:
        humidity, temp = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
        return [round(humidity, 2), round(temp, 2)]

    def _get_cam_temperature(self) -> float:
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        device_file = device_folder + '/w1_slave'

        def _read_temp_raw():
            f = open(device_file, 'r')
            lines = f.readlines()
            f.close()
            return lines

        def _read_temp():
            lines = _read_temp_raw()
            while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = _read_temp_raw()
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                return temp_c
        return _read_temp()


#if __name__ == '__main__':
print('Hi')
op = MainOperation()
db = DbOperations()
print('Hi')
while True:
    print('...Starting process...')
    _time = datetime.strftime(datetime.now(),'%H:%M:%S')
    CPU_TEMP = op._get_cput()
    OUT_HUM, OUT_TEMP = op._get_out_temp_hum()
    CAM_TEMP = op._get_cam_temperature()
    print('CPU temp: {}C, Camera temp: {}C, Outside temperature: {}C, Outside humidity: {}%'.format(
            CPU_TEMP, CAM_TEMP, OUT_TEMP, OUT_HUM))
    db.omit_data(_time,CPU_TEMP,CAM_TEMP,OUT_TEMP, OUT_HUM)
    time.sleep(2)