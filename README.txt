- v0.0.1 审阅脚本在src目录下，所有的作业文件放在judge_files里，不然脚本会识别不到。
因为Python Subprocess多线程模块的特性，导致捕获到的Error具有特殊格式。
在执行自动化审阅时可手动选择是否导出Error。
- v0.2.0 取消Error捕捉，表格可读性显著降低
- v0.4.0 添加了审阅报告自动生成的功能，系统将读取/template下的模板，
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
- v0. 0.1 the review script is in the SRC directory, and all job files are placed in judge_ Files, otherwise the script won't recognize it.
Due to the characteristics of Python subprocess multithreading module, the captured error has a special format.
You can manually select whether to export error when performing automated review.

- v0. 2.0 cancel error capture, and the readability of the table is significantly reduced

- v0. 4.0 adds the function of automatically generating review reports. The system will read the templates under / template,

The template is not specified and can be changed according to individual needs, but the template must contain necessary keywords such as the following

And enclosed in double braces, such as: {{report_generate_time}}

Keyword list:

context = {

'homework_ counts':homework_ counts,

'run_ success_ percent':run_ success_ percent,

'performance':performance,

'success_ percent_ images':success_ percent_ images,

'duplicate_ counts':duplicate_ counts,

'duplicate_ files':duplicate_ files,

'duplicate_ percent':duplicate_ percent,

'duplicate_ percent_ images':duplicate_ percent_ images,

'report_ generate_ time':report_ generate_ time

}
