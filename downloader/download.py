"""Logica de descarga"""

from pathlib import Path
import yt_dlp
from .options import build_options

def download(url, args):
    Path(args.directory).mkdir(parents=True, exist_ok=True)
    
    print(f"\nDownloading video: {url}")
    if args.audio:
        print("\nMode: audio only (MP3)")
    else:
        label = f" (max {args.max_res}p)" if args.max_res else " (best quality)"
        print(f"\nMode: video{label}")
    
    opt = build_options(args)
    
    try:
        with yt_dlp.YoutubeDL(opt) as ydl:
            ydl.download([url])
        print("\nDone")
    except yt_dlp.utils.DownloadError as e:
        print(f"\nDownload error: {e}.")
    except KeyboardInterrupt:
        print("\nCancelled by user.")
    except Exception as e:
        print(f"\nUnexpected error: {e}.")
        
