-v0.0.1 审阅脚本在src目录下，所有的作业文件放在judge_files里，不然脚本会识别不到。
因为Python Subprocess多线程模块的特性，导致捕获到的Error具有特殊格式。
在执行自动化审阅时可手动选择是否导出Error。
-v0.2.0 取消Error捕捉，表格可读性显著降低
-v0.4.0 添加了审阅报告自动生成的功能，系统将读取/template下的模板，
非指定模板，可根据个人需要进行更改，但模板中必须包含诸如下列必要关键字
并以双重大括号括起，如：{{report_generate_time}}
关键字列表：
context = {
    'homework_counts':homework_counts,
    'run_success_percent':run_success_percent,
    'performance':performance,
    'success_percent_images':success_percent_images,
    'duplicate_counts':duplicate_counts,
    'duplicate_files':duplicate_files,
    'duplicate_percent':duplicate_percent,
    'duplicate_percent_images':duplicate_percent_images,
    'report_generate_time':report_generate_time
}