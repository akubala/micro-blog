from django.urls import path
from .views import home_view


urlpatterns = [
    path('blog/', home_view, name='home'),
]