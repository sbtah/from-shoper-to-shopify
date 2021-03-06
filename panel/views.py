from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from users import forms
from translations.models import ProductTranslation, ImageTranslation
from images.models import Image
from products.models import Product
from categories.models import Category


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
        """Get data about Images, Products, ProductTranslations and ImageTranslations to context."""

        context = super().get_context_data(**kwargs)
        context["images_updated"] = Image.objects.all().order_by("-updated")[:11]
        context["products_updated"] = Product.objects.all().order_by("-updated")[:11]
        context["categories_updated"] = Category.objects.all().order_by("-updated")[:11]

        context["images_number"] = Image.objects.all().count()
        context["products_number"] = Product.objects.all().count()
        context["categories_number"] = Category.objects.all().count()

        return context


class ImageListView(LoginRequiredMixin, generic.ListView):

    model = Image
    context_object_name = "images"
    paginate_by = 10
    template_name = "panel/image_list.html"
