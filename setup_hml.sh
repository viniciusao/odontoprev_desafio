python -m venv "$PWD"/venv
source venv/bin/activate
pip install -e .
APP_PATH='src/guias_tratamentos_odontologicos'
python $APP_PATH/chalicelib/cli/setup_database.py
mypy $APP_PATH/
sleep 3
pytest -sv
sleep 5
cd $APP_PATH || exit
chalice local --stage hml