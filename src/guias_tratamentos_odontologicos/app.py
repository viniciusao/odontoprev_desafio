from chalice import Chalice

from guias_tratamentos_odontologicos.chalicelib.views import beneficiarios_b
from guias_tratamentos_odontologicos.chalicelib.views import dentistas_b
from guias_tratamentos_odontologicos.chalicelib.views import eventos_b
from guias_tratamentos_odontologicos.chalicelib.views import guias_b

app = Chalice(app_name='guias_tratamentos_odontologicos')

app.register_blueprint(beneficiarios_b)
app.register_blueprint(dentistas_b)
app.register_blueprint(eventos_b)
app.register_blueprint(guias_b)
