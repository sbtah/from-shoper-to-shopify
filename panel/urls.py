from django.urls import path
from panel import views


app_name = "panel"


urlpatterns = [
    path("", views.PanelView.as_view(), name="panel"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("images/", views.ImageListView.as_view(), name="image-list"),
    path("products/", views.ProductListView.as_view(), name="product-list"),
    path(
        "products/<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"
    ),
]