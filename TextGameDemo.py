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
    
def getChoice(options: list):
    """
    Only for Windows and MacOS
    """
    # showOptions = '\n'.join(options)
    # print(showOptions)
    print("操作選項")
    for i in range(len(options)):
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

def showWrongOption():
    print('Not a smart option..')
    input(':enter')

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
scene = {
    #forward scene
    'forward': {
        'description': "一張桌子，上面放著一張紙條，似乎還有一個抽屜",
        'options': "查看信 查看抽屜 向左轉 向右轉".split(),
    },
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

    #lefthand scene
    'lefthand': {
        'description': '就只是一面牆',
        'options': "向左轉 向右轉".split(),
    },

    #righthand scene
    'righthand': {
        'description': '就只是一面牆',
        'options': "向左轉 向右轉".split(),
    },

    #backward scene
    'backward': {
        'description': '有一到門，門旁邊有一個密碼鎖',
        'options': "使用密碼鎖 向左轉 向右轉".split(),
    },

    'lock': {
        'description': '看起來是要輸入六位數字的密碼',
        'options': '輸入密碼 向後退'.split()
    },

    'lockInput': {
        'description': '輸入六位數字的密碼',
    },
}

endScene = [
    "你成功的脫逃出這個奇怪的密室逃脫...",
    "但是你有一種預感",
    "這一切都還沒結束",
    "......",
    "阿，還有資科課要過啦..."
]

#game start

for s in startScene:
    showDesc(s)
    input('\n:enter')
    clearScene()

#set var nowScene
nowScene = 'forward'

#game choice
while nowScene != 'GetOut':
    showDesc(scene.get(nowScene).get('description'))
    if nowScene == 'lockInput':
        lockpw = input(': ')
    else:
        choice = getChoice(scene.get(nowScene).get('options'))

    #forward scene options
    if nowScene == 'forward':
        if choice == '1':
            nowScene = 'mail'
        elif choice == '2':
            nowScene = 'drawer'
        elif choice == '3':
            nowScene = 'lefthand'
        elif choice == '4':
            nowScene = 'righthand'
        else:
            showWrongOption()
    
    #mail scene options
    elif nowScene == 'mail':
        if choice == '1':
            nowScene = 'forward'
        else:
            showWrongOption()
    
    #drawer scene options
    elif nowScene == 'drawer':
        if choice == '1' or choice == '2':
            nowScene = 'forward'
        else:
            showWrongOption()
    
    #lefthand scene options
    elif nowScene == 'lefthand':
        if choice == '1':
            nowScene = 'backward'
        elif choice == '2':
            nowScene = 'forward'
        else:
            showWrongOption()
    
    #righthand scene options
    elif nowScene == 'righthand':
        if choice == '1':
            nowScene = 'forward'
        elif choice == '2':
            nowScene = 'backward'
        else:
            showWrongOption()

    #backward scene options
    elif nowScene == 'backward':
        if choice == '1':
            nowScene = 'lock'
        elif choice == '2':
            nowScene = 'righthand'
        elif choice == '3':
            nowScene = 'lefthand'
        else:
            showWrongOption()
    
    #lock scene options
    elif nowScene == 'lock':
        if choice == '1':
            nowScene = 'lockInput'
        elif choice == '2':
            nowScene = 'backward'
        else:
            showWrongOption()

    #lockInput scene options
    elif nowScene == 'lockInput':
        if len(lockpw) != 6:
            print('Not good passwords..')
            input(':enter')
            nowScene = 'lock'
        elif lockpw == '487919':
            nowScene = 'GetOut'
        else:
            print('wrong passwords..')
            input(':enter')
            nowScene = 'lock'

#end scene
for s in endScene:
    showDesc(s)
    input('\n:enter')
    clearScene()

showDesc('The end..')
input(':enter for end..')