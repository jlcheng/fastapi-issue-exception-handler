import logging

from fastapi import FastAPI

from .exception_handlers import add_exception_handlers
from .middlewares import add_cors_middleware
from .routes import add_routes

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="jcft",
    description="A simple FastAPI project"
)

add_exception_handlers(app)
add_cors_middleware(app)
add_routes(app)
