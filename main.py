from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pathlib import Path
import json
from fastapi.templating import Jinja2Templates

templates= Jinja2Templates(directory='Templates')

app = FastAPI()


@app.get("/")
def read_route(request:Request):
    user_name ="john"
    return templates.TemplateResponse("index.html", {"request":request, "user_name":user_name})

@app.get("/articles", response_class = HTMLResponse)
async def read_articles(request: Request):
    article_files= Path("Articles").glob("*json")
    articles= [json.loads(article_file.read_text())  for article_file in article_files]
    return templates.TemplateResponse("home.html", {"request":request, "articles": articles})


@app.get('/articles/{article_id}')
async def read_article(request: Request,article_id: int):
    article_path = Path(f"Articles/{article_id}.json")
    if(article_path.exists()):
        article =json.loads(article_path.read_text())
        return templates.TemplateResponse('article.html', {"request":request, "article":article})
    
    return "Article not found"
