from queue import Empty
from statistics import mode
from unicodedata import name
from django.db import models

# Enums 
class ClassTypes(models.TextChoices):
    DRUID = "Druid"
    DEATHKNIGHT = "DeathKnight"
    HUNTER = "Hunter"
    ROGUE = "Rogue"
    PALADIN = "Paladin"
    PRIEST = "Priest"
    MAGE = "Mage"
    SHAMAN = "Shaman"
    WARRIOR = "Warrior"
    WARLOCK = "Warlock"
class SpecTypes(models.TextChoices):
    #Druid
    RESTO = "Restoration"
    FERAL = "Feral"
    BALANCE = "Balance"
    #DeathKnight
    BLOOD = "Blood"
    FROST = "Frost"
    UNHOLY = "Unholy"
    #Hunter
    SURVIVAL = "Survival"
    MARKSMAN = "Marksman"
    BEAST_MASTER = "Beast Master"
    #Rogue
    COMBAT = "Combat"
    ASSASSINATION = "Assassination"
    SUBTLETY = "Subtlety"
    #Paladin
    HOLY = "Holy"
    RETRIBUTION = "Retribution"
    PROTECTION = "Protection"
    #Priest
    SHADOW = "Shadow"
    DISCIPLINE = "Discipline"
    #Mage
    FIRE = "Fire"
    Arcane = "Arcane"
    #Shaman
    ELEMENTAL = "Elemental"
    ENHANCEMENT = "Enhancement"
    #Warrior
    FURY = "Fury"
    ARMS = "Arms"
    #Warlock
    DESTRUCTION = "Destruction"
    DEMOLOGY = "Demology"
    AFFLICTION = "Affliction"
class BuffType(models.TextChoices):
    AGIL_AND_STR = "Agility and Strength"
    ARMOR_PERC = "Armor Percent"
    ATCK_POW = "Attack Power"
    ATCK_POW_PERC = "Attack Power Percent"
    HERO = "Heroism"
    DAMAGE_PERC = "Damage Percent"
    DAMAGE_REDUCT_PERC = "Damage Reduction Percent"
    HASTE_PERC = "Haste Percent"
    HEALING_REC_PERC = "Healing Recieved Percent"
    HEALTH = "Heath"
    INT = "Intellect"
    MANA_PER = "Mana Per Second"
    MELE_CRIT_PERC = "Melee Critical Percent"
    MELE_HASTE_PERC = "Melee Haste Percent"
    REPLINISH = "Replenishment"
class RoleType(models.TextChoices):
    TANK = "Tank"
    RANGED_DPS = "Ranged DPS"
    MELEE_DPS = "Melee DPS"
    HEALER = "Healer"
class FactionType(models.TextChoices):
    alliance = "Alliance"
    horde = "Horde"
    both = "Both"
# Create your models here.
class Spell(models.Model):
    spell_id = models.AutoField(primary_key = True)
    buff_name = models.CharField(max_length=200)
    buff_description = models.CharField(max_length=200)
    buff_type = models.CharField(max_length = 200, choices = BuffType.choices, default=Empty)

class Class(models.Model):
    class_id = models.AutoField(primary_key = True)
    class_name = models.CharField(max_length = 200, choices = ClassTypes.choices, default = ClassTypes.DRUID)
    spec = models.CharField(max_length = 200, choices = SpecTypes.choices, default = SpecTypes.AFFLICTION)
    buff_name = models.ForeignKey(Spell, on_delete=models.DO_NOTHING, default="", null=True)
    role = models.CharField(max_length=200, choices = RoleType.choices)

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    classes = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    start_free_time = models.DateTimeField
    end_free_time = models.DateField

class Roster(models.Model):
    roster_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    players = models.ForeignKey(Player, on_delete = models.CASCADE)
    guild = models.CharField(max_length=200, default="N/A")
    start_time = models.DateTimeField(null = True)
    end_time = models.DateTimeField(null = True)
    realm = models.CharField(max_length=200)
    faction = models.CharField(max_length=200, choices = FactionType.choices, default = FactionType.both)

    

