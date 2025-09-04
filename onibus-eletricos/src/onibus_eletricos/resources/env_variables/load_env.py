from dotenv import load_dotenv
import os

def get_proj_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..'))

def solve_env_file(env_file_name='.env', example_file_name='.env.example'):

    root = get_proj_root()
    env_file_path= os.path.join(root, env_file_name)
    env_file_example_path = os.path.join(root, example_file_name)
    if not os.path.exists(env_file_path):
        print(f".env {env_file_name} file not found, creating from {env_file_example_path}")
        with open(env_file_example_path, 'r') as f:
            env_content = f.read()

        with open(env_file_path, 'w') as f:
            f.write(env_content)

    return env_file_path


def load_env_var(varname:str, raise_if_not_found:bool=True) -> str|None:

    env_file_path = solve_env_file()
    load_dotenv(dotenv_path=env_file_path)

    try:
        return os.environ[varname]
    except KeyError:
        if raise_if_not_found:
            raise RuntimeError(f"Environment variable '{varname}' not found.")
        return None
