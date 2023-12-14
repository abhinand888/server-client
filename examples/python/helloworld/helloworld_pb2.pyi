from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ArithRequest(_message.Message):
    __slots__ = ("Num1", "Num2", "Id")
    NUM1_FIELD_NUMBER: _ClassVar[int]
    NUM2_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    Num1: int
    Num2: int
    Id: int
    def __init__(self, Num1: _Optional[int] = ..., Num2: _Optional[int] = ..., Id: _Optional[int] = ...) -> None: ...

class ArithReply(_message.Message):
    __slots__ = ("Result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    Result: float
    def __init__(self, Result: _Optional[float] = ...) -> None: ...
