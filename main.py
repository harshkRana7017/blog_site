from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pathlib import Path
import json
from fastapi.templating import Jinja2Templates
from models import User
from datetime import datetime

templates= Jinja2Templates(directory='Templates')

app = FastAPI()
USERNAME=''
PASSWORD=''

@app.get("/home")
def read_route(request:Request):
    user_name ="john"
    return templates.TemplateResponse("index.html", {"request":request, "user_name":user_name})


@app.get("/")
def loginForm(request: Request):
    return templates.TemplateResponse("loginForm.html", {"request":request})


# change this to confirm user
@app.post("/login" )
def login(request:Request, username:str =Form(...), password:str=Form(...)):
    USERNAME=username
    PASSWORD=password
    return templates.TemplateResponse("index.html", {"request":request, "user_name":"john"})



@app.get("/articles", response_class = HTMLResponse)
async def read_articles(request: Request):
    article_files= Path("Articles").glob("*json")
    articles= [json.loads(article_file.read_text())  for article_file in article_files]
    return templates.TemplateResponse("articleList.html", {"request":request, "articles": articles})


@app.get('/articles/{article_id}')
async def read_article(request: Request,article_id: int):
    article_path = Path(f"Articles/{article_id}.json")
    if(article_path.exists()):
        article =json.loads(article_path.read_text())
        return templates.TemplateResponse('article.html', {"request":request, "article":article})
    
    return "Article not found"

@app.get('/article/add')
def add_articleForm(request:Request):
   return templates.TemplateResponse("addArticleForm.html", {"request":request})


@app.post('/article/add')
def add_article(request:Request,title:str =Form(...), content:str =Form(...) ):
    today_date= datetime.now().strftime('%Y-%m-%d')
    article_id =len(list(Path("Articles").glob("*json")))
    article_path = Path(f"Articles/{article_id}.json")
    article_path.write_text(json.dumps({"id":article_id, "title":title, "content":content, "author":USERNAME, "date": today_date}))

    return templates.TemplateResponse('article.html', {"request":request,"article":json.loads(article_path.read_text()) })