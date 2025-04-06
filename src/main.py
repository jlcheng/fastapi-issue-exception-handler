import uvicorn
from starlette.middleware.cors import CORSMiddleware

from jcft.main_app import app


def main():
    # See https://github.com/fastapi/fastapi/discussions/8027
    # This expands on that solution to consider the case where the affected
    # URL requires cookie-based authentication.
    #
    # The parameters here must match the parameters used by the
    # CORSMiddleware instance used in `app.add_middleware()`. In this case,
    # it must match the code in `middlewares.py`.
    wrapped_app = CORSMiddleware(
        app,
        allow_origins=["https://example.com"],
        allow_credentials=True,
    )
    uvicorn.run(
        wrapped_app,
        host="0.0.0.0",
        port=8080,
    )


if __name__ == "__main__":
    main()
