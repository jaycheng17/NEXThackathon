import requests
from PIL import Image
from bs4 import BeautifulSoup
import os




# Send HTTP GET request
def getImageUrl(url):
    imageUrls = []

    response = requests.get(pinterest_board_url)

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
    for url in imageUrls:
        response = requests.get(url)
        imagePath = f"./images/{imageName}.jpg"
        imagesPath.append(imagePath)
        imageName += 1
        with open(imagePath, "wb") as f:
            f.write(response.content)
    return imagesPath

def convertToJPEG(imagesPath):
    for imagePath in imagesPath:
        if (imagePath.endswith(".jpg")):
            jpegPath = imagePath.split(".jpg")[0]
            image = Image.open(imagePath)
            image.save(f"{jpegPath}.jpeg", "JPEG")
            os.remove(imagePath)



# Pinterest board URL
pinterest_board_url = "https://www.pinterest.com/jaycheng120/test/"

imageUrls = getImageUrl(pinterest_board_url)

imagesPath = downloadImages(imageUrls)

convertToJPEG(imagesPath)




