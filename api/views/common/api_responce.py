from rest_framework.response import Response


class ApiResponce(Response):
    
    def __init__(
        serializer=None, status=None, headers=None, 
        exception=False, content_type=None
    ):
        
        super().__init__(
            data=serializer.data, status=status, 
            headers=headers, exception=exception, content_type=content_type
        )