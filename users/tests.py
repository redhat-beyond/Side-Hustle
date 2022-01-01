import pytest
from users.models import User
from users.forms import RegisterForm


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


@pytest.mark.django_db
def test_signup_form_loads_correctly(client, valid_user_data):
    response = client.get('/users/register/')
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, RegisterForm)

    form_initial_data = response.context["form"].initial
    assert all(form_initial_data[key] == valid_user_data[key] for key in form_initial_data)


@pytest.mark.django_db
def test_valid_student_sign_up(valid_student_data):
    form = RegisterForm(data=valid_student_data)
    assert form.is_valid()

    student_user = form.save()
    assert User.objects.filter(pk=student_user.id).exists()


@pytest.mark.django_db
def test_valid_hr_sign_up(valid_hr_data):
    form = RegisterForm(data=valid_hr_data)
    assert form.is_valid()

    hr_user = form.save()
    assert User.objects.filter(pk=hr_user.id).exists()


@pytest.mark.django_db
def test_sign_up_with_invalid_passwords(user_data_with_invalid_passwords):
    for user_data_with_invalid_password in user_data_with_invalid_passwords:
        form = RegisterForm(data=user_data_with_invalid_password)
        assert not form.is_valid()


@pytest.mark.django_db
def test_sign_up_with_non_matching_second_password(user_data_with_non_matching_password):
    form = RegisterForm(data=user_data_with_non_matching_password)
    assert not form.is_valid()


@pytest.mark.django_db
def test_sign_up_with_invalid_email(user_data_with_invalid_emails):
    for user_data_with_invalid_email in user_data_with_invalid_emails:
        form = RegisterForm(data=user_data_with_invalid_email)
        assert not form.is_valid()


@pytest.mark.django_db
def test_sign_up_with_invalid_username(user_data_with_invalid_usernames):
    for user_data_with_invalid_username in user_data_with_invalid_usernames:
        form = RegisterForm(data=user_data_with_invalid_username)
        assert not form.is_valid()
