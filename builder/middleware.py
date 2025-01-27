class CustomSecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Add or adjust security headers
        response["Content-Security-Policy"] = "frame-ancestors 'self' http://localhost:8000"
        response["X-Frame-Options"] = "ALLOW-FROM http://localhost:8000"
        
        return response