import pytest
from jobs.forms import JobForm
from jobs.models import Job


@pytest.mark.django_db
def test_add_job_form_loads_correctly(client, user_HR, valid_job_data):
    client.force_login(user_HR)
    response = client.get('/jobs/add/')
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, JobForm)

    form_initial_data = response.context["form"].initial
    assert all(form_initial_data[key] == valid_job_data[key] for key in form_initial_data)


@pytest.mark.django_db
def test_add_job_with_valid_data(valid_job_data):
    form = JobForm(data=valid_job_data)
    assert form.is_valid()

    job = form.save()
    assert Job.objects.filter(pk=job.id).exists()


@pytest.mark.django_db
def test_add_job_with_invalid_posts_until_data(job_data_with_invalid_posts_time):
    for job_data_with_invalid_post_time in job_data_with_invalid_posts_time:
        form = JobForm(data=job_data_with_invalid_post_time)
        assert not form.is_valid()
