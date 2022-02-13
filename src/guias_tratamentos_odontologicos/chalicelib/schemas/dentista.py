from marshmallow import fields, validate

from .compartilhado import EndpointsRequisitosCompartilhados


class DentistasReqs:
    """ Aqui serão enumerados alguns requisitos
    para cadastrar um dentista. """

    especialidades = [
        'Cirurgia',
        'Endodontia',
        'Semiologia',
        'Radiologia',
        'Implante',
        'Odontopediatria',
    ]
    """ Especialidades na especificação do desafio, 
    pus somente algumas como exposição, porém, 
    está passível de expansão. """

    UFs = ['AM', 'AC', 'RR', 'RO',]
    """ Federações no brasil, pus somente algumas
    como exposição, porém, está passível de expansão. 
    """


class CadastroDentista(EndpointsRequisitosCompartilhados):

    cro = fields.Str(
        validate=[
            validate.Length(min=4, max=10),
            lambda cro: bool(list(filter(lambda uf: cro.endswith(uf), DentistasReqs.UFs))) and
                        cro.split('-')[0].isdigit() and
                        int(cro.split('-')[0]) != 0
        ],
        required=True,
        error_messages={
            'validator_failed': 'CRO com formato '
                                'inválido, deve ser: '
                                'digítosválidos-UF'
        }
    )
    especialidades = fields.List(
        fields.Str(),
        validate=[
            validate.ContainsOnly(choices=DentistasReqs.especialidades),
            lambda especialidades: 5 >= len(especialidades) > 0
        ],
        required=True,
        error_messages={
            'validator_failed': 'selecione até 5 especialidades.'
        }
    )
    endereco = fields.Str(
        validate=validate.Length(min=10, max=100),
        required=True
    )
    """ o tamanho minímo é arbitrário. """
