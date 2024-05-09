import os


# Try to get the environment variable
def get_env_variable(key: str) -> str:
    try:
        return os.environ.get(key)
    except KeyError:
        raise KeyError(f"Environment variable {key} not found")
