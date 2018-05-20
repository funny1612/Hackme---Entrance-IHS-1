import requests
def start():
	try:
		with open("path.txt","r") as paths:
			for path in paths:
				path = str(path.replace("Disallow: ",""))
				path = path.replace("\n","")
				rq = requests.get('http://s88753-103149-w9k.sipontum.hack.me'+path)
				if rq.status_code==404:
					print 'Error 404: '+path
				else:
					print path
	except IOError:
		print 'file not found'
start()



