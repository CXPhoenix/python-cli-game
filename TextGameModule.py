"""
這是 Text Game 的教學用模組
"""
import os
import sys
import time


class TextGame:
    def __init__(self, playerName: str='player'):
        self.playerName = playerName
        self.scene = {}
        self.clearCmd = ''
        self.playerRecord = {}

        # detect system
        if sys.platform.startswith('win32'):
            self.clearCmd = 'cls'
        elif sys.platform.startswith('darwin'):
            self.clearCmd = 'clear'
        else:
            raise Exception('This game just support Windows and MacOS system..')
    
    """ about scene
        Scene's format:
        scene = {
            sceneName:{
                description -> str,
                options -> str-list,
                hiddenCondition -> list,
                actions -> dict : {
                    option -> str : go_to_scene -> str
                }
            },
            ...
        }
    """
    def setScene(self, sceneName: str, description: str, options: list, hiddenCondition: list=[]) -> None:
        self.scene[sceneName] = {
            'description': description,
            'options': options,
            'hiddenCondition': hiddenCondition,
            'actions': {},
        }
    
    def setMultiScenesByList(self, multiScene: list) -> None:
        for ms in multiScene:
            self.scene[ms.get('sceneName')] = {
                'description': ms.get('description'),
                'options': ms.get('options',[]),
                'hiddenCondition': ms.get('hiddenCondition',[]),
                'actions': ms.get('actions',{}),
            }
            
    def setMultiScenesByDict(self, multiScene: dict) -> None:
        self.scene.update(multiScene)
    
    def getFormatScene(self, sceneName: str, description: str, options: list, hiddenCondition: list=[], actions: dict={}) -> dict:
        return {
            'sceneName': sceneName,
            'description': description,
            'options': options,
            'hiddenCondition': hiddenCondition,
            'actions': actions
        }
    
    def getFormatMultiScene(self, *formatScene: dict) -> dict:
        scene = {}
        for fs in formatScene:
            if fs.get('sceneName'):
                scene.update({
                    fs.get('sceneName'):{
                        'desciption': fs.get('description', ''),
                        'options': fs.get('options', []),
                        'hiddenCondition': fs.get('hiddenCondition', []),
                        'actions': fs.get('actions', {}),
                    }
                })
        return scene

    def getSceneInfo(self, sceneName: str) -> dict:
        return self.scene.get(sceneName, {})
    
    def getAllScenesName(self) -> list:
        return [name for name in self.scene]
    
    def setOptionAction(self, sceneName: str, option: str, action: str) -> None:
        if self.scene.get(action):
            self.scene[sceneName]['actions'].update({option:action})
    
    def setOptionActions(self, sceneName: str, optionActions: dict) -> None:
        self.scenen[sceneName].update(optionActions)
    
    def getSceneOptions(self, sceneName: str) -> list:
        return self.scene.get(sceneName).get('options')
    
    def getSceneOptionAction(self, sceneName: str, option: str) -> str:
        return self.scene.get(sceneName).get('actions', lambda: [_ for _ in ()].throw(Exception(f"The scene {sceneName} no actions detail.."))).get(option)
    
    """ about screen """
    def clearScreen(self) -> None:
        os.system(self.clearCmd)
    
    """ about player"""
    def setPlayerName(self, playerName: str) -> None:
        self.playerName = playerName
    
    def getPlayerName(self) -> str:
        return self.playerName
    
    def setPlayerActionRecord(self, sceneName: str, action: str):
        self.playerRecord[sceneName]