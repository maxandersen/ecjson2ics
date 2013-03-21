= Convert EclipseCon feed into ical

Dependencies:
 https://pypi.python.org/pypi/icalendar
  
Install:
 
   $ git clone http://github.com/collective/icalendar
   $ cd icalendar
   $ python setup.py install
   $ cd ..
   $ git clone 
   
Usage:

curl {sessionurl} | python ecjson2ics.py > eclipsecon2013.ics

Example result:
   https://dl.dropbox.com/u/558690/eclipsecon2013.ics
