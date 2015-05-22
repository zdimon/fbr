from django.http import HttpResponse
from map.models import Burning, Radiation


def fire_init(request,gid):
    Burning.objects.all().delete()
    r = Radiation.objects.get(pk=gid)
    b = Burning()
    b.burning = 1
    b.day = 1
    b.time = 1
    b.geom = r.geom
    b.gridcode = r.gridcode
    b.save()
    for r in Radiation.objects.all():
        b = Burning()
        b.burning = 0
        b.day = 1
        b.time = 0
        b.geom = r.geom
        b.gridcode = r.gridcode
        b.save()
    html = 'Done!!!'
    return HttpResponse(html)

def fire_count(request,time):
    from decimal import Decimal
    try:
        Burning.objects.get(time=time)
    except:
        s = Burning.objects.get(burning=1)
        dist = Decimal(0.001)*Decimal(time)
        Burning.objects.filter(geom__dwithin=(s.geom , dist)).update(burning=1)
        #for r in Burning.objects.filter(geom__dwithin=(s.geom , dist)):
        #    r.burning = 1
        #    r.save()            
    
    html = time
    return HttpResponse(html)


