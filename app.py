import os
import json
from flask import Flask
from flask import render_template
from flask import json


app = Flask(__name__)


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


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/',methods=['GET','POST'])
def index():
    return  render_template('conversions.html')

@app.route('/data', methods =['POSt'])
def index():
    return  render_template('constants.html')

@app.route('/energy/ev_to_joules', endpoint='ev_to_joules')
def index():
    json_file = open('templates/json/ev_to_joules.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('ev_to_joules.html',data=data)

@app.route('/energy/ev_to_joules_json', endpoint='ev_to_joules_json')
def index():
    return  render_template('json/ev_to_joules.json')

#add.app_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
