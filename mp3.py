from flask import Flask
from flask import request
app=Flask(__name__)
app.debug=True
@app.route('/')
def main():
	html=''
	html+='<html><body>'
	html+='<form method="POST" action="form_input">\n'
	html+='Youtube URL: <input type="text" name="url"/>\n'
	html+='<p>\n'
	html+='<input type="radio" name="data" value="mp3" checked>mp3\n'
	html+='<input type="radio" name="data" value="videos">videos\n'
	html+='<input type="radio" name="data" value="videostreams">videostreams\n'
	html+='<input type="radio" name="data" value="audiostreams">audiostreams\n'
	html+='<p>\n'
	html+='<input type="submit" value="submit"/>\n'
	html+='</form>\n'
	html+='</body></html>'
	return html
@app.route('/form_input',methods=['POST'])
def form_input():
	url=request.form['url']
	u=url.split("=")
	vid=u[1]
	data=request.form["data"]
	d="https://youtubemp3api.com/@api/button/"+data+"/"+vid
	print(d)
	html=''
	html+='<html>\n'
	html+='<body>\n'
	html+='<iframe class=button-api-frame'+" "+"src="+d+" "+'width="100%" height="100%" allowtransparency="true" scrolling="no" style="border:none"></iframe>'
	html+='<script src="https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/3.5.14/iframeResizer.min.js"></script>'
	html+='<script>iFrameResize({}, ".button-api-frame");</script>'
	html+='</body>\n'
	html+='</html>\n'
	return html	
if __name__=='__main__':
	app.run()