from flask import Flask, render_template
import urllib2, json

key = "dc81912032b4af7db369363784b553ee"

joe = Flask(__name__)

url = "http://api.openweathermap.org/data/2.5/weather?id=5128638&units=imperial&appid=dc81912032b4af7db369363784b553ee"
request = urllib2.urlopen(url)
result = request.read()
r = json.loads(result)
m = r["main"]["temp"]
#print m

event = """http://api.eventful.com/json/events/search?...&keywords=music&location=New+York&date=Future&app_key=rqSF6Lsh3t772JPf"""
req = urllib2.urlopen(event)
res = req.read()
q = json.loads(res)
#print q['events']['event'][2]['latitude']


@joe.route("/")
def go():
    return render_template('home.html')

if __name__=="__main__":
    joe.debug = True
    joe.run(host='0.0.0.0', port=8000)
