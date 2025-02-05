from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import fields, validators
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

admin_email = "admin@gmail.com"
admin_password = "76102005"


class MyForm(FlaskForm):
    password = fields.StringField(label="password", validators=[validators.Length(min=8, max=20)])
    Email = fields.EmailField(label="Email", validators=[validators.Email(message="Must enter email")])
    submit = fields.SubmitField(label="Enter")


app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = "HelloWorld"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    form = MyForm()
    return_data = form.data
    if form.validate_on_submit():
        if return_data["Email"] == admin_email and return_data["password"] == admin_password:
            print(return_data)
            return render_template("success.html")
        else:
            print(return_data)
            return render_template("denied.html")

    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
