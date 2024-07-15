from django.contrib import admin
from .models import Class, Rarity, Type, Skill, Item, Artifact, Character

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Rarity)
class RarityAdmin(admin.ModelAdmin):
    list_display = ['name', 'text_color']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'related_name']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'rarity']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'rarity', 'require_strength', 'require_agility', 'require_intellect', 'buy_cost', 'sell_cost']

@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'rarity', 'sell_cost']

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'dignity', 'main_class', 'level', 'created_by']
