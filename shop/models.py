from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import uuid


class Computer(models.Model):

    LIST_COMPUTER_CATEGORIES = (
        ('game', 'For game'),
        ('worker', 'For work needs'),
        ('editing', 'For video editing'),
    )

    COMPUTER_PRODUCING_COUNTRIES = (
        ('us', 'USA'),
        ('cn', 'China',),
        ('kr', 'Korea',),
        ('jp', 'Japan',),
        ('ru', 'Russia',),
        ('vn', 'Vietnam',),
        ('de', 'Germany',),
        ('nl', 'Netherlands',),
    )

    VIDEO_CARD_LIST = (
        ('built-in', 'Built into the processor'),
        ('1080', 'Nvidia GTX 1080 ti 4gb'),
        ('1660', 'Nvidia GTX 1660 ti 6gb'),
        ('2060', 'Nvidia RTX 2060 ti 8gb'),
        ('3060', 'Nvidia RTX 3060 ti 8gb'),
        ('3070', 'Nvidia RTX 3070 ti 8gb'),
        ('3080', 'Nvidia RTX 3080 ti 12gb'),
        ('3090', 'Nvidia RTX 3090 ti 24gb'),
        ('4060', 'Nvidia RTX 4060 ti 8gb'),
        ('4070', 'Nvidia RTX 4070 ti 12gb'),
        ('4080', 'Nvidia RTX 4080 ti 16gb'),
        ('4090', 'Nvidia RTX 4090 ti 24gb'),
    )

    CPU = (
        ('13', 'Intel Core i3-13100F 4x8 3.4Hz'),
        ('i5', 'Intel Core i5-10400F 6x12 2.9Hz'),
        ('i7', 'Intel Core i7-12700KF 12x20 3.6Hz'),
        ('i9', 'Intel Core i9-13900F 24x32 2Hz')
    )

    LIST_OF_POWER_SUPPLIES = (
        ('execate', 'ExeCate AAA350 350W'),
        ('hiper', 'HIPER HP-300SFX 288W'),
        ('aerocool', 'AeroCool Cylon 700W'),
        ('cougar', 'Cougar XTC ARGB 600W')
    )

    MOTHERBOARD_LIST = (
        ('gigabyte', 'GIGABYTE B550 AORUS ELITE V2'),
        ('msi', 'MSI MPG B550 GAMING PLUS'),
        ('asrock', 'ASRock H510M-HVS R2.0'),
    )

    CASE_LIST = (
        ('cougar', 'Cougar Duoface RGB'),
        ('deepcool', 'DEEPCOOL MATREXX 30'),
        ('ardor', 'ARDOR GAMING Rare M2 ARGB'),
        ('dexp', 'DEXP DC-101B'),
        ('dexp', 'DEXP DC-201M'),
    )

    RAM_LIST = (
        ('kingston', 'Kingston FURY Beast Black 2x8 16gb'),
        ('adata xpg', 'ADATA XPG GAMMIX D20 2x8 16gb'),
        ('amd', 'AMD Radeon R9 Gamer Series 2x16 32gb'),
    )



    # External characteristics of the PC.
    computer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный идентификатор")
    category = models.CharField(choices=LIST_COMPUTER_CATEGORIES, max_length=7, default=LIST_COMPUTER_CATEGORIES[1])
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Цена будет в рублях. Максимальная длина - 10 цифр, а после запятой - 2 цифры.")
    producting_country = models.CharField(choices=COMPUTER_PRODUCING_COUNTRIES, max_length=2)
    guarantee = models.DecimalField(max_digits=3, decimal_places=1, help_text="Гарантия на ПК. (учтите, что после запятой должна идти только 1 цифра, а цифр по количеству не должно быть больше 3. Пример: 1.2 года, 1 год, 12.5 года).")
    description = models.TextField()

    # PC internal specifications.
    video_card = models.CharField(choices=VIDEO_CARD_LIST, max_length=8, default=VIDEO_CARD_LIST[0])
    cpu = models.CharField(choices=CPU, max_length=2, verbose_name='CPU')
    case = models.CharField(choices=CASE_LIST, max_length=8)
    motherboard = models.CharField(choices=MOTHERBOARD_LIST, max_length=8),
    power_supply = models.CharField(choices=LIST_OF_POWER_SUPPLIES, max_length=8)
    ram = models.CharField(choices=RAM_LIST, max_length=9, verbose_name='RAM')
    num_fans = models.PositiveIntegerField(default=3, verbose_name="Number of fans", validators=[MinValueValidator(0), MaxValueValidator(35)])

    class Meta:
        pass

    def __str__(self):
        return self.name