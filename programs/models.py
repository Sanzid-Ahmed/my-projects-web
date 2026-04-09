from django.db import models

class Programs(models.Model): 

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
    project = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    project_req=models.TextField(max_length=255, null=True)
    finish_date=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)


    def __str__(self):
        return f"{self.title} cost = {self.cost}"
