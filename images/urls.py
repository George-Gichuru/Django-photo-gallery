from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name = 'home'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('gallery/<int:image_id>', views.single_image_details, name = 'image_details'),
    path('about/', views.about_us, name = 'about'),
    path('search/', views.search_category, name= 'search_category'),
    path('category/sports/', views.sports, name = 'sports'),
    path('category/technology/', views.technology, name = 'technology'),
    path('category/nature/', views.nature, name = 'nature'),
    path('category/entertainment/', views.entertainment, name = 'entertainment'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)