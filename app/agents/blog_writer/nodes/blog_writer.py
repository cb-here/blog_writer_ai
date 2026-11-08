from ..state import BlogState
from app.llm import get_llm
from langchain_core.messages import SystemMessage, HumanMessage
from ..prompt import SYSTEM_PROMPT
from app.schemas.blog import Blog

async def blog_writer(state: BlogState): 
    llm = get_llm()

    topic = state["topic"]

    messages = [SystemMessage(content=SYSTEM_PROMPT), HumanMessage(content=topic)]

    response = await llm.with_structured_output(Blog).ainvoke(messages)

    return {
        "title": response.title, 
        "content": response.content
    }