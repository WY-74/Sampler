import textwrap
import os

mem_args = 'com.wanos.media (pid'
cpu_args = '/com.wanos.media: '
def remove_and_indent(s, char_to_remove):   
    # 去除指定字符
    new_s = s.replace(char_to_remove, '')
    return new_s

def whit_file(filepath):
    meminfo_list=[]
    print("file_name：",filepath)
    with open(filepath,encoding='utf-8') as f:
        for line in f:
            if mem_args in line:
                sp = line.split(':')
                rem1 = remove_and_indent(sp[0], ',')
                rem2 = remove_and_indent(rem1, 'K')
                meminfo_list.append(int(rem2))

    meminfo_set_list=set(meminfo_list)
    print("meminfo-max：",max(meminfo_set_list))
    print("meminfo-min：",min(meminfo_set_list))
    print("meminfo-avg：",sum(meminfo_list)/len(meminfo_list))


    cpuinfo_list=[]
    with open(filepath,encoding='utf-8') as f:
        for line in f:
            if cpu_args in line:
                sp = line.split(' ')
                rem1 = remove_and_indent(sp[2], '%')
                cpuinfo_list.append(float(rem1))
    cpuinfo_set_list=set(cpuinfo_list)

    print("cpu-max：",max(cpuinfo_set_list))
    print("cpu-min：",min(cpuinfo_set_list))
    print("cpu-avg：",sum(cpuinfo_list)/len(cpuinfo_list))

def traverse_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            whit_file(file_path)
        elif os.path.isdir(file_path):
            traverse_files(file_path)


if __name__ == "__main__":
    file_list = "C:/Users/18321/Desktop/银河171/171性能日志/"
    traverse_files(file_list)


class Meminfo:
    pass