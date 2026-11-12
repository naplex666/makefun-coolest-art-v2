# coolest-art-01: Celestial Phoenix

## Overview
`coolest-art-01` is a make.fun bounty entry featuring a breathtaking digital art piece: **Celestial Phoenix**.

- **Artwork Description**: A majestic celestial phoenix featuring one fire-gold wing and one starlight-blue wing soaring gracefully over a vibrant violet nebula.
- **Gate Specifications**:
  - Format: PNG
  - Dimensions: 1024x1024 pixels
  - File Size: 574,623 bytes (< 1 MiB)

## How the Program Works
`main.py` is a fully self-contained, deterministic Python 3.13 script. 
- It embeds the artwork bytes as a base64-encoded string directly within the source code at build time.
- At runtime, it reads no external files, makes zero network calls, uses no randomness, and performs no clock reads.
- It ensures `/output` exists and writes the exact original artwork bytes to `/output/entry.png`.
- Multiple runs are guaranteed to be 100% byte-identical.

## How to Run
```bash
python3 main.py
```
The output image will be generated at `/output/entry.png`.

## Verification
- Compiles cleanly under Python 3.13 (`python3 -m py_compile main.py`).
- Standard library only (`base64`, `os`).
