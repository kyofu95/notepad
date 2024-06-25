from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter

from . import templates

web_router = APIRouter()


@web_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    page_context = {"user_logged": False}
    return templates.TemplateResponse(request=request, name="index.html", context=page_context)
