from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
import requests

# Create your views here.


def Ide(request):
    return render(request, 'ide/index.html')



RUN_URL = "https://api.hackerearth.com/v3/code/run/"


def runCode(request):
    if request.is_ajax():
        source = request.POST['source']
        lang = request.POST['lang']
        data = {
            'client_secret': 'bc40b60349b9ddd98cf2fda31c9d1s7112chdsd85hs231',
            'async': 0,
            'source': source,
            'lang': lang,
            'time_limit': 5,
            'memory_limit': 262144,
        }
        if 'input' in request.POST:
            data['input'] = request.POST['input']
        r = requests.post(RUN_URL, data=data)
        return JsonResponse(r.json(), safe=False)
    else:
        return HttpResponseForbidden()
