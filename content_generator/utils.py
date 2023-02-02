import time

import openai

demo_prompt = "write a travel content about hawaii island with at least two detailed image captions wrap by bracket " \
              "and please include points such as including list of popular food, popular places to go, " \
              "Available activities to do,history etc."


def get_response(prompt):
    openai.api_key = "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"

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
            "success": True,
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


def prepare_prompt(topic,data):
    return "write a travel content about "+topic+" with at least two detailed image captions wrap by bracket " \
              "and please include points such as including list of popular food, popular places to go, " \
              "Available activities to do,history etc."


print(prepare_prompt("hawaii",""))
