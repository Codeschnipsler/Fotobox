#!/usr/bin/python

import RPi.GPIO as GPIO, time, os, subprocess
import os

counter=0

# GPIO setup
GPIO.setmode(GPIO.BCM)
SWITCH = 24
GPIO.setup(SWITCH, GPIO.IN)
RESET = 25
GPIO.setup(RESET, GPIO.IN)
PRINT_LED = 22
POSE_LED = 18
BUTTON_LED = 23
GPIO.setup(POSE_LED, GPIO.OUT)
GPIO.setup(BUTTON_LED, GPIO.OUT)
GPIO.setup(PRINT_LED, GPIO.OUT)
GPIO.output(BUTTON_LED, True)
GPIO.output(PRINT_LED, False)

#os.system("/home/pi/scripts/photobooth/script_instructions"
try:
    while True:
      if (GPIO.input(SWITCH)):
        snap = 0
        while snap < 4:
          print("pose!")
          GPIO.output(BUTTON_LED, False)
          GPIO.output(POSE_LED, True)
          time.sleep(0.1)
          for i in range(5):
            GPIO.output(POSE_LED, False)
            time.sleep(0.1)
            GPIO.output(POSE_LED, True)
            time.sleep(0.1)
          for i in range(2):
            GPIO.output(POSE_LED, False)
            time.sleep(0.1)
            GPIO.output(POSE_LED, True)
            time.sleep(0.1)
          GPIO.output(POSE_LED, False)
          print("SNAP")
          gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename /home/pi$
          print(gpout)
          if "ERROR" not in gpout: 
            snap += 1 
            os.system("/home/pi/scripts/photobooth/script_slideshow")

          GPIO.output(POSE_LED, False)
          time.sleep(0.1)
        print("please wait while your photos print...")
        GPIO.output(PRINT_LED, True)
        # build image and send to printer
        
    	os.system("/home/pi/scripts/photobooth/cloze_FEH")

        subprocess.call("sudo /home/pi/scripts/photobooth/assemble_and_print", shell=True)
        os.system("/home/pi/scripts/photobooth/script_slideshow_all")
        # TODO: implement a reboot button
        # Wait to ensure that print queue doesn't pile up

        time.sleep(10)
        counter +=1
        print("ready for next round")
        GPIO.output(PRINT_LED, False)
        GPIO.output(BUTTON_LED, True)

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print "\n", counter # print value of counter  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print "Other error or exception occurred!"  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit  

