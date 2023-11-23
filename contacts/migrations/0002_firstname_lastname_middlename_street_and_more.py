# Generated by Django 4.2.7 on 2023-11-23 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LastName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MiddleName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={},
        ),
        migrations.AlterField(
            model_name='contact',
            name='apartment',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='building_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='building_unit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.firstname'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.lastname'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='middle_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.middlename'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.street'),
        ),
    ]