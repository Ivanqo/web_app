from django.shortcuts import render
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import (
   ListView,
   DetailView,
)
 
from .models import Timetable

class TimetableListView(LoginRequiredMixin, ListView):
    model = Timetable
    queryset = Timetable.objects.all().order_by("time_range")
    
    redirect_field_name = '../timetable'
    def get_context_data(self,*args, **kwargs):
        
            model = Timetable
            queryset = Timetable.objects.all().order_by("time_range")

            context = super(TimetableListView, self).get_context_data(*args,**kwargs)
            context['Timetable_list'] = queryset
            today = date.today()

            def day_of_week(day):
                if day == 'Monday':
                    return 'понедельник'
                elif day == 'Tuesday':
                    return 'вторник'
                elif day == 'Wednesday':
                    return 'среда'
                elif day == 'Thursday':
                    return 'четверг'
                elif day == 'Friday':
                    return 'пятница'
                elif day == 'Saturday':
                    return 'суббота'
                elif day == 'Sunday':
                    return 'воскресенье'

                
            day_type = day_of_week(today.strftime('%A'))
            today = str(today).split('-')
            today = ' '.join(today[::-1])

            '''
            def time_dupl(rng):
                        #range = "10:00 11:20" => 
                        rng = rng.split()
                        rng = list(map(lambda x: x.split(':'),rng))
                        return rng
            cntx = {}
            for i in queryset:
                rng = time_dupl(i.time_range)
                if cntx == {}:
                    cntx = {'st1':rng[0][0],
                                'en1': rng[0][1],
                                'st2':rng[1][0],
                                'en2':rng[1][1]}
                else:
                    cntx =
            context['timing'] = cntx    
            '''
            context['today'] = today
            context['day_type'] = day_type
            return context
    



    


class TimetableDetailView(DetailView):
    model = Timetable