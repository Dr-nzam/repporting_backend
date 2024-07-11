# Generated by Django 5.0.7 on 2024-07-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupeElectrogene', '0003_client_equipementsite_site_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donneesenergetiques',
            fields=[
                ('id_energy', models.AutoField(db_column='ID_Energy', primary_key=True, serialize=False)),
                ('dates', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=30, null=True)),
                ('ch1_voltage', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch1_Voltage', max_length=30, null=True)),
                ('ch1_current', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch1_Current', max_length=30, null=True)),
                ('ch1_active_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch1_Active_Power', max_length=30, null=True)),
                ('ch1_apparent_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch1_Apparent_Power', max_length=30, null=True)),
                ('ch1_reactive_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch1_Reactive_Power', max_length=30, null=True)),
                ('ch1_power_factor', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch1_Power_Factor', max_length=30, null=True)),
                ('ch1_thd_u', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch1_THD_U', max_length=30, null=True)),
                ('ch1_thd_i', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch1_THD_I', max_length=30, null=True)),
                ('ch1_spectrum_u', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch1_Spectrum_U', max_length=30, null=True)),
                ('ch1_spectrum_i', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch1_Spectrum_I', max_length=30, null=True)),
                ('ch2_voltage', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch2_Voltage', max_length=30, null=True)),
                ('ch2_current', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch2_Current', max_length=30, null=True)),
                ('ch2_active_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch2_Active_Power', max_length=30, null=True)),
                ('ch2_apparent_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch2_Apparent_Power', max_length=30, null=True)),
                ('ch2_reactive_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch2_Reactive_Power', max_length=30, null=True)),
                ('ch2_power_factor', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch2_Power_Factor', max_length=30, null=True)),
                ('ch2_thd_u', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch2_THD_U', max_length=30, null=True)),
                ('ch2_thd_i', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch2_THD_I', max_length=30, null=True)),
                ('ch2_spectrum_u', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch2_Spectrum_U', max_length=30, null=True)),
                ('ch2_spectrum_i', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch2_Spectrum_I', max_length=30, null=True)),
                ('ch3_voltage', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch3_Voltage', max_length=30, null=True)),
                ('ch3_current', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch3_Current', max_length=30, null=True)),
                ('ch3_active_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch3_Active_Power', max_length=30, null=True)),
                ('ch3_apparent_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch3_Apparent_Power', max_length=30, null=True)),
                ('ch3_reactive_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch3_Reactive_Power', max_length=30, null=True)),
                ('ch3_power_factor', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch3_Power_Factor', max_length=30, null=True)),
                ('ch3_thd_u', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch3_THD_U', max_length=30, null=True)),
                ('ch3_thd_i', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch3_THD_I', max_length=30, null=True)),
                ('ch3_spectrum_u', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch3_Spectrum_U', max_length=30, null=True)),
                ('ch3_spectrum_i', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Ch3_Spectrum_I', max_length=30, null=True)),
                ('three_phase_active_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Three_Phase_Active_Power', max_length=30, null=True)),
                ('three_phase_reactive_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Three_Phase_Reactive_Power', max_length=30, null=True)),
                ('three_phase_apparent_power', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Three_Phase_Apparent_Power', max_length=30, null=True)),
                ('three_phase_unbalanced_load', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Three_Phase_Unbalanced_Load', max_length=30, null=True)),
                ('three_phase_zero_current', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Three_Phase_Zero_Current', max_length=30, null=True)),
                ('energy_counter_ch1_active_energy_bal', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Ch1_Active_Energy_BAL', max_length=30, null=True)),
                ('energy_counter_ch1_active_energy_con', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Ch1_Active_Energy_CON', max_length=30, null=True)),
                ('energy_counter_ch1_active_energy_gen', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Ch1_Active_Energy_GEN', max_length=30, null=True)),
                ('energy_counter_ch2_active_energy_bal', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Ch2_Active_Energy_BAL', max_length=30, null=True)),
                ('energy_counter_ch2_active_energy_con', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Ch2_Active_Energy_CON', max_length=30, null=True)),
                ('energy_counter_ch2_active_energy_gen', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Ch2_Active_Energy_GEN', max_length=30, null=True)),
                ('energy_counter_ch3_active_energy_bal', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Ch3_Active_Energy_BAL', max_length=30, null=True)),
                ('energy_counter_ch3_active_energy_con', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Ch3_Active_Energy_CON', max_length=30, null=True)),
                ('energy_counter_ch3_active_energy_gen', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Ch3_Active_Energy_GEN', max_length=30, null=True)),
                ('energy_counter_three_phase_active_energy_bal', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Three_Phase_Active_Energy_BAL', max_length=30, null=True)),
                ('energy_counter_three_phase_active_energy_con', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Three_Phase_Active_Energy_CON', max_length=30, null=True)),
                ('energy_counter_three_phase_active_energy_gen', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Three_Phase_Active_Energy_GEN', max_length=30, null=True)),
                ('energy_counter_three_phase_reactive_energy_counter', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Energy_Counter_Three_Phase_Reactive_Energy_Counter', max_length=30, null=True)),
            ],
            options={
                'db_table': 'DonneesEnergetiques',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Donneesonduleur',
            fields=[
                ('id_dataonduleur', models.AutoField(db_column='ID_dataonduleur', primary_key=True, serialize=False)),
                ('date_time', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Date_Time', max_length=20, null=True)),
                ('input_voltage', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Input_Voltage', max_length=30, null=True)),
                ('output_voltage', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Output_Voltage', max_length=30, null=True)),
                ('freq', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Freq', max_length=10, null=True)),
                ('loads', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Loads', max_length=5, null=True)),
                ('capacity', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Capacity', max_length=10, null=True)),
                ('battery_volt', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Battery_Volt', max_length=10, null=True)),
                ('cell_volt', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Cell_Volt', max_length=10, null=True)),
                ('temp_c_f', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Temp_C_F', max_length=20, null=True)),
                ('environmental_temp_c_f', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Environmental_Temp_C_F', max_length=20, null=True)),
                ('environmental_humidity', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Environmental_Humidity', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Donneesonduleur',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Donneessallesarchives',
            fields=[
                ('id_donnees', models.AutoField(db_column='ID_donnees', primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Date', max_length=15, null=True)),
                ('heure', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Heure', max_length=15, null=True)),
                ('perseverance', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Perseverance', max_length=10, null=True)),
                ('esprit_first', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Esprit_First', max_length=10, null=True)),
                ('motivation', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Motivation', max_length=10, null=True)),
                ('responsabilite', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Responsabilite', max_length=10, null=True)),
                ('excellence', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Excellence', max_length=10, null=True)),
                ('pense_positive', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Pense_positive', max_length=10, null=True)),
                ('humilite', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Humilite', max_length=10, null=True)),
                ('determine', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Determine', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Donneessallesarchives',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id_alerte', models.AutoField(db_column='ID_alerte', primary_key=True, serialize=False)),
                ('date_time', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Date_Time', max_length=50, null=True)),
                ('evenement', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Evenement', max_length=250, null=True)),
                ('type_evenement', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Type_evenement', max_length=100, null=True)),
                ('local_equipement', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Local_equipement', max_length=30, null=True)),
                ('utilisateur', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Utilisateur', max_length=50, null=True)),
                ('source_evenement', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Source_evenement', max_length=60, null=True)),
                ('nature_source_evenement', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Nature_source_evenement', max_length=50, null=True)),
                ('localisation', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Localisation', max_length=50, null=True)),
                ('categorie', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Categorie', max_length=80, null=True)),
                ('event_id', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Event_ID', max_length=10, null=True)),
                ('active_state', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Active_State', max_length=10, null=True)),
                ('set_state', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Set_State', max_length=10, null=True)),
                ('acknowledge_state', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Acknowledge_State', max_length=10, null=True)),
                ('event_parametric_data', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Event_Parametric_Data', max_length=15, null=True)),
                ('event_id_code', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Event_ID_Code', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Journal',
                'managed': False,
            },
        ),
    ]
