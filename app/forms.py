  
from flask_wtf import FlaskForm
from wtforms import  TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])