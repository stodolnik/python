from sqlalchemy import create_engine

from fast_zero.models import User, table_registry


def teste_create_user(session):
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    user = User(
        username='Lucas',
        email='lucas@raineri.com.br',
        password='mais_uma_senha',
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    assert user.username == 'Lucas'
