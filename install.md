### Fotobox install
original source https://www.instructables.com/id/Raspberry-Pi-photo-booth-controller/

## Setup the PI and install GPhoto2
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

  6) CUPS Printer setup
  Use CUPS to drive the printer. You can check to see if CUPS supports a particular printer. The Canon Selphy CP-900 is not on that list but people got it working using the SELPHY-CP770 driver. I have an old HP printer that I use for this project - it works but took some effort to find the right setup in CUPS. I also had to install hplip-gui in order to receive the printer that I intended to use in the CUPS drivers list.  
 
         sudo apt-get install hplip
         sudo apt-get install hplip-gui 
 
  6.1) Install CUPS from the RPi command line (for further guidance/troubleshooting, see here)

                sudo apt-get install cups

   Add the user (pi) to the group allowed to print (lpadmin)

                sudo usermod -a -G lpadmin pi


  6.2) Connect your printer and setup CUPS from the RPi desktop
    Attach to the RPi by USB and power up your printer.
    Open Midori and type into the URL line to open up the CUPS setup.
    http://127.0.0.1:631
    Click "administration" and "add printer;" enter your username and password (e.g., the defaults "pi" and "raspberry"). You should see your printer listed under "local printer;" select it and click "continue." Set the name and location of your printer as you like, and click "continue."

7. Hardware
 Following Safay's [setup](https://cdn.instructables.com/FP9/LHV6/HSE92TJ7/FP9LHV6HSE92TJ7.LARGE.jpg), I used a permanent prototyping board to solder together the hardware buttons and LEDs. I used momentary switches (any normally open would do). Besides the main "Take Picture Button", which I use an [illuminated Arcade](https://amzn.to/2GTtYEG) button for, I added added a red button to start/shutdown the PI button and a green reboot button. The later two will sit inside the housing (out of the users' hands) and is just a little bit of trouble shooting measure and to simplify the setup (no more ssh or keyboard/mouse needed).

      GPIO17(3,3 V) to Button (grey)
      BCM18 to green LED, then 330OHM resistor, connect to ground (blue)
      GPIO14(GND) as ground (green)
      BCM23 to LED in Arcade button (yellow)
      BCM24 as input from button (orange)
      BCM22 to red LED, then 330Ohm resistor connect to ground (red)
      

                         GPIO17(3,3 V)       
                              |  
                      "Take Picture Button"
                              |
         BCM24 -o-- 1kOhm --- | --- 10kOhm --- GND --   
                                                     |
         BCM18 -b-- 330Ohm ----- green LED --- GND ----g-   GPIO14(GND)
                                                     |
         BCM22 -r-- 330Ohm ------- red LED --- GND --
                                                     |
         BCM23 -y-- 330Ohm ---  button LED --- GND --
                                                     |         
         BCM17 -v-- 1kOhm --- | --- 10kOhm --- GND --
                              |
                          "Reboot Button"
                              |
                         GPIO17(3,3 V) 
         
         GPIO5 ---- "Shutdown/start-Button" ---- GPIO6      
         
         legend
         --- means that there is a cable to connect
         in my setup, I used the following colors (change to your liking)
            v = violet
            y = yellow
            r = red
            b = blue
            o = orange
            g = green

For a secure attachment to the GPIOs, I used [DuPont crimps](https://amzn.to/2Tt8lfV). Usually I just hijack a standard jumper cable, unlock the one pin housing and put the metal piece in one of the multi pin housings from the box. But of course it is also possible to use a crimping device and do it all manually.


8. Codes/Scripts

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


9) Test: try it out and run the script (ctrl-C to quit).

                sudo python ~/scripts/photobooth/photo_booth.py

If it's glowing, push the button.


10) Set script to run automatically.
If the step above works, then make the script run automatically at startup. This will be allow the booth to operate without an external computer or network.

                sudo nano /etc/rc.local

Now, add the line

                /home/pi/scripts/photobooth/startup_script &
above the "exit 0" line
^X to exit, save the changes

Restart the RPi
                Sudo reboot


11) Setup
1) Connect the printer and camera to the RPi.
2) optional: connect Screen via HMDI

Push the button to have fun
