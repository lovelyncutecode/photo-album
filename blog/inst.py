from requests import get  

import re

from datetime import datetime

def getMediaByLink(ref):
	response = get(ref)
	text = response.content.decode('utf-8')
	pattern = re.compile(r'{"text": .*?}}]}')
	des=re.search(pattern, text)
	if des!=None:
		des=des.group(0)
		des=des[10:-5]
		des=re.sub('\\\\u\w+','',des)
		print(text)
	else: des=''
	
	if 'GraphVideo' in text:
		pattern = re.compile(r'"video_url": "https:.*?", "')
		photo=re.search(pattern, text).group(0)
		photo=photo[14:-4]
	else:	
		pattern = re.compile(r'\[{"src": "https:.*?", "')
		photo=re.search(pattern, text).group(0)
		photo=photo[10:-4]

	response=get('http://api.instagram.com/oembed/?url='+ref)
	text = response.content.decode('utf-8')
	pattern = re.compile(r'datetime=.*?\"\\')
	date=re.search(pattern, text).group(0)
	date=date[11:-9]
	date= datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
	
	
	
	#print(photo)
	photoDescrDate=[photo,des,date]

	return photoDescrDate

#print(getMediaByLink('https://www.instagram.com/p/BL62ymVg2Q2/?hl=ru&taken-by=nightcall4'))