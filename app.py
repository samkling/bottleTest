from bottle import run, route,static_file

@route('/data/<filename>')
def data(filename): # = '<h1>AMAP: Automated Malware Analysis Platform</h1>'
	return static_file(filename,"./webfront/")

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./webfront/')


run(host='localhost', port=8080, debug=True)