from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('posts.urls')),
    path('main/', include('main.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/',
         CreateView.as_view(
             template_name='registration/registration_form.html',
             form_class=UserCreationForm,
             success_url=reverse_lazy('posts:index'),),
         name='registration'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
