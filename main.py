from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # 👈 これを追加
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉！素晴らしい幸運が舞い込むでしょう。",
        "中吉！努力が実を結び、良い結果が待っています。",
        "小吉！ちょっとした幸運があなたの元にやってきます。",
        "吉！安定した幸せな日々が続くでしょう。",
        "末吉！努力が実り始め、良い方向に進む時期です。",
        "凶。悪いことが起こるかもしれませんが、気を引き締めてください。",
        "小凶。注意が必要な日です。慎重に行動しましょう。",
        "大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。"
    ]
    return {"result" : omikuji_list[random.randrange(8)]}

# 👇 ここから課題9-1のコードです（HTMLの内容を好きなように書き換えています）
@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <meta charset="utf-8">
            <title>マイ・ホームページ</title>
            <style>
                body { font-family: sans-serif; text-align: center; background-color: #f0f8ff; padding: 50px; }
                h1 { color: #333399; }
                p { font-size: 18px; color: #555; }
            </style>
        </head>
        <body>
            <h1>ようこそ！私のホームページへ</h1>
            <p>FastAPIを使ってHTMLを表示する課題に挑戦中です！</p>
            <p>文字やデザインは好きなように書き換えることができます。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)