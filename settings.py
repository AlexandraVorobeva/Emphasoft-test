from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8060




settings = Settings(

    _env_file_encoding='utf-8',
)

jwt_secret = 'o9A-elwuIGHLAPu20Qz94AKzJpEad5U_u3HWIYXiOmU'
jwt_algorithm = 'HS256'
jwt_expiration = 3600