# Fotobox
A Fotobox based on the original script from www.github.com/safay/RPi_photobooth adapted to run via GPIOZERO and to include a slideshow with the current pictures and subsequently all pictures with the following hardware setup:
  - Raspberry Pi 3 (based on raspian) as controller
  - a few buttons and LEDs as interface (designed to cater for kids and drunks)
  - a Canon DSLR attached via USB Cable or any other Camera compatible with GPHOTO2
  - a HP Printer (HP Photosmart 5510 series) or any other printer compatible with CUPS
  - optionally: a screen via HDMI
To do: I am working on a webserver to allow download to other devices via WIFI
To do: build a nice case

The workflow is as follows:
  - as an admin: connect all hardware, start all devices
  - as a user:  
    - Push the button
    - Pose for four pics and see the latest one on the (optional) screen
    - wait for a few seconds and receive the printout of the 4 in 1 collage from the printer
    - future feature: connect via webbrowser to download pics

See manual.md for the install routine from @safay https://www.instructables.com/id/Raspberry-Pi-photo-booth-controller/ adapted for my setup.
