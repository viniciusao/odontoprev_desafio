import builtins
import unicodedata

from marshmallow import (
    fields,
    Schema,
    validate,
    validates,
    ValidationError
)


class SharedEndpointsRequirements(Schema):
    """
    Alguns schemas definidos pelos endpoints da aplicação
    possuem algumas propriedades e descrições idênticas,
    portanto, os endpoints herdarão este schema.
    """

    nome = fields.Str(
        validate=[
            validate.Length(max=20, min=1),
            validate.Regexp(r'[a-zA-Z\s]+$')
        ],
        required=True
    )
    """ o tamanho minímo é arbitrário. """

    email = fields.Str(
        validate=validate.Email(),
        required=True
    )
    genero = fields.Str(required=True)

    @validates('genero')
    def validar_genero(self, value: builtins.str):
        """ esta função demonstra uma forma alternativa
        de validar input data utilizando o marshmallow. """

        value_decoded = unicodedata.normalize('NFC', value)
        if value_decoded not in (
                'Masculino',
                'Feminino',
                'Prefiro não informar'
        ):

            length = len(value_decoded)
            # condição definida arbitrariamente.
            if not (20 >= length >= 2):
                raise ValidationError(
                    'Gênero informado deve ter '
                    'entre 2 e 20 caracteres'
                )