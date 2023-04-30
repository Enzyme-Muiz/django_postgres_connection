# Generated by Django 3.1.3 on 2023-04-30 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='room_descriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='JacksonDrivePeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=50)),
                ('Date_of_birth', models.DateField()),
                ('room_number_value', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='django_postgres_app.room_descriptions')),
            ],
        ),
    ]