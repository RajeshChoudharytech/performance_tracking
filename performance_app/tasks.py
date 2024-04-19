# performance_app/tasks.py

import time
from daily_performance.celery import shared_task
from .models import DailyPerformance


@shared_task
def slow_iteration():
    queryset = DailyPerformance.objects.all()[:50]
    for performance in queryset:
        time.sleep(60)  # Simulate a delay
        # Example processing: Update the revenue
        performance.revenue = calculate_updated_revenue(performance)
        performance.save()

def calculate_updated_revenue(performance):
    # Calculate updated revenue based on some criteria
    # double the revenue
    return performance.revenue * 2
