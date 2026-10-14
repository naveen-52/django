import os
from django.shortcuts import render
from django.conf import settings
from PIL import Image

# Create your views here.
def upload_image(request):
    message = ""
    file = request.FILES.get('image')

    if file:
        try:
            img = Image.open(file)
            img = img.convert('RGB')
            img.thumbnail((300, 300))

            os.makedirs(settings.MEDIA_ROOT, exist_ok = True)
            img.save(os.path.join(settings.MEDIA_ROOT, 'resized.jpg'))

            message = "Sucess to Upload"

        except(OSError,ValueError):
            message = " Invalid Photo"

    return render(request, 'upload.html', {'message':message})