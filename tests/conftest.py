import pytest

from guias_tratamentos_odontologicos.chalicelib.schemas.compartilhado import EndpointsRequisitosCompartilhados
from guias_tratamentos_odontologicos.chalicelib.schemas.beneficiario import CadastroBeneficiario
from guias_tratamentos_odontologicos.chalicelib.schemas.dentista import CadastroDentista


# FIXTUREs PARA MARSHMALLOW SCHEMAs

@pytest.fixture(scope='module')
def shared_endpoints_reqs():
    return EndpointsRequisitosCompartilhados()


@pytest.fixture(scope='module')
def beneficiario_endpoint_reqs():
    return CadastroBeneficiario()


@pytest.fixture(scope='module')
def dentista_endpoint_reqs():
    return CadastroDentista()