# Generated by Django 2.1.4 on 2018-12-07 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_companydata_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydata',
            name='sector',
            field=models.CharField(choices=[('Agri', 'Agriculture'), ('Fin', 'Finance'), ('Retail', 'Retail'), ('Med', 'Medical Research'), ('Infra', 'Infrastructure'), ('Oth', 'Others')], default='Oth', max_length=15),
        ),
    ]
