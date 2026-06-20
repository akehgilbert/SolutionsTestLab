from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Django language switcher
    path("i18n/", include("django.conf.urls.i18n")),

    # Redirect root URL to German
    path("", RedirectView.as_view(url="/de/", permanent=False)),
]

urlpatterns += i18n_patterns(
    # Main app URLs
    path("", include("main.urls")),

    # Keep language prefixes:
    # /de/
    # /en/
    # /fr/
    # /nl/
    prefix_default_language=True,
)

# MEDIA FILES
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )