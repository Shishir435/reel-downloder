import instaloader
import os
import yt_dlp

def download_instagram_reel(url, download_folder="Instagram_Reels"):
    loader = instaloader.Instaloader(download_pictures=False, download_videos=True, post_metadata_txt_pattern="")
    
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    try:
        shortcode = url.strip().split("/")[-2]  # Extract shortcode from URL
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        
        # Download only the video reel
        loader.download_post(post, target=download_folder)
        print(f"Downloaded Instagram Reel: {shortcode}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def download_facebook_reel(url, download_folder="Facebook_Reels"):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    ydl_opts = {
        'outtmpl': os.path.join(download_folder, '%(id)s.%(ext)s'),  # Save as ID only
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',  # Ensure proper merging
        'noplaylist': True,
        'quiet': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"Downloaded Facebook Reel: {url}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

def download_reels(reel_urls):
    for url in reel_urls:
        if "instagram.com/reel" in url:
            download_instagram_reel(url)
        elif "facebook.com/share/r/" in url or "facebook.com/reel" in url:
            download_facebook_reel(url)
        else:
            print(f"Unsupported URL format: {url}")


if __name__ == "__main__":
    reel_urls = [
        "https://www.instagram.com/reel/DCQMDzRPTdA/?igsh=MWlzaDV6N3VlazFjag==",
    "https://www.instagram.com/reel/DB8VT1ixsgS/?igsh=MWl2cGtsaGM3MnBzZg==",
    "https://www.instagram.com/reel/DC_F_gapJzb/?igsh=MW5uanVtdjR4dTNsbA==",
    "https://www.instagram.com/reel/DDZewjrPnkW/?igsh=MXRkYW84dzkwZjluMQ==",
    "https://www.instagram.com/reel/DEG5NOgoD66/?igsh=MnY0bnNhZ3d2OXpo",
    "https://www.instagram.com/reel/DEyydMYSij1/?igsh=MTV3b3hyMzRmMnV6dw==",
    "https://www.facebook.com/share/r/15tSkFTgxb/?mibextid=rS40aB7S9Ucbxw6v",
    "https://www.facebook.com/share/r/1QuFWUr9yf/?mibextid=rS40aB7S9Ucbxw6v",
    "https://www.facebook.com/share/r/15A219oELv/?mibextid=rS40aB7S9Ucbxw6v",
    "https://www.facebook.com/share/r/15cf3qSXZh/?mibextid=rS40aB7S9Ucbxw6v"
    ]  # Replace with actual reel URLs
    
    download_reels(reel_urls)
