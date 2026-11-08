from langgraph.graph import START, END, StateGraph
from .state import BlogState
from .nodes import blog_writer
from langgraph.checkpoint.base import BaseCheckpointSaver

def build_graph(checkpointer: BaseCheckpointSaver):
    graph = StateGraph(BlogState)

    graph.add_node("blog_writer", blog_writer)

    graph.add_edge(START, "blog_writer")
    graph.add_edge("blog_writer", END)

    return graph.compile(checkpointer=checkpointer)