from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

# http = "https://"
# location = []
# location_ = 0


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(), ])
    location = URLField(label="location", validators=[DataRequired(), URL()])
    Open = StringField("opening **AM or **PM", validators=[DataRequired()])
    Close = StringField("Closing **PM or **AM", validators=[DataRequired()])
    Wifi = SelectField(label="wifi rating", choices=["✘","💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"])
    Power = SelectField(label="power rating", choices=["✘","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"])
    Coffee = SelectField(label="Coffee Rating", choices=["✘","☕️","☕️☕️","☕️☕️☕️","☕️☕️☕️☕️","☕️☕️☕️☕️☕️"])
    submit = SubmitField('Submit')
# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        # location.append(form.location.data)
        with open("cafe-data.csv", "a", encoding='utf-8') as file:
            file.write(f"{form.cafe.data},{form.location.data},{form.Open.data},{form.Close.data},{form.Coffee.data},{form.Wifi.data},{form.Power.data}\n")
            file.close()
            # location.clear()
        # for i in location:
        #     location_link = http + i



    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows, raw_data=csv_file)


if __name__ == '__main__':
    app.run(debug=True)
