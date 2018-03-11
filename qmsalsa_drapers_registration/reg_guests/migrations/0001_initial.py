# Generated by Django 2.0.3 on 2018-03-11 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('instagram', models.CharField(max_length=150)),
                ('is_new_to_salsa', models.BooleanField(default=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]