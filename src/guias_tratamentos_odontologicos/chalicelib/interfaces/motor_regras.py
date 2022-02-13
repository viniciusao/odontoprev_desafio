import abc
import builtins
from datetime import datetime
import sqlite3
from typing import Optional

from dateutil.relativedelta import relativedelta

from guias_tratamentos_odontologicos.chalicelib.helpers import idade
from guias_tratamentos_odontologicos.chalicelib.middlewares import get_infos


class EventosRegras(abc.ABC):

    @abc.abstractmethod
    def eventos_por_idade(
            self,
            cod_evento: builtins.int,
            carteirinha_beneficiario: builtins.int
    ) -> Optional[builtins.bool]:

        pass

    @abc.abstractmethod
    def eventos_por_periodicidade(
            self,
            cod_evento: builtins.int,
            carteirinha_beneficiario: builtins.int,
            data_execucao: builtins.str,
            cursor: sqlite3.Cursor
    ) -> Optional[builtins.bool]:

        pass


class Eventos(EventosRegras):

    PERIODICIDADE = {
        85400076: 12,
        85400106: 60,
        85400467: 1
    }
    """ Unidade de tempo: mês """

    NEGAR_EVENTOS = {
        85400033: 18,
        85400076: 14,
        85400416: 25
    }
    """ Evento: Idade """

    FORMATO_DATA = '%d/%m/%Y'
    """ Padrão do formatos das datas na aplicação. """


    def eventos_por_idade(
            self,
            cod_evento: builtins.int,
            carteirinha_beneficiario: builtins.int
    ) -> Optional[builtins.bool]:

        info = get_infos(
            'beneficiarios',
            'carteirinha',
            carteirinha_beneficiario
        ).json()
        data = info['data_nascimento']
        negar = cod_evento in self.NEGAR_EVENTOS
        if negar:
            valor = self.NEGAR_EVENTOS[cod_evento]
            if valor == idade(datetime.strptime(data, self.FORMATO_DATA)):
                return True

        return None

    def eventos_por_periodicidade(
            self,
            cod_evento: builtins.int,
            carteirinha_beneficiario: builtins.int,
            data_execucao: builtins.str,
            cursor: sqlite3.Cursor
    ) -> Optional[builtins.bool]:

        if cod_evento in self.PERIODICIDADE:
            guias = cursor.execute(
                'SELECT data_execucao FROM guias WHERE '
                f'beneficiario = {carteirinha_beneficiario} AND '
                f'evento = {cod_evento}'
            ).fetchall()
            if guias:
                for guia in guias:
                    # sqlite driver no python retorna
                    # os resultados em uma tupla
                    guia = guia[0]
                    guia_existente = datetime.strptime(guia, self.FORMATO_DATA)
                    nova_guia = datetime.strptime(data_execucao, self.FORMATO_DATA)
                    if nova_guia <= guia_existente + relativedelta(months=self.PERIODICIDADE[cod_evento]):
                        return True

        return None