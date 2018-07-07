from django.shortcuts import render
from django.http import HttpResponse
from .helpers import *
# Create your views here.
def SearchHome(request):
    return render(request, 'search/home.html')

def find(request):
    print("In find")
    if request.method == 'POST':
        query = request.POST.get("symbol")
        result = getMatchedResult(query)
        print("In post")
        context = {
            "found" : True,
            "tutorials" : result,
        }
        # print(context)
        return render(request, 'search/result.html', context)
    return render(request, 'search/result.html')
