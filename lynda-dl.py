# adapted from http://fossbytes.com/how-to-download-lynda-com-videos-using-youtube-dl/
# this is an updated version from -> https://github.com/papapon/lynda-dl

import os
import httplib2
from bs4 import BeautifulSoup
import sys
'''
Lynda-dl
Tested on ubuntu 14.04 and python 2.7.6
How to use:
python lynda-dl username password courselink

Example:    
python lynda-dl.py happyguy@myhouse.com mypassword https://www.lynda.com/3D-Animation-Animation-tutorials/Getting-Started-3D-Animation/193805-2.html

Created: 25/April/2017
'''
user = sys.argv[1]
passw = sys.argv[2]
weblink = sys.argv[3]

current = os.getcwd()
http = httplib2.Http()
#weblink = 'https://www.lynda.com/3D-Animation-Animation-tutorials/Getting-Started-3D-Animation/193805-2.html'
 
status, response = http.request(weblink) # url from the site you'd like to scrape
root = weblink[:weblink.find('/',24)+1]
websplit = weblink.split('/')
coursename = websplit[-2]# get only the coursename

#create course folder
newpath = os.path.join(current,coursename)
if not os.path.exists(newpath):
    os.makedirs(newpath)
    
# go to new path
os.chdir(newpath)
# get files
Textfile = open('1-Content','w')
Textfile.write('{} :\n'.format(coursename))
num = 1
for link in BeautifulSoup(response).find_all('a', href=True):
    #print link['href']
    if root in link['href']: # parse only the links that contain the key URL to your specific tutorial
        l = link['href']
        nombre = l.replace(root,'')
        #print l
        Textfile.write('\n{}. {}'.format(num,nombre[0:nombre.find('/')]))
        num+=1
        os.system("youtube-dl --username {} --password {} ".format(user,passw) + l+" --write-srt --sub-lang en") # login + password lynda to change. nb : the space after your password is usefull
        
Textfile.write('\n Enjoy your course offline! \n updates-> https://github.com/JoseRZapata/lynda-dl')
Textfile.close()
os.chdir(current)
print('Download {} complete'.format(coursename))