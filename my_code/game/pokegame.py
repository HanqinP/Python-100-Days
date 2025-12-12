from enum import Enum
import random

class Suite(Enum):
    """花色（枚举）"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

class Card:
    """牌"""
    
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8',
        '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'
    
    def __lt__(self, other: Card ):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value


class Poker:
    """扑克"""

    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite 
                                        for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card
    
    @property
    def has_next(self):
        """是否还有牌"""
        return self.current < len(self.cards)
    
class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def receive(self, card):
        """接收牌"""
        self.cards.append(card)
    
    def arrange(self):
        """整理牌"""
        self.cards.sort(key=lambda card: (card.suite.value, card.face))

    
poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
# 将牌轮流发到每个玩家手上每人13张牌
for _ in range(13):
    for player in players:
        player.receive(poker.deal())
# 玩家整理手上的牌输出名字和手牌
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)