<div align="center">

# CuDownloader

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-2024.12.13-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-En%20Desarrollo-orange?style=for-the-badge)](https://github.com)

**Descargador de videos, playlists y audio de YouTube** — Rápido, ligero y fácil de usar.

[Instalación](#-instalación) • [Uso](#-uso) • [Características](#-características) • [Roadmap](#-roadmap)

</div>

---

## Características

- Descarga videos individuales o playlists completas
- Extracción de audio (MP3, M4A, etc.)
- Selección de calidad de video
- Historial de descargas para evitar duplicados
- Interfaz de línea de comandos (CLI) intuitiva
- **Próximamente:** Interfaz gráfica moderna

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/CuDownloader.git
cd CuDownloader

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
# Descargar un video
python main.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Descargar solo audio
python main.py "https://www.youtube.com/watch?v=VIDEO_ID" --audio

# Descargar una playlist
python main.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist
```

## Estructura del Proyecto

```
CuDownloader/
├── main.py              # Punto de entrada
├── downloader/          # Lógica de descarga
│   ├── download.py      # Motor de descarga
│   ├── options.py       # Configuración y opciones
│   ├── progress.py      # Barra de progreso
│   ├── info.py          # Información del video
│   └── cli.py           # Interfaz CLI
├── downloads/           # Carpeta de descargas
└── requirements.txt     # Dependencias
```

## Roadmap

- [x] Descarga de videos individuales
- [x] Descarga de playlists
- [x] Extracción de audio
- [x] Historial de descargas
- [ ] Interfaz gráfica (GUI)
- [ ] Soporte para subtítulos
- [ ] Descarga en segundo plano

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---

<div align="center">

Hecho con Python y yt-dlp

</div>
