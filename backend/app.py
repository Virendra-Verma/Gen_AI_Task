from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup
from moviepy.editor import ImageClip
from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI

# -------------------- APP INIT --------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")


# -------------------- ROOT --------------------
@app.get("/")
def home():
    return {"message": "🚀 Gen AI Backend Running Successfully"}


# =================================================
# 🔥 1. VIDEO GENERATOR (FIXED)
# =================================================

def get_trending_news():
    try:
        url = "https://news.google.com/topstories"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=5)

        soup = BeautifulSoup(res.text, "html.parser")
        headlines = [item.text for item in soup.select("a.DY5T1d")[:5]]

        return headlines if headlines else ["Breaking News Update"]

    except:
        return ["Breaking News Update"]


def generate_script(topic):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Write a 60-sec video script on: {topic}"}]
        )
        return response.choices[0].message.content
    except:
        return "Breaking news happening now. Stay tuned for updates."


def create_video(script):
    try:
        # Create image
        img = Image.new('RGB', (720, 1280), color=(0, 0, 0))
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 32)
        except:
            font = ImageFont.load_default()

        # Text wrapping
        words = script.split()
        lines = []
        line = ""

        for word in words:
            if len(line + word) < 40:
                line += word + " "
            else:
                lines.append(line)
                line = word + " "
        lines.append(line)

        y = 100
        for l in lines[:20]:
            draw.text((40, y), l, fill=(255, 255, 255), font=font)
            y += 50

        img_path = "frame.png"
        img.save(img_path)

        # Convert to video
        clip = ImageClip(img_path).set_duration(10)
        clip.write_videofile("output.mp4", fps=24)

        return "output.mp4"

    except Exception as e:
        print("Video Error:", e)
        return "Video failed"


@app.get("/generate-video")
def generate_video():
    news = get_trending_news()
    topic = news[0]

    script = generate_script(topic)
    video = create_video(script)

    return {"topic": topic, "script": script, "video": video}


# =================================================
# 🛒 2. BLOG GENERATOR
# =================================================

def get_products():
    try:
        url = "https://www.amazon.in/s?k=trending+products"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=5)

        soup = BeautifulSoup(res.text, "html.parser")
        products = [item.text.strip() for item in soup.select(".a-size-medium")[:5]]

        return products if products else ["Smartphone"]

    except:
        return ["Laptop", "Smart Watch"]


def generate_blog(product):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Write a 150-word SEO blog on {product}"
            }]
        )
        return response.choices[0].message.content
    except:
        return "This is a trending product you should check out."


@app.get("/generate-blog")
def blog_api():
    product = get_products()[0]
    blog = generate_blog(product)

    return {"product": product, "blog": blog}


# =================================================
# 🧠 3. ARCHITECTURE GENERATOR
# =================================================

@app.get("/generate-architecture")
def architecture():
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": "Design system for e-commerce app with login, cart, payment"
            }]
        )
        return {"architecture": response.choices[0].message.content}

    except:
        return {"architecture": "Failed to generate"}