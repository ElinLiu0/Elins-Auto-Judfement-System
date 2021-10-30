#Author:Elin  
#Create Time:2021-10-29 23:55:01  
#Last Modified By:Elin  
#Update Time:2021-10-29 23:55:01  
import os
import pandas as pd
from datetime import date, datetime
import subprocess
print("读取文件目录中....")
start_time = datetime.now()
root = os.walk('../judge_files')
files_list = []
for root,dir,files in root:
    files_list.append(files)
run_result = []
judge_time = []
files_info = []
run_output = []
output_withError = input("是否输出运行报错？")
print('审阅中...')
for i in files_list[0]:
    single_files = os.system(f"python ../judge_files/{i}")
    if output_withError == "否":
        output = os.popen(f"python ../judge_files/{i}").readlines()
    if output_withError == '是':
        output = subprocess.Popen(f"python ../judge_files/{i}",stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    run_output.append(output)
    run_result.append(single_files)
    judge_time.append(datetime.now())
    with open(f"../judge_files/{i}","r",encoding='utf-8') as judge_files:
        info = judge_files.read()
        files_info.append(info)
df = pd.DataFrame()
df['文件名'] = files_list[0]
df['运行结果'] = run_result
df['输出内容'] = run_output
df['输出内容'] = df['输出内容'].apply(lambda x:x if x != [] else "输出存在异常！")
df['审阅时间'] = judge_time
df['运行结果'] = df['运行结果'].apply(lambda x:"运行成功" if x == 0 else "运行失败")
df['代码内容'] = files_info
df['是否存在抄袭嫌疑'] = df['代码内容'].duplicated(keep=False).values
df['是否存在抄袭嫌疑'] = df['是否存在抄袭嫌疑'].apply(lambda x:'存在嫌疑' if x == True else '不存在')
df.to_csv(f'../results/审阅结果.csv',index=True)
end_time = datetime.now()
print(f'------------------------------------------------')
print(f'表已导出至同级目录完成！用时：{end_time-start_time}秒')