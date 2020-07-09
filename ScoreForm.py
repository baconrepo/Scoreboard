from wtforms import Form, StringField, SelectField

class ScoreForm(Form):
  name=StringField('Name')
  score=StringField('Score')
