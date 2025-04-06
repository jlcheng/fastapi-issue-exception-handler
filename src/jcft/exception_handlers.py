import logging

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_exception_handlers(app: FastAPI):
    @app.exception_handler(KeyError)
    async def key_error_handler(_request: Request, exc: KeyError) -> JSONResponse:
        logger.error("key_error_handler: Error occurred", exc_info=True)  # Log the generic error
        return JSONResponse(
            status_code=500,
            content={"message": "An internal server error occurred.", "detail": "none"},
        )

    @app.exception_handler(Exception)
    async def generic_error_handler(_request: Request, exc: Exception) -> JSONResponse:
        logger.error("generic_error_handler: Error occurred", exc_info=True)  # Log the generic error
        return JSONResponse(
            status_code=500,
            content={"message": "An internal server error occurred.", "detail": "none"},
        )
