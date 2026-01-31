from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.core.config import settings


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 30


def hash_password(password: str) -> str:
    """
    Hash a plain password using bcrypt.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a stored hash.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(subject: str) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=ACCES_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": subject,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=ALGORITHM
    )

    return token
