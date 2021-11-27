from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import dao

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:4200',
        'https://mf-calculatorr.herokuapp.com/'
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def set_cors_middleware(request: Request, call_next):
    res = await call_next(request)
    res.headers["Access-Control-Allow-Origin"] = '*'
    return res


@app.get("/")
def index():
    dao.cur.execute('SELECT * FROM user;')
    return f"MF Calculator      {dao.cur.fetchall()}"
