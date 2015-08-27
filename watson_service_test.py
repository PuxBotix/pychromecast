import pychromecast
from pychromecast.controllers import BaseController

__author__ = 'Pux0r3'

fake_result = '<?xml version="1.0" encoding="UTF-8"?><pod title="ninja"><subpod><plaintext>ninja text</plaintext></subpod></pod>'

class ChromecastDisplayController(BaseController):
	def __init__(self):
		super(ChromecastDisplayController, self).__init__(
			'urn:x-cast:com.sphero.watson_result',
			supporting_app_id='E4F91038'
		)

	def receive_message(self, message, data):
		print 'received', data
		return True

	def send_query(self, wolfram_query):
		self.send_message(wolfram_query)



watson_handler = ChromecastDisplayController()
cast = pychromecast.get_chromecast(friendly_name='PuxCast')
cast.register_handler(watson_handler)
watson_handler.launch()
watson_handler.send_query(fake_result)
