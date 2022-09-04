import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.utills.flussonic import generate_uri

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/playerjs/{video}", response_class=HTMLResponse)
async def endPoint_playerjs(request: Request, video: str):
    """
    Example using Playerjs

    video: str = video file name, with extension. example bunny.mp4
    """
    url = await generate_uri(video=video, ip=request.client.host, types='link')
    return templates.TemplateResponse("playerjs.html", {"request": request, "url": url, 'video': video})


@app.get("/embed/{video}", response_class=HTMLResponse)
async def endPoint_embed(request: Request, video: str):
    """
     Example using iframe

     video: str = video file name, with extension. example bunny.mp4
    """
    url = await generate_uri(video=video, ip=request.client.host, types='link')
    return templates.TemplateResponse("embed.html", {"request": request, "url": url, 'video': video})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
