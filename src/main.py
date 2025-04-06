import uvicorn
from starlette.middleware.cors import CORSMiddleware

from jcft.main_app import app


def main():
    wrapped_app = CORSMiddleware(app, allow_origins=["*"])  # https://github.com/fastapi/fastapi/discussions/8027
    uvicorn.run(
        wrapped_app,
        host="0.0.0.0",
        port=8080,
    )


if __name__ == "__main__":
    main()
