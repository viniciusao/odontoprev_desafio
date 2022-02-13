""" setup procedural, já está pronto como um script de execução. """

import pathlib
import sqlite3


DB_PATH = pathlib.Path(__file__).parent.parent.parent

def main():
    conn = sqlite3.connect(DB_PATH.joinpath('guias_tratamentos_odontologicos.db').resolve())
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE beneficiarios ('
        'nome TEXT, '
        'carteirinha INTEGER PRIMARY KEY, '
        'email TEXT, '
        'data_nascimento TEXT, '
        'genero TEXT)'
    )
    cursor.execute(
        'CREATE TABLE dentistas ('
        'nome TEXT, '
        'cro TEXT PRIMARY KEY, '
        'email TEXT, '
        'genero TEXT, '
        'especialidades TEXT, '
        'endereco TEXT)'
    )
    cursor.execute(
        'CREATE TABLE eventos ('
        'codigo TEXT PRIMARY KEY, '
        'descricao TEXT)'
    )
    cursor.execute(
        'CREATE TABLE guias ('
        'numero INTEGER PRIMARY KEY, '
        'beneficiario INTEGER, '
        'dentista TEXT, '
        'data_atendimento TEXT, '
        'data_execucao TEXT, '
        'evento TEXT, '
        'face TEXT, '
        'local TEXT, '
        'FOREIGN KEY (beneficiario) REFERENCES beneficiarios (carteirinha), '
        'FOREIGN KEY (evento) REFERENCES eventos (codigo), '
        'FOREIGN KEY (dentista) REFERENCES dentistas (cro))'
    )
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()