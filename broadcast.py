
import cgi, sys

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import mail

class Twit(db.Model):
  twid = db.IntegerProperty()
  desc = db.StringProperty(multiline=True)

class TwittusStatus(db.Model):
  status = db.IntegerProperty()

from twitter_grabber import TwitterGrabber

def get_status():
    ss = []
    for s in TwittusStatus().all().fetch(1):
	ss.append(s)
    if len(ss) == 0:
	s = TwittusStatus(status=0)
	s.put()
    else:
	s = ss[0]
    return s

class MainPage(webapp.RequestHandler):
  def get(self):

    s = get_status()
    if s.status == 0:
	status = 'OFF'	
    else:
	status = 'ON'	
    self.response.out.write('TWITTUS TWITTER BROADCAST SYSTEM: %s' % status)

class OffPage(webapp.RequestHandler):
  def get(self):
    s = get_status()
    s.delete()
    s = TwittusStatus(status=0)
    s.put()
    self.response.out.write('TWITTUS TWITTER BROADCAST SYSTEM, TURNED OFF!')

class OnPage(webapp.RequestHandler):
  def get(self):
    s = get_status()
    s.delete()
    s = TwittusStatus(status=1)
    s.put()
    self.response.out.write('TWITTUS TWITTER BROADCAST SYSTEM, TURNED ON!')


class Broadcast(webapp.RequestHandler):
  def get(self):

    if get_status().status == 0:
      return

    # uncomment this if you want to empyt the datastore
#    twits_query = Twit.all().order('-twid')
#    for twit in twits_query:
#	twit.delete()

    twits_query = Twit.all().order('-twid')
    twits = twits_query.fetch(20)
    twits = [(t.twid,t.desc) for t in twits]

#    user = 'twittustest1'
#    password = 'asdfasdf'
#    user = 'twittustest2'
#    password = 'asdfasdf'
    user = 'therm000'
    password = 'XXX'

    debug = False
    grabber = TwitterGrabber(user, password, debug)
    new_twits = grabber.send_sms(twits, '33404016')

    for newguid, newdesc in new_twits:
	twit = Twit(twid=long(newguid), desc=newdesc)
	twit.put()

application = webapp.WSGIApplication(
                                     [('/', MainPage),
				      ('/off', OffPage),
				      ('/on', OnPage),
                                      ('/broadcast/realtime', Broadcast)],
                                     debug=False)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
