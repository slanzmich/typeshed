import os
import sys
from typing import Any, BinaryIO, Callable, List, Optional, Protocol, Text, Union, overload

class _ReadableBinary(Protocol):
    def tell(self) -> int: ...
    def read(self, size: int) -> bytes: ...
    def seek(self, offset: int) -> Any: ...

_File = Union[Text, _ReadableBinary]

@overload
def what(file: _File, h: None = ...) -> Optional[str]: ...
@overload
def what(file: Any, h: bytes) -> Optional[str]: ...

tests: List[Callable[[bytes, Optional[BinaryIO]], Optional[str]]]
