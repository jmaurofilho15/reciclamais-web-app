from flask import render_template, redirect, url_for, request
from app import db
from app.models import PedidoColeta
from app.forms import ColetaForm
import random

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/formulario', methods=['GET', 'POST'])
    def formulario():
        form = ColetaForm()
        if form.validate_on_submit():
            numero_pedido = f"#REC-{random.randint(1000, 9999)}"
            novo_pedido = PedidoColeta(
                tipo_material=form.tipo_material.data,
                nome=form.nome.data,
                telefone=form.telefone.data,
                cep=form.cep.data,
                endereco=form.endereco.data,
                numero_pedido=numero_pedido
            )
            db.session.add(novo_pedido)
            db.session.commit()
            return redirect(url_for('confirmacao', pedido_id=novo_pedido.id))
        return render_template('formulario.html', form=form)

    @app.route('/confirmacao/<int:pedido_id>')
    def confirmacao(pedido_id):
        pedido = PedidoColeta.query.get_or_404(pedido_id)
        return render_template('confirmacao.html', pedido=pedido)