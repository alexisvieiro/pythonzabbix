#!/usr/bin/env python
import sys
import requests

def msgbot():
    id = '1140185753'
    asunto= str(sys.argv[1])
    mensaje= str(sys.argv[2])
    send_text = 'https://api.telegram.org/bot' + '1111786387:AAFYSxY4Mzy-jj7jwVMRvXurq7qlH9mQINc' + '/sendMessage?chat_id=' + id + '&parse_mode=Markdown&text=Asunto: ' + asunto
    response = requests.get(send_text)
    send_text = 'https://api.telegram.org/bot' + '1111786387:AAFYSxY4Mzy-jj7jwVMRvXurq7qlH9mQINc' + '/sendMessage?chat_id=' + id + '&parse_mode=Markdown&text=Mensaje: ' + mensaje
    response = requests.get(send_text)
#   if(len(sys.argv)<4):
#	    return -1

msgbot()

		

