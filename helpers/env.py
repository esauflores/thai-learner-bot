import os
from dotenv import load_dotenv


# Try to get the environment variable
def get_env_variable(key: str) -> str:
    load_dotenv()

    try:
        return os.environ.get(key)
    except KeyError:
        raise KeyError(f"Environment variable {key} not found")
