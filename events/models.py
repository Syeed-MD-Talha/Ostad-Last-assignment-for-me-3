from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=[('conference', 'Conference'), ('concert', 'Concert'), ('workshop', 'Workshop'), ('sports', 'Sports')])
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    max_attendees = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('draft', 'Draft')])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.event.name}"
