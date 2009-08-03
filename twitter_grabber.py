
# TODO: check that status numbers are unique
# TODO: bug in XMLHandler, newlines in twits are brokennnnn!!
#	FIX: concatenating chars in xmlhandler


# http://twitter.com/statuses/friends_timeline.rss

# http://therm000:XXX@twitter.com/statuses/friends_timeline.rss

from TwitterTimelineXMLHandler import TwitterTimelineXMLHandler
from smsear_claro import SMSearClaro

import urllib2, xml.sax, re, sys

class TwitterGrabber:

	url = 'http://twitter.com/statuses/friends_timeline.rss'

	def __init__(self, user=None, password=None, debug=False):
		self.debug = debug
		if not user or not password:
			raise Exception('you need a twitter user and password for TwitterGrabber!')
		self.user = user
		self.password = password


	def timeline(self):

            try:	        
		theurl = self.url 
		username = self.user
		password = self.password
		# a great password

		passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
		# this creates a password manager
		passman.add_password(None, theurl, username, password)
		# because we have put None at the start it will always
		# use this username/password combination for  urls
		# for which `theurl` is a super-url

		authhandler = urllib2.HTTPBasicAuthHandler(passman)
		# create the AuthHandler

		opener = urllib2.build_opener(authhandler)

		urllib2.install_opener(opener)
		# All calls to urllib2.urlopen will now use our handler
		# Make sure not to include the protocol in with the URL, or
		# HTTPPasswordMgrWithDefaultRealm will be very confused.
		# You must (of course) use it when fetching the page though.

		pagehandle = urllib2.urlopen(theurl)
		# authentication is now handled automatically for us

		content = pagehandle.read()

	    except:
                raise Exception('ERROR: grabbing URL, maybe a problem with twitter user/password or internet connection!')
    
    	    handler = TwitterTimelineXMLHandler()
	    xml.sax.parseString(content, handler)

	    #return handler.ret_list
	    t_list = [(dic['guid'],dic['description']) for dic in handler.ret_list]

	    n_t_list = []
	    prev_u = None
            regex = '[a-zA-Z0-9_-]+'
	    for g, twit in t_list:
                  twit_s = twit.split(':')
	          if not ':' in twit or re.search(regex,twit_s[0]).group() != twit_s[0]:
			twit =  prev_u + ': ' + twit
		  else:
                        prev_u = twit_s[0] 
		  n_t_list.append((g, twit))

	    t_list = n_t_list

	    # dict version
	    #ret = {}
	    #ret.update(  t_list )
	    #return ret

	    # list version
	    return [(long(guid.split('/')[-1]),desc) for (guid, desc) in t_list]


	def build_sms(self, twit):
		s = twit.split(':')
		return s[0], ':'.join( s[1:] )

	def sanitize(self, desc):
		desc = desc.replace(u'\xe1',u'a').replace(u'\xe9',u'e').replace(u'\xed',u'i').replace(u'\xf3',u'o').replace(u'\xfa',u'u')
		return ''.join([c for c in desc if ord(c) < 128])

	def send_sms(self, last20=[], cell_nr=None, prefix='11'):

		if self.debug:
			sys.stderr.write('last20\n')
			sys.stderr.write(str(last20))

		count = 0
		old_guids = set([guid for guid,desc in last20])		
		# dict version
#		for guid, desc in self.timeline().iteritems():		
		# list version
		new_guids = []
		timeline = self.timeline()
		timeline.reverse()

		if self.debug:
			sys.stderr.write('timeline\n')
			sys.stderr.write(str(timeline))

		for guid, desc in timeline:
			desc = self.sanitize(desc)
			email, msg = self.build_sms(desc)
			if not guid in old_guids:
				new_guids.append( (guid,desc) )

				if self.debug:
					sys.stderr.write(email + ' said:' + '\n' )
					sys.stderr.write(msg + '\n' )

				SMSearClaro(self.debug).send(cell_nr, msg, email, prefix)				
				count += 1
				if count >= 1:
					break

		return new_guids
		

if __name__ == '__main__':

#	user = 'therm000'
#	password = 'XXX'

	grabber = TwitterGrabber(user, password)

	for elem in grabber.timeline():
		#print elem
		pass

#	print len(grabber.timeline())
	grabber.send_sms([], '33404016')
