import RPi.GPIO as GPIO # type: ignore
import board # type: ignore
import busio # type: ignore
import adafruit_ads1x15.ads1115 as ADS # type: ignore
from adafruit_ads1x15.analog_in import AnalogIn # type: ignore
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

battery1 = 0
battery2 = 0
battery3 = 0
battery4 = 0
relay1 = 4
relay2 = 17
relay3 = 27
relay4 = 22
adc0 = AnalogIn(ads, ADS.P0)
adc1 = AnalogIn(ads, ADS.P1)
adc2 = AnalogIn(ads, ADS.P2)
adc3 = AnalogIn(ads, ADS.P3)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)

if adc0 * 0.0293255 > 16 and (battery2 == 0 and battery3 == 0 and battery4 == 0):
        GPIO.output(relay1, GPIO.HIGH)
        battery1 = 1
else: 
    GPIO.output(relay1, GPIO.LOW)
    battery1 = 0
  
if adc1 * 0.0293255 > 16 and (battery1 == 0 and battery3 == 0 and battery4 == 0):
        GPIO.output(relay2, GPIO.HIGH)
        battery2 = 1
else: 
    GPIO.output(relay2, GPIO.LOW)
    battery2 = 0

if adc2 * 0.0293255 > 16 and (battery1 == 0 and battery2 == 0 and battery4 == 0):
        GPIO.output(relay3, GPIO.HIGH)
        battery3 = 1
else: 
    GPIO.output(relay3, GPIO.LOW)
    battery3 = 0

if adc0 * 0.0293255 > 16 and (battery1 == 0 and battery2 == 0 and battery3 == 0):
        GPIO.output(relay4, GPIO.HIGH)
        battery1 = 1
else: 
    GPIO.output(relay4, GPIO.LOW)
    battery4 = 0

print(battery1)
print(battery2)
print(battery3)
print(battery4)
print(adc0)
print(adc1)
print(adc2)
print(adc3)
GPIO.cleanup()


#https://discord.com/channels/536623076796923924/536623076796923928/1389602042527613050
#https://discord.com/channels/536623076796923924/536623076796923928/1389602647564226591