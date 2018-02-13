from bottle import run, route

@route('/data')
def data():
	jsonStr = '<h1>AMAP: Automated Malware Analysis Platform</h1>'

	return htmlStr

if __name__ == '__main__':
	run()