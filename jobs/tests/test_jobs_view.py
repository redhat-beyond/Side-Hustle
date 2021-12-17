import pytest


@pytest.mark.django_db
def test_redirect_unauthenticated_user_when_enter_job_details(client, job_1):
    response = client.get(f'/jobs/{job_1.id}')
    assert response.status_code == 302
    assert response.url == '/home/'


@pytest.mark.django_db
def test_redirect_unauthenticated_user_when_enter_jobs(client):
    response = client.get('/jobs/')
    assert response.status_code == 302
    assert response.url == '/home/'


# Should move to another file - Good for Demo 3
@pytest.mark.django_db
def test_unauthenticated_user_when_enter_enter_home(client):
    response = client.get('/home/')
    assert response.status_code == 200


# Should move move another file - Good for Demo 3
@pytest.mark.django_db
def test_unauthenticated_user_enter_register(client):
    response = client.get('/users/register/')
    assert response.status_code == 200


# Should move move another file - Good for Demo 3
@pytest.mark.django_db
def test_unauthenticated_usersasa_enter_login(client):
    response = client.get('/users/login/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_enter_jobs(client, user_1):
    client.force_login(user_1)
    response = client.get('/jobs/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_enter_job_details(client, user_1, job_1):
    client.force_login(user_1)
    response = client.get(f'/jobs/{job_1.id}')
    assert response.status_code == 200


@pytest.mark.django_db
def test_redirect_student_user_when_enter_add_jobs(client, user_student):
    client.force_login(user_student)
    response = client.get('/jobs/add/')
    assert response.status_code == 302
    assert response.url == '/jobs/'


@pytest.mark.django_db
def test_redirect_student_user_when_enter_jobs_edit(client, user_student, job_1):
    client.force_login(user_student)
    response = client.get(f'/jobs/{job_1.id}')
    assert response.status_code == 200
    response = client.get(f'/jobs/edit/{job_1.id}')
    assert response.status_code == 302
    assert response.url == '/jobs/'


@pytest.mark.django_db
def test_redirect_student_user_when_enter_jobs_delete(client, user_student, job_1):
    client.force_login(user_student)
    response = client.get(f'/jobs/{job_1.id}')
    assert response.status_code == 200
    response = client.get(f'/jobs/delete/{job_1.id}')
    assert response.status_code == 302
    assert response.url == '/jobs/'


@pytest.mark.django_db
def test_HR_user_enter_add_jobs(client, user_HR):
    client.force_login(user_HR)
    response = client.get('/jobs/add/')
    assert response.status_code == 200
