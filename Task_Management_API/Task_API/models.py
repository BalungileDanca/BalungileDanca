from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from django.utils import timezone

User = get_user_model()
class Task(models.Model):
    PRIORITY_LEVELS = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority_level = models.CharField(max_length=10, choices=PRIORITY_LEVELS)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    completed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == 'Complete' and not self.completed_at:
            self.completed_at = timezone.now()  # Use timezone-aware datetime
        # Reset 'completed_at' if the status changes back to 'Pending'
        if self.status == 'Pending':
            self.completed_at = None
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
