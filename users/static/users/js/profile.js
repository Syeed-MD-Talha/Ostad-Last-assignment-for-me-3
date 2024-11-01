document.addEventListener('DOMContentLoaded', function() {
    // Profile picture upload
    const profilePicture = document.querySelector('.profile-picture');
    profilePicture.addEventListener('click', function() {
        // This would trigger file upload in the backend
        console.log('Upload profile picture');
    });

    // Form submission
    const saveButtons = document.querySelectorAll('.btn-primary');
    saveButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // e.preventDefault();
            // This would be connected to your backend
            alert('Changes saved successfully!');
        });
    });

    // Preference toggles
    const preferences = document.querySelectorAll('.preference-item input');
    preferences.forEach(pref => {
        pref.addEventListener('change', function() {
            // This would update preferences in the backend
            console.log(`${this.id} changed to ${this.checked}`);
        });
    });

    console.log("hello guys how are you?")
});



document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('profile-image-upload');
    const profileImage = document.querySelector('.profile-picture img');
    const defaultIcon = document.querySelector('.profile-picture .fas.fa-user');
    
    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            // Create a preview of the image
            const reader = new FileReader();
            reader.onload = function(event) {
                // If there's currently an icon showing, hide it
                if (defaultIcon) {
                    defaultIcon.style.display = 'none';
                }
                
                // If there's no img element yet, create one
                if (!profileImage) {
                    const newImage = document.createElement('img');
                    newImage.alt = "Profile picture";
                    document.querySelector('.profile-picture').prepend(newImage);
                    // Update the profileImage reference
                    profileImage = newImage;
                }
                
                // Show the preview
                profileImage.src = event.target.result;
                
                // Create a FormData object and submit
                const formData = new FormData();
                formData.append('image', file);
                formData.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);
                
                // Send the image to the server
                fetch(window.location.href, {
                    method: 'POST',
                    body: formData,
                    credentials: 'same-origin'
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Show success message
                        const messageDiv = document.createElement('div');
                        messageDiv.className = 'alert alert-success';
                        messageDiv.textContent = 'Profile picture updated successfully!';
                        document.querySelector('.profile-container').prepend(messageDiv);
                        
                        // Remove message after 3 seconds
                        setTimeout(() => messageDiv.remove(), 2000);
                    }
                })
                .catch(error => console.error('Error:', error));
            };
            reader.readAsDataURL(file);
        }
    });
});