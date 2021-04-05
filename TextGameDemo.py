import os
import sys
import time
def clearScene():
    if sys.platform.startswith('win32'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    else:
        raise Exception('This game just support Windows and MacOS system..')
    
def choice(options: list):
    """
    Only for Windows and MacOS
    """
    # showOptions = '\n'.join(options)
    # print(showOptions)
    print("操作選項")
    for i in range(len(optinos)):
        print(f"{i+1}. {options[i]}")
    choice = input(': ')
    clearScene()
    return choice

def showDesc(description: str):
    show = ""
    for string in description:
        clearScene()
        show += string
        print(show)
        time.sleep(0.1)

#start
#為了使用者名字，因此得先初始化
clearScene()
print('歡迎來到文字遊戲世界')
name = input('請輸入你的名字： ')
for i in range(3):
    clearScene()
    print(f"Hello，{name}\n遊戲即將開始{'.'*(i+1)}!")
    time.sleep(1)
clearScene()


#set scene
startScene = ["你醒來在一個房間中，房間非常狹小，除了一張桌子、一個通往外面的門外，沒有其他東西。",
              "桌子上面留有一封信給你",
              "門旁邊有數字按鈕鎖",
              "似乎你在一個...密室逃脫？"]
forward = {
    'description': "一張桌子，上面放著一張紙條，似乎還有一個抽屜",
    'options': "查看信 查看抽屜 向左轉 向右轉".split(),
    'mail': {
        'description': 
            f"""你好 {name}，
    歡迎來到文字型密室脫逃遊戲中。

    似乎你已經被困在這個狹小的房間中，
    巴不得趕快離開吧？
    其實呢，要離開這裡非常簡單，
    就是破解密碼而已，
    一旦破解成功，
    就直接逃出去了。

    祝福你  逃出升天！

        Best regards, 
            把你抓進來的人""",
            'options': "把信放回桌上".split()
    },
    'drawer': {
        'description': "打開抽屜後，空無一物，空氣中瀰漫著嘲笑你的聲音",
        'options': "平靜地關閉抽屜 憤怒地關上抽屜".split(),
    },
}

lefthand = None
righthand = None
backward = None




# for s in startScene:
#     showDesc(s)
#     input('\n:next')
#     clearScene()
    
showDesc(forward.get('mail').get('description'))

