# 🧪 Nessus Merger

**Nessus Merger** is a simple Python 3 script that merges multiple `.nessus` scan reports into a single consolidated Nessus file. This is particularly useful for penetration testers or vulnerability analysts who perform multiple segmented scans and need a unified view of results.

---

## 🛠 Example Use Case

Imagine you're conducting a full-scope vulnerability assessment to Microsoft, and you've performed three separate Nessus scans:

- 🏢 **Microsoft Office Network**
- 📶 **Microsoft Datacenter Wi-Fi**
- 🏠 **Bill Gates Local Network**

and it is possible to combine these files into a single scan.

---

## 🚀 Usage
![image](https://github.com/user-attachments/assets/bb6a89eb-104a-4083-a87e-392f5dcedfab)

### 🔧 Basic Command

```bash
python3 nessus_merger.py -d /path/to/nessus/files/
