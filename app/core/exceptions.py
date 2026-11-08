class AppError(Exception):
    status_code: int = 500
    detail: str = "Something went wrong"

class BlogNotFound(AppError):
    status_code = 404
    detail = "Blog not found"
