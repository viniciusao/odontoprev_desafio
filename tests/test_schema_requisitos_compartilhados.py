"""
Alguns schemas definidos pelos endpoints da aplicação
possuem algumas propriedades e descrições idênticas,
portanto, aqui serão testadas uma única vez.
"""

import pytest

@pytest.mark.parametrize('mocked_name', [
    'rodrigo lucas',
    'lucas fernandes',
    'aoskaoksoa soaksoa',
    'fernanda aquiles'
])
def test_nome_valido(mocked_name, shared_endpoints_reqs):
    shared_endpoints_reqs.load(
        {'nome': mocked_name}, partial=True)


@pytest.mark.parametrize('mocked_email', [
    'niceandsimple@example.com',
    'NiCeAnDsImPlE@eXaMpLe.CoM',
    'very.common@example.com',
    'a.little.lengthy.but.fine@a.iana-servers.net',
    'disposable.style.email.with+symbol@example.com',
    '"very.unusual.@.unusual.com"@example.com',
    "!#$%&'*+-/=?^_`{}|~@example.org",
    'niceandsimple@[64.233.160.0]',
    'niceandsimple@localhost',
    u'josé@blah.com',
    u'δοκ.ιμή@παράδειγμα.δοκιμή',
])
def test_email_valido(mocked_email, shared_endpoints_reqs):
    shared_endpoints_reqs.load(
        {'email': mocked_email}, partial=True)


@pytest.mark.parametrize('mocked_gender', [
    'Masculino',
    'Feminino',
    u'Prefiro não informar',
    'MockNovoGenero'
])
def test_genero_valido(mocked_gender, shared_endpoints_reqs):
    shared_endpoints_reqs.load(
        {'genero': mocked_gender}, partial=True
    )