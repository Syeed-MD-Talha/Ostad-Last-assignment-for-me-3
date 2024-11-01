from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from .models import Profile


from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View


class ProfileView(View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)

        # Check if the current user is the profile owner or an admin
        if request.user.is_authenticated and (
            request.user.is_staff or user.id == request.user.id
        ):
            return render(request, "users/profile.html", {"user": user})
        else:
            return redirect("404_page")

    def post(self, request, id):
        user = get_object_or_404(User, id=id)

        # Check if the current user is the profile owner or an admin
        if request.user.is_authenticated and (
            request.user.is_staff or user.id == request.user.id
        ):
            # Handle AJAX image upload
            if request.FILES.get("image"):
                user.profile.image = request.FILES["image"]
                user.profile.save()
                return JsonResponse({"success": True})

            # Handle regular form submission
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.save()

            user.profile.phone = request.POST.get("phone")
            user.profile.location = request.POST.get("location")
            user.profile.save()

            messages.success(request, "Profile updated successfully!")
            return render(request, "users/profile.html", {"user": user})

        return redirect("users:home")


# class ProfileView(View):
#     def get(self, request, id):
#         user = get_object_or_404(User, id=id)
#         if user and request.user.is_authenticated and user.id==request.user.id:
#             return render(request, "users/profile.html", {"user": user})
#         else:
#           return redirect('404_page')

#     def post(self, request, id):
#         user = get_object_or_404(User, id=id)
#         if user and  request.user.is_authenticated and user.id==request.user.id:
#             # Check if it's an AJAX image upload
#             if request.FILES.get("image"):
#                 user.profile.image = request.FILES["image"]
#                 user.profile.save()
#                 return JsonResponse({"success": True})

#             # Handle regular form submission
#             user.first_name = request.POST.get("first_name")
#             user.last_name = request.POST.get("last_name")
#             user.email = request.POST.get("email")
#             user.save()

#             user.profile.phone = request.POST.get("phone")
#             user.profile.location = request.POST.get("location")
#             user.profile.save()

#             messages.success(request, "Profile updated successfully!")
#             return render(request, "users/profile.html", {"user": user})

#         return redirect("users:home")

# class ProfileView(View):
#     def get(self, request, id):
#         profile = get_object_or_404(Profile, id=id)
#         return render(request, "users/profile.html", {"profile": profile})

#     def post(self, request, id):
#         profile = get_object_or_404(Profile, id=id)
#         user = profile.user

#         # Check if it's an AJAX image upload
#         if request.FILES.get("image"):
#             profile.image = request.FILES["image"]
#             profile.save()
#             return JsonResponse({"success": True})

#         # Handle regular form submission
#         user.first_name = request.POST.get("first_name")
#         user.last_name = request.POST.get("last_name")
#         user.email = request.POST.get("email")
#         user.save()

#         profile.phone = request.POST.get("phone")
#         profile.location = request.POST.get("location")
#         profile.save()

#         messages.success(request, "Profile updated successfully!")
#         return redirect("profile", id=profile.id)


class sign_up(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have singed up successfully.")
            login(request, user)
            return redirect("users:home")
        else:
            return render(request, "users/register.html", {"form": form})


def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("users:home")

        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    elif request.method == "POST":
        form = LoginForm(
            request, data=request.POST
        )  # Pass request as the first argument
        if form.is_valid():
            # No need to use authenticate manually; form is valid if user credentials are correct
            user = form.get_user()  # Retrieve the authenticated user from the form
            login(request, user)
            messages.success(request, f"Hi {user.username.title()}, welcome back!")
            return redirect("users:home")
        else:
            messages.error(request, "Invalid username or password")
        return render(request, "users/login.html", {"form": form})


def sign_out(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("users:home")


def home(request):
    user = request.user
    return render(request, "./events/home.html", {"user": user})
