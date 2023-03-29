from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('outscapebooking.urls'), name='booking_urls'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Change Admin panel header text
# https://www.section.io/engineering-education/customizing-django-admin/
admin.site.site_header = "OUTscape game ADMIN"
admin.site.site_title = "OUTscape game ADMIN"
admin.site.index_title = "OUTscape game admin"
