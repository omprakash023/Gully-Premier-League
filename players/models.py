from django.db import models

# Create your models here.

CHOICES = (
    ("RBM", "RBM"),
    ("LBM", "LBM"),
    ("BW", "BW"),
    ("AR", "AR"),
)


class player(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12)
    rank = models.IntegerField()
    skill = models.CharField(max_length=20, choices=CHOICES)
    captain = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
