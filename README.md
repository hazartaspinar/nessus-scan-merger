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

### 🔹 Before merging

![Before](https://github.com/user-attachments/assets/329000bc-3cbf-45b8-9703-9332f03a7704)

---

### 🔹 After merging

![After](https://github.com/user-attachments/assets/f3beb7fd-1618-4acb-a279-4970b33b9435)

---

### 📤 Exporting `.nessus` files from Nessus to Downloads folder

![Export](https://github.com/user-attachments/assets/67fdbc51-1ca8-4db8-8884-dec98a1639a7)

---

### 🧪 Merge Command

```bash
python3 nessus_merger.py -d /home/user/Downloads
