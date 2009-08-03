#http://www.paginasmoviles.com.ar/envioSMS.asp?email=a@a.com&prefijo=11&celular=33404016&compania=AutoDetectar&mensaje=probnado%20http%20headers&emailsubject=SMS%20Gratis%200%3A56%3A59&sesID=933707111

import urllib2, urllib, time

class SMSearClaro:

	def_msg = 'THIS IS A TEST OF THE EMERGENCY BROADCAST SYSTEM! %s' % time.ctime()
	head_url = 'http://www.paginasmoviles.com.ar/envioSMS.asp?prefijo=%s&celular=%s&'
	tail_url = '&compania=AutoDetectar&emailsubject=SMS%20Gratis%200%3A56%3A59&sesID=933707111'

	def __init__(self, debug=False):
		self.debug = debug

	def send(self, cell_nr=None, msg=None, email='twittus', prefix='11'):
		
		if not msg:
			msg = self.def_msg

		msg = str(msg)

		if not cell_nr:
			raise Exception('ERROR: no cell phone number!! in send()')



		url = self.head_url % (prefix,cell_nr) + urllib.urlencode({'email':email, 'mensaje': msg}) + self.tail_url

		if self.debug:
			print 'Enviando mensaje sms...'
			print url
		try:
			urllib2.urlopen(url)
		except:
	                raise Exception('ERROR: sms send() error grabbing URL, maybe a problem with internet connection!')

		if self.debug:
			print 'Mensaje sms enviado.'


if __name__ == '__main__':
	
	sms = SMSearClaro(True)
#	sms.send('33404016')
#	sms.send('57731237')
	sms.send('66190004', 'decime si te llega esto pancho, soy jose, test1')
