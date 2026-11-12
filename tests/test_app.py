import os
import unittest
from app import create_app, db
from app.models import Doador, PedidoColeta

class ReciclaMaisTestCase(unittest.TestCase):
    def setUp(self):
        """Configura o ambiente de testes com banco em memória"""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['WTF_CSRF_ENABLED'] = False  # Desativa CSRF para facilitar testes de formulário
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Limpa o banco de dados após cada teste"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index_route(self):
        """Testa se a página inicial (Menu Inicial) carrega com status 200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ReciclaMais Web App', response.data)

    def test_formulario_e_cadastro_coleta(self):
        """Testa o envio do formulário de coleta e a persistência no banco de dados"""
        response = self.client.post('/formulario', data={
            'tipo_material': 'Plástico PET',
            'nome': 'Maria Aparecida',
            'telefone': '61988887777',
            'cep': '70000000',
            'endereco': 'Lote 12'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Doacao Registrada com Sucesso!', response.data)
        
        # Verifica se o doador e o pedido foram salvos no banco
        with self.app.app_context():
            doador = Doador.query.first()
            self.assertIsNotNone(doador)
            self.assertEqual(doador.nome, 'Maria Aparecida')
            
            pedido = PedidoColeta.query.first()
            self.assertIsNotNone(pedido)
            self.assertEqual(pedido.tipo_material, 'Plástico PET')

if __name__ == '__main__':
    unittest.main()