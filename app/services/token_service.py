import jwt
import datetime

SECRET_KEY = "your_secret_key"

class TokenService:
    @staticmethod
    def generate_token(request_type: str, user_id: str):
        """Generates a token with request-specific payload."""
        payload = {
            "request_type": request_type,
            "user_id": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token

    @staticmethod
    def validate_token(token: str):
        """Validates and decodes a token."""
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")
