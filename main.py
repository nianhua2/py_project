# Name:         main.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/6 17:22
import pytest
from datetime import datetime

# 时间戳
time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
# pytest.main()
# 筛选出冒烟用例运行
# pytest.main(["-m","smoke"])
# 失败的用例的重运行2次，每次间隔5秒
pytest.main(["-s", "-m", "smoke",
             "--reruns", "2", "--reruns-delay", "5",
             "--junit-xml=OutPuts/reports/" + "auto_" + time_stamp + ".xml",
             "--html=OutPuts/reports/" + "auto_" + time_stamp + ".html",
             "--alluredir=OutPuts/allure_reports"])

'''pytest.main(["-s",
              "--reruns", "2", "--reruns-delay", "5",
             "--junit-xml=OutPuts/reports/"+"auto_"+time_stamp+".xml",
             "--html=OutPuts/reports/"+"auto_"+time_stamp+".html",
              "--alluredir=OutPuts/allure_reports"])'''
