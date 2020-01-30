import RPi.GPIO as GPIO
import lcd_i2c
import time
import numpy
GPIO.setmode(GPIO.BCM)

servoPIN = 22
GPIO.setup(servoPIN, GPIO.OUT)

def setupLCD():
    lcd_i2c.lcd_init();

def printLCD(string1, string2):
    lcd_i2c.printer(string1,string2);


p = GPIO.PWM(servoPIN, 50) # GPIO 22 is set for PWM with 50Hz

p.start(2.5) # Initialization

try:
    setupLCD();
    printLCD("Servo will now ", "begin");
    while True:
        time.sleep(1);
        printLCD("Going,", "Counterclockwise");
        for dutyCycle in numpy.arange (2.5,12,0.25): #gives evenlu spaced non-integer values within the range
            p.ChangeDutyCycle(dutyCycle);
            time.sleep(0.025);
        time.sleep(1);
        printLCD("Going,","Clockwise");
        for dutyCycle in numpy.arange (12,2.5,-0.25):
            p.ChangeDutyCycle(dutyCycle);
            time.sleep(0.025);

except KeyboardInterrupt:
    p.stop()
    print("Cleaning up!");
    lcd_i2c.cleanup();
    GPIO.cleanup()
