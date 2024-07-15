# Generated by Django 5.0.7 on 2024-07-15 20:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименования класса')),
                ('description', models.CharField(max_length=9999, verbose_name='Описание класса')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование предмета')),
                ('require_strength', models.IntegerField(verbose_name='Необходимая сила персонажа')),
                ('require_agility', models.IntegerField(verbose_name='Необходимая ловкость персонажа')),
                ('require_intellect', models.IntegerField(verbose_name='Необходимый интеллект персонажа')),
                ('description', models.CharField(max_length=9999, verbose_name='Описание предмета')),
                ('buy_cost', models.PositiveIntegerField(verbose_name='Стоимость предмета к покупке')),
                ('sell_cost', models.PositiveIntegerField(verbose_name='Стоимость предмета к продаже')),
                ('image', models.ImageField(upload_to='images/items/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование редкости')),
                ('text_color', models.CharField(max_length=20, verbose_name='HEX-представление цвета выделения редкости')),
            ],
            options={
                'verbose_name': 'Редкость',
                'verbose_name_plural': 'Редкости',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование типа')),
                ('related_name', models.CharField(max_length=30, verbose_name='Что описывает')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя персонажа')),
                ('dignity', models.CharField(max_length=100, verbose_name='Титул персонажа')),
                ('max_health', models.IntegerField(verbose_name='Максимальное здоровье персонажа')),
                ('health', models.IntegerField(verbose_name='Текущие здоровье персонажа')),
                ('strength', models.IntegerField(verbose_name='Сила персонажа')),
                ('agility', models.IntegerField(verbose_name='Ловкость персонажа')),
                ('intellect', models.IntegerField(verbose_name='Интеллект персонажа')),
                ('charisma', models.IntegerField(verbose_name='Харизма персонажа')),
                ('educability', models.IntegerField(verbose_name='Способность к обучению персонажа')),
                ('inventory_capacity', models.IntegerField(verbose_name='Размер инвентаря')),
                ('level', models.PositiveIntegerField(verbose_name='Уровень персонажа')),
                ('lore', models.CharField(max_length=9999, verbose_name='Лор персонажа')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Кто создал')),
                ('main_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_class', to='character.class', verbose_name='Класс персонажа')),
                ('equipped_boots', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_boots', to='character.item', verbose_name='Экипированные ботинки')),
                ('equipped_chest', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_chest', to='character.item', verbose_name='Экипированный нагрудник')),
                ('equipped_gloves', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_gloves', to='character.item', verbose_name='Экипированные перчатки')),
                ('equipped_helm', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_helm', to='character.item', verbose_name='Экипированный шлем')),
                ('equipped_neck', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_neck', to='character.item', verbose_name='Экипированное ожерелье')),
                ('equipped_pants', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_pants', to='character.item', verbose_name='Экипированные штаны')),
                ('equipped_ring', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_ring', to='character.item', verbose_name='Экипированное кольцо')),
                ('inventory', models.ManyToManyField(blank=True, related_name='character_inventory', to='character.item', verbose_name='Инвентарь персонажа')),
            ],
            options={
                'verbose_name': 'Персонаж',
                'verbose_name_plural': 'Персонажи',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='rarity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_rarity', to='character.rarity', verbose_name='Редкость предмета'),
        ),
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование артефакта')),
                ('description', models.CharField(max_length=9999, verbose_name='Описание артефакта')),
                ('image', models.ImageField(upload_to='images/artifacts/', verbose_name='Изображение')),
                ('sell_cost', models.PositiveIntegerField(verbose_name='Стоимость артефакта к продаже')),
                ('rarity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artifact_rarity', to='character.rarity', verbose_name='Редкость артефакта')),
            ],
            options={
                'verbose_name': 'Артефакт',
                'verbose_name_plural': 'Артефакты',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование способности')),
                ('description', models.CharField(max_length=9999, verbose_name='Описание способности')),
                ('image', models.ImageField(upload_to='images/skills/', verbose_name='Изображение')),
                ('rarity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_rarity', to='character.rarity', verbose_name='Редкость способности')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_type', to='character.type', verbose_name='Тип способности')),
            ],
        ),
    ]
