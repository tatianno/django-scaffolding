from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from utils.auth import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
]


schema_view_redoc = get_schema_view(

    openapi.Info(
        x_logo={
            "url": "/static/images/logo.png",
            "backgroundColor": "#FFFFFF",
            "altText": "Logo"
        },
        title="APP - API",
        default_version='V 0.0.1',
        contact=openapi.Contact(
            name="APP",
            email="contato@< DOMINIO APP >",
            url="https://< DOMINIO APP >/"
        ),
        terms_of_service="https://< DOMINIO APP >/",
        description='''
            Nessa documentação você verá como 
            realizar consultas através dos endpoints disponíveis. 
        ''',
    ),
    patterns=urlpatterns,
    public=False,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('documentacao/swagger/', schema_view_redoc.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('documentacao/', schema_view_redoc.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('django_prometheus.urls')),
]
