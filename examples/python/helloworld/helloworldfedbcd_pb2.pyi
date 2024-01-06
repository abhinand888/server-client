from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TrainModelRequest(_message.Message):
    __slots__ = ("features", "label", "weights")
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedScalarFieldContainer[float]
    label: float
    weights: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, features: _Optional[_Iterable[float]] = ..., label: _Optional[float] = ..., weights: _Optional[_Iterable[float]] = ...) -> None: ...

class TrainModelResponse(_message.Message):
    __slots__ = ("loss", "updated_weights")
    LOSS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    loss: float
    updated_weights: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, loss: _Optional[float] = ..., updated_weights: _Optional[_Iterable[float]] = ...) -> None: ...
