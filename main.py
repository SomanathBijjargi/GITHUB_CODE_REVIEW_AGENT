from fastapi import FastAPI
from api.reviews import router as review_router
from api.webhook import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="GitHub Review Agent"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
app.include_router(review_router)