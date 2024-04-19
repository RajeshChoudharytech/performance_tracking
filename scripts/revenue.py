from performance_app.models import DailyPerformance
import random


def random_revenue(min_roi):
    queryset = DailyPerformance.filter_by_min_roi(min_roi=min_roi)
    print("Length of queryset:", queryset.count())
    print("Length of queryset multiplied by 2:", queryset.count() * 2)
    
    for idx, performance in enumerate(queryset, start=1):
        print(f"{idx}/{queryset.count()}")
        random_factor = random.uniform(0.5, 2)
        performance.revenue *= random_factor
        performance.save()

