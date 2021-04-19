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

    def setScene(self, sceneName: str, description: str, options: list, hiddenCondition: list = [], actions: dict = {}) -> None:
        self.scene[sceneName] = {
            'description': description,
            'options': options,
            'hiddenCondition': hiddenCondition,
            'actions': {},
        }
    
    def checkUploadSceneFormat(self, scene: dict, complete: bool = False) -> bool:
        formatCondition = ['sceneName', 'description', 'options', 'hiddenCondition', 'actions']
        if not complete:
            formatCondition = formatCondition[:3]
        for fc in formatCondition:
            if not scene.get(fc):
                return False
                break
        else:
            return True
        
    def compareHiddenCondition(self, sceneName: str, actionRecords: list) -> bool:
        hc = self.scene.get(sceneName).get("hiddenCondition")
        if len(actionRecords) >= len(hc):
            return hc == list(reversed(actionRecords[-1:-1-len(hc):-1]))

    # def setSceneByDict(self, scene: dict) -> None:
    #     self.scene[scene.get(sceneName)]

    def getFormatScene(self, sceneName: str, description: str, options: list, hiddenCondition: list=[], actions: dict={}) -> dict:
        return {
            'sceneName': sceneName,
            'description': description,
            'options': options,
            'hiddenCondition': hiddenCondition,
            'actions': actions
        }