# 🧪 Nessus Merger

**Nessus Merger** is a simple Python 3 script that merges multiple `.nessus` scan reports into a single consolidated Nessus file. This is particularly useful for penetration testers or vulnerability analysts who perform multiple segmented scans and need a unified view of results.

---

## 🛠 Example Use Case

Imagine you're conducting a full-scope vulnerability assessment to Microsoft, and you've performed three separate Nessus scans:

- 🏢 **Microsoft Office Network**
- 📶 **Microsoft Datacenter Wi-Fi**
- 🏠 **Bill Gates Local Network**

and it is possible to combine these files into a single scan.

## 🚀 Usage

### 📥 Exporting `.nessus` files from Nessus to Downloads folder

This is how you can export `.nessus` scan files to your local `Downloads` folder from Nessus:

![Export](https://github.com/user-attachments/assets/67fdbc51-1ca8-4db8-8884-dec98a1639a7)

---

### 🧪 Merge Command

Once you've exported your `.nessus` files, run the following command:

```bash
python3 nessus_merger.py -d /home/user/Downloads



