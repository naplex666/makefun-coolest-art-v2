import hashlib
from pathlib import Path
import struct

def validate(data: bytes):
    if not data:
        raise SystemExit("ERROR: Image data is empty.")
    
    size = len(data)
    if size > 1048576:
        raise SystemExit(f"ERROR: Image size {size} exceeds 1 MiB limit.")
        
    png_magic = b"\x89PNG\r\n\x1a\n"
    if not data.startswith(png_magic):
        raise SystemExit("ERROR: Invalid PNG magic bytes.")
        
    if len(data) < 24:
        raise SystemExit("ERROR: Image data too short to contain IHDR chunk.")
        
    width, height = struct.unpack(">II", data[16:24])
    if width != 1024 or height != 1024:
        raise SystemExit(f"ERROR: Invalid dimensions {width}x{height}, expected 1024x1024.")

def main():
    src_path = Path("assets/entry.png")
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    dst_path = output_dir / "entry.png"

    data = src_path.read_bytes()
    validate(data)
    dst_path.write_bytes(data)

    file_size = len(data)
    sha256_hash = hashlib.sha256(data).hexdigest()

    print(f"VALIDATION: OK size={file_size} sha256={sha256_hash}")

if __name__ == "__main__":
    main()

