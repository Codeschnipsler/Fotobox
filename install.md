### original source https://www.instructables.com/id/Raspberry-Pi-photo-booth-controller/

1) Update the system:

                sudo apt-get update

2) Download and run this script, which installs and updates gphoto2: https://github.com/gonzalo/gphoto2-updater/

                sudo wget raw.github.com/gonzalo/gphoto2-updater/master/gphoto2-updater.sh
                sudo chmod 755 gphoto2-updater.sh
                sudo ./gphoto2-updater.sh

3) To ensure your camera mounts properly to be controlled via USB (see this thread), remove these files: (not always needed)

                sudo rm /usr/share/dbus-1/services/org.gtk.Private.GPhoto2VolumeMonitor.service
                sudo rm /usr/share/gvfs/mounts/gphoto2.mount
                sudo rm /usr/share/gvfs/remote-volume-monitors/gphoto2.monitor
                sudo rm /usr/lib/gvfs/gvfs-gphoto2-volume-monitor

4) Restart

                sudo shutdown -r 0

5) Attach your camera to the RPi with USB and test it out

                ls
                gphoto2 --capture-image-and-download
                ls

Use CUPS to drive the printer. You can check to see if CUPS supports a particular printer. The Canon Selphy CP-900 is not on that list. I got it working using the SELPHY-CP770 driver (this was the lucky part), which, though it was available through the actual CUPS installation, I do not see on the list linked to above (as of Feb 2014).

1. Install CUPS from the RPi command line (for further guidance/troubleshooting, see here)

                sudo apt-get install cups

Add the user (pi) to the group allowed to print (lpadmin)

                sudo usermod -a -G lpadmin pi


2. Connect your printer and setup CUPS from the RPi desktop
Attach to the RPi by USB and power up your printer.

Open Midori and type into the URL line
http://127.0.0.1:631
This will open up the CUPS setup.

Click "administration" and "add printer;" enter your username and password (e.g., the defaults "pi" and "raspberry").

You should see your printer listed under "local printer;" select it and click "continue."

Set the name and location of your printer as you like, and click "continue."

I also had to install hplip-gui in order to receive the printer in the list that I intended to use _ 

Hardware
https://cdn.instructables.com/FP9/LHV6/HSE92TJ7/FP9LHV6HSE92TJ7.LARGE.jpg

                GPIO17(3,3 V) to Button (grey)
                BCM18 to green LED, then 330OHM resistor, connect to ground (blue)
                GPIO14(GND) as ground (green)
                BCM23 to LED in Arcade button (yellow)
                BCM24 as input from button (orange)
                BCM22 to red LED, then 330Ohm resistor connect to ground (red)

                                GPIO17(3,3 V)       
                                     |  
                                  Button
                BCM24 -o-- 1kOhm --- | --- 10kOhm --- GND --   
                                                            |
                BCM18 -b-- 330Ohm ----- green LED --- GND ----g-   GPIO14(GND)
                                                            |
                BCM22 -r-- 330Ohm ------- red LED --- GND --
                                                            |
                BCM23 -y-- 330Ohm ---  button LED --- GND --


Codes/Scripts

                cd ~
                mkdir photobooth_images
                mkdir PB_archive
                mkdir -p ~/scripts/photobooth
                cd ~/scripts/photobooth

                sudo wget raw.github.com/codeschnipsler/Fotobox/master/assemble_and_print
                sudo wget raw.github.com/codeschnipsler/Fotobox/master/photo_booth.py
                sudo wget raw.github.com/codeschnipsler/Fotobox/master/startup_script
                sudo wget raw.github.com/codeschnipsler/Fotobox/master/cloze_FEH
                sudo wget raw.github.com/codeschnipsler/Fotobox/master/scripts_slideshow
                sudo wget raw.github.com/codeschnipsler/Fotobox/master/scripts_slideshow_all

                sudo chmod 755 *

                sudo nano assemble_and_print
Edit the "assemble_and_print" script. Change the "lp" line to include your printer name.


6) Test: try it out and run the script (ctrl-C to quit).

                sudo python ~/scripts/photobooth/photo_booth.py

If it's glowing, push the button.


7) Set script to run automatically.
If the step above works, then make the script run automatically at startup. This will be allow the booth to operate without an external computer or network.

                sudo nano /etc/rc.local

Now, add the line
                /home/pi/scripts/photobooth/startup_script &
                above the "exit 0" line
                ^X to exit, save the changes

Restart the RPi
                Sudo reboot


Setup
1) Connect the printer and camera to the RPi using a USB hub.
2) optional: connect Screen via HMDI

Push the button to have fun
