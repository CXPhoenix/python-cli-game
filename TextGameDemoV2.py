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
    
    print("操作選項")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choice = input(': ')
    clearScene()
    return choice

def getNewScene(nowScene: str, choice: str, options: list, move: dict):
    try:
        choice = int(choice)-1
        scene = move.get(options[choice])
        
        return scene
    except (ValueError, IndexError):
        showWrongOption()
        return nowScene

def showDesc(description: str, timeSet: float = 0.05):
    show = ""
    timer = int(timeSet*1000)
    if timer != 0:
        timer = 0.001 if timeSet < 0.001 else timeSet
        for string in description:
            clearScene()
            show += string
            print(show)
            # time.sleep(timer)
    else:
        print(description)

#def showDesc(description: str):
#    for string in description:
#        ended = '' if description.index(string) != len(description)-1 else "\n"
#        print(string, end='')
#        time.sleep(0.1)

def showWrongOption():
    print('Not a smart option..')
    input(':enter')
    clearScene()

#start
#為了使用者名字，因此得先初始化
clearScene()
print('歡迎來到文字遊戲世界')
name = input('請輸入你的名字： ')
for i in range(3):
    clearScene()
    print(f"Hello，{name}\n遊戲即將開始{'.'*(i+1)}!")
    # time.sleep(1)
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
        'move': {
            '查看信': 'mail',
            '查看抽屜': 'drawer',
            '向左轉': 'lefthand',
            '向右轉': 'righthand',
        },
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
        'options': "把信放回桌上".split(),
        'move': {
            "把信放回桌上": "forward"
        },
    },
    'drawer': {
        'description': "打開抽屜後，空無一物，空氣中瀰漫著嘲笑你的聲音",
        'options': "平靜地關閉抽屜 憤怒地關上抽屜".split(),
        'move': {
            '平靜地關閉抽屜': 'forward',
            '憤怒地關上抽屜': 'forward',
        },
    },

    'tableText': {
        'description': "信風吹盡日，\n山中人歸心。\n壺中有高樓，\n飄蓬萊密林，\n千年未央碼。",
        'options': "查看完畢".split(),
        'move': {
            '查看完畢': 'forward',
        },
    },

    #lefthand scene
    'lefthand': {
        'description': '就只是一面牆',
        'options': "向左轉 向右轉".split(),
        'move': {
            '向左轉': 'backward',
            '向右轉': 'forward',
        },
    },

    #righthand scene
    'righthand': {
        'description': '就只是一面牆',
        'options': "向左轉 向右轉".split(),
        'move': {
            '向左轉': 'forward',
            '向右轉': 'backward',
        },
    },

    #backward scene
    'backward': {
        'description': '有一到門，門旁邊有一個密碼鎖',
        'options': "使用密碼鎖 向左轉 向右轉".split(),
        'move': {
            '使用密碼鎖': 'lock',
            '向左轉': 'righthand',
            '向右轉': 'lefthand',
        },
    },

    'lock': {
        'description': '看起來是要輸入六位數字的密碼',
        'options': '輸入密碼 向後退'.split(),
        'move': {
            '輸入密碼': 'lockInput',
            '向後退': 'backward',
        },
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
    if scene.get(nowScene).get('readed') or nowScene == 'mail':
        showDesc(scene.get(nowScene).get('description'), 0)
    else:
        showDesc(scene.get(nowScene).get('description'))
        scene.get(nowScene)['readed'] = True
    if nowScene == 'lockInput':
        lockpw = input(': ')
    else:
        print()
        choice = getChoice(scene.get(nowScene).get('options'))

    #scene options rebuild
    
    #lockInput scene options
    if nowScene == 'lockInput':
        if len(lockpw) != 6:
            clearScene()
            print('Not good passwords..')
            input(':enter')
            nowScene = 'lock'
        elif lockpw == '487919':
            nowScene = 'GetOut'
        else:
            clearScene()
            print('wrong passwords..')
            input(':enter')
            nowScene = 'lock'
        clearScene()
    
    #drawer scene options
    elif nowScene == 'drawer':
        nowScene = getNewScene(nowScene, choice, scene.get(nowScene).get("options"), scene.get(nowScene).get("move"))
        scene.get('drawer')['hiddenCondition'] = scene.get('drawer').get('hiddenCondition') + choice + ' ' if scene.get('drawer').get('hiddenCondition') else choice + ' '
        
        if scene.get('drawer').get('hiddenCondition'):
            hiddenCondition = scene.get('drawer').get('hiddenCondition').split()
            if len(hiddenCondition) >= 2:
                if hiddenCondition[-2:len(hiddenCondition)] == ['1', '2']:
                    scene.get('forward')['description'] = "一張桌子，上面放著一張紙條，似乎還有一個抽屜\n桌子上好像有一段模糊的文字顯示出來..." 
                    scene.get('forward')['options'] = "查看信 查看抽屜 向左轉 向右轉 查看桌上顯示的字".split()
                    scene.get('forward')['move']['查看桌上顯示的字'] = 'tableText'
    
    else:
        nowScene = getNewScene(nowScene, choice, scene.get(nowScene).get("options"), scene.get(nowScene).get("move"))
    

#end scene
for s in endScene:
    showDesc(s)
    input('\n:enter')
    clearScene()

showDesc('The end..')
input(':enter for end..')