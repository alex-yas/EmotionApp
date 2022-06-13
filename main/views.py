from django.shortcuts import render, redirect
from .forms import InputForm
from .controler import predict
from PIL import Image


def index(request):
    emotion = ""
    transform_image = Image.new("P", (48, 48))
    if request.method == "POST":
        form = InputForm(request.POST, request.FILES)
        data = request.POST
        predicted, transform_image = predict(data)
        emotion = "Person on this image is " + predicted
    form = InputForm()
    context = {
        "data": request.POST,
        "dir": "d:/Work/Softarex/Test/AntWeb/images/media/",
        "face_picture": request.POST.get("image"),
        "form": form,
        "emotion": emotion
    }
    return render(request, 'main/index.html', context)
