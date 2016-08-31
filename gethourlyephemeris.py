import os
import time
import urllib.request
import ftplib

#Gets the day of year
DOY = time.localtime().tm_yday

###Generate URL
#print ("Generating current hourly URL..." + '\n')
basefileurl = "ftp://cddis.gsfc.nasa.gov/gnss/data/hourly/"
fourdyear = time.localtime().tm_year
twodyear = str(fourdyear)[-2:]
pathfileurl = basefileurl + str(fourdyear) + "/" + str(DOY) + "/"
ephemerisfilename = "hour" + str(DOY) + "0." + str(twodyear) + "n.Z"
fullurl = pathfileurl + ephemerisfilename
#Sets up parsed URL if needed
parsedurl = urllib.parse.urlparse(fullurl)
#print ("URL Generated " + fullurl + '\n')

###Download File from URL
try:
	print ("Connecting to FTP " + parsedurl.netloc)
	ftp = ftplib.FTP(parsedurl.netloc)
	print ("FTP Login...")
	ftp.login()
	print ("FTP Changing directory...")
	ftp.cwd(os.path.dirname(parsedurl.path)[1:])
	ftp.dir()
	print ("Downloading hourly ephemeris data to " + ephemerisfilename)
	ftp.retrbinary('RETR %s' % ephemerisfilename, open(ephemerisfilename, 'wb').write)
	print ("Disconnecting from " + parsedurl.netloc)
	ftp.quit()
except ftplib.all_errors as err:
	print (err)
