import time

from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .crawler import Crawler
from .utils import prepare_prompt, get_response, extract_caption, replace_image

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


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

        res = prepare_prompt(templateData["topic"], templateData["options"])
        generated = get_response(res)
        text = ""
        if generated["success"]:
            text = generated["text"]
        else:
            return render(request, 'error.html', {"msg": "Internal Server Error"})

        captions = extract_caption(text)
        print(captions)
        crawl = Crawler()
        if not crawl.run(captions):
            return render(request, 'error.html', {"msg": "Internal Server Error"})
        generate_content = replace_image(text, crawl.images)
        print(generate_content)

        return render(request, "generated_post.html", {"content": generate_content})


@csrf_exempt
def save(request):
    if request.method == "POST":
        return render(request, 'admin.html')
