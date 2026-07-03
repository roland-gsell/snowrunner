# SnowRunner Archive Structure (Observed)

## Source
Based on inspection of `initial.pak` (Steam Deck version).

---

## Top-level structure

- `[media]` → main game content
- `[media]/_dlc` → DLC organization layer
- `[media]/_templates` → base XML templates
- `[media]/classes` → primary gameplay definitions
- `[strings]` → localization data (not yet analyzed)
- `[ssl_cache]` → unknown (not yet analyzed)

---

## classes/ (core gameplay data)

### Observed categories

| Directory | Content type | Notes |
|----------|-------------|------|
| engines | Engine definitions | ~24 XML files |
| gearboxes | Transmission definitions | ~5 XML files |
| suspensions | Suspension configs | ~40+ XML files |
| wheels | Wheel definitions | ~45 XML files |
| winches | Winch definitions | ~5 XML files |
| trucks | Vehicle definitions | 42 base trucks + tuning folders |
| models | Asset/model descriptors | ~1100 XML files (likely non-gameplay) |

---

## Key structural insight

- `trucks/` is hierarchical:
  - base vehicle XML
  - tuning subfolders per vehicle

- Most other systems are flat catalogs.

---

## Open questions

- What is `[media]/ssl_cache` used for?
- What is `[media]/_templates` lifecycle?
- How are trucks linked to engines/gearboxes internally?
- How are DLC vehicles injected into base lists?
