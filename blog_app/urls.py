from django.urls import path
import blog_app.views

urlpatterns = [
    path('', blog_app.views.blog_home, name="blog_home"),
    path('about', blog_app.views.blog_about, name="blog_about"),
    path('<int:blog_id>/', blog_app.views.blog_detail, name="blog_detail"),
]