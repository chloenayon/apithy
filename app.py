from flask import Flask, render_template
import urllib2, json

key = "dc81912032b4af7db369363784b553ee"

joe = Flask(__name__)

url = "http://api.openweathermap.org/data/2.5/weather?id=5128638&units=imperial&appid=dc81912032b4af7db369363784b553ee"
request = urllib2.urlopen(url)
result = request.read()
r = json.loads(result)
m = r["main"]["temp"]
print m

@joe.route("/")
def go():
#    return m
    pass

if __name__=="__main__":
    joe.debug = True
    joe.run(host='0.0.0.0', port=8000)
