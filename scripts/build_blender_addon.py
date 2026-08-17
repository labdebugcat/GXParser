from pathlib import Path
import tomllib
from zipfile import ZIP_DEFLATED, ZipFile


root = Path(__file__).resolve().parents[1]
source = root / "blender_addon" / "nova1492_gx_importer"
project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
version = project["project"]["version"]
destination = root / "dist" / f"GXParser-Blender-Addon-{version}.zip"
destination.parent.mkdir(exist_ok=True)
with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
    for path in sorted(source.glob("*.py")):
        archive.write(path, Path("nova1492_gx_importer", path.name))
print(destination)
