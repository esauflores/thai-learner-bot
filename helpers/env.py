import os


# use file .env to read environment variables
def env_variable(key: str, root_path: str = ".") -> str:
    with open(os.path.join(root_path, ".env"), "r") as file:
        for line in file:
            if line.startswith(key):
                return line.split("=")[1].strip()
    return ""
