from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
   path ('', views.home, name= 'home'),
   path('gallery', views.gallery, name= 'gallery'),
   path('pricing', views.pricing, name= 'pricing'),
   path('gallery_detail/<int:id>', views.gallery_detail, name= 'gallery_detail'),
   path('register',views.register, name='register'),
   path('login',views.login, name='login'),
   path('services',views.services, name='services'),
   path('sessions',views.sessions, name='sessions'),
 
]
if settings.DEBUG:
   urlpatterns +=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)