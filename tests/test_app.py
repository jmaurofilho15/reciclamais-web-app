import pytest
from app import create_app, db
from app.models import PedidoColeta

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False  # Desativa CSRF apenas no ambiente de testes

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_rotas_principais(client):
    """Valida se as telas principais carregam corretamente (HTTP 200)."""
    assert client.get('/').status_code == 200
    assert client.get('/formulario').status_code == 200
    assert client.get('/status').status_code == 200
    assert client.get('/gestao').status_code == 200

def test_fluxo_completo_doacao_e_gestao(client):
    """Testa a criação de um pedido no formulário e a baixa no painel de gestão."""
    # 1. Submete uma nova doação via formulário
    resposta_post = client.post('/formulario', data={
        'tipo_material': 'Plástico PET',
        'nome': 'Roberto Mendes',
        'telefone': '(61) 98888-7777',
        'cep': '70000-000',
        'endereco': 'Quadra 10 Lote 5',
        'referencia_volume': 'Portão verde / 2 sacos'
    }, follow_redirects=True)

    assert resposta_post.status_code == 200
    assert b'Doa\xc3\xa7\xc3\xa3o Registrada com Sucesso!' in resposta_post.data

    # 2. Verifica se o registro foi salvo no banco de dados
    with client.application.app_context():
        pedido = PedidoColeta.query.first()
        assert pedido is not None
        assert pedido.nome == 'Roberto Mendes'
        assert pedido.status == 'Aguardando Coleta'
        pedido_id = pedido.id

    # 3. Conclui o pedido pelo painel de gestão (RF02)
    resposta_baixa = client.post(f'/concluir/{pedido_id}', follow_redirects=True)
    assert resposta_baixa.status_code == 200

    with client.application.app_context():
        pedido_atualizado = PedidoColeta.query.get(pedido_id)
        assert pedido_atualizado.status == 'Coletado'