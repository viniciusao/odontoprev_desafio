import pytest


@pytest.mark.parametrize('mocked_cro', [
    '12321-AM',
    '111111-RR',
    '000001-AM',
    '1231232-AC'
])
def test_cro_valido(mocked_cro, dentista_endpoint_reqs):
    dentista_endpoint_reqs.load(
        {'cro': mocked_cro}, partial=True
    )


@pytest.mark.parametrize('mocked_especialidades', [
    ['Cirurgia', 'Endodontia', 'Semiologia', 'Radiologia', 'Odontopediatria'],
    ['Cirurgia'],
    ['Implante', 'Semiologia'],
    ['Radiologia']
])
def test_especialidades_validas(mocked_especialidades, dentista_endpoint_reqs):
    dentista_endpoint_reqs.load(
        {'especialidades': mocked_especialidades},
        partial=True
    )


@pytest.mark.parametrize('mocked_endereco', [
    'rua angelonno, numero 12'
    'rua silvestre assis, 154, centro, manaus'
    'avenida brasil, 150, curitiba - PR'
])
def test_endereco_valido(mocked_endereco, dentista_endpoint_reqs):
    dentista_endpoint_reqs.load(
        {'endereco': mocked_endereco}, partial=True
    )