#!/usr/bin/python

import subprocess
import os
from gpiozero import Button,LED
from signal import pause
from time import sleep
from subprocess import check_call


SWITCH = Button(24)
RESET = Button(17)
SHUT = Button(3)

PRINT_LED = LED(22)
POSE_LED = LED(18)
BUTTON_LED = LED(23)

def def_SHUT():
            PRINT_LED.on()
            sleep(0.1)
            PRINT_LED.off()
            sleep(0.1)
            PRINT_LED.on()
            sleep(0.1)
            PRINT_LED.off()
            sleep(0.1)
            os.system("sudo shutdown -h now")  #shutdown now
def def_RESET():
            PRINT_LED.on()
            sleep(0.1)
            PRINT_LED.off()
            sleep(0.1)
            POSE_LED.on()
            sleep(0.1)
            POSE_LED.off()
            sleep(0.1)
            os.system("sudo reboot")     #reboot

def def_SWITCH():
            snap = 0
            while snap < 4:
              print("pose!")
              BUTTON_LED.off()
              POSE_LED.on()
              sleep(1.5)
              for i in range(5):
                POSE_LED.off()
                sleep(0.1)
                POSE_LED.on()
                sleep(0.1)
              for i in range(2):
                POSE_LED.off()
                sleep(0.1)
                POSE_LED.on()
                sleep(0.1)
              POSE_LED.off()
              print("SNAP")
              gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename /home/pi/photobooth_images/photobooth%H%M%S.$
              print(gpout)
              if "ERROR" not in gpout:
                snap += 1
              os.system("/home/pi/scripts/photobooth/script_slideshow")
              POSE_LED.off()
              sleep(0.5)
            print("please wait while your photos print...")
            PRINT_LED.on()
            #stop slideshow
            os.system("/home/pi/scripts/photobooth/cloze_FEH")
            # build image and send to printer
            subprocess.call("sudo /home/pi/scripts/photobooth/assemble_and_print", shell=True)
            #start new slideshow with all pics
            os.system("/home/pi/scripts/photobooth/script_slideshow_all")
            sleep(10)
            print("ready for next round")
            PRINT_LED.off()
            BUTTON_LED.on()

BUTTON_LED.on()
SHUT.when_pressed = def_SHUT
RESET.when_pressed = def_RESET
SWITCH.when_pressed = def_SWITCH

pause()