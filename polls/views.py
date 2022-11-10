from django.shortcuts import render, HttpResponse
from clickup_priorities import priorities
from .models import Priorities
from datetime import datetime
import json


def index(request):

    # try:
        p = datetime.today().strftime('%Y-%m-%d')
        priority_today = Priorities.objects.get(date=datetime.today().strftime('%Y-%m-%d'))
        priority = Priorities.objects.all(date=datetime.today().strftime('%Y-%m-%d'))

        return render(request, 'base.html',{'priorities_today': priority_today, 'priorities': priority})
        
    # except:
    #     view_urls = ['dvd8-11485', 'dvd8-11525','dvd8-11545' ,'dvd8-11565']
    #     i = priorities(view_urls, {"Authorization": 'pk_49588273_8NHVFF6AVGYL1SW3OH9K6WWDFUGMK4H7' })
    #     x = Priorities(date=datetime.today().strftime('%Y-%m-%d'), urgent_count=i.get('urgent_count'), urgent_time=i.get('urgent_time'), high_count=i.get('high_count'), high_time=i.get('high_time'), normal_count=i.get('normal_count'), normal_time=i.get('normal_time'), low_count=i.get('low_count'), low_time=i.get('low_time'))

    #     x.save()
    #     priority = Priorities.objects.get(date=datetime.today().strftime('%Y-%m-%d'))
    #     return render(request, 'base.html',{'priorities': priority})
