# Generated by Django 4.2 on 2023-05-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='speciality',
            name='courses',
            field=models.ManyToManyField(blank=True, to='app.course'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
