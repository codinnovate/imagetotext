from django.shortcuts import render
import base64
import pytesseract
from django.contrib import messages
from PIL import Image
import numpy as np



def homepage(request):
    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            messages.add_message(
                request, messages.ERROR, "No image selected or uploaded"
            )
            return render(request, "home.html")
        img = np.array(Image.open(image))
        text = pytesseract.image_to_string(img,)
        return render(request, "home.html", {"extractor": text, "image": image_base64})

    return render(request, "home.html")
