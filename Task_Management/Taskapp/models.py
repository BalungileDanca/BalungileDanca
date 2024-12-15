from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(
        max_length=10,
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        default='medium'
    )
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=15,
        choices=[('incomplete', 'Incomplete'), ('complete', 'Complete')],
        default='incomplete'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

