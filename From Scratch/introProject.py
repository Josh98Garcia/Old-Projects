from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def urlask():
    return '''Input Video URL:
    <br><input type="text" id="vidurl" value=""><button onclick="redirect()">go</button><br>
    <p>YouTube seems to be acting up with embed codes.<br>Many videos simply give a "Video unavailable" message and don't play.<br>I've concluded this is an issue with YouTube's embed codes interacting with my browsers (Chrome and Firefox).<br>Vimeo should work just fine.<br>(both demonstrated below)<br><br>There are, however, some YouTube videos that work.<br>The common denominator seems to be the age of the videos.<br>Videos older than about a year have issues being embedded for some reason.<br>Videos younger than a year, however, work perfectly fine.</p>
    <script>
    function redirect() {
        url = document.getElementById("vidurl").value.replace('?', '');
        window.location.href = "http://127.0.0.1:5000/processing/" + url;
    }
    </script>
    <iframe width="1280" height="720" src="https://www.youtube.com/embed/HAwFVibypVM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><iframe width="1280" height="720" src="https://www.youtube.com/embed/W9iUh23Xrsg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><iframe src="https://player.vimeo.com/video/148751763" width="640" height="480" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>'''

@app.route('/processing/<path:vidurl>/<urlid>')
def process(vidurl, urlid):
    vu = escape(vidurl)
    uid = escape(urlid)
    url = ""
    if "embed" in vu:
        url = "http://127.0.0.1:5000/vid/you/" + uid.rsplit('/', 1)[-1]
    elif "www.youtube.com" in vu:
        url = "http://127.0.0.1:5000/vid/you/" + uid.rsplit("=", 2)[1].rsplit("&", 1)[0]
    elif "vimeo.com" in vu:
        url = "http://127.0.0.1:5000/vid/vim/" + uid.rsplit('/', 1)[-1]
    return '''Loading...<meta http-equiv="refresh" content="2; URL=%s" />''' % url
    
@app.route('/vid/you/<url>')
def youtube(url):
    return '''
        <iframe width="1280" height="720" src="https://www.youtube.com/embed/%s"
        frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    ''' % escape(url)

@app.route('/vid/vim/<url>')
def vimeo(url):
    return '''
        <iframe src="https://player.vimeo.com/video/%s" width="640" height="480"
        frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>
    ''' % escape(url) 