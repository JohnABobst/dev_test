# Generated by Django 2.0.2 on 2018-12-05 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recordings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputRecording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=512)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('isrc', models.CharField(blank=True, max_length=30, null=True)),
                ('duration', models.CharField(blank=True, max_length=256, null=True)),
                ('match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='recordings.Recording')),
            ],
        ),
        migrations.CreateModel(
            name='MatchReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songs', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='inputrecording',
            name='match_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_songs', to='matcher.MatchReport'),
        ),
    ]