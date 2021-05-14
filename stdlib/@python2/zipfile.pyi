import io
import sys
from _typeshed import StrPath
from types import TracebackType
from typing import (
    IO,
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Pattern,
    Protocol,
    Sequence,
    Text,
    Tuple,
    Type,
    Union,
)

_SZI = Union[Text, ZipInfo]
_DT = Tuple[int, int, int, int, int, int]

class BadZipfile(Exception): ...

error = BadZipfile

class LargeZipFile(Exception): ...

class ZipExtFile(io.BufferedIOBase):
    MAX_N: int = ...
    MIN_READ_SIZE: int = ...

    PATTERN: Pattern[str] = ...

    newlines: Optional[List[bytes]]
    mode: str
    name: str
    def __init__(
        self,
        fileobj: IO[bytes],
        mode: str,
        zipinfo: ZipInfo,
        decrypter: Optional[Callable[[Sequence[int]], bytes]] = ...,
        close_fileobj: bool = ...,
    ) -> None: ...
    def read(self, n: Optional[int] = ...) -> bytes: ...
    def readline(self, limit: int = ...) -> bytes: ...  # type: ignore
    def __repr__(self) -> str: ...
    def peek(self, n: int = ...) -> bytes: ...
    def read1(self, n: Optional[int]) -> bytes: ...  # type: ignore

class _Writer(Protocol):
    def write(self, __s: str) -> Any: ...

class ZipFile:
    filename: Optional[Text]
    debug: int
    comment: bytes
    filelist: List[ZipInfo]
    fp: Optional[IO[bytes]]
    NameToInfo: Dict[Text, ZipInfo]
    start_dir: int  # undocumented
    def __init__(
        self, file: Union[StrPath, IO[bytes]], mode: Text = ..., compression: int = ..., allowZip64: bool = ...
    ) -> None: ...
    def __enter__(self) -> ZipFile: ...
    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]
    ) -> None: ...
    def close(self) -> None: ...
    def getinfo(self, name: Text) -> ZipInfo: ...
    def infolist(self) -> List[ZipInfo]: ...
    def namelist(self) -> List[Text]: ...
    def open(self, name: _SZI, mode: Text = ..., pwd: Optional[bytes] = ..., *, force_zip64: bool = ...) -> IO[bytes]: ...
    def extract(self, member: _SZI, path: Optional[StrPath] = ..., pwd: Optional[bytes] = ...) -> str: ...
    def extractall(
        self, path: Optional[StrPath] = ..., members: Optional[Iterable[Text]] = ..., pwd: Optional[bytes] = ...
    ) -> None: ...
    def printdir(self) -> None: ...
    def setpassword(self, pwd: bytes) -> None: ...
    def read(self, name: _SZI, pwd: Optional[bytes] = ...) -> bytes: ...
    def testzip(self) -> Optional[str]: ...
    def write(self, filename: StrPath, arcname: Optional[StrPath] = ..., compress_type: Optional[int] = ...) -> None: ...
    def writestr(self, zinfo_or_arcname: _SZI, bytes: bytes, compress_type: Optional[int] = ...) -> None: ...

class PyZipFile(ZipFile):
    def writepy(self, pathname: Text, basename: Text = ...) -> None: ...

class ZipInfo:
    filename: Text
    date_time: _DT
    compress_type: int
    comment: bytes
    extra: bytes
    create_system: int
    create_version: int
    extract_version: int
    reserved: int
    flag_bits: int
    volume: int
    internal_attr: int
    external_attr: int
    header_offset: int
    CRC: int
    compress_size: int
    file_size: int
    def __init__(self, filename: Optional[Text] = ..., date_time: Optional[_DT] = ...) -> None: ...
    def FileHeader(self, zip64: Optional[bool] = ...) -> bytes: ...

class _PathOpenProtocol(Protocol):
    def __call__(self, mode: str = ..., pwd: Optional[bytes] = ..., *, force_zip64: bool = ...) -> IO[bytes]: ...

def is_zipfile(filename: Union[StrPath, IO[bytes]]) -> bool: ...

ZIP_STORED: int
ZIP_DEFLATED: int
ZIP64_LIMIT: int
ZIP_FILECOUNT_LIMIT: int
ZIP_MAX_COMMENT: int
