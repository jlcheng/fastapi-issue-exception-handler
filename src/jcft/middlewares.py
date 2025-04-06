from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def add_cors_middleware(app: FastAPI):
    # See https://github.com/fastapi/fastapi/discussions/8027
    # The parameters here must be in sync with the parameters used to
    # launch the FastAPI instance. In this case it must
    # match src/main.py.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://example.com"],
        allow_credentials=True,
    )
