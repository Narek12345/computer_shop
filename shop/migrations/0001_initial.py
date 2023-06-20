# Generated by Django 4.2.2 on 2023-06-19 08:49

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('computer_id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный идентификатор', primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('For game', 'For game'), ('For work needs', 'For work needs'), ('For video editing', 'For video editing')], default=('For work needs', 'For work needs'), max_length=17)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=2, help_text='Цена будет в рублях. Максимальная длина - 10 цифр, а после запятой - 2 цифры.', max_digits=10)),
                ('producting_country', models.CharField(choices=[('USA', 'USA'), ('China', 'China'), ('Korea', 'Korea'), ('Japan', 'Japan'), ('Russia', 'Russia'), ('Vietnam', 'Vietnam'), ('Germany', 'Germany'), ('Netherlands', 'Netherlands')], max_length=11)),
                ('guarantee', models.DecimalField(decimal_places=1, help_text='Гарантия на ПК. (учтите, что после запятой должна идти только 1 цифра, а цифр по количеству не должно быть больше 3. Пример: 1.2 года, 1 год, 12.5 года).', max_digits=3)),
                ('description', models.TextField()),
                ('video_card', models.CharField(choices=[('Встроенная в процессор', 'Встроенная в процессор'), ('Nvidia GTX 1080 ti 4gb', 'Nvidia GTX 1080 ti 4gb'), ('Nvidia GTX 1660 ti 6gb', 'Nvidia GTX 1660 ti 6gb'), ('Nvidia RTX 2060 ti 8gb', 'Nvidia RTX 2060 ti 8gb'), ('Nvidia RTX 3060 ti 8gb', 'Nvidia RTX 3060 ti 8gb'), ('Nvidia RTX 3070 ti 8gb', 'Nvidia RTX 3070 ti 8gb'), ('Nvidia RTX 3080 ti 12gb', 'Nvidia RTX 3080 ti 12gb'), ('Nvidia RTX 3090 ti 24gb', 'Nvidia RTX 3090 ti 24gb'), ('Nvidia RTX 4060 ti 8gb', 'Nvidia RTX 4060 ti 8gb'), ('Nvidia RTX 4070 ti 12gb', 'Nvidia RTX 4070 ti 12gb'), ('Nvidia RTX 4080 ti 16gb', 'Nvidia RTX 4080 ti 16gb'), ('Nvidia RTX 4090 ti 24gb', 'Nvidia RTX 4090 ti 24gb')], default=('Встроенная в процессор', 'Встроенная в процессор'), max_length=23)),
                ('cpu', models.CharField(choices=[('Intel Core i3-13100F 4x8 3.4Hz', 'Intel Core i3-13100F 4x8 3.4Hz'), ('Intel Core i5-10400F 6x12 2.9Hz', 'Intel Core i5-10400F 6x12 2.9Hz'), ('Intel Core i7-12700KF 12x20 3.6Hz', 'Intel Core i7-12700KF 12x20 3.6Hz'), ('Intel Core i9-13900F 24x32 2Hz', 'Intel Core i9-13900F 24x32 2Hz')], max_length=33, verbose_name='CPU')),
                ('case', models.CharField(choices=[('Cougar Duoface RGB', 'Cougar Duoface RGB'), ('DEEPCOOL MATREXX 30', 'DEEPCOOL MATREXX 30'), ('ARDOR GAMING Rare M2 ARGB', 'ARDOR GAMING Rare M2 ARGB'), ('DEXP DC-101B', 'DEXP DC-101B'), ('DEXP DC-201M', 'DEXP DC-201M')], max_length=25)),
                ('motherboard', models.CharField(choices=[('GIGABYTE B550 AORUS ELITE V2', 'GIGABYTE B550 AORUS ELITE V2'), ('MSI MPG B550 GAMING PLUS', 'MSI MPG B550 GAMING PLUS'), ('ASRock H510M-HVS R2.0', 'ASRock H510M-HVS R2.0')], max_length=28)),
                ('power_supply', models.CharField(choices=[('ExeCate AAA350 350W', 'ExeCate AAA350 350W'), ('HIPER HP-300SFX 288W', 'HIPER HP-300SFX 288W'), ('AeroCool Cylon 700W', 'AeroCool Cylon 700W'), ('Cougar XTC ARGB 600W', 'Cougar XTC ARGB 600W')], max_length=20)),
                ('ram', models.CharField(choices=[('Kingston FURY Beast Black 2x8 16gb', 'Kingston FURY Beast Black 2x8 16gb'), ('ADATA XPG GAMMIX D20 2x8 16gb', 'ADATA XPG GAMMIX D20 2x8 16gb'), ('AMD Radeon R9 Gamer Series 2x16 32gb', 'AMD Radeon R9 Gamer Series 2x16 32gb')], max_length=36, verbose_name='RAM')),
                ('num_fans', models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(35)], verbose_name='Number of fans')),
            ],
        ),
    ]
