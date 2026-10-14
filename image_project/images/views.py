import os
from django.shortcuts import render
from django.conf import settings
from PIL import Image

def uploadimage(request):
    message = ""

    if request.method == 'POST':
        file = request.FILES.get('image')
        if file:
            try:
                img = Image.open(file)
                img = img.convert('RGB')
                img.thumbnail((300,300))

                os.makedirs(settings.MEDIA_ROOT, exist_ok = True)
                img.save(os.path.join(settings.MEDIA_ROOT,'resize.jpg'))

                message = "sucess"

            except(OSError, ValueError):
                message = "invalid"
    return render(request, 'upload.html', {'message' : message})