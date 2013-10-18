# Create your views here.
from django.shortcuts import render
import datetime,os, time
def home(request):
    context={'ts':datetime.datetime.now()}
    return render (request,'home.html',context)

def listing(request,path):
    content=os.listdir("/var/"+str(path))
    context={"dir_content":content}
#    return render(request,'listing.html',context)
    fileList=[]
    dirList=[]
    for item in context:
        if(os.path.isfile("/var/"+str(path)+"/"+item)):
            fileList.append(item)
        else:
            dirList.append(item)
    return render(request,'listing.html',context)
    
