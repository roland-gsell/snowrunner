# SnowRunner Toolkit

A reverse-engineering and data extraction toolkit for SnowRunner game archives.

## Requirements

- Python 3.12+
- Linux (tested on Steam Deck / Ubuntu / Arch)

---

## Legal Notice

This repository does **not** contain any SnowRunner game assets.

To use this project, you must own a legitimate copy of SnowRunner and extract data from your own installation.

The main game archive is typically located at:

* **Windows (Steam):**
  `...\Steam\steamapps\common\SnowRunner\preload\paks\client\initial.pak`

* **Steam Deck / Linux (Steam Proton):**
  `~/.local/share/Steam/steamapps/common/SnowRunner/preload/paks/client/initial.pak`

Do **not** commit or redistribute extracted game assets (such as `.pak` files, XML files, textures, models, or localization files). This repository intentionally contains only original source code and documentation.

SnowRunner and all associated game assets are the intellectual property of Saber Interactive and Focus Entertainment.


## Setup

Clone the repository:

```bash
git clone https://github.com/roland-gsell/snowrunner.git
cd snowrunner

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip

pip install ruff pytest mypy
```
