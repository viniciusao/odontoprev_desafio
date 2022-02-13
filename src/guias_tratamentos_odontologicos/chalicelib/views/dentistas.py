import os

from chalice import Blueprint

from ..helpers import cadastrar_info, get_view
from ..schemas import CadastroDentista


dentistas_b = Blueprint(__name__)
PATH = '/dentistas'


@dentistas_b.route(PATH)
def get():
    return get_view(
        os.environ['TABLE_DENTISTAS'],
        PATH[1:],
        dentistas_b.current_request.query_params
    )


@dentistas_b.route(PATH, methods=['POST'])
def cadastrar():
    body = dentistas_b.current_request.json_body
    CadastroDentista().load(dentistas_b.current_request.json_body)
    body['especialidades'] = str(body['especialidades'])
    return cadastrar_info(
        os.environ['TABLE_DENTISTAS'],
        body
    )