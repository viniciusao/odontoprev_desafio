from datetime import datetime

from marshmallow import fields, validate

from .compartilhado import EndpointsRequisitosCompartilhados


class CadastroBeneficiario(EndpointsRequisitosCompartilhados):
    carteirinha = fields.Int(
        validate=validate.Range(min=1, max=9999999999),
        required=True
    )
    data_nascimento = fields.Date(
        validate=lambda x:
        datetime.now().year - 12 >=
        x.year >=
        datetime.now().year - 65,
        format='%d/%m/%Y',
        required=True,
        error_messages={
            'validator_failed': 'disponível somente '
                               'para pessoas de 18 a 65 anos.'
        }
    )
    """ O python marshmallow também permite validação 
    utlizando lambda (keyword) no python. """
