# Instagram facebook Reel Downloader

## Step to run

# Download Social Reels

This project allows you to download Instagram and Facebook reels using Python. It automatically detects the type of URL and downloads the corresponding video.

## Prerequisites

Ensure you have Python installed on your system (Python 3.x is recommended).

## Setup

Follow these steps to set up the project and install dependencies.

### 1. Create a Virtual Environment

To keep dependencies isolated, create a virtual environment:

```sh
python -m venv venv
```

Activate the virtual environment:

- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 2. Install Dependencies

Install the required Python packages from `requirements.txt`:

```sh
pip install -r requirements.txt
```

### 3. Run the Script

Once dependencies are installed, you can run the script by executing:

```sh
python download_reels.py
```

## Usage

Modify the `reel_urls` list in `download_reels.py` with the URLs of the Instagram and Facebook reels you want to download. Then, run the script to download them.

### Example URL List:

```python
reel_urls = [
    "https://www.instagram.com/reel/SHORTCODE1/",
    "https://www.facebook.com/share/r/15tSkFTgxb/?mibextid=rS40aB7S9Ucbxw6v",
]
```

The videos will be saved in `Instagram_Reels` and `Facebook_Reels` folders accordingly.

## Notes

- The script only downloads `.mp4` videos and avoids unnecessary metadata files.
- Ensure your internet connection is stable for successful downloads.

## License

This project is open-source and available for modification and distribution.

Happy downloading! 🚀
