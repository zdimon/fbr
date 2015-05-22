from django.http import HttpResponse
from map.models import Burning, Radiation
from django.db.models import Max, Min

def fire_init(request,gid):
    # DEL ALL 
    Burning.objects.all().delete()
    # get the origin of the fires
    r = Radiation.objects.get(pk=gid)
    # CREATE DUBLE
    b = Burning()
    b.burning = 1
    b.day = 1
    b.time = 0
    b.geom = r.geom
    b.gridcode = r.gridcode
    b.save()
    # copy all grid
    for r in Radiation.objects.all():
        b = Burning()
        b.burning = 0
        b.day = 1
        b.time = 0
        b.geom = r.geom
        b.gridcode = r.gridcode
        b.save()
    html = 'Done!!! So now you can choice a distance of time (in hours) what you are interested in'
    return HttpResponse(html)

def fire_count(request,time):
    '''
        time - int value in hour
    '''
    from decimal import Decimal # to  convert fucking numbers
    #to know max val of time in db
    max_time = Burning.objects.all().aggregate(Max('time'))['time__max']
    dist = Decimal(0.001)*Decimal(time) # 0.001 ~ 115 miters
    if max_time == 0: # start of the burning (when only one object is burning)
        s = Burning.objects.get(burning=1)
        Burning.objects.filter(geom__dwithin=(s.geom , dist)).update(burning=1,time=time)
        return HttpResponse(max_time) # return current time
    else: # continue
        new_time = int(time) + int(max_time) # make the new time layer mark
        for i in Burning.objects.filter(time=max_time):
            Burning.objects.filter(geom__dwithin=(i.geom , dist), burning=0).update(time=new_time, burning=1)
        return HttpResponse(new_time) # return current time



def fire_simulation(request):
    return HttpResponse('FFFF')   




