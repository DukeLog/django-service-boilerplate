from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^app/', include("app.urls", namespace="app")),
    # use section urls if need!
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()