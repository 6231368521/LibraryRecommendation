from fastapi import FastAPI
from route.user import user
from route.book import book
from route.subject import subject
from route.faculty import faculty
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def healthz():
    return { "message": "hello server"}

app.include_router(user, prefix = "/users")
app.include_router(book, prefix = "/books")
app.include_router(subject, prefix = "/subjects")
app.include_router(faculty, prefix = "/facultys")