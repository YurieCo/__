# Generated by Django 2.1.3 on 2018-12-02 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='start working on')),
                ('end_date', models.DateTimeField(verbose_name='end working on')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_description', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets.Task'),
        ),
    ]
