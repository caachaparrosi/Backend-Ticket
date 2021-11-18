# Generated by Django 3.2.7 on 2021-10-07 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myticket', '0002_auto_20211002_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50)),
                ('dni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myticket.person')),
            ],
        ),
    ]
