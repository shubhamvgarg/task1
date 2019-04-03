from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.edit import FormView, CreateView
from django.template import RequestContext
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import ImageFiles
from .models import Image_Attachment
from django.conf import settings


def Upload(request):
    #if request is get request
    if request.method=='GET':
        return render(request,"dynamic.html",{})
    #if request is post request
    if request.method=='POST':
        obj=ImageFiles.objects.create()

        val=(request.FILES.getlist("uploadfiles[]"))
        print(len(val))
        obj.Title=request.POST["Title"]
        obj.Description=request.POST["Description"]
        obj.save();
        #Create ImageFiles object and use it id as foreign key in Image_Attachment
        print(obj.id)
        #save all images one by one
        for i in val:
            name=i.name
            path = default_storage.save(name, ContentFile(i.read()))
            j=Image_Attachment.objects.create(key=obj,file=path)
        v=list(map(lambda x: "../media/"+x.file,Image_Attachment.objects.filter(key_id=obj.id)))
        #return data for visualization
        return render(request,'images.html',{'Title':obj.Title,'Description':obj.Description,"path":v})

