from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from users import forms
from images.models import Image
from products.models import Product


class LoginUserView(SuccessMessageMixin, LoginView):
    """View for loging in users."""

    authentication_form = forms.CustomUserAuthenticationForm
    template_name = "panel/login_user.html"
    success_message = "Your are logged in"


class LogoutUserView(LoginRequiredMixin, SuccessMessageMixin, LogoutView):
    """View for loging out users. User have to be authenticated first."""

    template_name = "panel/logout_user.html"
    success_message = "Your are logged out"


class PanelView(LoginRequiredMixin, generic.TemplateView):
    """Panel main view."""

    template_name = "panel/panel_home.html"

    def get_context_data(self, **kwargs):
        """Get data about Images and Products to context."""

        context = super().get_context_data(**kwargs)
        context["images"] = Image.objects.all()
        context["products"] = Product.objects.all()
        return context
