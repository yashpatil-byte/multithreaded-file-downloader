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

1️⃣ **Clone or download this repository**

```bash
git clone https://github.com/<your-username>/multithreaded-file-downloader.git
cd multithreaded-file-downloader


Example output:
Starting download: https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-zip-file.zip
 Download complete: sample.zip
 Time taken: 0.73 seconds
```

🧠 Concepts Used
threading.Thread for concurrency
requests for network I/O
tqdm for progress tracking
File I/O and chunk merging
Performance benchmarking with time.perf_counter()
Exception handling and logging

Author
Yash Patil
🎓 Northeastern University, Boston
💼 Aspiring Software Development Engineer
⭐ If you found this project helpful, consider giving it a star on GitHub!
