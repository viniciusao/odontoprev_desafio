import setuptools

setuptools.setup(
    name="guias_tratamentos_odontologicos",
    version="0.1.0",
    author="Vinícius Aguiar",
    author_email="viniciusoa@protonmail.com",
    description="Desafio Técnico Arquiteto de soluções. ",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        'chalice',
        'marshmallow',
        'mypy',
        'pytest',
        'requests',
        'types-requests',
        'types-python-dateutil'
    ],
    package_data={'*': ['.chalice/*.json']},
    entry_points={
        'console_scripts': [
            'setup_db = guias_tratamentos_odontologicos.chalicelib.cli.setup_database:main'
        ]
    }
)
