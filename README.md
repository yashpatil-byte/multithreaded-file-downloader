# 🧵 Multithreaded File Downloader (Python)

A simple, efficient **multithreaded file downloader** built in Python.  
This project demonstrates how to use threads to download files faster by splitting them into chunks and downloading parts concurrently.

---

## 🚀 Features
- Single-threaded & multi-threaded versions for comparison
- Real-time download progress using `tqdm`
- Automatic chunk merging
- Exception handling for failed downloads
- Simple and lightweight (no external config)

---

## 🧩 Files
| File | Description |
|------|--------------|
| `downloader_basic.py` | Single-threaded file downloader (baseline) |
| `downloader_multi.py` | Multithreaded downloader with progress bar |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## ⚙️ Setup

1️⃣ Clone or download this repository.  
2️⃣ (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```