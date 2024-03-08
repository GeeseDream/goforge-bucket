# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import base64
import os
import json

#数据预处理，从当前目录开始，遍历所有文件夹，找到所有的json文件，将json文件中的数据对象提取出来，合并到一个json文件中
def main():
    path = os.getcwd()
    # 创建一个列表
    gpt_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".json") and file != "gptlist.json":
                # 转换为相对路径
                file = os.path.join(root, file)
                icon = os.path.join(root, "icon.png")
                icon_base64 = ""
                if os.path.exists(icon):
                    with open(icon, 'rb') as f:
                        icon_base64 = base64.b64encode(f.read()).decode()
                # 读取json文件
                with open(file, 'r', encoding='utf-8') as f:
                    data = f.read()
                    data = json.loads(data)
                    data['icon'] = icon_base64
                    
                gpt_list.append(data)
    # 输出json文件
    with open("gptlist.json", 'w', encoding='utf-8') as f:
        json.dump(gpt_list, f, ensure_ascii=False, indent=4)    
    
    
if __name__ == '__main__':
    main()