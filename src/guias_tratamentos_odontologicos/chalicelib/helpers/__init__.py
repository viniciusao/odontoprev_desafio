""" este package contém funções que auxiliam em
certas tarefas que são repetitivas e frequentemente usadas. """

import builtins
from datetime import date, datetime
import os
import pathlib
from typing import (
    Collection,
    Dict,
    List,
    Mapping,
    Optional,
    Union
)

from chalice import Response
from marshmallow import ValidationError
from marshmallow.schema import SchemaMeta

from guias_tratamentos_odontologicos.chalicelib.interfaces.db import SqliteOps

TOTEST_DB_PATH = pathlib.Path(__file__).parent.parent.parent.joinpath('guias_tratamentos_odontologicos.db').resolve()
DATABASE_FILE = os.environ.get('DATABASE_FILE', TOTEST_DB_PATH)

# ---- CHALICE VIEWs ----

# GLOBAL
def get_view(
    table: builtins.str,
    context_path: builtins.str,
    query_params: Mapping[builtins.str, builtins.str] = None
) -> Union[Collection[Collection[str]], Response]:

    infos = _get_infos(table, query_params)
    if not infos:
        return Response(
            body={'error': f'não há {context_path} cadastrados'},
            status_code=404
        )
    return infos

# GLOBAL
def _get_infos(
        table: builtins.str,
        query_params: Mapping[builtins.str, builtins.str] = None
) -> Union[Optional[Collection[Collection[Union[str, str]]]], Response]:

    cursor = SqliteOps(db=DATABASE_FILE)
    if query_params and len(query_params) == 1:
        field, value = next(iter(query_params.items()))
        infos = cursor.retrieve(
            table=table,
            field_condition={field: value}
        )
        if not infos:
            return Response(
                body={'error': 'info não achada'},
                status_code=404
            )

        return infos

    return cursor.retrieve(
        table=table,
        all_=True,
        field_condition={}
    )

# GLOBAL
def cadastrar_info(
        table: builtins.str,
        values: Mapping[builtins.str, Union[builtins.str, builtins.int]],
        schema: SchemaMeta = None
) -> Union[
    Mapping[builtins.str, builtins.str],
    Union[builtins.str, List, Dict]
]:

    try:
        if schema:
            schema().load(values)
        cursor = SqliteOps(db=DATABASE_FILE)
        cursor.insert(
            table=table,
            fields_values=values
        )
        cursor.close_connection()
        return {'message': 'cadastrado com sucesso'}
    except ValidationError as e:
        return e.messages


# ---- MOTOR REGRAs ----

def idade(data_nascimento: datetime) -> builtins.int:
    hoje = date.today()
    diferenca_ano = hoje.year - data_nascimento.year
    diferenca_mes_dia = ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return diferenca_ano - diferenca_mes_dia
