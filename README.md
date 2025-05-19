# 🧪 Nessus Merger

**Nessus Merger** is a simple Python 3 script that merges multiple `.nessus` scan reports into a single consolidated Nessus file. This is particularly useful for penetration testers or vulnerability analysts who perform multiple segmented scans and need a unified view of results.

---

## 📌 Features

- ✅ Merge unlimited `.nessus` XML files
- ✅ Avoids duplicate hosts and plugin findings
- ✅ Outputs a valid `.nessus` file, importable back into Nessus or Tenable.sc
- ✅ Python 3 compatible and portable
- ✅ Easy CLI interface

---

## 📦 Requirements

- Python 3.x  
- No external dependencies (uses only built-in Python libraries)

---

## 🚀 Usage

### 🔧 Basic Command

```bash
python3 nessus_merger.py -d /path/to/nessus/files/
