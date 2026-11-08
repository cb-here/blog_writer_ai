from fastapi import Request

def get_writer(request: Request):
    return request.app.state.writer