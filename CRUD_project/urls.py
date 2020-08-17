from django.contrib import admin
from django.urls import path, include
import accounts_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_app.views.login, name="login"),
    path('logout/', accounts_app.views.logout, name="logout"),

    path('blog/', include('blog_app.urls')),
]
