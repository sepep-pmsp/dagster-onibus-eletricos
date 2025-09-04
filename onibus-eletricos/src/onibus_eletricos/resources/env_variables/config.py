from .load_env import load_env_var, get_proj_root

PROJ_ROOT=get_proj_root()
OLHO_VIVO_TOKEN=load_env_var("OLHO_VIVO_TOKEN", raise_if_not_found=True)
LOCALHOST_DATAFOLDER=load_env_var("LOCALHOST_DATAFOLDER", raise_if_not_found=True)
