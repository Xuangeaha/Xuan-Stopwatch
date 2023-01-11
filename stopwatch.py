print("秒表   版权所有：轩哥啊哈OvO")
print("--------------------------------------------------")

import time

a = int(input("0-->正计时  1-->倒计时: "))

if a == 0:
    while True:
        input("Enter-->开始计时   Ctrl+C-->停止计时")
        starttime = time.time()
        print('计时开始')
        try:
            while True:
                for x in range(1000):
                    print(str(x) + "'")
                    time.sleep(1)
        except KeyboardInterrupt:
            print('计时结束')
            endtime = time.time()
            print('总时间:', round(endtime - starttime, 2),'secs')
            break

elif a == 1:

    tl = int(input("请设置倒计时时间："))
    print("计时开始")
    starttime = time.time()
    try:
        while tl > -1:
            print(str(tl) + "'")
            time.sleep(1)
            tl -= 1
    except KeyboardInterrupt:
        print("计时结束")
        endtime = time.time()
        print('总时间:',round(endtime - starttime,2),'secs')

Stop = input()
