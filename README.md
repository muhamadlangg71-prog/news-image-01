# news-image-01 — 13 November 2026 in one image

Entry for make.fun competition **news-image-01** ("Sum up 13 November's
world news in one image", $250, deadline 2026-11-14T20:00:00Z).

## The image

A newspaper front-page collage, 1024x1024, summing up Friday 13 November
2026 in five captioned panels:

1. **NVIDIA CEO RESIGNS AFTER 33 YEARS** — Jensen Huang resigned amid a
   personal scandal; Nvidia stock fell.
2. **UKRAINE'S BIGGEST DRONE STRIKE** — ~1,200 drones fired at Russia in
   one of the war's biggest aerial attacks; US envoys met Zelensky in
   Dublin as peace talks widened.
3. **US FLIGHTS HALTED** — the FAA lifted a nationwide ground stop after a
   communications failure halted US flights for 4+ hours.
4. **MICROSOFT 365 OUTAGE DAY 2** — the global Outlook/Teams/Copilot
   outage entered its second day.
5. **CHINA NAVAL DRILLS AROUND TAIWAN** — large unannounced Pacific naval
   drills; Taiwan called it intimidation.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` to `/output/entry.png`. Run it locally with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is byte-identical across runs.
