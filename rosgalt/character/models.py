from django.contrib.auth.models import User
from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименования класса')
    description = models.CharField(max_length=9999, verbose_name='Описание класса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"


class Rarity(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование редкости')
    text_color = models.CharField(max_length=20, verbose_name='HEX-представление цвета выделения редкости')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Редкость"
        verbose_name_plural = "Редкости"


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование типа')
    related_name = models.CharField(max_length=30, verbose_name='Что описывает')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование способности')
    type = models.ForeignKey(Type, related_name='slill_type', on_delete=models.CASCADE,
                             verbose_name='Тип способности')
    description = models.CharField(max_length=9999, verbose_name='Описание способности')
    image = models.ImageField(upload_to='images/skills/', verbose_name='Изображение')
    rarity = models.ForeignKey(Rarity, related_name='item_rarity', on_delete=models.CASCADE,
                               verbose_name='Редкость способности')


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование предмета')
    rarity = models.ForeignKey(Rarity, related_name='item_rarity', on_delete=models.CASCADE,
                               verbose_name='Редкость предмета')
    require_strength = models.IntegerField(verbose_name='Необходимая сила персонажа')
    require_agility = models.IntegerField(verbose_name='Необходимая ловкость персонажа')
    require_intellect = models.IntegerField(verbose_name='Необходимый интеллект персонажа')
    description = models.CharField(max_length=9999, verbose_name='Описание предмета')
    buy_cost = models.PositiveIntegerField(verbose_name='Стоимость предмета к покупке')
    sell_cost = models.PositiveIntegerField(verbose_name='Стоимость предмета к продаже')
    image = models.ImageField(upload_to='images/items/', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Artifact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование артефакта')
    description = models.CharField(max_length=9999, verbose_name='Описание артефакта')
    rarity = models.ForeignKey(Rarity, related_name='item_rarity', on_delete=models.CASCADE,
                               verbose_name='Редкость артефакта')
    image = models.ImageField(upload_to='images/artifacts/', verbose_name='Изображение')
    sell_cost = models.PositiveIntegerField(verbose_name='Стоимость артефакта к продаже')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Артефакт"
        verbose_name_plural = "Артефакты"


class Character(models.Model):
    created_by = models.ForeignKey(User, related_name='character_created_by', on_delete=models.CASCADE,
                                   verbose_name='Кто создал')
    name = models.CharField(max_length=100, verbose_name='Имя персонажа')
    dignity = models.CharField(max_length=100, verbose_name='Титул персонажа')
    main_class = models.ForeignKey(Class, related_name='character_class', on_delete=models.CASCADE,
                                   verbose_name='Класс персонажа')
    max_health = models.IntegerField(verbose_name="Максимальное здоровье персонажа")
    health = models.IntegerField(verbose_name='Текущие здоровье персонажа')
    strength = models.IntegerField(verbose_name='Сила персонажа')
    agility = models.IntegerField(verbose_name='Ловкость персонажа')
    intellect = models.IntegerField(verbose_name='Интеллект персонажа')
    charisma = models.IntegerField(verbose_name='Харизма персонажа')
    educability = models.IntegerField(verbose_name='Способность к обучению персонажа')
    inventory_capacity = models.IntegerField(verbose_name='Размер инвентаря')
    inventory = models.ManyToManyField(Item, related_name='character_inventory', blank=True,
                                       verbose_name='Инвентарь персонажа')
    level = models.PositiveIntegerField(verbose_name='Уровень персонажа')
    lore = models.CharField(max_length=9999, verbose_name='Лор персонажа')
    equipped_helm = models.ForeignKey(Item, related_name='character_helm', blank=True, on_delete=models.CASCADE,
                                      verbose_name='Экипированный шлем')
    equipped_chest = models.ForeignKey(Item, related_name='character_chest', blank=True, on_delete=models.CASCADE,
                                       verbose_name='Экипированный нагрудник')
    equipped_pants = models.ForeignKey(Item, related_name='character_pants', blank=True, on_delete=models.CASCADE,
                                       verbose_name='Экипированные штаны')
    equipped_boots = models.ForeignKey(Item, related_name='character_boots', blank=True, on_delete=models.CASCADE,
                                       verbose_name='Экипированные ботинки')
    equipped_gloves = models.ForeignKey(Item, related_name='character_gloves', blank=True, on_delete=models.CASCADE,
                                        verbose_name='Экипированные перчатки')
    equipped_ring = models.ForeignKey(Item, related_name='character_ring', blank=True, on_delete=models.CASCADE,
                                      verbose_name='Экипированное кольцо')
    equipped_neck = models.ForeignKey(Item, related_name='character_neck', blank=True, on_delete=models.CASCADE,
                                      verbose_name='Экипированное ожерелье')

    # TODO Культивация-синоним, как будут применяться способности и вообще как будут проходить бои

    def __str__(self):
        return f"{self.name} {self.dignity} {self.level} уровня"

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"
