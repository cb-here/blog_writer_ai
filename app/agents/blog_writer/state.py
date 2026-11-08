from typing import TypedDict, NotRequired

class BlogState(TypedDict):
    topic: str
    title: NotRequired[str]
    content: NotRequired[str]