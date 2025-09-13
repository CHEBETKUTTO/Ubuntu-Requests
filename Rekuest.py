import os
import requests
from urllib.parse import urlparse
import uuid

def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully downloading images from the web\n")

    # Step 1: Ask for the URL
    print("[Step 1] Prompting user for image URL...")
    url = input("👉 Enter the URL of the image: ").strip()
    print("[Step 1] You entered:", url,)

    # Step 2: Create save directory
    print("\n[Step 2] Creating save directory...")
    save_dir = "downloaded_images"
    os.makedirs(save_dir, exist_ok=True)
    print(f"[Step 2] Directory ready: {save_dir}",)

    try:
        # Step 3: Fetch the image
        print("\n[Step 3] Fetching image from the web...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("[Step 3] Image fetched successfully ✅",)

        # Step 4: Extract filename or generate one
        print("\n[Step 4] Determining filename...")
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename or "." not in filename:  # no extension → generate
            filename = f"downloaded_{uuid.uuid4().hex}.jpg"

        filepath = os.path.join(save_dir, filename)
        print(f"[Step 4] Filename chosen: {filename}",)

        # Step 5: Save the image
        print("\n[Step 5] Saving image to disk...")
        with open(filepath, "wb") as file:
            file.write(response.content)
        print(f"[Step 5] ✅ Image saved successfully at: {filepath}", flush=True)

    except requests.exceptions.RequestException as e:
        print(f"\n⚠️ Network error: {e}")
    except Exception as e:
        print(f"\n⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    main()
