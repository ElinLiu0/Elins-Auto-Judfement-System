-v0.0.1 审阅脚本在src目录下，所有的作业文件放在judge_files里，不然脚本会识别不到。
因为Python Subprocess多线程模块的特性，导致捕获到的Error具有特殊格式。
在执行自动化审阅时可手动选择是否导出Error。
-v0.2.0 取消Error捕捉，表格可读性显著降低