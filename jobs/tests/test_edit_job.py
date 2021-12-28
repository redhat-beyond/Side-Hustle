import pytest
from jobs.forms import JobForm
# from jobs.views import UpdateJobsView
# from jobs.models import Job


@pytest.mark.django_db
def test_view_edit_job_form(client, user_HR, job_1):
    client.force_login(user_HR)
    response = client.get(f'/jobs/edit/{job_1.id}')
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, JobForm)


@pytest.mark.django_db
def test_load_edit_form(client, user_HR, job_1):
    client.force_login(user_HR)
    response = client.get(f'/jobs/edit/{job_1.id}')
    assert response.status_code == 200

    form_load_data = response.context['form'].initial
    assert form_load_data['company_name'] == job_1.company_name
    assert form_load_data['title'] == job_1.title
    assert form_load_data['location'] == job_1.location
    assert form_load_data['description'] == job_1.description
    assert str(form_load_data['post_until']) == job_1.post_until
    assert form_load_data['is_active'] == job_1.is_active
    assert form_load_data['apply_link'] == job_1.apply_link


@pytest.mark.django_db
def test_edit_job_description(client, user_HR, job_1, job_1_data):
    client.force_login(user_HR)
    response = client.get(f'/jobs/edit/{job_1.id}')
    assert response.status_code == 200

    job_1_data['description'] = job_1.description + 'wow'
    response = client.post(f'/jobs/edit/{job_1.id}', data=job_1_data)
    # assert response.status_code == 302
    # assert response.url == '/jobs/'

    # new_job_1 = Job.objects.get(pk=job_1.id)
    # assert new_job_1.description == job_1_data['description']
