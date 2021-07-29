from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    url('profile/', views.profile, name='profile'),
    path('update/<id>', views.update_profile, name='update_profile'),
    path('appointment/', views.book_appointment, name='app'),
    path('about/', views.about, name='about'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
