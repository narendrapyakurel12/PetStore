from django.urls import path
from .views import *
app_name = 'newsapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-Us/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact-Us/', ContactView.as_view(), name='contact'),
    path('blog/', NewsView.as_view(), name='news')

]
