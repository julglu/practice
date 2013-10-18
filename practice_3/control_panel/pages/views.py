# Create your views here.
from django.shortcuts import render
import datetime,os, time
def home(request):
    context={'ts':datetime.datetime.now()}
    return render (request,'home.html',context)

def listing(request,path):
    content=os.listdir("/var/"+str(path))
    context={"dir_content":content}
    return render(request,'listing.html',context)
    
