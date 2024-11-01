// Toggle password visibility
function togglePassword() {
    const passwordField = document.getElementById("password");
    const toggleIcon = passwordField.nextElementSibling;
    if (passwordField.type === "password") {
        passwordField.type = "text";
        toggleIcon.classList.replace("fa-eye", "fa-eye-slash");
    } else {
        passwordField.type = "password";
        toggleIcon.classList.replace("fa-eye-slash", "fa-eye");
    }
}

function toggleConfirmPassword() {
    const confirmPasswordField = document.getElementById("confirmPassword");
    const toggleIcon = confirmPasswordField.nextElementSibling;
    if (confirmPasswordField.type === "password") {
        confirmPasswordField.type = "text";
        toggleIcon.classList.replace("fa-eye", "fa-eye-slash");
    } else {
        confirmPasswordField.type = "password";
        toggleIcon.classList.replace("fa-eye-slash", "fa-eye");
    }
}

// Form validation
function validateForm(event) {
    let isValid = true;
    const username = document.getElementById("fullName").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Username validation
    if (username === "") {
        document.getElementById("nameError").style.display = "block";
        isValid = false;
    } else {
        document.getElementById("nameError").style.display = "none";
    }

    // Email validation (basic)
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        document.getElementById("emailError").style.display = "block";
        isValid = false;
    } else {
        document.getElementById("emailError").style.display = "none";
    }

    // Password validation
    if (password.length < 8) {
        document.getElementById("passwordError").style.display = "block";
        isValid = false;
    } else {
        document.getElementById("passwordError").style.display = "none";
    }

    // Confirm password validation
    if (password !== confirmPassword) {
        document.getElementById("confirmPasswordError").style.display = "block";
        isValid = false;
    } else {
        document.getElementById("confirmPasswordError").style.display = "none";
    }

    // Prevent form submission if invalid
    if (!isValid) event.preventDefault();
    return isValid;
}

// Password strength meter
document.getElementById("password").addEventListener("input", function () {
    const strengthMeter = document.getElementById("strengthMeter");
    const password = this.value;

    let strength = 0;
    if (password.length >= 8) strength += 1;
    if (/[A-Z]/.test(password)) strength += 1;
    if (/[a-z]/.test(password)) strength += 1;
    if (/[0-9]/.test(password)) strength += 1;
    if (/[^A-Za-z0-9]/.test(password)) strength += 1;

    strengthMeter.style.width = (strength * 20) + "%";
    if (strength <= 2) {
        strengthMeter.style.backgroundColor = "red";
    } else if (strength <= 4) {
        strengthMeter.style.backgroundColor = "orange";
    } else {
        strengthMeter.style.backgroundColor = "green";
    }
});
