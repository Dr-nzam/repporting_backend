from django.db import models

# Create your models here.

class Client(models.Model):
    id_client = models.CharField(db_column='ID_client', primary_key=True, max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nom_client = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class Site(models.Model):
    id_site = models.CharField(db_column='ID_site', primary_key=True, max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nom_lieu = models.CharField(unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_client = models.ForeignKey('Client', models.DO_NOTHING, db_column='ID_client')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Site'

class Equipementsite(models.Model):
    adresse_ip = models.CharField(primary_key=True, max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    nom_equipement = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_site = models.ForeignKey('Site', models.DO_NOTHING, db_column='ID_Site')  # Field name made lowercase.
    etat_equipement = models.CharField(db_column='Etat_equipement', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    est_actif = models.CharField(max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')
    est_accessible = models.CharField(max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')
    login_connexion = models.CharField(max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    password = models.CharField(max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    login_double_authentif = models.CharField(max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    password_double_authentif = models.CharField(max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    port_acces = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Equipementsite'

    def __str__(self):
        return self.nom_equipement


class Donneegroupeelectrogene(models.Model):
    id_groupe = models.AutoField(db_column='ID_groupe', primary_key=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rpm = models.CharField(db_column='RPM', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pwr = models.CharField(db_column='Pwr', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pf = models.CharField(db_column='PF', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gfrq = models.CharField(db_column='Gfrq', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vg1 = models.CharField(db_column='Vg1', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vg2 = models.CharField(db_column='Vg2', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vg3 = models.CharField(db_column='Vg3', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    il1 = models.CharField(db_column='IL1', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    il2 = models.CharField(db_column='IL2', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    il3 = models.CharField(db_column='IL3', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ef = models.CharField(db_column='EF', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vm1 = models.CharField(db_column='Vm1', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vm2 = models.CharField(db_column='Vm2', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vm3 = models.CharField(db_column='Vm3', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mfrq = models.CharField(db_column='Mfrq', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ubat = models.CharField(db_column='UBat', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    oilp = models.CharField(db_column='OilP', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ai2 = models.CharField(db_column='AI2', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ai3 = models.CharField(db_column='AI3', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bin = models.CharField(db_column='BIN', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bout = models.CharField(db_column='BOUT', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bioe = models.CharField(db_column='BIOE', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adresse_ip = models.ForeignKey('Equipementsite', models.DO_NOTHING, db_column='Adresse_ip')

    class Meta:
        managed = False
        db_table = 'DonneegroupeElectrogene'  # Ensure this matches the exact table name in your database
    
    def __str__(self):
        return self.reason



class Donneesenergetiques(models.Model):
    id_energy = models.AutoField(db_column='ID_Energy', primary_key=True)  # Field name made lowercase.
    dates = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ch1_voltage = models.CharField(db_column='Ch1_Voltage', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch1_current = models.CharField(db_column='Ch1_Current', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch1_active_power = models.CharField(db_column='Ch1_Active_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch1_apparent_power = models.CharField(db_column='Ch1_Apparent_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch1_reactive_power = models.CharField(db_column='Ch1_Reactive_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch1_power_factor = models.CharField(db_column='Ch1_Power_Factor', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch1_thd_u = models.CharField(db_column='Ch1_THD_U', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch1_thd_i = models.CharField(db_column='Ch1_THD_I', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch1_spectrum_u = models.CharField(db_column='Ch1_Spectrum_U', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch1_spectrum_i = models.CharField(db_column='Ch1_Spectrum_I', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch2_voltage = models.CharField(db_column='Ch2_Voltage', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch2_current = models.CharField(db_column='Ch2_Current', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch2_active_power = models.CharField(db_column='Ch2_Active_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch2_apparent_power = models.CharField(db_column='Ch2_Apparent_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch2_reactive_power = models.CharField(db_column='Ch2_Reactive_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch2_power_factor = models.CharField(db_column='Ch2_Power_Factor', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch2_thd_u = models.CharField(db_column='Ch2_THD_U', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch2_thd_i = models.CharField(db_column='Ch2_THD_I', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch2_spectrum_u = models.CharField(db_column='Ch2_Spectrum_U', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch2_spectrum_i = models.CharField(db_column='Ch2_Spectrum_I', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch3_voltage = models.CharField(db_column='Ch3_Voltage', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch3_current = models.CharField(db_column='Ch3_Current', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch3_active_power = models.CharField(db_column='Ch3_Active_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch3_apparent_power = models.CharField(db_column='Ch3_Apparent_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch3_reactive_power = models.CharField(db_column='Ch3_Reactive_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch3_power_factor = models.CharField(db_column='Ch3_Power_Factor', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch3_thd_u = models.CharField(db_column='Ch3_THD_U', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch3_thd_i = models.CharField(db_column='Ch3_THD_I', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch3_spectrum_u = models.CharField(db_column='Ch3_Spectrum_U', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ch3_spectrum_i = models.CharField(db_column='Ch3_Spectrum_I', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    three_phase_active_power = models.CharField(db_column='Three_Phase_Active_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    three_phase_reactive_power = models.CharField(db_column='Three_Phase_Reactive_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    three_phase_apparent_power = models.CharField(db_column='Three_Phase_Apparent_Power', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    three_phase_unbalanced_load = models.CharField(db_column='Three_Phase_Unbalanced_Load', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    three_phase_zero_current = models.CharField(db_column='Three_Phase_Zero_Current', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_ch1_active_energy_bal = models.CharField(db_column='Energy_Counter_Ch1_Active_Energy_BAL', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_ch1_active_energy_con = models.CharField(db_column='Energy_Counter_Ch1_Active_Energy_CON', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_ch1_active_energy_gen = models.CharField(db_column='Energy_Counter_Ch1_Active_Energy_GEN', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_ch2_active_energy_bal = models.CharField(db_column='Energy_Counter_Ch2_Active_Energy_BAL', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_ch2_active_energy_con = models.CharField(db_column='Energy_Counter_Ch2_Active_Energy_CON', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_ch2_active_energy_gen = models.CharField(db_column='Energy_Counter_Ch2_Active_Energy_GEN', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_ch3_active_energy_bal = models.CharField(db_column='Energy_Counter_Ch3_Active_Energy_BAL', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_ch3_active_energy_con = models.CharField(db_column='Energy_Counter_Ch3_Active_Energy_CON', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_ch3_active_energy_gen = models.CharField(db_column='Energy_Counter_Ch3_Active_Energy_GEN', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_three_phase_active_energy_bal = models.CharField(db_column='Energy_Counter_Three_Phase_Active_Energy_BAL', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_three_phase_active_energy_con = models.CharField(db_column='Energy_Counter_Three_Phase_Active_Energy_CON', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_three_phase_active_energy_gen = models.CharField(db_column='Energy_Counter_Three_Phase_Active_Energy_GEN', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    energy_counter_three_phase_reactive_energy_counter = models.CharField(db_column='Energy_Counter_Three_Phase_Reactive_Energy_Counter', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adresse_ip = models.ForeignKey('Equipementsite', models.DO_NOTHING, db_column='adresse_ip')

    class Meta:
        managed = False
        db_table = 'DonneesEnergetiques'

class Donneesonduleur(models.Model):
    id_dataonduleur = models.AutoField(db_column='ID_dataonduleur', primary_key=True)  # Field name made lowercase.
    date_time = models.CharField(db_column='Date_Time', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    input_voltage = models.CharField(db_column='Input_Voltage', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    output_voltage = models.CharField(db_column='Output_Voltage', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    freq = models.CharField(db_column='Freq', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    loads = models.CharField(db_column='Loads', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    capacity = models.CharField(db_column='Capacity', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    battery_volt = models.CharField(db_column='Battery_Volt', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cell_volt = models.CharField(db_column='Cell_Volt', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    temp_c_f = models.CharField(db_column='Temp_C_F', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    environmental_temp_c_f = models.CharField(db_column='Environmental_Temp_C_F', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    environmental_humidity = models.CharField(db_column='Environmental_Humidity', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adresse_ip = models.ForeignKey('Equipementsite', models.DO_NOTHING, db_column='adresse_ip')

    class Meta:
        managed = False
        db_table = 'Donneesonduleur'


class Donneessallesarchives(models.Model):
    id_donnees = models.AutoField(db_column='ID_donnees', primary_key=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    heure = models.CharField(db_column='Heure', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    perseverance = models.CharField(db_column='Perseverance', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esprit_first = models.CharField(db_column='Esprit_First', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    motivation = models.CharField(db_column='Motivation', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    responsabilite = models.CharField(db_column='Responsabilite', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    excellence = models.CharField(db_column='Excellence', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pense_positive = models.CharField(db_column='Pense_positive', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    humilite = models.CharField(db_column='Humilite', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    determine = models.CharField(db_column='Determine', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_site = models.ForeignKey('Site', models.DO_NOTHING, db_column='ID_Site')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Donneessallesarchives'


class Journal(models.Model):
    id_alerte = models.AutoField(db_column='ID_alerte', primary_key=True)  # Field name made lowercase.
    date_time = models.CharField(db_column='Date_Time', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    evenement = models.CharField(db_column='Evenement', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_evenement = models.CharField(db_column='Type_evenement', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    local_equipement = models.CharField(db_column='Local_equipement', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    utilisateur = models.CharField(db_column='Utilisateur', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    source_evenement = models.CharField(db_column='Source_evenement', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nature_source_evenement = models.CharField(db_column='Nature_source_evenement', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    localisation = models.CharField(db_column='Localisation', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    categorie = models.CharField(db_column='Categorie', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    event_id = models.CharField(db_column='Event_ID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    active_state = models.CharField(db_column='Active_State', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    set_state = models.CharField(db_column='Set_State', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    acknowledge_state = models.CharField(db_column='Acknowledge_State', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    event_parametric_data = models.CharField(db_column='Event_Parametric_Data', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    event_id_code = models.CharField(db_column='Event_ID_Code', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adresse_ip = models.ForeignKey(Equipementsite, models.DO_NOTHING, db_column='adresse_ip')

    class Meta:
        managed = False
        db_table = 'Journal'