# Generated by Django 2.2 on 2019-07-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_name', models.CharField(max_length=250)),
                ('sponsor_bio', models.TextField(help_text='A short bio about sponsor.')),
                ('sponsor_logo', models.ImageField(upload_to='sponsor_pics')),
                ('sponsor_website_url', models.CharField(default='#', max_length=250)),
                ('sponsor_twitter_url', models.CharField(default='#', max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
