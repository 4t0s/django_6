from django.db import models
from django.core.validators import MinValueValidator
import ast

class Team(models.Model):
    class Sport(models.TextChoices):
        FOOTBALL = 'FB'
        BASKETBALL = 'BS'
        VOLLEYBALL = 'VL'
    name = models.CharField(max_length=100)
    creation_year = models.IntegerField(validators = [MinValueValidator(0)])
    sport = models.CharField(max_length=2, choices = Sport.choices)
    coach = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} {self.creation_year} - {self.get_sport_display()}'

class Player(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    height = models.IntegerField(validators = [MinValueValidator(100)])
    weight = models.IntegerField(validators = [MinValueValidator(0)])
    def __str__(self):
        return f'{self.f_name} {self.l_name} - {self.team}'
    
class ListField(models.TextField):
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return ast.unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class dz(models.Model):
    test_list = ListField()
    def __str__(self):
        return f'{test_list}'
