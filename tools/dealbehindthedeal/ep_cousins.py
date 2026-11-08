import json, os
SRC = "/home/claude/deals/cousins.mp4"
VO = "/home/claude/deals/vo/cousins_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP20"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/cousins_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': "Now it's more than eighty food trucks in over thirty states, plus restaurants. And Barbara is still in.",
 'ask': '2012. Jim Tselikis and Sabin Lomac, two cousins from Maine. One lobster truck in Los Angeles, open for a few months. They ask for fifty five thousand, for five percent. A one point one '
        'million dollar company.',
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': 'They push Barbara. She comes down to fifteen. They take her deal: fifty five thousand, for fifteen percent. Less money, but the partner they wanted.',
 'exit': 'No sale here. Instead, the cousins did something smarter for growth. They franchised.',
 'hook': "Barbara paid fifty five thousand dollars for fifteen percent of a lobster truck. Today it's more than eighty trucks in over thirty states.",
 'lesson': "The lesson: you don't have to sell the company to build value. Sometimes the best structure lets you grow without paying for every unit.",
 'math': "Here's why franchising scales. The franchisee funds the truck. Per the franchise disclosure document, the initial investment runs about one hundred eighty seven thousand to four hundred "
         "ninety three thousand dollars. The brand grows on other people's capital.",
 'offers': 'Robert offers the money, for twenty five percent. Barbara offers it for seventeen percent: her lucky number. Robert raises to one hundred thousand, for twenty five percent.'}
COLD_SHOTS = [(478.0, 3.5, 'fit'), (639.0, 3.5, 'fit')]
SHOTS = {'after': [(252.0, 2.5, 'fit'), (330.0, 2.5, 'fit'), (630.0, 2.5, 'full')],
 'ask': [(8.0, 3.5, 'fit'), (354.0, 2.5, 'fit'), (558.0, 2.5, 'fit'), (22.0, 3.0, 'fit')],
 'cta': [(642.0, 1.5, 'fit'), (648.0, 2.0, 'fit')],
 'deal': [(612.0, 2.5, 'full'), (639.0, 3.0, 'fit'), (654.0, 2.5, 'fit')],
 'exit': [(72.0, 2.5, 'fit'), (324.0, 2.5, 'fit'), (546.0, 2.5, 'fit')],
 'hook': [(540.0, 2.5, 'fit'), (654.0, 2.0, 'fit'), (72.0, 2.5, 'fit')],
 'lesson': [(396.0, 2.5, 'full'), (564.0, 2.0, 'full'), (432.0, 2.0, 'fit')],
 'math': [(120.0, 2.5, 'full'), (204.0, 2.5, 'full'), (222.0, 2.5, 'full')],
 'offers': [(478.0, 3.0, 'fit'), (498.0, 3.0, 'fit'), (300.0, 2.5, 'full'), (521.0, 3.0, 'fit')]}
CALLOUTS = {'after': [(0.0, 'label', 'TODAY'), (0.2, 'big', [('80+ trucks', 'o')]), (0.5, 'line', [('30+ states, plus restaurants', 'w')]), (0.8, 'sub', [('Barbara is still in', 'p')])],
 'ask': [(0.0, 'label', 'THE ASK · 2012 · COUSINS MAINE LOBSTER'),
         (0.25, 'sub', [('One lobster truck in LA', 'p')]),
         (0.45, 'big', [('$55K for 5%', 'w')]),
         (0.72, 'card', ('In plain English, the company is worth', [('$1.1M', 'o')]))],
 'cold': [(0.04, 'label', 'THE OFFERS, ON THE SHOW'), (0.16, 'line', [('Robert: $55K for ', 'w'), ('25%', 'o')]), (0.62, 'slam', [('They took Barbara: 15%.', 'oi')])],
 'cta': [(0.0, 'label', 'BEFORE YOU SIGN A DEAL'), (0.15, 'big', [('Follow the ', 'w'), ('money.', 'oi')])],
 'deal': [(0.0, 'label', 'THE DEAL THEY TOOK'), (0.12, 'big', [('Barbara: $55K for ', 'w'), ('15%', 'o')]), (0.6, 'sub', [('Less money, chosen partner', 'p')])],
 'exit': [(0.0, 'label', 'NO SALE'), (0.3, 'big', [('They franchised.', 'w')])],
 'hook': [(0.0, 'big', [('$55K', 'w')]), (0.5, 'card', ('for 15% of one truck. Today:', [('80+ trucks, 30+ states', 'o')]))],
 'lesson': [(0.0, 'line', [("You don't have to sell", 'w')]), (0.18, 'line', [('to build ', 'w'), ('value.', 'oi')]), (0.55, 'chips', ['Structure', "Other people's capital"])],
 'math': [(0.0, 'label', 'WHY FRANCHISING SCALES'),
          (0.12, 'line', [('Franchisee funds the truck', 'w')]),
          (0.42, 'line', [('Initial investment: ', 'w'), ('$187K–$493K', 'o')]),
          (0.75, 'sub', [('Per the franchise disclosure document', 'p')])],
 'offers': [(0.0, 'label', 'THE OFFERS'),
            (0.15, 'line', [('Robert: ', 'w'), ('$55K for 25%', 'o')]),
            (0.4, 'line', [('Barbara: ', 'w'), ('$55K for 17%', 'o')]),
            (0.7, 'line', [('Robert: ', 'w'), ('$100K for 25%', 'o')])]}
