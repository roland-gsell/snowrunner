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

## Features

Current capabilities:

* Explore the directory structure of SnowRunner `.pak` archives
* Browse archive directories
* Display directory statistics
* Search for files by name
* View the contents of text and XML files directly from the archive
* Fast archive indexing with in-memory path lookup

Planned features:

* XML structure inspection
* Truck dependency extraction
* Truck database export (CSV / Excel)
* Automatic discovery of engines, gearboxes, suspensions and addons
* DLC and season comparison

## Usage

The main archive can be explored directly without extracting it first.

### Show the archive tree

```bash
python3 src/snowrunner/explore.py initial.pak tree
```

### List the contents of a directory

```bash
python3 src/snowrunner/explore.py initial.pak ls [media]/classes/trucks
```

### Display directory statistics

```bash
python3 src/snowrunner/explore.py initial.pak stats [media]/classes
```

### Search for files

```bash
python3 src/snowrunner/explore.py initial.pak find azov
```

### Display a file

```bash
python3 src/snowrunner/explore.py initial.pak cat [media]/classes/trucks/azov_5319.xml
```

