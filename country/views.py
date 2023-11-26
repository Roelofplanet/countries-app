from django.shortcuts import render

def home(request):
    import requests
    import json
    api_request = requests.get('https://restcountries.com/v3.1/all')
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api})
