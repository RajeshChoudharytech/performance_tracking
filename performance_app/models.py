from django.db import models


class Performance(models.Model):
    cost = models.FloatField()
    revenue = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)
    profit = models.FloatField()


class HourlyPerformance(Performance):
    datetime = models.DateTimeField()


class DailyPerformance(Performance):
    date = models.DateField()
    
    @classmethod
    def filter_by_min_roi(cls, min_roi: float):
        return cls.objects.filter(profit__gt=min_roi * models.F('cost'))

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        


