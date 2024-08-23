from django.contrib import admin
from django.urls import path, include

# This is a list of URL patterns that maps specific URL paths to their respective view or application.
urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path("media/", include("media.urls"), name="media-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),
] 
