# 📝 Advanced Notes Application

## 🚀 What This Advanced Version Will Do

- 📅 **Add timestamps** when a note is created.  
- 🏷 **Allow categories/tags** for each note.  
- 📂 **Save notes in a CSV file** instead of plain text (easier to parse/search).  
- 💾 **Create a backup file** automatically every time a note is added or deleted.  
- 🔍 **Search by keyword or category**.

---

## 📋 Step-by-Step Plan

### **1️⃣ Use CSV for Storing Notes**
- **Structure:** `timestamp,category,note`  
- Easier for organizing, searching, and sorting later.

### **2️⃣ Add Backup System**
- After any write/delete, copy the CSV into a backup file (e.g., `notes_backup.csv`).

### **3️⃣ Timestamp Generation**
- Use `datetime.now()` to get the exact time a note was created.

### **4️⃣ Search Function**
- Let the user search by:
  - **Keyword** (inside note text)  
  - **Category**  

---
