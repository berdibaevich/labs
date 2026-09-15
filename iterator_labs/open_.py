import os


def open_(path, *, mode="r", chunk_size=1024):
    """Generator, works like as open() function"""
    
    flags = {"r": os.O_RDONLY}

    fd = os.open(path, flags=flags[mode])
    buffer = os.read(fd, chunk_size)
    try:
        while True:
            while (index := buffer.find(b"\n")) != -1:
                line = buffer[:index].decode("utf-8")
                buffer = buffer[index + 1:]
                yield line

            chunk = os.read(fd, chunk_size)
            if chunk:
                buffer += chunk
            else:
                if buffer:
                    line = buffer.decode("utf-8")
                    buffer = b""
                    yield line
                break
    finally:
        os.close(fd)