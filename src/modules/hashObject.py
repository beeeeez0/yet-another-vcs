import hashlib
import os
import zlib


def hash_object(data, type, write=True):
    """Compute the hash of an object"""
    header = f"{type} {len(data)}\0"
    fulldata = header.encode() + data
    sha1 = hashlib.sha1(fulldata).hexdigest()
    if write:
        path = os.path.join(".git", "objects", sha1[:2], sha1[2:])
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as f:
                f.write(zlib.compress(fulldata))
    return sha1
