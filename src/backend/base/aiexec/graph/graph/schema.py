from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple, Protocol

from typing_extensions import NotRequired, TypedDict

from aiexec.graph.edge.schema import EdgeData
from aiexec.graph.vertex.schema import NodeData

if TYPE_CHECKING:
    from aiexec.graph.schema import ResultData
    from aiexec.graph.vertex.base import Vertex
    from aiexec.schema.log import LoggableType


class ViewPort(TypedDict):
    x: float
    y: float
    zoom: float


class GraphData(TypedDict):
    nodes: list[NodeData]
    edges: list[EdgeData]
    viewport: NotRequired[ViewPort]


class GraphDump(TypedDict, total=False):
    data: GraphData
    is_component: bool
    name: str
    description: str
    endpoint_name: str


class VertexBuildResult(NamedTuple):
    result_dict: ResultData
    params: str
    valid: bool
    artifacts: dict
    vertex: Vertex


class OutputConfigDict(TypedDict):
    cache: bool


class StartConfigDict(TypedDict):
    output: OutputConfigDict


class LogCallbackFunction(Protocol):
    def __call__(self, event_name: str, log: LoggableType) -> None: ...
