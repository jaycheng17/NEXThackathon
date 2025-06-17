import requests
import base64
import os
import shutil
from PIL import Image
from bs4 import BeautifulSoup
from PIL import Image
from strands import Agent
from strands.models import BedrockModel
import asyncio


# Send HTTP GET request
def getImageUrl(url):
    imageUrls = []

    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        imgs = soup.find_all("img")

        for img in imgs:
            src = img.get("src")
            if src and "pinimg.com" and "236x" in src:
                imageUrls.append(src)

    return imageUrls

def downloadImages(imageUrls):
    imagesPath = []
    imageName = 1
    
    newpath = './images' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for url in imageUrls:
        response = requests.get(url)
        imagePath = f"./images/{imageName}.jpg"
        imagesPath.append(imagePath)
        imageName += 1
        with open(imagePath, "wb") as f:
            f.write(response.content)
    return imagesPath

def convertToJPEG(imagesPath):
    finalPath = []
    for imagePath in imagesPath:
        if (imagePath.endswith(".jpg")):
            jpegPath = imagePath.split(".jpg")[0]
            image = Image.open(imagePath)
            image.save(f"{jpegPath}.jpeg", "JPEG")
            finalPath.append(jpegPath)
            os.remove(imagePath)
    return finalPath


#Prompting the AI
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded

def prompt_for_agent(image_path, text_prompt, count):
    prompts = []
    for index in range(0, count, 5):
        prompt = text_prompt
        for i in range(index, index+5):
            img = image_path[i] + ".jpeg"
            image_base64 = encode_image_to_base64(img)
            prompt = prompt + f"\n\nImage: data:image/jpeg;base64,{image_base64}"
        prompts.append(prompt)
    return prompts

async def promptOne(prompt, agent):
    response = agent(prompt)
    return response

async def promptTwo(prompt, agent):
    response = agent(prompt)
    return response

async def agentPrompt(finalPrompts, agent):
    results = await asyncio.gather(
        promptOne(finalPrompts[0], agent),
        promptTwo(finalPrompts[1], agent)
    )

def main():
    # Pinterest board URL
    pinterest_board_url = "https://pin.it/5Nu8evShN"

    imageUrls = getImageUrl(pinterest_board_url)
    imagesPath = downloadImages(imageUrls)

    finalPath = convertToJPEG(imagesPath)

    bedrock_model = BedrockModel(
        model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        temperature=0,
        top_p=0.9,
        top_k=50,
    )
    agent = Agent(model = bedrock_model               )
    
    finalPrompts = prompt_for_agent(finalPath, "What do you see in this image? Can you suggest a wedding theme based on this image?" , len(finalPath))
    
    asyncio.run(agentPrompt(finalPrompts, agent))
    


    # shutil.rmtree("./images")


if __name__ == "__main__":
    main()

