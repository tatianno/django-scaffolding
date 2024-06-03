from django_prometheus.middleware import PrometheusBeforeMiddleware, PrometheusAfterMiddleware
from django.utils.deprecation import MiddlewareMixin


class CustomPrometheusBeforeMiddleware(PrometheusBeforeMiddleware):
    def process_request(self, request):
        if request.path in ['/metrics']:
            request.prometheus_no_monitoring = True
        return super().process_request(request)


class CustomPrometheusAfterMiddleware(PrometheusAfterMiddleware):
    def process_response(self, request, response):
        if getattr(request, 'prometheus_no_monitoring', False):
            return response
        return super().process_response(request, response)