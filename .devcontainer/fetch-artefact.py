#!/usr/bin/env python3
"""Download the MASHUP artefact from Zenodo, verify its md5 and unpack it.

Idempotent: does nothing if artefact/hybrid/ already exists. Standard library
only, so it runs before or without any pip install.
"""
import hashlib
import os
import shutil
import sys
import urllib.request
import zipfile

URL = "https://zenodo.org/api/records/5733395/files/MashUP.zip/content"
MD5 = "b9e96748b36c7916b93c0df286b69499"
SIZE = 60961151

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(ROOT, "artefact")
ZIP = os.path.join(DEST, "MashUP.zip")


def md5sum(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if os.path.isdir(os.path.join(DEST, "hybrid")):
        print("MASHUP already unpacked in artefact/hybrid/")
        return 0
    os.makedirs(DEST, exist_ok=True)
    if not (os.path.exists(ZIP) and md5sum(ZIP) == MD5):
        print("Downloading MashUP.zip (61 MB) from Zenodo ...")
        with urllib.request.urlopen(URL) as r, open(ZIP + ".part", "wb") as f:
            shutil.copyfileobj(r, f)
        os.replace(ZIP + ".part", ZIP)
    size, digest = os.path.getsize(ZIP), md5sum(ZIP)
    if size != SIZE or digest != MD5:
        print("Checksum mismatch: %d bytes, md5 %s (expected %d, %s)"
              % (size, digest, SIZE, MD5), file=sys.stderr)
        return 1
    print("md5 OK, unpacking into artefact/ ...")
    with zipfile.ZipFile(ZIP) as z:
        z.extractall(DEST)
    # zipfile drops the executable bit; restore it for the task binaries.
    for dirpath, _, files in os.walk(os.path.join(DEST, "hybrid")):
        for name in files:
            if name.endswith(".exe"):
                p = os.path.join(dirpath, name)
                os.chmod(p, os.stat(p).st_mode | 0o111)
    print("Done: artefact/hybrid/README.md is the authors' entry point.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
