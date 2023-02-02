import time

from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .utils import get_response


# Create your views here.
def index_handler(request):
    if request.method == 'GET':
        print(settings.MEDIA_URL)
        # time.sleep(50)
        # Code to handle GET request goes here
        return render(request, 'admin.html', {'MEDIA_URL': settings.MEDIA_URL})


@csrf_exempt
def generate_content(request):
    templateData = {
        "topic": "",
        "options": []
    }
    if request.method == 'POST':
        for data in request.POST:
            if data == "topic":
                templateData["topic"] = request.POST["topic"]
            if data.startswith("option-"):
                templateData["options"].append(request.POST[data])

        print(templateData)
        # get_response()
        return render(request, "generated_post.html")
