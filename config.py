import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://karthik1:Info123tech@localhost:5433/realoneinvest")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Prevents warning logs
