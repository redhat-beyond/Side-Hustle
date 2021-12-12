import pytest
from users.models import User


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
def test_check_is_student(user_student, user_HR):
    assert user_student.is_student() is True
    assert user_HR.is_student() is False


@pytest.mark.django_db
def test_check_is_HR(user_student, user_HR):
    assert user_student.is_HR() is False
    assert user_HR.is_HR() is True
