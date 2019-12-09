import request

def handler (event, context):
	r = requests.get('https://icinga.com/')
	print(r.text[500])
	if r.status_code == 200:
		return 'Success'
	else :
		return 'Failure'
