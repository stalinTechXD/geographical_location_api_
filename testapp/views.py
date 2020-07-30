from django.shortcuts import render
import requests
import json

# Create your views here.
def get_geographic_info(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get('REMOTE_ADDR')
    url = 'http://api.ipstack.com/157.49.189.102?access_key=bbfff8ae668033d1e0c4f285fe587395'
    response = requests.get(url)
    data = response.json()
    return render(request,'testapp/info.html',data)


 


    #/home/stalin/Documents/myProjects/consuming_third_party_api/consuming_third_party_api

















   # def get_client_ip(request):
    #x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #if x_forwarded_for:
     #   ip = x_forwarded_for.split(',')[0]
    #else:
     #   ip = request.META.get('REMOTE_ADDR')
    #return ip