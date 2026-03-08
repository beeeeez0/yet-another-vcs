import collections
import os

IndexEntry = collections.namedtuple(
    "IndexEntry",
    [
        "ctime_s",
        "ctime_ns",
        "mtime_s",
        "mtime_ns",
        "dev",
        "ino",
        "sha1",
        "mode",
        "path",
        "flags",
        "uid",
        "gid",
        "size",
    ],
)


def read_index():
    """Reads the index file and returns a list of IndexEntry objects."""
    try:
        with open(os.path.join(".git", "index"), "rb") as f:
            return f.read()
    except FileNotFoundError:
        return []
