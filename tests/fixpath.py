import sys
from os.path import dirname, join, normpath

local_tinge_module = normpath(join(dirname(__file__), ".."))
sys.path.insert(0, local_tinge_module)
