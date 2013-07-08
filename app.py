import os
#import json
from flask import Flask, render_template, json, request
from math import log10, floor


app = Flask(__name__)
#app.jinja_env.autoescape = False


CSRF_ENABLED = True
app.secret_key="cheese"


#class Main(flask.views.MethodView):
#    def get(self):
#        pass
#    def post(self):
#        required = ['first']
#            for r in required:
#                if r not request.form:
#                    flash("error:{0} is required.".format(r))
#                    return render_template('conversions.html')
#            first = request.form['first']

def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(x)))-1)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/')
def index():
    global foo
    foo = request.form.get('units',None)
    data = {'num':0, 'unit':'', 'unitres':foo, 'res':'', 'mainunit':''}
    data['mainunit'] = request.form.get('maincat',None)
    options = {"kg": "kg","pounds": "pounds","ounces": "ounces"};
    return  render_template('conversions.html',data=data,options=options)

@app.route('/data', methods =['GET','POST'])
def handle_data():
    data = {'num':0, 'unit':'', 'unitres':foo, 'res':'', 'mainunit':''}
    data['num'] = request.form.get('number',None)
    data['unit'] = request.form.get('units',None)
    data['unitres'] = request.form.get('resultunit',None)
    data['mainunit'] = request.form.get('maincat',None)
    trigger = 5
    try:
        val = float(data['num'])
    except:
        data['num'] = "Type value here"
        data['res'] = "Result appears here"
        trigger = 6
    #modify data['num'] with json data
    if data['unit'] == 'meters' and data['unitres'] == 'meters' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'meters' and data['unitres'] == 'inches' and trigger == 5:
        json_file = open('templates/json/distance/meters_to_inches.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'meters' and data['unitres'] == 'feet' and trigger == 5:
        json_file = open('templates/json/distance/meters_to_feet.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'meters' and data['unitres'] == 'yards' and trigger == 5:
        json_file = open('templates/json/distance/meters_to_yards.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'meters' and data['unitres'] == 'leagues' and trigger == 5:
        json_file = open('templates/json/distance/meters_to_leagues.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])

    elif data['unit'] == 'inches' and data['unitres'] == 'meters' and trigger == 5:
        json_file = open('templates/json/distance/inches_to_meters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'inches' and data['unitres'] == 'inches' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'inches' and data['unitres'] == 'feet' and trigger == 5:
        json_file = open('templates/json/distance/inches_to_feet.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'inches' and data['unitres'] == 'yards' and trigger == 5:
        json_file = open('templates/json/distance/inches_to_yards.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'inches' and data['unitres'] == 'leagues' and trigger == 5:
        json_file = open('templates/json/distance/inches_to_leagues.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])

    elif data['unit'] == 'feet' and data['unitres'] == 'meters' and trigger == 5:
        json_file = open('templates/json/distance/feet_to_meters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'feet' and data['unitres'] == 'inches' and trigger == 5:
        json_file = open('templates/json/distance/feet_to_inches.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'feet' and data['unitres'] == 'feet' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'feet' and data['unitres'] == 'yards' and trigger == 5:
        json_file = open('templates/json/distance/feet_to_yards.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'feet' and data['unitres'] == 'leagues' and trigger == 5:
        json_file = open('templates/json/distance/feet_to_leagues.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])

    elif data['unit'] == 'yards' and data['unitres'] == 'meters' and trigger == 5:
        json_file = open('templates/json/distance/yards_to_meters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'yards' and data['unitres'] == 'inches' and trigger == 5:
        json_file = open('templates/json/distance/yards_to_inches.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'yards' and data['unitres'] == 'feet' and trigger == 5:
        json_file = open('templates/json/distance/yards_to_feet.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'yards' and data['unitres'] == 'yards' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'yards' and data['unitres'] == 'leagues' and trigger == 5:
        json_file = open('templates/json/distance/yards_to_leagues.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])

    elif data['unit'] == 'leagues' and data['unitres'] == 'meters' and trigger == 5:
        json_file = open('templates/json/distance/leagues_to_meters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'leagues' and data['unitres'] == 'inches' and trigger == 5:
        json_file = open('templates/json/distance/leagues_to_inches.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'leagues' and data['unitres'] == 'feet' and trigger == 5:
        json_file = open('templates/json/distance/leagues_to_feet.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'leagues' and data['unitres'] == 'yards' and trigger == 5:
        json_file = open('templates/json/distance/leagues_to_yards.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'leagues' and data['unitres'] == 'leagues' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    
    else:
        data['res'] = 1

    data['res'] = round_sig(data['res'], 6)
    return  render_template('dataconfig2.html', data=data)



"""REFERENCE PAGES"""

@app.route('/energy/ev_to_joules', endpoint='ev_to_joules')
def index():
    json_file = open('templates/json/ev_to_joules.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('ev_to_joules.html',data=data)


"""JSON PAGES"""

@app.route('/energy/ev_to_joules_json', endpoint='ev_to_joules_json')
def index():
    return  render_template('json/energy/ev_to_joules.json')

"""meters"""

@app.route('/distance/meters_to_inches_json', endpoint='meters_to_inches_json')
def index():
    return  render_template('json/distance/meters_to_inches.json')

@app.route('/distance/meters_to_feet_json', endpoint='meters_to_feet_json')
def index():
    return  render_template('json/distance/meters_to_feet.json')

@app.route('/distance/meters_to_yards_json', endpoint='meters_to_yards_json')
def index():
    return  render_template('json/distance/meters_to_yards.json')

@app.route('/distance/meters_to_leagues_json', endpoint='meters_to_leagues_json')
def index():
    return  render_template('json/distance/meters_to_leagues.json')

"""inches"""

@app.route('/distance/inches_to_meters_json', endpoint='inches_to_meters_json')
def index():
    return  render_template('json/distance/inches_to_meters.json')

@app.route('/distance/inches_to_feet_json', endpoint='inches_to_feet_json')
def index():
    return  render_template('json/distance/inches_to_feet.json')

@app.route('/distance/inches_to_yards_json', endpoint='inches_to_yards_json')
def index():
    return  render_template('json/distance/inches_to_yards.json')

@app.route('/distance/inches_to_leagues_json', endpoint='inches_to_leagues_json')
def index():
    return  render_template('json/distance/inches_to_leagues.json')

"""feet"""

@app.route('/distance/feet_to_meters_json', endpoint='feet_to_meters_json')
def index():
    return  render_template('json/distance/feet_to_meters.json')

@app.route('/distance/feet_to_inches_json', endpoint='feet_to_inches_json')
def index():
    return  render_template('json/distance/feet_to_inches.json')

@app.route('/distance/feet_to_yards_json', endpoint='feet_to_yards_json')
def index():
    return  render_template('json/distance/feet_to_yards.json')

@app.route('/distance/feet_to_leagues_json', endpoint='feet_to_leagues_json')
def index():
    return  render_template('json/distance/feet_to_leagues.json')

"""yards"""

@app.route('/distance/yards_to_meters_json', endpoint='yards_to_meters_json')
def index():
    return  render_template('json/distance/yards_to_meters.json')

@app.route('/distance/yards_to_inches_json', endpoint='yards_to_inches_json')
def index():
    return  render_template('json/distance/yards_to_inches.json')

@app.route('/distance/yards_to_feet_json', endpoint='yards_to_feet_json')
def index():
    return  render_template('json/distance/yards_to_feet.json')

@app.route('/distance/yards_to_leagues_json', endpoint='yards_to_leagues_json')
def index():
    return  render_template('json/distance/yards_to_leagues.json')

"""leagues"""

@app.route('/distance/leagues_to_meters_json', endpoint='leagues_to_meters_json')
def index():
    return  render_template('json/distance/leagues_to_meters.json')

@app.route('/distance/leagus_to_inches_json', endpoint='leagues_to_inches_json')
def index():
    return  render_template('json/distance/leagues_to_inches.json')

@app.route('/distance/leagues_to_feet_json', endpoint='leagues_to_feet_json')
def index():
    return  render_template('json/distance/leagues_to_feet.json')

@app.route('/distance/leagues_to_yards_json', endpoint='leagues_to_yards_json')
def index():
    return  render_template('json/distance/leagues_to_yards.json')


#add.app_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

