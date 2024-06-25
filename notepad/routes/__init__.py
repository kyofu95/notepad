from pathlib import Path

from fastapi.templating import Jinja2Templates

base_dir = Path(__file__).resolve().parent.parent
templates_dir = base_dir.joinpath("resources/templates")

assert templates_dir.exists()

templates = Jinja2Templates(directory=str(templates_dir))
