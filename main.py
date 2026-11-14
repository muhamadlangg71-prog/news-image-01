# news-image-01 entry v2 (Python 3.13, standard library only, no network):
# copies the entry image beside this file to /output/entry.png.
# v2 image: newspaper front page "13 NOVEMBER 2026" with 8 captioned panels
# in a 2x4 grid — Nvidia CEO resigns, Ukraine drone strike, US flights halted,
# Microsoft 365 outage day 2, China naval drills around Taiwan, US downs 2
# Iranian drones, Trump double Mexico tariffs, Houthis hit Saudi oil pipeline.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
import os
import shutil
import struct
import sys
from pathlib import Path

MAX_BYTES = 1_048_576  # competition cap: image at most 1 MiB

src = Path(__file__).resolve().parent / "entry.png"
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"

if not src.is_file():
    print(f"missing entry image: {src}", file=sys.stderr)
    sys.exit(1)

size = src.stat().st_size
if size > MAX_BYTES:
    print(f"entry image too large: {size} bytes > {MAX_BYTES}", file=sys.stderr)
    sys.exit(1)

# Validate it is a JPEG or PNG and read its pixel dimensions.
with open(src, "rb") as f:
    head = f.read(33)
if head[:3] == b"\xff\xd8\xff":
    # JPEG: scan segments for the SOF marker carrying width/height.
    w = h = None
    i = 2
    while i + 9 <= len(head) and w is None:
        if head[i] != 0xFF:
            break
        marker = head[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            h = struct.unpack(">H", head[i + 5:i + 7])[0]
            w = struct.unpack(">H", head[i + 7:i + 9])[0]
            break
        seg_len = struct.unpack(">H", head[i + 2:i + 4])[0]
        i += 2 + seg_len
    if w is None:
        # Header too short to hold the SOF segment; fall back to a full read.
        with open(src, "rb") as f:
            data = f.read()
        i = 2
        while i + 9 <= len(data):
            if data[i] != 0xFF:
                break
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2):
                h = struct.unpack(">H", data[i + 5:i + 7])[0]
                w = struct.unpack(">H", data[i + 7:i + 9])[0]
                break
            seg_len = struct.unpack(">H", data[i + 2:i + 4])[0]
            i += 2 + seg_len
elif head[:8] == b"\x89PNG\r\n\x1a\n":
    w, h = struct.unpack(">II", head[16:24])
else:
    print("entry image is neither JPEG nor PNG", file=sys.stderr)
    sys.exit(1)
if w is None or h is None or w > 1024 or h > 1024:
    print(f"entry image dimensions invalid: {w}x{h} (max 1024x1024)", file=sys.stderr)
    sys.exit(1)

out.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out)
print(f"wrote {out} ({w}x{h}, {size} bytes)")
