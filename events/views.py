from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Booking
from .forms import EventForm

def event_list(request):
    events = Event.objects.filter(status="active")
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user).values_list('event_id', flat=True)
    else:
        user_bookings = []
    return render(request, 'events/event_list.html', {'events': events, 'user_bookings': user_bookings})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            messages.success(request, 'Event created successfully.')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/edit_event.html', {'form': form})

# @login_required
def update_event(request, event_id):
    events=Event.objects.all()
    for event in events:
        print(event.id,event.name,event.created_by,request.user)
    event = get_object_or_404(Event, id=event_id)
    print(event)
    print(event.id,event.name,event.created_by,request.user)
    
    # event = get_object_or_404(Event, id=event_id, created_by=request.user)
    
    
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully.')
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form})

@login_required
def delete_event(request, event_id):
    # event = get_object_or_404(Event, id=event_id, created_by=request.user)
    print(event_id,request.method)
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        # event.delete()
        print(event_id,request.method)
        messages.success(request, 'Event deleted successfully.')
        return redirect('event_list')
    # return render(request, 'events/event_list.html', {'event': event})
    return redirect('event_list')

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, status="active")
    if Booking.objects.filter(event=event, user=request.user).exists():
        messages.info(request, 'You have already booked this event.')
    else:
        Booking.objects.create(event=event, user=request.user)
        messages.success(request, 'Event booked successfully.')
    return redirect('event_list')
