from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def handle_file(request):
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    
    return render(request, 'core/simple_upload.html', {
    'uploaded_file_url': uploaded_file_url
        })