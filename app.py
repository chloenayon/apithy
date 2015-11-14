from flask import Flask, render_template, request, session, redirect
import urllib2, json

key = "dc81912032b4af7db369363784b553ee"

app = Flask(__name__)

#url = "http://api.openweathermap.org/data/2.5/weather?id=5128638&units=imperial&appid=dc81912032b4af7db369363784b553ee"
#request = urllib2.urlopen(url)
#result = request.read()
#r = json.loads(result)
#m = r["main"]["temp"]
#print m

@app.route("/", methods = ["GET", "POST"])
def go():
    if request.method == "GET":
        return render_template('home.html')
    else:
        event = """http://api.eventful.com/json/events/search?...&keywords=%s&location=New+York&date=Future&app_key=rqSF6Lsh3t772JPf"""                      
        event = event%(request.form['search'])
#        print event
        req = urllib2.urlopen(event)                                           
        res = req.read()                                                       
        q = json.loads(res)                
        things = q['events']['event']
#        for a in things:
#            print a
        return render_template('home.html', things = things)

@app.route("/results")
def results():
    return render_template('results.html')

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
