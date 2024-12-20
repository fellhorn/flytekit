import json
from typing import Any, Dict

from flyteidl.core import types_pb2 as _types_pb2
from google.protobuf import json_format as _json_format
from google.protobuf import struct_pb2 as _struct


class TypeAnnotation:
    """Python class representation of the flyteidl TypeAnnotation message."""

    def __init__(self, annotations: Dict[str, Any]):
        self._annotations = annotations

    @property
    def annotations(self) -> Dict[str, Any]:
        """
        :rtype: dict[str, Any]
        """
        return self._annotations

    def to_flyte_idl(self) -> _types_pb2.TypeAnnotation:
        """
        :rtype: flyteidl.core.types_pb2.TypeAnnotation
        """

        if self._annotations is not None:
            annotations = _json_format.Parse(json.dumps(self.annotations), _struct.Struct())
        else:
            annotations = None

        return _types_pb2.TypeAnnotation(
            annotations=annotations,
        )

    @classmethod
    def from_flyte_idl(cls, proto):
        """
        :param flyteidl.core.types_pb2.TypeAnnotation proto:
        :rtype: TypeAnnotation
        """

        return cls(annotations=_json_format.MessageToDict(proto.annotations))

    @classmethod
    def merge_annotations(cls, annotation: "TypeAnnotation", other_annotation: "TypeAnnotation") -> "TypeAnnotation":
        """
        Merges two annotations together. If the same key exists in both annotations, the value in the other annotation
        will be used.
        :param TypeAnnotation annotation: The first annotation
        :param TypeAnnotation other_annotation: The second annotation
        :rtype: TypeAnnotation
        """
        merged_annotations = annotation.annotations.copy()
        merged_annotations.update(other_annotation.annotations)
        return cls(annotations=merged_annotations)

    def __eq__(self, x: object) -> bool:
        if not isinstance(x, self.__class__):
            return False
        return self.annotations == x.annotations
