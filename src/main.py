# Author:Elin
# Create Time:2021-10-29 23:55:01
# Last Modified By:Elin
# Update Time:2021-10-29 23:55:01
# -*- coding: utf-8 -*-
import os
import pandas as pd
from datetime import date, datetime
import subprocess
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
import plotly as py
import plotly.graph_objs as go
print("读取文件目录中....")
doc = DocxTemplate('../template/审阅报告模板.docx')
start_time = datetime.now()
root = os.walk('../judge_files')
files_list = []
for root, dir, files in root:
    files_list.append(files)
run_result = []
judge_time = []
files_info = []
run_output = []
print('审阅中...')
for i in files_list[0]:
    single_files = os.system(f"python ../judge_files/{i}")
    output = os.popen(f"python ../judge_files/{i}").readlines()
    run_output.append(output)
    run_result.append(single_files)
    judge_time.append(datetime.now())
    with open(f"../judge_files/{i}", "r", encoding='utf-8') as judge_files:
        info = judge_files.read()
        files_info.append(info)
df = pd.DataFrame()
df['文件名'] = files_list[0]
df['运行结果'] = run_result
df['输出内容'] = run_output
df['输出内容'] = df['输出内容'].apply(lambda x: x if x != [] else "输出存在异常！")
df['审阅时间'] = judge_time
df['运行结果'] = df['运行结果'].apply(lambda x: "运行成功" if x == 0 else "运行失败")
df['代码内容'] = files_info
df['是否存在抄袭嫌疑'] = df['代码内容'].duplicated(keep=False).values
df['是否存在抄袭嫌疑'] = df['是否存在抄袭嫌疑'].apply(lambda x: '存在嫌疑' if x == True else '不存在')
df.to_csv(f'../results/审阅结果.csv', index=True)
homework_counts = df.shape[0]
run_success_percent = float(
    df[df['运行结果'] == "运行成功"].shape[0] / df.shape[0] * 100)
if run_success_percent >= 60:
    performance = "良好"
else:
    performance = "欠佳"
labels = df["运行结果"].groupby(df["运行结果"]).count().index.tolist()
values = df["运行结果"].groupby(df["运行结果"]).count().values.tolist()
trace = [go.Pie(
    labels=labels,
    values=values,
    hole=0.7,
    hoverinfo="label + value")]
layout = go.Layout(
    title="当前作业完成率",
    title_x=0.5
)
fig = go.Figure(data=trace, layout=layout)
fig.write_image('../images/success_percent_images.jpeg')
success_percent_images = InlineImage(
    doc, '../images/success_percent_images.jpeg', Cm(15))
duplicate_counts = df[df['是否存在抄袭嫌疑'] == "存在嫌疑"].shape[0]
duplicate_files = df[df['是否存在抄袭嫌疑'] == "存在嫌疑"]['文件名']
duplicate_percent = float(len(duplicate_files) / df.shape[0] * 100)
labels2 = df["是否存在抄袭嫌疑"].groupby(df["是否存在抄袭嫌疑"]).count().index.tolist()
values2 = df["是否存在抄袭嫌疑"].groupby(df["是否存在抄袭嫌疑"]).count().values.tolist()
trace2 = [go.Pie(
    labels=labels2,
    values=values2,
    hole=0.7,
    hoverinfo="label + value")]
layout2 = go.Layout(
    title="当前作业抄袭嫌疑占比图表",
    title_x=0.5
)
fig2 = go.Figure(data=trace2, layout=layout2)
fig2.write_image('../images/duplicate_percent_images.jpeg')
duplicate_percent_images = InlineImage(
    doc, '../images/duplicate_percent_images.jpeg', Cm(15))
report_generate_time = str(datetime.now())
context = {
    'homework_counts': str(homework_counts) + '%',
    'run_success_percent': run_success_percent,
    'performance': performance,
    'success_percent_images': success_percent_images,
    'duplicate_counts': duplicate_counts,
    'duplicate_files': duplicate_files,
    'duplicate_percent': duplicate_percent,
    'duplicate_percent_images': duplicate_percent_images,
    'report_generate_time': report_generate_time
}

doc.render(context=context)
doc.save('../results/审阅报告.docx')
end_time = datetime.now()
print(f'------------------------------------------------')
print(f'结果和报告已导出至/results目录下！用时：{end_time-start_time}秒')
