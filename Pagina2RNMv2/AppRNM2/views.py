from django.shortcuts import render

# Create your views here.




def inicio(request):

    return render (request, 'AppRNM2/index.html')



def Job(request):

    return render (request, 'AppRNM2/job.html')
