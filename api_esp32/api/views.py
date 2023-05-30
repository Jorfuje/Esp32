import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Esp

# Create your views here.

class Esp32View(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(sel,request):
        esps=list(Esp.objects.values())
        if len(esps)>0:
            datos = {'message': "Success", 'esps': esps}
        else:
            datos = {'message': "Esp not found ..."}
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Esp.objects.create(temperatura=jd['temperatura'], humedad=jd['humedad'], 
                           voltajeradiacion=jd['voltajeradiacion'], valorradiacion=jd['valorradiacion'],
                           agua=jd['agua'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
