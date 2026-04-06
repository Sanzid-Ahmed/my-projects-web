from django.db import models

class Projects(models.Model): 

    STATUS_TYPE = [
        ('locked', 'Locked'),
        ('unlocked', 'Unlocked'),
        ('restricted', 'Restricted'),
    ]


    title=models.CharField(max_length=255)
    cost=models.IntegerField(default=0)
    status=models.CharField(
        max_length=25,
        choices=STATUS_TYPE,
        default='locked'
    )
    profile_req=models.IntegerField(default=0)
    project_req=models.TextField(max_length=255)
    finish_date=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} cost = {self.cost}"
