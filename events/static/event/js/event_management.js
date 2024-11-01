// Show/Hide Event Form
const createEventBtn = document.getElementById('createEventBtn');
const eventForm = document.getElementById('eventForm');
const deleteModal = document.getElementById('deleteModal');
let currentDeleteId = null;

createEventBtn.addEventListener('click', () => {
    eventForm.style.display = 'block';
    eventForm.reset();
    window.scrollTo({ top: eventForm.offsetTop - 100, behavior: 'smooth' });
});

function hideEventForm() {
    eventForm.style.display = 'none';
}

// Form Submission
eventForm.addEventListener('submit', (e) => {
    e.preventDefault();
    // Here you would typically send the data to your backend
    const formData = {
        name: document.getElementById('eventName').value,
        category: document.getElementById('eventCategory').value,
        date: document.getElementById('eventDate').value,
        location: document.getElementById('eventLocation').value,
        description: document.getElementById('eventDescription').value,
        maxAttendees: document.getElementById('maxAttendees').value,
        status: document.getElementById('eventStatus').value
    };
    console.log('Form submitted:', formData);
    hideEventForm();
});

// Edit Event
function editEvent(id) {
    // Here you would typically fetch the event data from your backend
    eventForm.style.display = 'block';
    window.scrollTo({ top: eventForm.offsetTop - 100, behavior: 'smooth' });
}

// Delete Event
function deleteEvent(id) {
    currentDeleteId = id;
    deleteModal.style.display = 'block';
}

function confirmDelete() {
    // Here you would typically send the delete request to your backend
    console.log('Deleting event:', currentDeleteId);
    closeDeleteModal();
}

function closeDeleteModal() {
    deleteModal.style.display = 'none';
    currentDeleteId = null;
}

// Close modal when clicking outside
window.onclick = function(event) {
    if (event.target == deleteModal) {
        closeDeleteModal();
    }
}

// Close modal when clicking X
document.querySelector('.close').onclick = closeDeleteModal;