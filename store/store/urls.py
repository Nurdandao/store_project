from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import index, products
from users.views import login, register, profile, email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),
    path('products/', products, name='products'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('email/', email, name='email'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
