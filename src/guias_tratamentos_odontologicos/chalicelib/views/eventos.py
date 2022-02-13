import os

from chalice import Blueprint

from ..helpers import cadastrar_info, get_view


eventos_b = Blueprint(__name__)
PATH = '/eventos'


@eventos_b.route(PATH)
def get():
    return get_view(
        os.environ['TABLE_EVENTOS'],
        PATH[1:],
        eventos_b.current_request.query_params
    )


@eventos_b.route(PATH, methods=['POST'])
def cadastrar():
    return cadastrar_info(
        os.environ['TABLE_EVENTOS'],
        eventos_b.current_request.json_body
    )