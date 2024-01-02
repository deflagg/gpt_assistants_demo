from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ThreadForm(FlaskForm):
    prompt = StringField('Prompt')
    submit = SubmitField('Send')
    messages = []