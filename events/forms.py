from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'category', 'date', 'location', 'description', 'max_attendees', 'status']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Adding custom attributes for each field to match HTML template
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'id': 'eventName', 'required': True})
        
        self.fields['category'].widget = forms.Select(
            attrs={'class': 'form-control', 'id': 'eventCategory', 'required': True},
            choices=[('', 'Select Category'), ('conference', 'Conference'), ('concert', 'Concert'), ('workshop', 'Workshop'), ('sports', 'Sports')]
        )
        
        self.fields['date'].widget = forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control', 'id': 'eventDate', 'required': True}
        )
        
        self.fields['location'].widget.attrs.update({'class': 'form-control', 'id': 'eventLocation', 'required': True})
        
        self.fields['description'].widget = forms.Textarea(
            attrs={'class': 'form-control', 'id': 'eventDescription', 'rows': 4, 'required': True}
        )
        
        self.fields['max_attendees'].widget.attrs.update({'class': 'form-control', 'id': 'maxAttendees', 'min': 1, 'required': True})
        
        self.fields['status'].widget = forms.Select(
            attrs={'class': 'form-control', 'id': 'eventStatus', 'required': True},
            choices=[('active', 'Active'), ('draft', 'Draft')]
        )
