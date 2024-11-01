from django.contrib import admin
from .models import Event, Booking

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date', 'location', 'status', 'created_by')
    list_filter = ('status', 'category', 'date')
    search_fields = ('name', 'location', 'description')
    date_hierarchy = 'date'
    ordering = ('-date',)
    readonly_fields = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not change:  # Only set created_by during creation
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'booked_at')
    list_filter = ('event', 'user')
    search_fields = ('event__name', 'user__username')
    ordering = ('-booked_at',)
