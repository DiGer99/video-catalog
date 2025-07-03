from fastapi import (
    FastAPI,
    Request,
)


app = FastAPI(title="Video Hosting")


@app.get("/")
def read_root(
    request: Request,
):
    url_docs = request.url.replace(path="docs", query={})
    return {
        "message": "index page",
        "url": str(url_docs),
    }
