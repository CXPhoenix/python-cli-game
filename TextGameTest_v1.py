from TextGameModule import TextGame

# Game start
# To get user's name, we need to build a welcome scene to do it.
TextGame.clearScreen()
# print('歡迎來到文字遊戲世界')
# name = input('請輸入你的名字: ')
# TextGame.clearScreen()
# print("Hello", name)
# print("遊戲即將開始...")
# TextGame.screenWait(500)
# TextGame.showString('abcdefg')
# input(':')
# # TextGame.showString('hijklmnop', 200)
options = 'test1 test2 test3 test4'.split()
TextGame.userInputOptions(options)


#Game Setting
# tg = TextGame(name)

#開始場景
startScene = ""

#遊戲過程場景
# tg.setScene('front',
#            'test',
#             ['test1','test2','test3'],
#            ['1','2'])
