from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Remove Stale Reports'
    
    def handle(self, *args, **kwargs):
        from reportengine.models import ReportRequest
        ReportRequest.objects.cleanup_stale_requests()

