"""
轩氏秒表 Xuan-StopWatch
Copyright (c) 2022-2023 轩哥啊哈OvO
"""

import time

select = int(input("0-->正计时  1-->倒计时: "))

if select == 0:
    while True:
        input("Enter-->开始计时   Ctrl+C-->停止计时")
        start_time = time.time()
        print('计时开始')
        tick = 0

        try:
            while True:
                print(str(tick) + "'")
                time.sleep(1)
                tick += 1

        except KeyboardInterrupt:
            end_time = time.time()
            print("计时结束")
            print("总时间：", round(end_time - start_time, 2), "'")
            break

elif select == 1:
    tick = int(input("请设置倒计时时间："))
    print("计时开始")
    while True:
        print(str(tick) + "'")
        time.sleep(1)
        tick -= 1
        if tick == 0:
            print("计时结束")
            break
