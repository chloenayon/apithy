from flask import Flask, render_template, request, session, redirect
import urllib2, json
import helper

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
        req = urllib2.urlopen(event)                                           
        res = req.read()                                                       
        q = json.loads(res)                
        f = q['events']
        things = q['events']['event']
        #a is a dictionary with information about an individual event
        str_list = []
        #print things[0]
        for a in things:
            str_list.append(helper.format_event(a))
            eventlat = a['latitude']
            eventlong = a['longitude']
        return render_template('results.html', things = things, eventlat= eventlat, eventlong = eventlong, str_list = str_list)


if __name__=="__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8000)
