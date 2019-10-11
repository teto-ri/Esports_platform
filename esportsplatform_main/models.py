from django.db import models

# Create your models here.
class Competition_info(models.Model):
    GAME = (
        ('LOL', '리그오브레전드'),
        ('OW', '오버워치'),
        ('PUBG', '배틀그라운드'),
    )
    c_game = models.CharField(max_length = 20, choices = GAME)
    c_name = models.CharField(max_length = 20)
    c_date = models.DateField()
    c_time = models.TimeField()
    c_tag = models.CharField(max_length = 10)

    c_rule = models.TextField()
    c_rule_file = models.FileField(null = True)
    c_prize = models.TextField()
    c_schedule = models.TextField()
    c_contact = models.TextField()


    


