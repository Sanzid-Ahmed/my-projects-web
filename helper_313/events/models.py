from django.db import models

class Event(models.Model):

    # ✅ STATUS (controlled values)
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('pending', 'Pending'),
        ('finished', 'Finished'),
    ]

    TASK_TYPE_CHOICES = [
        ('normal', 'Normal'),
        ('event', 'Event'),
        ('assignment', 'Assignment'),
        ('project', 'Project'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    occur_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ FROM FRONTEND (but controlled)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    # ✅ FROM FRONTEND (flexible input)
    part_of = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    branch_of = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    sub_branch_of = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    task_type = models.CharField(
        max_length=20,
        choices=TASK_TYPE_CHOICES,
        default='normal'
    )

    def __str__(self):
        return f"{self.title} ({self.status})"