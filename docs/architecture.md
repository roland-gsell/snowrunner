# Project Architecture

```text
SnowRunner .pak
       │
       ▼
  PakReader
       │
       ▼
   XmlParser
       │
       ▼
 XML Document
       │
       ▼
  Domain Model
       │
       ├── CLI
       ├── CSV Exporter
       ├── XLSX Exporter
       ├── JSON Exporter
       └── HTML Exporter (planned)
```

The project follows a layered architecture:

1. **PakReader** provides transparent access to files inside SnowRunner `.pak` archives.
2. **XmlParser** parses SnowRunner's custom XML format into a reusable document model.
3. The **Domain Model** represents game concepts such as trucks, engines, gearboxes and addons.
4. Exporters and command-line tools consume the domain model without needing to understand the XML format.
