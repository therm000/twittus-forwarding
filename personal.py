import urllib
import urllib2

url = 'http://sms1.personal.com.ar/Mensajes/sms.php'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = "form_flag=&Snb=1166190004&subname=1166190004&sig=titi&msgtext=hola+loco+test8+desde+sms.personal.com.ar&form=ht4&size=10&btn_send=SEND&historico=&Filename=tmp%2F81152d748d8f855d.png&FormValidar=validar&CODAREA=11&NRO=66190004&DE_MESG_TXT=titi&sizebox=65&MESG_TXT=hola+loco+test8+desde+sms.personal.com.ar&codigo=9247&Enviar.x=35&Enviar.y=10&pantalla="

#data = urllib.urlencode(values)
req = urllib2.Request(url, data)
print 'enviando...'
response = urllib2.urlopen(req)
the_page = response.read()
print 'enviado!'



