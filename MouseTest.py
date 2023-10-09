import pyautogui
import time
import threading

# async def delayed_operation(x,y,s):
#     pyautogui.moveTo(x,y,s) #鼠标移动到(x,y)并保持s秒，同理还有拖动方法dragTo(x,y,s)
#     pyautogui.click(x,y) #鼠标点击(x,y)     
#     # 等待2秒
#     await asyncio.sleep(2)
#     # 在等待后执行的操作
#     print("等待结束，执行操作")


def ue_capturemanagercall():
    # 在新线程中执行的代码
    print("这是新线程")
    # x=239
    # y=11
    # s=0
    # delayed_click(x=x,y=y,s=s)
    # x=335
    # y=222
    # delayed_click(x=x,y=y,s=s)

    img_dir = 'F:/MyCode/UnrealEngine/PythonMetahuman/'

    pqd = pyautogui.locateCenterOnScreen(img_dir+'tools.png', confidence=0.9)
    print(pqd)
    if pqd:
        pyautogui.click(*pqd)
        pyautogui.sleep(1)

    pqd = pyautogui.locateCenterOnScreen(img_dir+'capturemanager.png', confidence=0.9)
    print(pqd)
    if pqd:
        pyautogui.click(*pqd)
        pyautogui.sleep(1)
    
    pqd = pyautogui.locateCenterOnScreen(img_dir+'mycs.png', confidence=0.9)
    print(pqd)
    if pqd:
        pyautogui.click(*pqd)
        pyautogui.sleep(1)

    pqd = pyautogui.locateCenterOnScreen(img_dir+'myslate.png', confidence=0.9)
    print(pqd)
    if pqd:
        pyautogui.click(*pqd)
        pyautogui.sleep(1)
    else:
        pqd = pyautogui.locateCenterOnScreen(img_dir+'mycs.png', confidence=0.9)
        print(pqd)
        if pqd:
            pyautogui.click(*pqd)
            pyautogui.sleep(1)
        pqd = pyautogui.locateCenterOnScreen(img_dir+'myslate.png', confidence=0.9)
        print(pqd)
        if pqd:
            pyautogui.click(*pqd)
            pyautogui.sleep(1)

    pqd = pyautogui.locateCenterOnScreen(img_dir+'addtoqueue.png', confidence=0.9)
    print(pqd)
    if pqd:
        pyautogui.click(*pqd)
        pyautogui.sleep(1)
    
    pqd = pyautogui.locateCenterOnScreen(img_dir+'importall.png', confidence=0.9)
    print(pqd)
    if pqd:
        pyautogui.click(*pqd)
        pyautogui.sleep(2)
    
    pqd = pyautogui.locateCenterOnScreen(img_dir+'importallyes.png', confidence=0.9)
    print(pqd)
    if pqd:
        pyautogui.click(*pqd)
        pyautogui.sleep(1)




def delayed_click(x,y,s):
    pyautogui.moveTo(x,y,s) #鼠标移动到(x,y)并保持s秒，同理还有拖动方法dragTo(x,y,s)
    pyautogui.click(None,None) #鼠标点击(x,y)     
    # 等待2秒
    pyautogui.sleep(2)
    # 在等待后执行的操作
    print("等待结束，执行操作")

if __name__ == '__main__':

    # 打开CaptureManager
    # x=335
    # y=222
    # s=0.1
    # asyncio.run(delayed_operation(x=x,y=y,s=s))

    # x=239
    # y=11
    # s=0
    # delayed_click(x=x,y=y,s=s)
    # x=335
    # y=222
    # delayed_click(x=x,y=y,s=s)

    # pqd = pyautogui.locateCenterOnScreen('2.png', confidence=0.9)
    # print(pqd)
    # pyautogui.click(*pqd)


    # x=558
    # y=44
    # s=0.1
    # pydirectinput.moveTo(x,y,s)
    # pydirectinput.click(None,None)
    # time.sleep(2)
    # x=345
    # y=40
    # pydirectinput.moveTo(x,y,s)
    # pydirectinput.click(None,None)

    # 创建并启动新线程
    my_thread = threading.Thread(target=ue_capturemanagercall)
    my_thread.start()

    # # 等待线程执行结束
    # my_thread.join()

    # 在主线程中执行的代码
    print("这是主线程")
    


