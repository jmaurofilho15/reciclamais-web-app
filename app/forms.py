# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length

class ColetaForm(FlaskForm):
    # RadioField com as opções exatas utilizadas nos cards visuais
    tipo_material = RadioField(
        'Tipo de Material', 
        choices=[
            ('Plástico PET', 'Plástico PET'),
            ('Papel / Papelão', 'Papel / Papelão'),
            ('Metal / Latas', 'Metal / Latas'),
            ('Vidro Limpo', 'Vidro Limpo')
        ], 
        validators=[DataRequired(message="Selecione um material.")]
    )
    
    nome = StringField('Nome Completo', validators=[DataRequired(), Length(min=3, max=100)])
    telefone = StringField('Telefone', validators=[DataRequired(), Length(min=10, max=15)])
    cep = StringField('CEP', validators=[DataRequired(), Length(min=8, max=9)])
    endereco = StringField('Endereço e Número', validators=[DataRequired(), Length(min=5, max=200)])
    referencia_volume = StringField('Ponto de Referência / Volume')
    
    submit = SubmitField('Enviar Solicitação')