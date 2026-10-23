"""Construccion de opciones para yt-dlp"""

from pathlib import Path
from . import HISTORY_FILE
from .progress import progress_hook

def build_options(args):
    
    template = str(
        Path(args.directory) / "%(uploader)s" / "%(title)s.%(ext)s"
    )
    
    opt = {
        "outtmpl": template,
        "progress_hooks": [progress_hook],
        "ignoreerrors": True,          
        "no_warnings": True,           
        "quiet": True,                
        "noprogress": True,         
        "download_archive": HISTORY_FILE,
    }
    
    if args.audio:
        opt.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
        })
    else:
        #De momento descarga el video con la mejor calidad posible + audio
        filtro = f"[height<={args.max_res}]" if args.max_res else ""
        opt["format"] = f"bestvideo{filtro}+bestaudio/best{filtro}/best"
        opt["merge_output_format"] = "mp4"
    
    if not args.playlist:
        opt["noplaylist"] = True
        
    #cookies (opcionales)
    cookies = getattr(args, "cookies_from_browser", None)
    if cookies:
        opt["cookiesfrombrowser"] = (cookies,)
        
    return opt
