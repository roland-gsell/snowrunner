# SnowRunner Toolkit – Discoveries Log

## 2026-07-03

### Archive indexing

We implemented a full in-memory directory index.

#### Facts
- ~11,500 XML files in archive
- Full directory tree built at startup
- No repeated archive scanning in CLI commands

---

### Performance

| Command | Runtime |
|--------|--------|
| tree | ~0.81s |
| ls | ~1.04s |
| stats | ~1.02s |

---

### Structural observations

- Trucks are split into:
  - base XML
  - tuning subdirectories

- Engines / gearboxes / winches are flat catalogs

- `models/` contains ~1100 XML files and is likely non-gameplay data
