from fastapi import FastAPI

from apps.api.app.api import router

app = FastAPI(
    title="truck-telemetry",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix="/api")

for route in app.routes:
    print(f"{route.path} -> {route.methods}")