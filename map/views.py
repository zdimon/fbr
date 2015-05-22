from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, RequestContext
from map.models import Cotter, Radiation, Vegetation, Veget, Slope, Structure, Effectiveness, Ndvi001250, Burning
from djgeojson.views import GeoJSONLayerView
from djgeojson.serializers import Serializer as GeoJSONSerializer
# Create your views here.
from map.models import Structure

def get_old_info(request):
    obj = Vegetation.objects.get(objectid=request.GET['id'])
    context = {'obj': obj}
    return render_to_response('old_info.html', context, RequestContext(request))

def home(request):
    context = {}
    return render_to_response('index.html', context, RequestContext(request))


def radiation(request):
    context = {}
    return render_to_response('radiation.html', context, RequestContext(request))
    
def ndvi001250(request):
    context = {}
    return render_to_response('ndvi001250.html', context, RequestContext(request))    


def vegetation(request):
    context = {}
    return render_to_response('vegetation.html', context, RequestContext(request))
    

def burning(request):
    context = {}
    return render_to_response('burning.html', context, RequestContext(request))



def veget(request):
    context = {}
    return render_to_response('vegetstructure.html', context, RequestContext(request))    



def cot(request):
    context = {}
    return render_to_response('cotter.html', context, RequestContext(request))

def slope(request):
    context = {}
    return render_to_response('slope.html', context, RequestContext(request))

def slope_json(request):
    context = {'structures': Effectiveness.objects.all()}
    return render_to_response('effectiveness-json.html', context, RequestContext(request))


def radiation_json(request):
    context = {}
    return render_to_response('radiation-json.html', context, RequestContext(request))
    
    
def ndvi001250_json(request):
    context = {}
    return render_to_response('ndvi001250-json.html', context, RequestContext(request))    


def vegetation_json(request):
    context = {'structures': Structure.objects.all()}
    return render_to_response('vegetation-json.html', context, RequestContext(request))


def burning_json(request):
    context = {'structures': Structure.objects.all()}
    return render_to_response('burning-json.html', context, RequestContext(request))


def veget_json(request):    
    context = {'structures': Structure.objects.all()}
    return render_to_response('veget-json.html', context, RequestContext(request))


class GetPolygonJsonCotter(GeoJSONLayerView):
    # Options
    from fbr.settings import BASE_DIR
    precision = 4   # float
    simplify = 0.5  # generalization
    def get_queryset(self):
        return Cotter.objects.all()

    def render_to_response(self, context, **response_kwargs):
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/cotter.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       precision=self.precision,
                       simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response


class GetPolygonJsonRadiation(GeoJSONLayerView):
    # Options
    from fbr.settings import BASE_DIR
    precision = 4   # float
    simplify = 0.5  # generalization
    def get_queryset(self):
        return Radiation.objects.all()

    def render_to_response(self, context, **response_kwargs):
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/radiation.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       precision=self.precision,
                       simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response




class GetPolygonJsonNdvi001250(GeoJSONLayerView):
    # Options
    from fbr.settings import BASE_DIR
    #precision = 4   # float
    #simplify = 0.5  # generalization
    def get_queryset(self):
        return Ndvi001250.objects.all()

    def render_to_response(self, context, **response_kwargs):
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/ndvi001250.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       #precision=self.precision,
                       #simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response






class GetPolygonJsonVegetation(GeoJSONLayerView):
    from fbr.settings import BASE_DIR
    #precision = 4   # float
    #simplify = 0.5  # generalization
    def get_queryset(self):
        return Vegetation.objects.all()
    def render_to_response(self, context, **response_kwargs):
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/vegetation.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(#properties=self.properties,
                       #precision=self.precision,
                       simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response



class GetPolygonJsonBurning(GeoJSONLayerView):
    from fbr.settings import BASE_DIR
    #precision = 4   # float
    #simplify = 0.5  # generalization
    def get_queryset(self):
        return Burning.objects.all()
    def render_to_response(self, context, **response_kwargs):
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/burning.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(#properties=self.properties,
                       #precision=self.precision,
                       simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response




class GetPolygonJsonVeget(GeoJSONLayerView):
    from fbr.settings import BASE_DIR
    #precision = 4   # float
    #simplify = 0.5  # generalization
    def get_queryset(self):
        return Veget.objects.all()
    def render_to_response(self, context, **response_kwargs):
        #import pdb; pdb.set_trace()
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/veget.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       #precision=self.precision,
                       #simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=True)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response



class GetPolygonJsonVegetType(GeoJSONLayerView):
    from fbr.settings import BASE_DIR
    #precision = 4   # float
    #simplify = 0.5  # generalization
    def get_queryset(self):
        #self.args[0]
        tp = Structure.objects.get(id=self.request.GET['type'])
        return Veget.objects.filter(struct=tp)
    def render_to_response(self, context, **response_kwargs):
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/veget%s.txt' % tp.id
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(#properties=self.properties,
                       #precision=self.precision,
                       simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response




class GetPolygonJsonSlope(GeoJSONLayerView):
    # Options
    from fbr.settings import BASE_DIR
    #precision = 4   # float
    #simplify = 0.5  # generalization
    def get_queryset(self):
        return Slope.objects.all()

    def render_to_response(self, context, **response_kwargs):
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/slope.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       #precision=self.precision,
                       #simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response


class GetBurningJson(GeoJSONLayerView):
    # Options

    def get_queryset(self):
        if(self.request.GET['time']=='0'):
            return Burning.objects.all()
        else:
            return Burning.objects.all().filter(time=int(self.request.GET['time']))

    def render_to_response(self, context, **response_kwargs):
        from config.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/burning_'+self.request.GET['id']+'.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        #f = open(cpath,'w')
        #f.write(response.content)
        #f.close()
        return response




