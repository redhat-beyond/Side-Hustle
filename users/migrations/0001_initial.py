# Generated by Django 3.2.9 on 2021-11-15 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              primary_key=True, serialize=False, to='auth.user')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True,
                                            choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unspecified')], default='U',
                                            max_length=1, null=True)),
                ('role', models.CharField(blank=True, choices=[('employer', 'Employer'), ('employee', 'Employee')],
                                          default='employee', max_length=10, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
