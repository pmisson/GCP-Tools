#!/usr/bin/env python

import asciitable,sys
import numpy as np
import os
#from astropy.io import ascii
nameori = sys.argv[1]
#nameori="ISS053-E-46037.gcp"
try:
    nameori.split('new')[0]+nameori.split('new')[1]
    new=1
except:
    new=0
datos=asciitable.read(nameori,Reader=asciitable.NoHeader,delimiter=",")
if new==1:
    nameori=nameori.split('new')[0]+nameori.split('new')[1]
mision=nameori.split('-E-')[0]

if mision[:3]=='iss':
    mision=nameori.split('e')[0]
    number=mision.split('iss')[1]
else:
    number=mision.split('ISS')[1]


number=int(number)

if number<41:
    datos.col1=datos.col1+13
    datos.col2=datos.col2+6
    datos.col1=datos.col1/2
    datos.col2=datos.col2/2
else:
    datos.col1=datos.col1+6
    datos.col2=datos.col2+6
    datos.col1=datos.col1/2
    datos.col2=datos.col2/2
nameori=nameori.lower()
try:
    frame=nameori.split('-e-')[1].split('.gcp')[0]
except IndexError:
    frame=nameori.split('e')[1].split('.gcp')[0]
frame1=frame.zfill(6)
nameori=mision.lower()+'e'+frame1+'RGB.gcp'
asciitable.write({'x': datos.col1, 'y': datos.col2,'z':datos.col3,'a':datos.col4},nameori, names=['x', 'y','z','a'],Writer=asciitable.NoHeader,delimiter=",")
nameori=mision.lower()+'e'+frame+'RGB.gcp'
asciitable.write({'x': datos.col1, 'y': datos.col2,'z':datos.col3,'a':datos.col4},nameori, names=['x', 'y','z','a'],Writer=asciitable.NoHeader,delimiter=",")
#ascii.write(datos,'values.dat',format='no_header')

ex1=os.path.exists(mision.upper()+'e'+frame1+".NEF")
ex2=os.path.exists(mision.upper()+'-E-'+frame1+".NEF")
ex3=os.path.exists(mision.lower()+'e'+frame1+".NEF")
ex4=os.path.exists(mision.lower()+'e'+frame+".NEF")
ex12=np.logical_or(ex1,ex2)
ex123=np.logical_or(ex12,ex3)
ex1234=np.logical_or(ex123,ex4)
baja=np.logical_not(ex1234)
if baja:
    print('Descarga '+mision.upper()+'e'+frame1+".NEF")
    import os
    import datetime,time
    import numpy as np
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from pyvirtualdisplay import Display
    import asciitable,sys
    #from getdata import *
    DisplayU=1
    if DisplayU:
            display = Display(visible=0, size=(800, 600))
            display.start()



    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList', 2) # custom location
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference("browser.download.dir", os.getcwd())
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'image/x-nikon-nef')
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'image/nikon')
    profile.set_preference("browser.helperApps.alwaysAsk.force", False);
    profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
    profile.set_preference("browser.download.manager.focusWhenStarting", False);
    profile.set_preference("browser.download.manager.useWindow", False);
    profile.set_preference("browser.download.manager.showAlertOnComplete", False);
    profile.set_preference("browser.download.manager.closeWhenDone", False);
    xpad='/html/body/div[1]/div/div/a'
    path=os.getcwd()
    try: ####### Sometimes you will need the geckodriver to prevent Firefox to stop
        driver = webdriver.Firefox()
    except:
        driver = webdriver.Firefox(firefox_profile=profile,executable_path=path+'/geckodriver')
    driver.get("http://eol.jsc.nasa.gov/SearchPhotos/RequestOriginalImage.pl?mission="+mision.upper()+"&roll=E&frame="+frame+"&file="+mision.upper()+'e'+frame1+".NEF")
    time.sleep(400)
    #elem = driver.find_element_by_xpath(xpad).click()
    try:
        elem = driver.find_element_by_xpath(xpad)
    except NoSuchElementException:
        driver.get("http://eol.jsc.nasa.gov/SearchPhotos/RequestOriginalImage.pl?mission="+mision.upper()+"&roll=E&frame="+frame+"&file="+mision.upper()+'e'+frame1+".NEF")
        #time.sleep(300)
        elem = driver.find_element_by_xpath(xpad).click()
        
    URL=elem.get_attribute('href')
    #
    os.system('wget '+URL)
    driver.close()
    if DisplayU:
            display.stop()
    os.system('rename "s\ISS\iss\\" *.NEF')
