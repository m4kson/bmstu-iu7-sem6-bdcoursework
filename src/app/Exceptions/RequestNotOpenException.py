class RequestNotOpenError(Exception):
    def __init__(self, request_id: int):
        self.request_id = request_id
        self.message = f"Service request with id {request_id} is not open"
        super().__init__(self.message)