from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

import uuid


class Computer(models.Model):

    LIST_COMPUTER_CATEGORIES = (
        ('Для игр', 'Для игр'),
        ('Для работы', 'Для работы'),
        ('Для монтажа видео', 'Для монтажа видео'),
    )

    COMPUTER_PRODUCING_COUNTRIES = (
        ('США', 'USA'),
        ('Китай', 'China',),
        ('Корея', 'Korea',),
        ('Япония', 'Japan',),
        ('Россия', 'Russia',),
        ('Вьетнам', 'Vietnam',),
        ('Германия', 'Germany',),
        ('Нидерланды', 'Netherlands',),
    )

    VIDEO_CARD_LIST = (
        ('Встроенная в процессор', 'Встроенная в процессор'),
        ('Nvidia GTX 1080 ti 4gb', 'Nvidia GTX 1080 ti 4gb'),
        ('Nvidia GTX 1660 ti 6gb', 'Nvidia GTX 1660 ti 6gb'),
        ('Nvidia RTX 2060 ti 8gb', 'Nvidia RTX 2060 ti 8gb'),
        ('Nvidia RTX 3060 ti 8gb', 'Nvidia RTX 3060 ti 8gb'),
        ('Nvidia RTX 3070 ti 8gb', 'Nvidia RTX 3070 ti 8gb'),
        ('Nvidia RTX 3080 ti 12gb', 'Nvidia RTX 3080 ti 12gb'),
        ('Nvidia RTX 3090 ti 24gb', 'Nvidia RTX 3090 ti 24gb'),
        ('Nvidia RTX 4060 ti 8gb', 'Nvidia RTX 4060 ti 8gb'),
        ('Nvidia RTX 4070 ti 12gb', 'Nvidia RTX 4070 ti 12gb'),
        ('Nvidia RTX 4080 ti 16gb', 'Nvidia RTX 4080 ti 16gb'),
        ('Nvidia RTX 4090 ti 24gb', 'Nvidia RTX 4090 ti 24gb'),
    )

    CPU = (
        ('Intel Core i3-13100F 4x8 3.4Hz', 'Intel Core i3-13100F 4x8 3.4Hz'),
        ('Intel Core i5-10400F 6x12 2.9Hz', 'Intel Core i5-10400F 6x12 2.9Hz'),
        ('Intel Core i7-12700KF 12x20 3.6Hz', 'Intel Core i7-12700KF 12x20 3.6Hz'),
        ('Intel Core i9-13900F 24x32 2Hz', 'Intel Core i9-13900F 24x32 2Hz')
    )

    LIST_OF_POWER_SUPPLIES = (
        ('ExeCate AAA350 350W', 'ExeCate AAA350 350W'),
        ('HIPER HP-300SFX 288W', 'HIPER HP-300SFX 288W'),
        ('AeroCool Cylon 700W', 'AeroCool Cylon 700W'),
        ('Cougar XTC ARGB 600W', 'Cougar XTC ARGB 600W')
    )

    MOTHERBOARD_LIST = (
        ('GIGABYTE B550 AORUS ELITE V2', 'GIGABYTE B550 AORUS ELITE V2'),
        ('MSI MPG B550 GAMING PLUS', 'MSI MPG B550 GAMING PLUS'),
        ('ASRock H510M-HVS R2.0', 'ASRock H510M-HVS R2.0'),
    )

    CASE_LIST = (
        ('Cougar Duoface RGB', 'Cougar Duoface RGB'),
        ('DEEPCOOL MATREXX 30', 'DEEPCOOL MATREXX 30'),
        ('ARDOR GAMING Rare M2 ARGB', 'ARDOR GAMING Rare M2 ARGB'),
        ('DEXP DC-101B', 'DEXP DC-101B'),
        ('DEXP DC-201M', 'DEXP DC-201M'),
    )

    RAM_LIST = (
        ('Kingston FURY Beast Black 2x8 16gb', 'Kingston FURY Beast Black 2x8 16gb'),
        ('ADATA XPG GAMMIX D20 2x8 16gb', 'ADATA XPG GAMMIX D20 2x8 16gb'),
        ('AMD Radeon R9 Gamer Series 2x16 32gb', 'AMD Radeon R9 Gamer Series 2x16 32gb'),
    )

    # External characteristics of the PC.
    computer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный идентификатор")
    category = models.CharField(choices=LIST_COMPUTER_CATEGORIES, max_length=17, default=LIST_COMPUTER_CATEGORIES[1])
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Цена будет в рублях. Максимальная длина - 10 цифр, а после запятой - 2 цифры.")
    producting_country = models.CharField(choices=COMPUTER_PRODUCING_COUNTRIES, max_length=11)
    guarantee = models.DecimalField(max_digits=3, decimal_places=1, help_text="Гарантия на ПК. (учтите, что после запятой должна идти только 1 цифра, а цифр по количеству не должно быть больше 3. Пример: 1.2 года, 1 год, 12.5 года).")
    description = models.TextField()

    # PC internal specifications.
    video_card = models.CharField(choices=VIDEO_CARD_LIST, max_length=23, default=VIDEO_CARD_LIST[0])
    cpu = models.CharField(choices=CPU, max_length=33, verbose_name='CPU')
    case = models.CharField(choices=CASE_LIST, max_length=25)
    motherboard = models.CharField(choices=MOTHERBOARD_LIST, max_length=28)
    power_supply = models.CharField(choices=LIST_OF_POWER_SUPPLIES, max_length=20)
    ram = models.CharField(choices=RAM_LIST, max_length=36, verbose_name='RAM')
    num_fans = models.PositiveIntegerField(default=3, verbose_name="Number of fans", validators=[MinValueValidator(0), MaxValueValidator(35)])


    class Meta:
        pass


    def get_absolute_url(self):
        """Возвращает URL адрес для доступа к конкретному компьютеру."""
        return reverse('shop:computer-detail', args=[str(self.computer_id)])


    def __str__(self):
        return self.name