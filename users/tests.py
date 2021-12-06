import pytest
from users.models import Role, User
from django.contrib.auth.models import User as DjangoUser


@pytest.fixture
def create_user_1():
    return User.create_user('user1', 'test@test.com', '132456', 'b', Role.STUDENT)


@pytest.fixture
def create_user_2():
    return User.create_user('user2', 'test@test.com', '132456', 'b', Role.STUDENT)


@pytest.fixture
def create_user_student():
    return User.create_user('Morty', 'Morty@test.com', 'Morty', 'b', Role.STUDENT)


@pytest.fixture
def create_user_HR():
    return User.create_user('Rick', 'Rick@test.com', 'Rick', 'b', Role.HR)


@pytest.mark.django_db
def test_create_user(create_user_1):
    assert isinstance(create_user_1, User)
    assert DjangoUser.objects.count() == 1


@pytest.mark.django_db
def test_create_two_users(create_user_1, create_user_2):
    assert isinstance(create_user_1, User)
    assert isinstance(create_user_2, User)
    assert DjangoUser.objects.count() == 2


@pytest.mark.django_db
def test_create_dup_users():
    try:
        User.create_user('dup', 'ts@dd.com', '1', "ba", Role.STUDENT)
        User.create_user('dup', 'td@dw.com', '13', "bla bla", Role.HR)
        assert False
    except Exception:
        assert True


@pytest.mark.django_db
def test_delete_user(create_user_1):
    userId = create_user_1.user.id
    create_user_1.del_user()
    assert not User.objects.filter(user=userId).exists()


@pytest.mark.django_db
def test_user_name(create_user_1):
    assert str(create_user_1) == create_user_1.full_name


@pytest.mark.django_db
def test_check_is_student(create_user_student, create_user_HR):
    assert create_user_student.is_student() is True
    assert create_user_HR.is_student() is False


@pytest.mark.django_db
def test_check_is_HR(create_user_student, create_user_HR):
    assert create_user_student.is_HR() is False
    assert create_user_HR.is_HR() is True
