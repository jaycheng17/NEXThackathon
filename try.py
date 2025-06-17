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

def prompt_for_agent(image_path,text_prompt, count):
    image_base64 = encode_image_to_base64(image_path)
    if count != 1:
        prompt = f"{text_prompt}\n\nImage: data:image/jpeg;base64,{image_base64}"
    else:
        prompt = f"\n\nImage: data:image/jpeg;base64,{image_base64}"
    return prompt

def main():
    # Pinterest board URL
    pinterest_board_url = "https://pin.it/7E6gemt9O"

    imageUrls = getImageUrl(pinterest_board_url)
    imagesPath = downloadImages(imageUrls)

    finalPath = convertToJPEG(imagesPath)

    bedrock_model = BedrockModel(
        model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        temperature=0,
        top_p=0.9,
        top_k=50,
    )
    agent = Agent(model = bedrock_model, 
                  system_prompt=
                  (""" You are a seasoned wedding planner with a sharp eye for décor, layout, guest experience, location, and thematic cohesion.
                        Take note of the features of the images and provide details on how the couple should have for the wedding.
                        Output
                        - Theme / Mood 
                        - Decor
                        - Setting
                        - Color Palette   
                   """))
    
    numberImages = len(imageUrls)
    final_prompt = prompt_for_agent(finalPath[0] + ".jpeg", "What do you see in this image? Can you suggest a wedding theme based on this image?" , 0)
    if (numberImages > 1):
        for i in range(1,numberImages):
            final_prompt += prompt_for_agent(finalPath[i] + ".jpeg", "nothing" , 1)
            print("test")
    # final_prompt = prompt_for_agent("image_converted.jpeg", "What do you see in this image? Can you suggest a wedding theme based on this image?")
    
    response2 = agent(final_prompt)
    print(response2)

    # shutil.rmtree("./images")


if __name__ == "__main__":
    main()

