import chronological
from gtts import gTTS
import os
import openai

async def logic():
    # you call the Chronology functions, awaiting the ones that are marked await
    prompt = chronological.read_prompt('example_prompt')
    completion = await chronological.cleaned_completion(prompt, max_tokens=280, engine="davinci", temperature=0.4, top_p=1, frequency_penalty=0.2, stop=["\n\n"])
    print('Completion Response: {0}'.format(completion))
    
    myText = completion
    language = "fr"
    output = gTTS(text=myText, lang=language,slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")
    response = openai.Image.create(
    prompt=completion,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(image_url)
    with open('logs.txt', 'a') as f:
        f.write(prompt.splitlines()[3]+"\n")
        f.write(completion+"\n")
        f.write(image_url+"\n")

# invoke the Chronology main fn to run the async logic
chronological.main(logic)
