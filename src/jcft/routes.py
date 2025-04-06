from fastapi import FastAPI
from starlette.responses import JSONResponse


def add_routes(app: FastAPI):
    @app.get("/health")
    def health():
        return JSONResponse({"status": "ok"})

    @app.get("/exceptions/keyerror")
    def keyerror():
        raise KeyError("a key error was raised")

    @app.get("/exceptions/generic")
    def generic():
        raise Exception("a generic exception was raised")