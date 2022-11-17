#!/usr/bin/env python
#-*- coding = utf-8 -*-

import sys, os

sdk_env_name = "MY_SDK_PATH"


# # check python version , for kflash not python2 compatable
# check_version = False
# try:
#     if sys.implementation.version.major>=3:
#         check_version = True
# except Exception:
#     pass
# if not check_version:
#     print("Please use python3 to run me!")
#     exit(1)

# get SDK absolute path
sdk_path = os.path.abspath(f"{sys.path[0]}/../../")
try:
    sdk_path = os.environ[sdk_env_name]
except Exception:
    pass
print(f"-- SDK_PATH:{sdk_path}")

# execute project script from SDK
project_file_path = f"{sdk_path}/tools/cmake/project.py"
with open(project_file_path) as f:
    exec(f.read())

