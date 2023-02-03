import time
import openai
from bs4 import BeautifulSoup


def get_response(prompt):
    print("entered in openai")
    openai.api_key = ""
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    except Exception as e:
        print(e)
        return {
            "text": "",
            "success": False,
            "message": e,
            "created": time.gmtime(),
            "id": ""
        }

    if len(response["choices"]) > 0:
        return {
            "text": response["choices"][0].text,
            "success": True,
            "message": "request successfully completed",
            "created": response.created,
            "id": response.id
        }


def prepare_prompt(topic: str, options):
    res = ""
    for option in options:
        res += option + "\n"

    return f"""write travel content about {topic}
Give a perfect awesome image caption with html image tag must in top Write a proper title for the article
Include an introduction of at least 300 words 
{res}give me in a html with style.css link"""


def extract_caption(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    return [img['alt'] for img in img_tags]


def replace_image(html, image_list):
    print(image_list)
    soup = BeautifulSoup(html, 'html.parser')
    img_tags = soup.find_all("img")
    for i, img_tag in enumerate(img_tags):
        img_tag["src"] = image_list[i]
        return soup.prettify()
