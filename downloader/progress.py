"""Barra de progreso para las descargas de yt-dlp"""


def progress_hook(d):
    
    pct = d.get("_percent_str", "??%").strip()
    vel = d.get("_speed_str", "??").strip()
    eta = d.get("_eta_str", "??").strip()
    
    if d["status"] == "downloading":
        print(f'\r ⬇️ {pct} | {vel} | {eta}', end="")
    elif d["status"] == "finished":
        print("\n ☑️ Descarga completada, procesando...")
    elif d["status"] == "error":
        print("\n ❌ Error en la descarga")