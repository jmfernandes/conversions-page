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
    global boo
    foo = request.form.get('units',None)
    boo = request.form.get('resultunit',None)
    data = {'num':0, 'unit':foo, 'unitres':boo, 'res':'', 'mainunit':''}
    data['unit'] = request.form.get('units',None)
    data['unitres'] = request.form.get('resultunit',None)
    data['mainunit'] = request.form.get('maincat',None)
    return  render_template('conversions.html',data=data)

@app.route('/data', methods =['GET','POST'])
def handle_data():
    data = {'num':0, 'unit':foo, 'unitres':boo, 'res':'', 'mainunit':''}
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
    elif data['unit'] == 'meters' and data['unitres'] == 'angstroms' and trigger == 5:
        json_file = open('templates/json/distance/meters_to_angstroms.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'meters' and data['unitres'] == 'astronomical unit' and trigger == 5:
        json_file = open('templates/json/distance/meters_to_astronomical_unit.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'meters' and data['unitres'] == 'light years' and trigger == 5:
        json_file = open('templates/json/distance/meters_to_light_years.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'meters' and data['unitres'] == 'centimeters' and trigger == 5:
        json_file = open('templates/json/distance/meters_to_centimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'meters' and data['unitres'] == 'millimeters' and trigger == 5:
        json_file = open('templates/json/distance/meters_to_millimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'meters' and data['unitres'] == 'nanometers' and trigger == 5:
        json_file = open('templates/json/distance/meters_to_nanometers.json')
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
    elif data['unit'] == 'inches' and data['unitres'] == 'angstroms' and trigger == 5:
        json_file = open('templates/json/distance/inches_to_angstroms.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'inches' and data['unitres'] == 'astronomical unit' and trigger == 5:
        json_file = open('templates/json/distance/inches_to_astronomical_unit.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'inches' and data['unitres'] == 'light years' and trigger == 5:
        json_file = open('templates/json/distance/inches_to_light_years.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'inches' and data['unitres'] == 'centimeters' and trigger == 5:
        json_file = open('templates/json/distance/inches_to_centimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'inches' and data['unitres'] == 'millimeters' and trigger == 5:
        json_file = open('templates/json/distance/inches_to_millimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'inches' and data['unitres'] == 'nanometers' and trigger == 5:
        json_file = open('templates/json/distance/inches_to_nanometers.json')
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
    elif data['unit'] == 'feet' and data['unitres'] == 'angstroms' and trigger == 5:
        json_file = open('templates/json/distance/feet_to_angstroms.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'feet' and data['unitres'] == 'astronomical unit' and trigger == 5:
        json_file = open('templates/json/distance/feet_to_astronomical_unit.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'feet' and data['unitres'] == 'light years' and trigger == 5:
        json_file = open('templates/json/distance/feet_to_light_years.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'feet' and data['unitres'] == 'centimeters' and trigger == 5:
        json_file = open('templates/json/distance/feet_to_centimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'feet' and data['unitres'] == 'millimeters' and trigger == 5:
        json_file = open('templates/json/distance/feet_to_millimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'feet' and data['unitres'] == 'nanometers' and trigger == 5:
        json_file = open('templates/json/distance/feet_to_nanometers.json')
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
    elif data['unit'] == 'yards' and data['unitres'] == 'angstroms' and trigger == 5:
        json_file = open('templates/json/distance/yards_to_angstroms.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'yards' and data['unitres'] == 'astronomical unit' and trigger == 5:
        json_file = open('templates/json/distance/yards_to_astronomical_unit.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'yards' and data['unitres'] == 'light years' and trigger == 5:
        json_file = open('templates/json/distance/yards_to_light_years.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'yards' and data['unitres'] == 'centimeters' and trigger == 5:
        json_file = open('templates/json/distance/yards_to_centimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'yards' and data['unitres'] == 'millimeters' and trigger == 5:
        json_file = open('templates/json/distance/yards_to_millimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'yards' and data['unitres'] == 'nanometers' and trigger == 5:
        json_file = open('templates/json/distance/yards_to_nanometers.json')
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
    elif data['unit'] == 'leagues' and data['unitres'] == 'angstroms' and trigger == 5:
        json_file = open('templates/json/distance/leagues_to_angstroms.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'leagues' and data['unitres'] == 'astronomical unit' and trigger == 5:
        json_file = open('templates/json/distance/leagues_to_astronomical_unit.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'leagues' and data['unitres'] == 'light years' and trigger == 5:
        json_file = open('templates/json/distance/leagues_to_light_years.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'leagues' and data['unitres'] == 'centimeters' and trigger == 5:
        json_file = open('templates/json/distance/leagues_to_centimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'leagues' and data['unitres'] == 'millimeters' and trigger == 5:
        json_file = open('templates/json/distance/leagues_to_millimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'leagues' and data['unitres'] == 'nanometers' and trigger == 5:
        json_file = open('templates/json/distance/leagues_to_nanometers.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])


    elif data['unit'] == 'angstroms' and data['unitres'] == 'meters' and trigger == 5:
        json_file = open('templates/json/distance/angstroms_to_meters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'angstroms' and data['unitres'] == 'inches' and trigger == 5:
        json_file = open('templates/json/distance/angstroms_to_inches.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'angstroms' and data['unitres'] == 'feet' and trigger == 5:
        json_file = open('templates/json/distance/angstroms_to_feet.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'angstroms' and data['unitres'] == 'yards' and trigger == 5:
        json_file = open('templates/json/distance/angstroms_to_yards.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'angstroms' and data['unitres'] == 'leagues' and trigger == 5:
        json_file = open('templates/json/distance/angstroms_to_leagues.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'angstroms' and data['unitres'] == 'angstroms' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'angstroms' and data['unitres'] == 'astronomical unit' and trigger == 5:
        json_file = open('templates/json/distance/angstroms_to_astronomical_unit.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'angstroms' and data['unitres'] == 'light years' and trigger == 5:
        json_file = open('templates/json/distance/angstroms_to_light_years.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'angstroms' and data['unitres'] == 'centimeters' and trigger == 5:
        json_file = open('templates/json/distance/angstroms_to_centimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'angstroms' and data['unitres'] == 'millimeters' and trigger == 5:
        json_file = open('templates/json/distance/angstroms_to_millimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'angstroms' and data['unitres'] == 'nanometers' and trigger == 5:
        json_file = open('templates/json/distance/angstroms_to_nanometers.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])


    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'meters' and trigger == 5:
        json_file = open('templates/json/distance/astronomical_unit_to_meters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'inches' and trigger == 5:
        json_file = open('templates/json/distance/astronomical_unit_to_inches.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'feet' and trigger == 5:
        json_file = open('templates/json/distance/astronomical_unit_to_feet.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'yards' and trigger == 5:
        json_file = open('templates/json/distance/astronomical_unit_to_yards.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'leagues' and trigger == 5:
        json_file = open('templates/json/distance/astronomical_unit_to_leagues.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'angstroms' and trigger == 5:
        json_file = open('templates/json/distance/astronomical_unit_to_angstroms.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'astronomical unit' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'light years' and trigger == 5:
        json_file = open('templates/json/distance/astronomical_unit_to_light_years.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'centimeters' and trigger == 5:
        json_file = open('templates/json/distance/astronomical_unit_to_centimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'millimeters' and trigger == 5:
        json_file = open('templates/json/distance/astronomical_unit_to_millimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'astronomical unit' and data['unitres'] == 'nanometers' and trigger == 5:
        json_file = open('templates/json/distance/astronomical_unit_to_nanometers.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])


    elif data['unit'] == 'light years' and data['unitres'] == 'meters' and trigger == 5:
        json_file = open('templates/json/distance/light_years_to_meters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'light years' and data['unitres'] == 'inches' and trigger == 5:
        json_file = open('templates/json/distance/light_years_to_inches.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'light years' and data['unitres'] == 'feet' and trigger == 5:
        json_file = open('templates/json/distance/light_years_to_feet.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'light years' and data['unitres'] == 'yards' and trigger == 5:
        json_file = open('templates/json/distance/light_years_to_yards.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'light years' and data['unitres'] == 'leagues' and trigger == 5:
        json_file = open('templates/json/distance/light_years_to_leagues.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'light years' and data['unitres'] == 'angstroms' and trigger == 5:
        json_file = open('templates/json/distance/light_years_to_angstroms.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'light years' and data['unitres'] == 'astronomical unit' and trigger == 5:
        json_file = open('templates/json/distance/light_years_to_astronomical_unit.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'light years' and data['unitres'] == 'light years' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'light years' and data['unitres'] == 'centimeters' and trigger == 5:
        json_file = open('templates/json/distance/light_years_to_centimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'light years' and data['unitres'] == 'millimeters' and trigger == 5:
        json_file = open('templates/json/distance/light_years_to_millimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'light years' and data['unitres'] == 'nanometers' and trigger == 5:
        json_file = open('templates/json/distance/light_years_to_nanometers.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])



    elif data['unit'] == 'centimeters' and data['unitres'] == 'meters' and trigger == 5:
        json_file = open('templates/json/distance/centimeters_to_meters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'centimeters' and data['unitres'] == 'inches' and trigger == 5:
        json_file = open('templates/json/distance/centimeters_to_inches.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'centimeters' and data['unitres'] == 'feet' and trigger == 5:
        json_file = open('templates/json/distance/centimeters_to_feet.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'centimeters' and data['unitres'] == 'yards' and trigger == 5:
        json_file = open('templates/json/distance/centimeters_to_yards.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'centimeters' and data['unitres'] == 'leagues' and trigger == 5:
        json_file = open('templates/json/distance/centimeters_to_leagues.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'centimeters' and data['unitres'] == 'angstroms' and trigger == 5:
        json_file = open('templates/json/distance/centimeters_to_angstroms.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'centimeters' and data['unitres'] == 'astronomical unit' and trigger == 5:
        json_file = open('templates/json/distance/centimeters_to_astronomical_unit.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'centimeters' and data['unitres'] == 'light years' and trigger == 5:
        json_file = open('templates/json/distance/centimeters_to_light_years.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'centimeters' and data['unitres'] == 'centimeters' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'centimeters' and data['unitres'] == 'millimeters' and trigger == 5:
        json_file = open('templates/json/distance/centimeters_to_millimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'centimeters' and data['unitres'] == 'nanometers' and trigger == 5:
        json_file = open('templates/json/distance/centimeters_to_nanometers.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])



    elif data['unit'] == 'millimeters' and data['unitres'] == 'meters' and trigger == 5:
        json_file = open('templates/json/distance/millimeters_to_meters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'millimeters' and data['unitres'] == 'inches' and trigger == 5:
        json_file = open('templates/json/distance/millimeters_to_inches.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'millimeters' and data['unitres'] == 'feet' and trigger == 5:
        json_file = open('templates/json/distance/millimeters_to_feet.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'millimeters' and data['unitres'] == 'yards' and trigger == 5:
        json_file = open('templates/json/distance/millimeters_to_yards.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'millimeters' and data['unitres'] == 'leagues' and trigger == 5:
        json_file = open('templates/json/distance/millimeters_to_leagues.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'millimeters' and data['unitres'] == 'angstroms' and trigger == 5:
        json_file = open('templates/json/distance/millimeters_to_angstroms.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'millimeters' and data['unitres'] == 'astronomical unit' and trigger == 5:
        json_file = open('templates/json/distance/millimeters_to_astronomical_unit.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'millimeters' and data['unitres'] == 'light years' and trigger == 5:
        json_file = open('templates/json/distance/millimeters_to_light_years.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'millimeters' and data['unitres'] == 'centimeters' and trigger == 5:
        json_file = open('templates/json/distance/millimeters_to_centimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'millimeters' and data['unitres'] == 'millimeters' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'millimeters' and data['unitres'] == 'nanometers' and trigger == 5:
        json_file = open('templates/json/distance/millimeters_to_nanometers.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])



    elif data['unit'] == 'nanometers' and data['unitres'] == 'meters' and trigger == 5:
        json_file = open('templates/json/distance/nanometers_to_meters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'nanometers' and data['unitres'] == 'inches' and trigger == 5:
        json_file = open('templates/json/distance/nanometers_to_inches.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'nanometers' and data['unitres'] == 'feet' and trigger == 5:
        json_file = open('templates/json/distance/nanometers_to_feet.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'nanometers' and data['unitres'] == 'yards' and trigger == 5:
        json_file = open('templates/json/distance/nanometers_to_yards.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'nanometers' and data['unitres'] == 'leagues' and trigger == 5:
        json_file = open('templates/json/distance/nanometers_to_leagues.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'nanometers' and data['unitres'] == 'angstroms' and trigger == 5:
        json_file = open('templates/json/distance/nanometers_to_angstroms.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'nanometers' and data['unitres'] == 'astronomical unit' and trigger == 5:
        json_file = open('templates/json/distance/nanometers_to_astronomical_unit.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'nanometers' and data['unitres'] == 'light years' and trigger == 5:
        json_file = open('templates/json/distance/nanometers_to_light_years.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'nanometers' and data['unitres'] == 'centimeters' and trigger == 5:
        json_file = open('templates/json/distance/nanometers_to_centimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'nanometers' and data['unitres'] == 'millimeters' and trigger == 5:
        json_file = open('templates/json/distance/nanometers_to_millimeters.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'nanometers' and data['unitres'] == 'nanometers' and trigger == 5:
        data['res'] = float(data['num'])*1.0


    elif data['unit'] == 'eV' and data['unitres'] == 'eV' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'eV' and data['unitres'] == 'Joules' and trigger == 5:
        json_file = open('templates/json/energy/eV_to_Joules.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'eV' and data['unitres'] == 'calories' and trigger == 5:
        json_file = open('templates/json/energy/eV_to_calories.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'eV' and data['unitres'] == 'Btu' and trigger == 5:
        json_file = open('templates/json/energy/eV_to_Btu.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])


    elif data['unit'] == 'Joules' and data['unitres'] == 'eV' and trigger == 5:
        json_file = open('templates/json/energy/Joules_to_eV.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'Joules' and data['unitres'] == 'Joules' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'Joules' and data['unitres'] == 'calories' and trigger == 5:
        json_file = open('templates/json/energy/Joules_to_calories.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'Joules' and data['unitres'] == 'Btu' and trigger == 5:
        json_file = open('templates/json/energy/Joules_to_Btu.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])


    elif data['unit'] == 'calories' and data['unitres'] == 'eV' and trigger == 5:
        json_file = open('templates/json/energy/calories_to_eV.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'calories' and data['unitres'] == 'Joules' and trigger == 5:
        json_file = open('templates/json/energy/calories_to_Joules.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'calories' and data['unitres'] == 'calories' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    elif data['unit'] == 'calories' and data['unitres'] == 'Btu' and trigger == 5:
        json_file = open('templates/json/energy/calories_to_Btu.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])


    elif data['unit'] == 'Btu' and data['unitres'] == 'eV' and trigger == 5:
        json_file = open('templates/json/energy/Btu_to_eV.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'Btu' and data['unitres'] == 'Joules' and trigger == 5:
        json_file = open('templates/json/energy/Btu_to_Joules.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'Btu' and data['unitres'] == 'calories' and trigger == 5:
        json_file = open('templates/json/energy/Btu_to_calories.json')
        jsondata = json.load(json_file)
        json_file.close()
        data['res'] = float(data['num'])*float(jsondata['value'])
    elif data['unit'] == 'Btu' and data['unitres'] == 'Btu' and trigger == 5:
        data['res'] = float(data['num'])*1.0
    
    else:
        data['res'] = "Result appears here"


    """rounds the numbers to 6 significant figures, unless not a number was entered"""

    if data['res'] == "Result appears here":
        pass
    else:
        data['res'] = round_sig(data['res'], 6)

    """return the webpage"""

    return  render_template('dataconfig2.html', data=data)



"""REFERENCE PAGES"""

#@app.route('/energy/ev_to_joules', endpoint='ev_to_joules')
#def index():
#    json_file = open('templates/json/eV_to_joules.json')
#    data = json.load(json_file)
#    json_file.close()
#    return  render_template('ev_to_joules.html',data=data)


"""JSON PAGES"""

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

@app.route('/distance/meters_to_angstroms_json', endpoint='meters_to_angstroms_json')
def index():
    return  render_template('json/distance/meters_to_angstroms.json')

@app.route('/distance/meters_to_astronomical_unit_json', endpoint='meters_to_astronomical_unit_json')
def index():
    return  render_template('json/distance/meters_to_astronomical_unit.json')

@app.route('/distance/meters_to_light_years_json', endpoint='meters_to_light_years_json')
def index():
    return  render_template('json/distance/meters_to_light_years.json')

@app.route('/distance/meters_to_centimeters_json', endpoint='meters_to_centimeters_json')
def index():
    return  render_template('json/distance/meters_to_centimeters.json')

@app.route('/distance/meters_to_millimeters_json', endpoint='meters_to_millimeters_json')
def index():
    return  render_template('json/distance/meters_to_millimeters.json')

@app.route('/distance/meters_to_nanometers_json', endpoint='meters_to_nanometers_json')
def index():
    return  render_template('json/distance/meters_to_nanometers.json')

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

@app.route('/distance/inches_to_angstroms_json', endpoint='inches_to_angstroms_json')
def index():
    return  render_template('json/distance/inches_to_angstroms.json')

@app.route('/distance/inches_to_astronomical_unit_json', endpoint='inches_to_astronomical_unit_json')
def index():
    return  render_template('json/distance/inches_to_astronomical_unit.json')

@app.route('/distance/inches_to_light_years_json', endpoint='inches_to_light_years_json')
def index():
    return  render_template('json/distance/inches_to_light_years.json')

@app.route('/distance/inches_to_centimeters_json', endpoint='inches_to_centimeters_json')
def index():
    return  render_template('json/distance/inches_to_centimeters.json')

@app.route('/distance/inches_to_millimeters_json', endpoint='inches_to_millimeters_json')
def index():
    return  render_template('json/distance/inches_to_millimeters.json')

@app.route('/distance/inches_to_nanometers_json', endpoint='inches_to_nanometers_json')
def index():
    return  render_template('json/distance/inches_to_nanometers.json')

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

@app.route('/distance/feet_to_angstroms_json', endpoint='feet_to_angstroms_json')
def index():
    return  render_template('json/distance/feet_to_angstroms.json')

@app.route('/distance/feet_to_astronomical_unit_json', endpoint='feet_to_astronomical_unit_json')
def index():
    return  render_template('json/distance/feet_to_astronomical_unit.json')

@app.route('/distance/feet_to_light_years_json', endpoint='feet_to_light_years_json')
def index():
    return  render_template('json/distance/feet_to_light_years.json')

@app.route('/distance/feet_to_centimeters_json', endpoint='feet_to_centimeters_json')
def index():
    return  render_template('json/distance/feet_to_centimeters.json')

@app.route('/distance/feet_to_millimeters_json', endpoint='feet_to_millimeters_json')
def index():
    return  render_template('json/distance/feet_to_millimeters.json')

@app.route('/distance/feet_to_nanometers_json', endpoint='feet_to_nanometers_json')
def index():
    return  render_template('json/distance/feet_to_nanometers.json')

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

@app.route('/distance/yards_to_angstroms_json', endpoint='yards_to_angstroms_json')
def index():
    return  render_template('json/distance/yards_to_angstroms.json')

@app.route('/distance/yards_to_astronomical_unit_json', endpoint='yards_to_astronomical_unit_json')
def index():
    return  render_template('json/distance/yards_to_astronomical_unit.json')

@app.route('/distance/yards_to_light_years_json', endpoint='yards_to_light_years_json')
def index():
    return  render_template('json/distance/yards_to_light_years.json')

@app.route('/distance/yards_to_centimeters_json', endpoint='yards_to_centimeters_json')
def index():
    return  render_template('json/distance/yards_to_centimeters.json')

@app.route('/distance/yards_to_millimeters_json', endpoint='yards_to_millimeters_json')
def index():
    return  render_template('json/distance/yards_to_millimeters.json')

@app.route('/distance/yards_to_nanometers_json', endpoint='yards_to_nanometers_json')
def index():
    return  render_template('json/distance/yards_to_nanometers.json')

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

@app.route('/distance/leagues_to_angstroms_json', endpoint='leagues_to_angstroms_json')
def index():
    return  render_template('json/distance/leagues_to_angstroms.json')

@app.route('/distance/leagues_to_astronomical_unit_json', endpoint='leagues_to_astronomical_unit_json')
def index():
    return  render_template('json/distance/leagues_to_astronomical_unit.json')

@app.route('/distance/leagues_to_light_years_json', endpoint='leagues_to_light_years_json')
def index():
    return  render_template('json/distance/leagues_to_light_years.json')

@app.route('/distance/leagues_to_centimeters_json', endpoint='leagues_to_centimeters_json')
def index():
    return  render_template('json/distance/leagues_to_centimeters.json')

@app.route('/distance/leagues_to_millimeters_json', endpoint='leagues_to_millimeters_json')
def index():
    return  render_template('json/distance/meters_to_millimeters.json')

@app.route('/distance/leagues_to_nanometers_json', endpoint='leagues_to_nanometers_json')
def index():
    return  render_template('json/distance/meters_to_nanometers.json')

"""Angstroms"""
@app.route('/distance/angstroms_to_meters_json', endpoint='angstroms_to_meters_json')
def index():
    return  render_template('json/distance/angstroms_to_meters.json')

@app.route('/distance/angstroms_to_inches_json', endpoint='angstroms_to_inches_json')
def index():
    return  render_template('json/distance/angstroms_to_inches.json')

@app.route('/distance/angstroms_to_feet_json', endpoint='angstroms_to_feet_json')
def index():
    return  render_template('json/distance/angstroms_to_feet.json')

@app.route('/distance/angstroms_to_yards_json', endpoint='angstroms_to_yards_json')
def index():
    return  render_template('json/distance/angstroms_to_yards.json')

@app.route('/distance/angstroms_to_leagues_json', endpoint='angstroms_to_leagues_json')
def index():
    return  render_template('json/distance/angstroms_to_leagues.json')

@app.route('/distance/angstroms_to_astronomical_unit_json', endpoint='angstroms_to_astronomical_unit_json')
def index():
    return  render_template('json/distance/angstroms_to_astronomical_unit.json')

@app.route('/distance/angstroms_to_light_years_json', endpoint='angstroms_to_light_years_json')
def index():
    return  render_template('json/distance/angstroms_to_light_years.json')

@app.route('/distance/angstroms_to_centimeters_json', endpoint='angstroms_to_centimeters_json')
def index():
    return  render_template('json/distance/angstroms_to_centimeters.json')

@app.route('/distance/angstroms_to_millimeters_json', endpoint='angstroms_to_millimeters_json')
def index():
    return  render_template('json/distance/angstroms_to_millimeters.json')

@app.route('/distance/angstroms_to_nanometers_json', endpoint='angstroms_to_nanometers_json')
def index():
    return  render_template('json/distance/angstroms_to_nanometers.json')

"""astronomical unit"""
@app.route('/distance/astronomical_unit_to_meters_json', endpoint='astronomical_unit_to_meters_json')
def index():
    return  render_template('json/distance/astronomical_unit_to_meters.json')

@app.route('/distance/astronomical_unit_to_inches_json', endpoint='astronomical_unit_to_inches_json')
def index():
    return  render_template('json/distance/astronomical_unit_to_inches.json')

@app.route('/distance/astronomical_unit_to_feet_json', endpoint='astronomical_unit_to_feet_json')
def index():
    return  render_template('json/distance/astronomical_unit_to_feet.json')

@app.route('/distance/astronomical_unit_to_yards_json', endpoint='astronomical_unit_to_yards_json')
def index():
    return  render_template('json/distance/astronomical_unit_to_yards.json')

@app.route('/distance/astronomical_unit_to_leagues_json', endpoint='astronomical_unit_to_leagues_json')
def index():
    return  render_template('json/distance/astronomical_unit_to_leagues.json')

@app.route('/distance/astronomical_unit_to_angstroms_json', endpoint='astronomical_unit_to_angstroms_json')
def index():
    return  render_template('json/distance/astronomical_unit_to_angstroms.json')

@app.route('/distance/astronomical_unit_to_light_years_json', endpoint='astronomical_unit_to_light_years_json')
def index():
    return  render_template('json/distance/astronomical_unit_to_light_years.json')

@app.route('/distance/astronomical_unit_to_centimeters_json', endpoint='astronomical_unit_to_centimeters_json')
def index():
    return  render_template('json/distance/astronomical_unit_to_centimeters.json')

@app.route('/distance/astronomical_unit_to_millimeters_json', endpoint='astronomical_unit_to_millimeters_json')
def index():
    return  render_template('json/distance/astronomical_unit_to_millimeters.json')

@app.route('/distance/astronomical_unit_to_nanometers_json', endpoint='astronomical_unit_to_nanometers_json')
def index():
    return  render_template('json/distance/astronomical_unit_to_nanometers.json')


"""light years"""
@app.route('/distance/light_years_to_meters_json', endpoint='light_years_to_meters_json')
def index():
    return  render_template('json/distance/light_years_to_meters.json')

@app.route('/distance/light_years_to_inches_json', endpoint='light_years_to_inches_json')
def index():
    return  render_template('json/distance/light_years_to_inches.json')

@app.route('/distance/light_years_to_feet_json', endpoint='light_years_to_feet_json')
def index():
    return  render_template('json/distance/light_years_to_feet.json')

@app.route('/distance/light_years_to_yards_json', endpoint='light_years_to_yards_json')
def index():
    return  render_template('json/distance/light_years_to_yards.json')

@app.route('/distance/light_years_to_leagues_json', endpoint='light_years_to_leagues_json')
def index():
    return  render_template('json/distance/light_years_to_leagues.json')

@app.route('/distance/light_years_to_angstroms_json', endpoint='light_years_to_angstroms_json')
def index():
    return  render_template('json/distance/light_years_to_angstroms.json')

@app.route('/distance/light_years_to_astronomical_unit_json', endpoint='light_years_to_astronomical_unit_json')
def index():
    return  render_template('json/distance/light_years_to_astronomical_unit.json')

@app.route('/distance/light_years_to_centimeters_json', endpoint='light_years_to_centimeters_json')
def index():
    return  render_template('json/distance/light_years_to_centimeters.json')

@app.route('/distance/light_years_to_millimeters_json', endpoint='light_years_to_millimeters_json')
def index():
    return  render_template('json/distance/light_years_to_millimeters.json')

@app.route('/distance/light_years_to_nanometers_json', endpoint='light_years_to_nanometers_json')
def index():
    return  render_template('json/distance/light_years_to_nanometers.json')


"""centimeters"""
@app.route('/distance/centimeters_to_meters_json', endpoint='centimeters_to_meters_json')
def index():
    return  render_template('json/distance/centimeters_to_meters.json')

@app.route('/distance/centimeters_to_inches_json', endpoint='centimeters_to_inches_json')
def index():
    return  render_template('json/distance/centimeters_to_inches.json')

@app.route('/distance/centimeters_to_feet_json', endpoint='centimeters_to_feet_json')
def index():
    return  render_template('json/distance/centimeters_to_feet.json')

@app.route('/distance/centimeters_to_yards_json', endpoint='centimeters_to_yards_json')
def index():
    return  render_template('json/distance/centimeters_to_yards.json')

@app.route('/distance/centimeters_to_leagues_json', endpoint='centimeters_to_leagues_json')
def index():
    return  render_template('json/distance/centimeters_to_leagues.json')

@app.route('/distance/centimeters_to_angstroms_json', endpoint='centimeters_to_angstroms_json')
def index():
    return  render_template('json/distance/centimeters_to_angstroms.json')

@app.route('/distance/centimeters_to_astronomical_unit_json', endpoint='centimeters_to_astronomical_unit_json')
def index():
    return  render_template('json/distance/centimeters_to_astronomical_unit.json')

@app.route('/distance/centimeters_to_light_years_json', endpoint='centimeters_to_light_years_json')
def index():
    return  render_template('json/distance/centimeters_to_light_years.json')

@app.route('/distance/centimeters_to_millimeters_json', endpoint='centimeters_to_millimeters_json')
def index():
    return  render_template('json/distance/centimeters_to_millimeters.json')

@app.route('/distance/centimeters_to_nanometers_json', endpoint='centimeters_to_nanometers_json')
def index():
    return  render_template('json/distance/centimeters_to_nanometers.json')


"""millimeters"""
@app.route('/distance/millimeters_to_meters_json', endpoint='millimeters_to_meters_json')
def index():
    return  render_template('json/distance/millimeters_to_meters.json')

@app.route('/distance/millimeters_to_inches_json', endpoint='millimeters_to_inches_json')
def index():
    return  render_template('json/distance/millimeters_to_inches.json')

@app.route('/distance/millimeters_to_feet_json', endpoint='millimeters_to_feet_json')
def index():
    return  render_template('json/distance/millimeters_to_feet.json')

@app.route('/distance/millimeters_to_yards_json', endpoint='millimeters_to_yards_json')
def index():
    return  render_template('json/distance/millimeters_to_yards.json')

@app.route('/distance/millimeters_to_leagues_json', endpoint='millimeters_to_leagues_json')
def index():
    return  render_template('json/distance/millimeters_to_leagues.json')

@app.route('/distance/millimeters_to_angstroms_json', endpoint='millimeters_to_angstroms_json')
def index():
    return  render_template('json/distance/millimeters_to_angstroms.json')

@app.route('/distance/millimeters_to_astronomical_unit_json', endpoint='millimeters_to_astronomical_unit_json')
def index():
    return  render_template('json/distance/millimeters_to_astronomical_unit.json')

@app.route('/distance/millimeters_to_light_years_json', endpoint='millimeters_to_light_years_json')
def index():
    return  render_template('json/distance/millimeters_to_light_years.json')

@app.route('/distance/millimeters_to_centimeters_json', endpoint='millimeters_to_centimeters_json')
def index():
    return  render_template('json/distance/millimeters_to_centimeters.json')

@app.route('/distance/millimeters_to_nanometers_json', endpoint='millimeters_to_nanometers_json')
def index():
    return  render_template('json/distance/millimeters_to_nanometers.json')


"""nanometers"""
@app.route('/distance/nanometers_to_meters_json', endpoint='nanometers_to_meters_json')
def index():
    return  render_template('json/distance/nanometers_to_meters.json')

@app.route('/distance/nanometers_to_inches_json', endpoint='nanometers_to_inches_json')
def index():
    return  render_template('json/distance/nanometers_to_inches.json')

@app.route('/distance/nanometers_to_feet_json', endpoint='nanometers_to_feet_json')
def index():
    return  render_template('json/distance/nanometers_to_feet.json')

@app.route('/distance/nanometers_to_yards_json', endpoint='nanometers_to_yards_json')
def index():
    return  render_template('json/distance/nanometers_to_yards.json')

@app.route('/distance/nanometers_to_leagues_json', endpoint='nanometers_to_leagues_json')
def index():
    return  render_template('json/distance/nanometers_to_leagues.json')

@app.route('/distance/nanometers_to_angstroms_json', endpoint='nanometers_to_angstroms_json')
def index():
    return  render_template('json/distance/nanometers_to_angstroms.json')

@app.route('/distance/nanometers_to_astronomical_unit_json', endpoint='nanometers_to_astronomical_unit_json')
def index():
    return  render_template('json/distance/nanometers_to_astronomical_unit.json')

@app.route('/distance/nanometers_to_light_years_json', endpoint='nanometers_to_light_years_json')
def index():
    return  render_template('json/distance/nanometers_to_light_years.json')

@app.route('/distance/nanometers_to_centimeters_json', endpoint='nanometers_to_centimeters_json')
def index():
    return  render_template('json/distance/nanometers_to_centimeters.json')

@app.route('/distance/nanometers_to_millimeters_json', endpoint='nanometers_to_millimeters_json')
def index():
    return  render_template('json/distance/nanometers_to_millimeters.json')


"""eV"""
@app.route('/energy/eV_to_Joules_json', endpoint='eV_to_Joules_json')
def index():
    return  render_template('json/energy/eV_to_Joules.json')

@app.route('/energy/eV_to_calories_json', endpoint='eV_to_calories_json')
def index():
    return  render_template('json/energy/eV_to_calories.json')

@app.route('/energy/eV_to_Btu_json', endpoint='eV_to_Btu_json')
def index():
    return  render_template('json/energy/eV_to_Btu.json')


"""Joules"""
@app.route('/energy/Joules_to_eV_json', endpoint='Joules_to_eV_json')
def index():
    return  render_template('json/energy/Joules_to_eV.json')

@app.route('/energy/Joules_to_calories_json', endpoint='Joules_to_calories_json')
def index():
    return  render_template('json/energy/Joules_to_calories.json')

@app.route('/energy/Joules_to_Btu_json', endpoint='Joules_to_Btu_json')
def index():
    return  render_template('json/energy/Joules_to_Btu.json')


"""calories"""
@app.route('/energy/calories_to_eV_json', endpoint='calories_to_eV_json')
def index():
    return  render_template('json/energy/calories_to_eV.json')

@app.route('/energy/calories_to_Joules_json', endpoint='calories_to_Joules_json')
def index():
    return  render_template('json/energy/calories_to_Joules.json')

@app.route('/energy/calories_to_Btu_json', endpoint='calories_to_Btu_json')
def index():
    return  render_template('json/energy/calories_to_Btu.json')


"""Btu"""
@app.route('/energy/Btu_to_Joules_json', endpoint='Btu_to_Joules_json')
def index():
    return  render_template('json/energy/Btu_to_Joules.json')

@app.route('/energy/Btu_to_calories_json', endpoint='Btu_to_calories_json')
def index():
    return  render_template('json/energy/Btu_to_calories.json')

@app.route('/energy/Btu_to_eV_json', endpoint='Btu_to_eV_json')
def index():
    return  render_template('json/energy/Btu_to_eV.json')

#add.app_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

