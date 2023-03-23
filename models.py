from django.db import models

# Create your models here.
TYPE_CHOICES = {
    ('0/10', '0/10'),
    ('1/10', '1/10'),
    ('2/10', '2/10'),
    ('3/10', '3/10'),
    ('4/10', '4/10'),
    ('5/10', '5/10'),
    ('6/10', '6/10'),
    ('7/10', '7/10'),
    ('8/10', '8/10'),
    ('9/10', '9/10'),
    ('10/10', '10/10'),
}

class MoviePickerModel(models.Model):
    Name = models.CharField(max_length=30, default="", blank=True)
    Title = models.CharField(max_length=30, default="", blank=True)
    Rate = models.CharField(max_length=10, choices=TYPE_CHOICES, default='0/10')
    Review = models.TextField(max_length=150, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Name
