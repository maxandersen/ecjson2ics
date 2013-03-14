
import simplejson as json
import sys
import codecs
import io
import re
from icalendar import Calendar, Event
import pytz
import time

#data = json.load(codecs.open('sessions.json','r', 'utf-8-sig'))

data = json.loads(''.join(sys.stdin.readlines()))

cal = Calendar()
from datetime import datetime
cal.add('prodid', '-//EclipseCon2ical//xam.dk//')
cal.add('version', '2.0')

for session in data:
    if session["title"]!="Transition Time":
        event = Event()
        start = datetime.strptime(session["date"] + " " + session["start"], "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime(session["date"] + " " + session["end"], "%Y-%m-%d %H:%M:%S")
    
        event.add('summary', session["title"])
        event.add('description', session["abstract"])
        if "room" in session and session["room"] is not None:
            event.add('location', session["room"])
        if "presenter" in session:
            for presenter in session["presenter"]:
                event.add('attendee', presenter["fullname"] + "<@" + (presenter["organization"] or 'unknown.org') + ">")
        if "category" in session:
            event.add('categories', session["category"])

        event.add('url', 'http://www.eclipsecon.org/2013/node/'+session["id"])
        event.add('dtstart', datetime(start.year,start.month,start.day,start.hour,start.minute,start.second,tzinfo=pytz.timezone('US/Eastern')))
        event.add('dtend', datetime(end.year,end.month,end.day,end.hour,end.minute,end.second,tzinfo=pytz.timezone('US/Eastern')))
        #event.add('dtstamp', datetime(2005,4,4,0,10,0,tzinfo=pytz.utc))
        event['uid'] = session["id"] + '@xam.dk'
        event.add('priority', 5)
        cal.add_component(event)

print cal.to_ical()
