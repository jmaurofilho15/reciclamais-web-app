from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class ColetaForm(FlaskForm):
    tipo_material = SelectField('Tipo de Material', choices=[
        ('Papel / Papelão', 'Papel / Papelão'),
        ('Plástico PET', 'Plástico PET'),
        ('Metal / Latas', 'Metal / Latas'),
        ('Vidro Limpo', 'Vidro Limpo')
    ], validators=[DataRequired()])
    
    nome = StringField('Nome Completo', validators=[DataRequired(), Length(min=3, max=100)])
    telefone = StringField('Telefone / WhatsApp', validators=[DataRequired(), Length(min=10, max=20)])
    cep = StringField('CEP', validators=[DataRequired(), Length(min=8, max=10)])
    endereco = StringField('Número / Lote', validators=[DataRequired(), Length(min=1, max=200)])
    submit = SubmitField('Enviar Solicitação de Coleta')