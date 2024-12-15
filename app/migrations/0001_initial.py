# Generated by Django 5.1.4 on 2024-12-15 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('cout', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Graylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suspicion_reason', models.TextField(blank=True, null=True)),
                ('reviewed_date', models.DateTimeField(auto_now_add=True)),
                ('url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.url')),
            ],
        ),
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detection', models.CharField(blank=True, choices=[('manual_review', 'Manual Review'), ('external_database', 'External Database'), ('phishing_detection', 'Phishing Detection')], max_length=25, null=True)),
                ('threat_type', models.CharField(max_length=255)),
                ('url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.url')),
            ],
        ),
        migrations.CreateModel(
            name='WhiteList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('verified_date', models.DateTimeField(auto_now_add=True)),
                ('url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.url')),
            ],
        ),
    ]
