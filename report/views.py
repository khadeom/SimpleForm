from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
# Create your views here.
from .models import incidentData
def incident(request):

    if request.method =='POST':

        print("post triggered")
        x= incidentData()

        x.location = request.POST.get("loc")
        x.incident_department = request.POST.get("inci_dept")
        # x.date_time = request.POST.get("datetime")
        x.incident_location  = request.POST.get("inci_loc")
        x.immidiate_action_taken = request.POST.get("immid_Act")

        x.save()

        print(request.POST)


        # return JsonResponse(x, safe=False)


        return HttpResponse('data saved',x.location)
    return render(request, 'index.html')