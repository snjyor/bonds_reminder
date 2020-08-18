# bonds_reminder
可转债打新提醒小助手

# 使用方法介绍
1. 根据requirement.txt安装环境所需要的库,命令： pip install -r requirement.txt
2. 修改send_email.py程序里的发送以及接收提醒信息的邮箱地址
2.2修改send_sms.py程序中的相关信息，自行搜索twilio相关使用方法
3. 运行主函数main_bonds.py
4. 若需要线上部署运行程序，可执行start.sh文件，命令：/bin/bash start.sh, 主函数main_bonds.py将在后台执行
5. 查看程序运行状态，命令：ps aux | grep python
6. 查看程序运行输出内容：cat bondreminder.out
