import os
import json
from flask import Flask
from flask import render_template
from flask import json

from wtforms import Form, BooleanField, TextField, PasswordField, validators


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

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
                                              validators.Required(),
                                              validators.EqualTo('confirm', message='Passwords must match')
                                              ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
