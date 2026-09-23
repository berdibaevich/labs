import os


class FileStream:
    def __init__(self, fd: int, chunk_size: int=1024):
        self._fd = fd
        self._chunk_size = chunk_size
        self._buffer = b""
        self.closed = False

    def close(self):
        if not self.closed:
            os.close(self._fd)
            self.closed = True

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.closed:
            raise ValueError("ValueError: I/O operation on closed file.")

        while True:
            if (index := self._buffer.find(b"\n")) != -1:
                line = self._buffer[:index].decode("utf-8")
                self._buffer = self._buffer[index + 1 :]
                return line
            
            chunk = os.read(self._fd, self._chunk_size)
            if chunk:
                self._buffer += chunk
            else:
                if self._buffer:
                    line = self._buffer.decode("utf-8")
                    self._buffer = b""
                    return line
                
                raise StopIteration


class Open:
    FLAGS = {
        "r": os.O_RDONLY,
        "w": os.O_WRONLY
    }

    def __init__(self, path: str, *, mode: str="r", chunk_size: int=1024):
        self.path = path
        self.mode = mode
        self.chunk_size = chunk_size
        self._fd = None
        self._stream = None


    def __enter__(self):
        self._fd = os.open(self.path, self.FLAGS[self.mode])

        self._stream = FileStream(
            self._fd,
            chunk_size=self.chunk_size
        )
        return self._stream
    

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._stream:
            self._stream.close()
        return False




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