
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from posts.views import post_detail



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^social/', include('allauth.urls')),
    url(r'^post/', include('posts.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

