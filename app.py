from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Load all songs from songs.json
with open("songs.json", "r", encoding="utf-8") as f:
    songs_data = json.load(f)

# Slugify helper function
def slugify(text: str) -> str:
    return text.lower().replace(" ", "-").replace("/", "-").replace("?", "").replace(",", "").replace("'", "")

# Homepage with category list and optional search
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, q: str = ""):
    if q:
        filtered_categories = []
        for cat in songs_data:
            matched_songs = [s for s in cat["songs"] if q.lower() in s["title"].lower()]
            if matched_songs:
                filtered_categories.append({
                    "category": cat["category"],
                    "songs": matched_songs
                })
        return templates.TemplateResponse("index.html", {
            "request": request,
            "categories": filtered_categories,
            "search_mode": True
        })

    return templates.TemplateResponse("index.html", {
        "request": request,
        "categories": songs_data,
        "search_mode": False
    })

# Song detail page
@app.get("/song/{title_slug}", response_class=HTMLResponse)
async def song_detail(request: Request, title_slug: str):
    for cat in songs_data:
        for song in cat["songs"]:
            if slugify(song["title"]) == title_slug:
                song["image_paths"] = [f"/static/songs/{img}" for img in song.get("images", [])]
                return templates.TemplateResponse("song.html", {"request": request, "song": song})

    return HTMLResponse(content="Song not found", status_code=404)

# Category page
@app.get("/category", response_class=HTMLResponse)
async def category_page(request: Request, category: str):
    selected_slug = slugify(category)
    for cat in songs_data:
        if slugify(cat["category"]) == selected_slug:
            return templates.TemplateResponse("category.html", {
                "request": request,
                "category": cat
            })

    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
