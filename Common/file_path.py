# Name:         file_path.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/3 19:23
import os

# 获得项目根路径
BAS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取OutPuts目录路径
OUTPUTS_DIR = os.path.join(BAS_DIR, "OUTPuts")
# 获取OutPuts目录下logs目录路径
LOGS_DIR = os.path.join(OUTPUTS_DIR, "logs")
# 获取OutPuts目录下picture目录路径
PICTURE_DIR = os.path.join(OUTPUTS_DIR, "picture")
# 获取OutPuts目录下reports目录路径
REPORTS_DIR = os.path.join(OUTPUTS_DIR, "reports")

# 获取TestCases目录路径
TESTCASES_DIR = os.path.join(BAS_DIR, "TestCases")

# 获取TestDatas目录路径
TESTDATAS_DIR = os.path.join(BAS_DIR, "TestDatas")


