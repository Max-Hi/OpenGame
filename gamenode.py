from typing import Dict
import logging

from worldstate import Worldstate
from condition import Condition
from randomEvent import RandomEvent


# Base GameNode class
class GameNode:
    def __init__(self, id: str, nodes: Dict[str, 'GameNode'], text: str) -> None:
        self.id = id
        self.nodes: Dict[str, GameNode] = nodes
        self.text: str = text

    def add_node(self, option_text: str, node: 'GameNode') -> None:
        if option_text in self.nodes:
            logging.warning(f"Attempt to add a node with an existing key: {option_text}")
        else:
            self.nodes[option_text] = node
    
    def save_to_file(self) -> None:
        pass #TODO

class ConditionalGameNode(GameNode):
    def __init__(self, id: str, nodes: Dict[str, 'GameNode'], text: str, condition: Condition) -> None:
        super().__init__(id, nodes, text)
        self.condition: Condition = condition

class RandomGameaenode(GameNode):
    def __init__(self, id: str, nodes: Dict[str, 'GameNode'], text: str , randomEvent: RandomEvent) -> None:
        super().__init__(id, nodes, text)
        self.randomEvent :  RandomEvent = randomEvent

class OpenConversationGameNode(GameNode):
    def __init__(self, id: str, nodes: Dict[str, 'GameNode'], text: str, characterID: str) -> None:
        super().__init__(id, nodes, text)
        self.characterID: str = characterID
        