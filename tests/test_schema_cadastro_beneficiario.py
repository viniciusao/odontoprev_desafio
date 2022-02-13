from random import randint

import pytest


@pytest.mark.parametrize('mock_year', [
    '01/05/1960',
    '02/04/1990',
    '11/11/1995',
    '12/02/1965'
])
def test_data_nascimento_valido(mock_year, beneficiario_endpoint_reqs):
    beneficiario_endpoint_reqs.load(
        {'data_nascimento': mock_year}, partial=True
    )

@pytest.mark.parametrize('mock_carteirinha', [
    str(randint(1, 9999999999)) for carteirinha in range(4)
])
def test_carteirinha_valida(mock_carteirinha, beneficiario_endpoint_reqs):
    beneficiario_endpoint_reqs.load(
        {'carteirinha': mock_carteirinha}, partial=True
    )