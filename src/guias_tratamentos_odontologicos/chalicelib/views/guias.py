import os

from chalice import Blueprint, Response

from ..helpers import cadastrar_info, get_view
from ..interfaces.db import SqliteOps
from ..interfaces.motor_regras import Eventos
from ..middlewares import get_infos


guias_b = Blueprint(__name__)
PATH = '/guias'
regras = Eventos()


# ---- MIDDLEWAREs ----

@guias_b.middleware('http')
def check_beneficiario(event, get_response):
    if event.path == PATH and event.method == 'POST':
        if get_infos(
            path='beneficiarios',
            query='carteirinha',
            value=event.json_body.get('beneficiario')
        ).status_code != 200:

            return Response(
                body={'error': 'beneficiario não achado'},
                status_code=404
            )

    return get_response(event)


@guias_b.middleware('http')
def check_eventos(event, get_response):
    if event.path == PATH and event.method == 'POST':
        cod_evento = event.json_body.get('evento')
        if get_infos(
            path='eventos',
            query='codigo',
            value=cod_evento
        ).status_code != 200:

            return Response(
                body={'error': f'evento <{cod_evento}> não achado'},
                status_code=404
            )

    return get_response(event)


@guias_b.middleware('http')
def check_regras_de_negocios(event, get_response):
    if event.path == PATH and event.method == 'POST':
        body = event.json_body
        evento = body.get('evento')
        beneficiario = body.get('beneficiario')
        data_execucao = body.get('data_execucao')
        cursor = SqliteOps(db=os.environ['DATABASE_FILE']).cursor
        if regras.eventos_por_periodicidade(evento, beneficiario, data_execucao, cursor):
            print('ahiu')
            return Response(
                body={'error': 'data de execução não disponível.'},
                status_code=400
            )
        if regras.eventos_por_idade(evento, beneficiario):
            return Response(
                body={'error': 'evento não permitido devido a idade do beneficiário.'},
                status_code=400
            )

    return get_response(event)

# ---- VIEWs ----

@guias_b.route(PATH)
def get():
    return get_view(
        os.environ['TABLE_GUIAS'],
        PATH[1:],
        guias_b.current_request.query_params
    )


@guias_b.route(PATH, methods=['POST'])
def cadastrar():
    return cadastrar_info(
        os.environ['TABLE_GUIAS'],
        guias_b.current_request.json_body
    )
