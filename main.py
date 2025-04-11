from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from router.hr_voice_router import router as hr_voice_router

# Initialize FastAPI app
app = FastAPI(
    title="AI Interview Tracker API",
    description="API for managing AI-powered interview tracking",
    version="1.0.0"
)

# Configure CORS (adjust as needed for your frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only - restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routers
app.include_router(
    hr_voice_router,
    prefix="/api/v1",  # Optional prefix for versioning
    tags=["HR Voice Interview"]
)

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to the AI Interview Tracker API",
        "docs": "Visit /docs for Swagger documentation",
        "redoc": "Visit /redoc for ReDoc documentation"
    }

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # Accessible from other devices on network
        port=8000,
        reload=True,  # Auto-reload during development
        workers=1  # Single worker for development
    )