import pytest
from users.models import User


@pytest.fixture
def user_1() -> User:
    user1 = User.objects.create_user(username='user1',
                                     first_name='first_name',
                                     last_name='last_name',
                                     email='email',
                                     password='password1')
    user1.role = 'Student'
    user1.save()
    return user1


@pytest.fixture
def user_2() -> User:
    user2 = User.objects.create_user(username='user2',
                                     first_name='first_name',
                                     last_name='last_name',
                                     email='email',
                                     password='password2')
    user2.role = 'Student'
    user2.save()
    return user2


@pytest.fixture
def create_user_student() -> User:
    user_student = User.objects.create_user(username='user_student',
                                            first_name='first_name',
                                            last_name='last_name',
                                            email='email',
                                            password='password1')
    user_student.role = 'Student'
    user_student.save()
    return user_student


@pytest.fixture
def create_user_HR() -> User:
    user_HR = User.objects.create_user(username='user_HR',
                                       first_name='first_name',
                                       last_name='last_name',
                                       email='email',
                                       password='password1')
    user_HR.role = 'HR'
    user_HR.save()
    return user_HR


@pytest.mark.django_db
def test_create_user(user_1):
    assert isinstance(user_1, User)
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_create_two_users(user_1, user_2):
    assert isinstance(user_1, User)
    assert isinstance(user_2, User)
    assert User.objects.count() == 2


@pytest.mark.django_db
def test_create_dup_users():
    try:
        user_dup1 = User.objects.create_user(username='dup',
                                             first_name='first_name1',
                                             last_name='last_name1',
                                             email='email1',
                                             password='password1')
        user_dup1.Role = 'STUDENT'
        user_dup1.save()
        user_dup2 = User.objects.create_user(username='dup',
                                             first_name='first_name2',
                                             last_name='last_name2',
                                             email='email2',
                                             password='password2')
        user_dup2.Role = 'HR'
        user_dup2.save()
        assert False
    except Exception:
        assert True


@pytest.mark.django_db
def test_delete_user(user_1):
    userId = user_1.id
    user_1.delete()
    assert not User.objects.filter(id=userId).exists()


@pytest.mark.django_db
def test_user_name(user_1):
    assert str(user_1) == user_1.get_full_name()


@pytest.mark.django_db
def test_check_is_student(create_user_student, create_user_HR):
    assert create_user_student.is_student() is True
    assert create_user_HR.is_student() is False


@pytest.mark.django_db
def test_check_is_HR(create_user_student, create_user_HR):
    assert create_user_student.is_HR() is False
    assert create_user_HR.is_HR() is True
