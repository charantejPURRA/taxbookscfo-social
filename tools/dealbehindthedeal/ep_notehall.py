import json, os
SRC = "/home/claude/deals/notehall.mp4"
VO = "/home/claude/deals/vo/notehall_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP15"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/notehall_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': "Chegg hired both founders. The buyer didn't just get a website. It got the team that built it.",
 'ask': '2009. Season one. D J Stephan and Sean Conway, two college students. Notehall: a marketplace where students buy and sell class notes. They ask for ninety thousand dollars.',
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': "They shake on it. On TV, it's a deal. But weeks after the episode aired, they walked away from it.",
 'exit': 'June 2011. Chegg buys Notehall. According to the S E C filing, three point seven million dollars in equity, plus undisclosed cash.',
 'hook': "They walked away from a Shark's money. Less than two years later, Chegg bought them.",
 'lesson': 'The lesson: a handshake on TV is not a closed deal. Until the papers are signed, both sides can still walk.',
 'math': "Barbara's offer valued Notehall at three hundred sixty thousand dollars. The exit was worth more than ten times that. And they kept the twenty five percent they would have given away.",
 'offers': 'Barbara offers the full ninety thousand... for twenty five percent of the company.'}
COLD_SHOTS = [(20.0, 4.0, 'fit'), (200.0, 4.5, 'fit')]
SHOTS = {'after': [(72.0, 2.5, 'fit'), (116.0, 2.5, 'fit'), (36.0, 2.5, 'fit')],
 'ask': [(16.0, 3.5, 'fit'), (60.0, 2.5, 'fit'), (4.0, 2.5, 'fit'), (20.5, 3.0, 'fit')],
 'cta': [(52.0, 1.5, 'fit'), (164.0, 2.0, 'fit')],
 'deal': [(276.0, 2.5, 'fit'), (268.0, 2.5, 'fit'), (252.0, 2.5, 'fit')],
 'exit': [(64.0, 2.5, 'fit'), (96.0, 2.5, 'fit'), (148.0, 2.5, 'fit')],
 'hook': [(200.0, 2.5, 'fit'), (252.0, 2.5, 'fit'), (152.0, 2.0, 'fit')],
 'lesson': [(248.0, 2.5, 'fit'), (212.0, 2.0, 'fit'), (176.0, 2.0, 'fit')],
 'math': [(128.0, 2.5, 'fit'), (232.0, 2.5, 'fit'), (188.0, 2.5, 'fit')],
 'offers': [(80.0, 3.0, 'fit'), (92.0, 2.5, 'fit'), (168.0, 2.5, 'fit'), (200.0, 3.0, 'fit')]}
CALLOUTS = {'after': [(0.0, 'label', 'WHAT CHEGG BOUGHT'), (0.25, 'big', [('The team.', 'w')]), (0.6, 'sub', [('Both founders hired', 'p')])],
 'ask': [(0.0, 'label', 'THE ASK · 2009 · NOTEHALL'),
         (0.25, 'sub', [('Student class-notes marketplace', 'p')]),
         (0.45, 'big', [('$90K for 10%', 'w')]),
         (0.72, 'card', ('In plain English, the company is worth', [('$900K', 'o')]))],
 'cold': [(0.04, 'label', 'THE ASK, ON THE SHOW'), (0.16, 'line', [('$90K for ', 'w'), ('10%', 'o')]), (0.62, 'slam', [('They shook on 25%.', 'oi')])],
 'cta': [(0.0, 'label', 'BEFORE YOU SIGN A DEAL'), (0.15, 'big', [('Follow the ', 'w'), ('money.', 'oi')])],
 'deal': [(0.0, 'label', 'THE HANDSHAKE'), (0.12, 'big', [('Deal… on TV', 'w')]), (0.55, 'sub', [('Weeks after airing: they walked', 'p')])],
 'exit': [(0.0, 'label', 'JUNE 2011 · CHEGG'), (0.2, 'big', [('$3.7M', 'o')]), (0.55, 'sub', [('In equity, per SEC filing · plus undisclosed cash', 'p')])],
 'hook': [(0.0, 'big', [('Walked away', 'w')]), (0.5, 'card', ('Less than two years later', [('Chegg bought them', 'o')]))],
 'lesson': [(0.0, 'line', [('A handshake is', 'w')]), (0.18, 'line', [('not a ', 'w'), ('closed deal.', 'oi')]), (0.55, 'chips', ["Until it's signed", 'Both sides can walk'])],
 'math': [(0.0, 'label', 'THE MATH'),
          (0.12, 'line', [("Barbara's deal: ", 'w'), ('$360K', 'o')]),
          (0.4, 'line', [('The exit: ', 'w'), ('$3.7M+', 'o')]),
          (0.72, 'slam', [('10x+, and they kept the 25%', 'oi')])],
 'offers': [(0.0, 'label', 'THE OFFERS'), (0.2, 'line', [('Kevin: ', 'w'), ('$90K for 35%', 'o')]), (0.55, 'line', [('Barbara: ', 'w'), ('$90K for 25%', 'o')])]}
