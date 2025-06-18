import base64
import os
import shutil
from bs4 import BeautifulSoup
from strands import Agent
from strands.models import BedrockModel
import json
import urllib.request
import urllib.error
import boto3

# Send HTTP GET request
def getImageUrl(url):
    imageUrls = []
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req) as response:
            html = response.read()
            soup = BeautifulSoup(html, "html.parser")
            imgs = soup.find_all("img")
            for img in imgs:
                src = img.get("src")
                if src and "pinimg.com" in src and "236x" in src:
                    imageUrls.append(src)
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")
    
    return imageUrls

def downloadImages(imageUrls):
    imagesPath = []
    imageName = 1
    
    newpath = "/tmp/images"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        
    for url in imageUrls:
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req) as response:
                imagePath = f"{newpath}/{imageName}.jpg"
                with open(imagePath, "wb") as f:
                    f.write(response.read())
                imagesPath.append(imagePath)
                imageName += 1
        except urllib.error.URLError as e:
            print(f"Error downloading image: {e}")
    return imagesPath

def convertToJPEG(imagesPath):
    finalPath = []
    for imagePath in imagesPath:
        if imagePath.endswith(".jpg"):
            jpegPath = imagePath.rsplit(".jpg", 1)[0]
            os.rename(imagePath, jpegPath + ".jpeg")
            finalPath.append(jpegPath)
    return finalPath

# Prompting the AI
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

def lambda_handler(event, context):
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "POST,OPTIONS"
            },
            'body': json.dumps("CORS preflight OK")
        }

    # Pinterest board URL
    pinterest_board_url = event.get("url", "https://pin.it/5Nu8evShN")

    imageUrls = getImageUrl(pinterest_board_url)
    imagesPath = downloadImages(imageUrls[:5])
    finalPath = convertToJPEG(imagesPath)

    # Create a custom boto3 session
    session = boto3.Session(
        aws_access_key_id='ASIA3WWPJAH7YCXEZJ4E',
        aws_secret_access_key='M9hz6f5VRwwUlKfiVmaWwdkI1QMqw9SuX80MtrYY',
        aws_session_token='IQoJb3JpZ2luX2VjEKH//////////wEaCXVzLWVhc3QtMSJGMEQCIGbYd9u3/VxB2YP3EpEwCKpEge2zdSU7R02uu8B0nomTAiAKUiIqFKGziwUDkgJrcX4P0UEdRsOqf2IeUQ2FTNsebCqiAgiK//////////8BEAEaDDgwNDY2NzMyNjk3NSIMOYQY2B6pl7bX1rXyKvYBNQxmEYYXZ8LoQ6D4CS5qjbiQ6aM5BVKZhW3EQ6JIlu5+enVRFkemSPX2tyiUkrup8GhOoIkR5hrXRIb5o93V/igt1MvJeH9nbw54+slGAZgKoyo3IQTmNHFe+Vrw+CAKjdnmd4NZYQIMqUNZca8FuRSvKSKxPsvTi73GJCW04FXM+/DF8rVAp/c6kRhcAYp7osoV4Ld1L+JMpr8BbdQ637uHL7AnZ7QkRHmkTTawe4GwbmnYW/GagQKIkiCtMpC5OC2PENVPwWPkrjb3+6kPv80DUSW6y8J/RcsNfcPjqTtfACHqteqJLjEaPk2YcvdDoE/t564tMJWBysIGOp4Bm9/CeTpNULbUqg5TZOx2mmWfPm1WwWM6rc2WllrxL+B5t3u41nEwyyk0+6xBmPk3UFZK1sj5xwnTau6e+Y26e7h8SblMwvwLjSZOeY5MXAuSX+icK4bXNgeCzNmMlO8uMGvt/vsgS2tEGbwii/dVSWtG5weLcZcf7rqMOmPvF5cOxM6UTZb2NU7UEy5OWqMbBd/SWb4q6HeeXT+WTVo=',  # If using temporary credentials
        region_name='us-west-2',
    )

    bedrock_model = BedrockModel(
        model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        temperature=0,
        top_p=0.9,
        top_k=50,
        boto_session=session
    )
    agent = Agent(model=bedrock_model)
    
    finalPrompts = prompt_for_agent(
        finalPath,
        "What do you see in this image? Can you suggest a wedding theme based on this image?",
        len(finalPath)
    )
    result = agent(finalPrompts[0])


    shutil.rmtree("/tmp/images")

    
    # to change to another lambda call
    return {
        "statusCode": 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "POST,OPTIONS"
        },
        "body": json.dumps(str(result))
    }