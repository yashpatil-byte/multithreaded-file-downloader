import threading
import requests
import os
import time
from tqdm import tqdm

def download_chunk(url, start, end, filename, thread_index, progress_bar):
    """
    Downloads a specific byte range (chunk) of the file.
    """
    headers = {'Range': f'bytes={start}-{end}'}
    try:
        response = requests.get(url, headers=headers, stream=True, timeout=10)
        response.raise_for_status()
        with open(f"{filename}.part{thread_index}", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    progress_bar.update(len(chunk))
    except requests.RequestException as e:
        print(f" Thread {thread_index} failed: {e}")

def merge_chunks(filename, num_threads):
    """
    Combines all downloaded parts into a single file.
    """
    with open(filename, "wb") as output_file:
        for i in range(num_threads):
            part_file = f"{filename}.part{i}"
            with open(part_file, "rb") as pf:
                output_file.write(pf.read())
            os.remove(part_file)

def download_file_multithreaded(url, filename, num_threads=4):
    """
    Splits the file into chunks and downloads them in parallel threads.
    """
    response = requests.head(url)
    if 'Content-Length' not in response.headers:
        print("Cannot determine file size. Server does not support partial downloads.")
        return

    file_size = int(response.headers['Content-Length'])
    chunk_size = file_size // num_threads

    print(f" File size: {file_size / 1_000_000:.2f} MB")
    print(f" Starting download with {num_threads} threads...")

    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc="Downloading")

    threads = []
    start_time = time.perf_counter()

    for i in range(num_threads):
        start = i * chunk_size
        end = file_size - 1 if i == num_threads - 1 else (start + chunk_size - 1)
        t = threading.Thread(
            target=download_chunk,
            args=(url, start, end, filename, i, progress_bar)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    progress_bar.close()
    merge_chunks(filename, num_threads)

    end_time = time.perf_counter()
    print(f" Download complete: {filename}")
    print(f" Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    # Test file (you can replace this URL)
    url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-zip-file.zip"
    download_file_multithreaded(url, "sample_multi.zip", num_threads=4)
