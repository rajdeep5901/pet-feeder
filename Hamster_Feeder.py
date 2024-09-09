# Import libraries
import RPi.GPIO as GPIO
import time
import datetime

GPIO.setwarnings(False)

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pins 11 & 12 as outputs, and define as PWM servo1 & servo2
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1
GPIO.setup(12,GPIO.OUT)
servo2 = GPIO.PWM(12,50) # pin 12 for servo2

# Start PWM running on both servos, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

#Wait for used to press ENTER
dummy = input('Close pod bay door 1 & press ENTER: ')

# Turn servo1 to 105 (closed position: 105/18 +2 = 7.83)
servo1.ChangeDutyCycle(7.83)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# set variable pod1 to 1 (closed)
pod1 = 1

#Wait for used to press ENTER
dummy = input('Close pod bay door 2 & press ENTER: ')

# Turn servo2 to 105 (closed position: 105/18 +2 = 7.83)
servo2.ChangeDutyCycle(7.83)
time.sleep(0.5)
servo2.ChangeDutyCycle(0)

# set variable pod 2 to be value of 1 (closed)
pod2 = 1

print ("Load the pod bays. Nuts will release as programmed.")

try:
    while pod2 == 1:
        now = datetime.datetime.now() # get current date and time
        if now.month==5 and now.day==19 and now.hour==11 and now.minute==15 and pod1==1:
            print ("Opening Pod 1")
            servo1.ChangeDutyCycle(2) #set angle to 0 degrees (open)
            time.sleep(0.5)
            servo1.ChangeDutyCycle(0)
            pod1 = 0 #set value to open
            servo1.stop() #stop the servo - no longer needed
        elif now.month==5 and now.day==19 and now.hour==11 and now.minute==15 and pod2==1:
            print ("Opening Pod 2")
            servo2.ChangeDutyCycle(2) #set value to 0 degrees (open)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(0)
            pod2 = 0 #set value to open
            servo2.stop() #stop the servo - no longer needed
        time.sleep(1) # pause to lower CPU activity

except KeyboardInterrupt:
    print("Keyboard Interrupt detected. Exiting program.")
    
finally:
    #Clean things up at the end
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()
    print("Goodbye!")
    