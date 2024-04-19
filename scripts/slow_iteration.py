import time
from daily_performance.celery import shared_task
from performance_app.models import DailyPerformance


@shared_task
def slow_iteration():
    queryset = DailyPerformance.objects.all()[:50]
    for performance in queryset:
        time.sleep(60)
