from fastapi import HTTPException, status


class ModelDoesNotExists(HTTPException):
    def __init__(self, model, *args, **kwargs):
        message = f"{str(model)} not found"
        super().__init__(status.HTTP_404_NOT_FOUND, message, *args, **kwargs)
