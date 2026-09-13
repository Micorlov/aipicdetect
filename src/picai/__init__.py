"""picai: re-render images from pixels and drop all embedded metadata."""

from pillow_heif import register_heif_opener

from picai.scrub import ScrubResult, scrub_bytes, scrub_file

register_heif_opener()  # lets every Image.open() in the package decode HEIC/HEIF

__all__ = ["ScrubResult", "scrub_bytes", "scrub_file"]
