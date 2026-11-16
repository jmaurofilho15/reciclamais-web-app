from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length

class ColetaForm(FlaskForm):
    tipo_material = RadioField(
        'Tipo de Material',
        choices=[
            ('Plástico PET', 'Plástico PET'),
            ('Papel / Papelão', 'Papel / Papelão'),
            ('Metal / Latas', 'Metal / Latas'),
            ('Vidro Limpo', 'Vidro Limpo')
        ],
        validators=[DataRequired(message="Selecione um tipo de material.")]
    )
    nome = StringField('Nome Completo', validators=[DataRequired(), Length(min=3, max=100)])
    telefone = StringField('Telefone / WhatsApp', validators=[DataRequired(), Length(min=10, max=15)])
    cep = StringField('CEP', validators=[DataRequired(), Length(min=8, max=9)])
    endereco = StringField('Endereço / Lote', validators=[DataRequired(), Length(min=2, max=150)])
    submit = SubmitField('Enviar Solicitação de Coleta')