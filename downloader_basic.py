import requests
import time

def download_file(url, filename):
    print(f"Starting download: {url}")
    start_time = time.perf_counter()

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    end_time = time.perf_counter()
    print(f" Download complete: {filename}")
    print(f" Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    # Example file (small test)
    url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-zip-file.zip"
    download_file(url, "sample.zip")
