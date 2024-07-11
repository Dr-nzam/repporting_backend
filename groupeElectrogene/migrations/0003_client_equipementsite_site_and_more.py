# Generated by Django 5.0.7 on 2024-07-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupeElectrogene', '0002_alter_donneegroupeelectrogene_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ID_client', max_length=7, primary_key=True, serialize=False)),
                ('nom_client', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=20, null=True)),
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipementsite',
            fields=[
                ('adresse_ip', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=15, primary_key=True, serialize=False)),
                ('nom_equipement', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=30, null=True)),
                ('etat_equipement', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Etat_equipement', max_length=10, null=True)),
                ('est_actif', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=3)),
                ('est_accessible', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=3)),
                ('login_connexion', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=40, null=True)),
                ('password', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=40, null=True)),
                ('login_double_authentif', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=40, null=True)),
                ('password_double_authentif', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=40, null=True)),
                ('port_acces', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Equipementsite',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id_site', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ID_site', max_length=4, primary_key=True, serialize=False)),
                ('nom_lieu', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'Site',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='donneegroupeelectrogene',
            options={'managed': False},
        ),
    ]
