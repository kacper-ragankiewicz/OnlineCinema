# Generated by Django 4.0.1 on 2022-02-09 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ankieta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pytanie', models.CharField(max_length=200)),
                ('data_publikacji', models.DateTimeField(verbose_name='Data publikacji')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tytul', models.CharField(max_length=100, verbose_name='Tytuł filmu')),
                ('opis', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Opis filmu')),
                ('obraz', models.ImageField(blank=True, null=True, upload_to='Strona_kino')),
                ('kategoria', models.CharField(choices=[('AKCJA', 'AKCJA'), ('BIOGRAFIA', 'BIOGRAFICZNY'), ('DRAMAT', 'DRAMAT'), ('FANTASY', 'FANTASY'), ('KOMEDIA', 'KOMEDIA'), ('ROMANS', 'ROMANS')], max_length=15)),
                ('jezyk', models.CharField(choices=[('PL', 'POLSKI'), ('EN', 'ENGLISH'), ('RU', 'РУССКИЙ')], max_length=2)),
                ('status', models.CharField(choices=[('ND', 'NIEDAWNO DODANE'), ('NO', 'NAJCZĘŚCIEJ OGLĄDANE'), ('TR', 'NAJLEPIEJ OCENIANE')], max_length=2)),
                ('data_wydania', models.IntegerField(default=0)),
                ('wyswietlenia', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=30, verbose_name='Imię użytkownika')),
                ('nazwisko', models.CharField(max_length=30, verbose_name='Nazwisko użytkownika')),
                ('email', models.EmailField(max_length=100, verbose_name='Adres email użytkownika')),
            ],
        ),
        migrations.CreateModel(
            name='Wybor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('odpowiedz', models.CharField(max_length=200)),
                ('glosy', models.PositiveIntegerField(default=0)),
                ('ankieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Strona_kino.ankieta')),
            ],
        ),
        migrations.CreateModel(
            name='Rezerwacja',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rodzaj_biletu', models.CharField(choices=[('N', 'NORMALNY'), ('U', 'ULGOWY'), ('R', 'RODZINNY')], max_length=10)),
                ('cena_biletu', models.PositiveIntegerField(default=0)),
                ('ilosc_biletow', models.PositiveIntegerField(default=0)),
                ('data_zakupu', models.DateTimeField(verbose_name='Data zakupu')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Strona_kino.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Strona_kino.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bilet',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('film', models.ManyToManyField(to='Strona_kino.Film')),
                ('rezerwacja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Strona_kino.rezerwacja')),
                ('user', models.ManyToManyField(blank=True, null=True, to='Strona_kino.User')),
            ],
        ),
    ]