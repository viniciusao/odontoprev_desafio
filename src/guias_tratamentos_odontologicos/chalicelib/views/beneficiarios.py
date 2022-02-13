import os

from chalice import Blueprint

from ..helpers import cadastrar_info, get_view
from ..schemas import CadastroBeneficiario


beneficiarios_b = Blueprint(__name__)
PATH = '/beneficiarios'


@beneficiarios_b.route(PATH)
def get():
    return get_view(
        os.environ.get('TABLE_BENEFICIARIOS', 'beneficiarios'),
        PATH[1:],
        beneficiarios_b.current_request.query_params
    )


@beneficiarios_b.route(PATH, methods=['POST'])
def cadastrar():
    return cadastrar_info(
        os.environ['TABLE_BENEFICIARIOS'],
        beneficiarios_b.current_request.json_body,
        CadastroBeneficiario
    )