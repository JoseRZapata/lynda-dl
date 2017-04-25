# lynda-dl [Updated Version 25-Apr-2017]

This script is an updated version from: https://github.com/papapon/lynda-dl

Works for ubuntu 14.04 and Python 2.7.6.
you can check in your own linux distribution

## Install beautifulsoup:

    sudo apt-get install python-bs4  or  sudo pip install bs4

## Install youtube-dl:

Install youtube-dl via pip (not apt) to have the "good" version:  

    sudo apt-get install python-setuptools  
    sudo easy_install pip
    sudo pip install --upgrade youtube-dl

## HOW TO:
1. Select your course link on **http://www.lynda.com/**
   Example: https://www.lynda.com/3D-Animation-Animation-tutorials/Getting-Started-3D-Animation/193805-2.html 
2. Run script:
       python lynda-dl username password courselink
   Example:
       python lynda-dl.py happyguy@myhouse.com mypassword https://www.lynda.com/3D-Animation-Animation-tutorials/Getting-Started-3D-Animation/193805-2.html     
3. The downloaded videos with english subtitles are in a new folder named by the coursename.  
