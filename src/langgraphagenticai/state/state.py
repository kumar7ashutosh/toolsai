from pydantic import BaseModel,Field
from typing_extensions import Annotated,List,Sequence,TypedDict
from langgraph.graph.message import add_messages,BaseMessage

class State(TypedDict):
    """Represent the structure of state used in graph"""
    messages:Annotated[list,add_messages]
    