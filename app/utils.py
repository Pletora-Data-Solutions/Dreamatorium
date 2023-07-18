
import requests
import openai
import os

openai.organization = "org-Urk1Ei6EFtzc2wwglwsAwRn9"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate image using DALL-E API
def generate_image(prompt: str) -> str:
    # Make a POST request to the DALL-E API
    # response = openai.Image.create(
    #     prompt=prompt,
    #     model="image-alpha-001",
    #     size="256x256",
    #     response_format="url",
    #     n = 4
    # )

    # return [item['url'] for item in response['data']]
    figures = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdAtF2GzAoXFBEJ2plFhoFZ4GXZ-SZ3J9yWRZ-hos_1QwA-IHqFlL3A8mw-8EaQFCWdyQ&usqp=CAU',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROv6K5reSBnLdnGY7BBfkEMvD3y54MSoiMT1SFNkWr5KcZVv_Rb3Ht9Q0VHf3rVvdY8Z8&usqp=CAU',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTL5wKOjDaGeeaOAbxR8g2-VsljK2FT1h6AKTG7U4rHcp0rt-tmrYIWP46w9REiqP4JOtk&usqp=CAU',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAoMnIpP-8Ol0NruZ7nuPpCOh-4ULSBwVVErnxkw_tjdl9iYbv2K0WgT69SaAdZKVZlQc&usqp=CAU']
    return figures

# Download image function
def download_image(url: str) -> bool:
    response = requests.get(url)
    if response.status_code == 200:
        with open("dall_e_image.jpg", "wb") as f:
            f.write(response.content)
        return True
    else:
        return False