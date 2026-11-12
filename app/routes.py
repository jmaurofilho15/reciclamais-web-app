from flask import render_template, redirect, url_for, request
from app import db
from app.models import Doador, PedidoColeta
from app.forms import ColetaForm

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/formulario', methods=['GET', 'POST'])
    def formulario():
        form = ColetaForm()
        if form.validate_on_submit():
            # Verifica se o doador já existe pelo telefone ou cadastra um novo
            doador = Doador.query.filter_by(telefone=form.telefone.data).first()
            if not doador:
                doador = Doador(
                    nome=form.nome.data,
                    telefone=form.telefone.data,
                    cep=form.cep.data,
                    endereco=form.endereco.data
                )
                db.session.add(doador)
                db.session.commit()

            # Criação do pedido de coleta vinculado ao doador
            novo_pedido = PedidoColeta(
                id_doador=doador.id_doador,
                tipo_material=form.tipo_material.data,
                volume_estimado='Volume Padrão MVP',
                status_pedido='Pendente'
            )
            db.session.add(novo_pedido)
            db.session.commit()

            return redirect(url_for('confirmacao', id_pedido=novo_pedido.id_pedido))
        
        return render_template('formulario.html', form=form)

    @app.route('/confirmacao/<int:id_pedido>')
    def confirmacao(id_pedido):
        pedido = PedidoColeta.query.get_or_404(id_pedido)
        codigo_formatado = f"#REC-{pedido.id_pedido + 8400}" # Alinhado visualmente ao wireframe
        return render_template('confirmacao.html', pedido=pedido, codigo_formatado=codigo_formatado)