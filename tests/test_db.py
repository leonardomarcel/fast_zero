from sqlalchemy import select
from fast_zero.models import User

def test_create_user(session):
    new_user = User(username='testuser', password='testpassword', email='testuser@example.com')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).filter_by(username='testuser'))
    assert new_user.id is not None


