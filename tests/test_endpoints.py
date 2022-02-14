""" Este módulo é apenas para demonstrar uma funcionalidade
do chalice para desenvolver os endpoints por teste. """

from chalice.test import Client
from guias_tratamentos_odontologicos.app import app

def test_cadastro_beneficiarios():
    with Client(app) as client:
        response = client.http.get('/beneficiarios')
        assert 'error' in response.body.decode()