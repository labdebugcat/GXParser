from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


root = Path(__file__).resolve().parents[1]
source = root / "blender_addon" / "nova1492_gx_importer"
destination = root / "dist" / "GXParser-Blender-Addon-0.6.0.zip"
destination.parent.mkdir(exist_ok=True)
with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
    for path in sorted(source.glob("*.py")):
        archive.write(path, Path("nova1492_gx_importer", path.name))
print(destination)
