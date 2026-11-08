import json, os
SRC = "/home/claude/deals/kodiak.mp4"
VO = "/home/claude/deals/vo/kodiak_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP12"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/kodiak_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': 'They brought in a growth investor later, on their own timeline. And when L Catterton bought in, the founders kept a minority stake.',
 'ask': '2014. Joel Clark and Cameron Smith. Kodiak Cakes: whole grain pancake mix from Utah. They ask for five hundred thousand dollars, for ten percent. A five million dollar company.',
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': 'They turn down both. No deal. They keep one hundred percent.',
 'exit': 'Two months after the show, they launch Power Cakes at Target. And in 2021, private equity firm L Catterton buys a majority stake. The price was never disclosed.',
 'hook': 'The best offer valued this pancake company at one point four million dollars. The founders said no to both.',
 'lesson': 'The lesson: dilution is permanent. Before you sell equity cheap, ask what it costs you at the exit, not today.',
 'math': 'Now run the offers. Thirty five percent for five hundred thousand values the company at about one point four million. Fifty percent values it at one million. Saying no kept the real '
         'decision in their hands: when to sell, and to whom.',
 'offers': 'Robert offers the full five hundred thousand, for thirty five percent. Then Barbara and Kevin team up: five hundred thousand, for fifty percent.'}
COLD_SHOTS = [(158.5, 4.0, 'fit'), (268.0, 5.0, 'fit')]
SHOTS = {'after': [(68.0, 2.5, 'full'), (104.0, 2.5, 'full'), (192.0, 2.5, 'fit')],
 'ask': [(5.5, 3.0, 'fit'), (16.0, 2.5, 'fit'), (20.0, 2.0, 'full'), (12.0, 3.0, 'fit')],
 'cta': [(288.0, 1.5, 'full'), (284.0, 2.0, 'fit')],
 'deal': [(280.0, 2.5, 'full'), (284.0, 2.5, 'fit'), (300.0, 2.0, 'full')],
 'exit': [(4.0, 2.5, 'fit'), (8.0, 2.5, 'fit'), (292.0, 2.5, 'full')],
 'hook': [(20.0, 2.0, 'full'), (268.5, 2.5, 'fit'), (188.0, 2.0, 'full')],
 'lesson': [(132.0, 2.5, 'full'), (60.0, 2.0, 'full'), (200.0, 2.0, 'fit')],
 'math': [(220.0, 2.5, 'full'), (256.0, 2.5, 'full'), (144.0, 2.5, 'full')],
 'offers': [(148.0, 2.0, 'full'), (158.5, 3.0, 'fit'), (248.0, 2.0, 'full'), (268.0, 3.5, 'fit')]}
CALLOUTS = {'after': [(0.0, 'label', 'WHAT THEY KEPT'), (0.2, 'line', [('Control of ', 'w'), ('timing', 'oi')]), (0.55, 'big', [('Minority stake at exit', 'w')])],
 'ask': [(0.0, 'label', 'THE ASK · 2014 · KODIAK CAKES'),
         (0.25, 'sub', [('Whole grain pancake mix', 'p')]),
         (0.45, 'big', [('$500K for 10%', 'w')]),
         (0.72, 'card', ('In plain English, the company is worth', [('$5M', 'o')]))],
 'cold': [(0.04, 'label', 'THE OFFERS, ON THE SHOW'), (0.16, 'line', [('$500K for ', 'w'), ('35%', 'o')]), (0.62, 'slam', [('They said no.', 'oi')])],
 'cta': [(0.0, 'label', 'BEFORE YOU SIGN A DEAL'), (0.15, 'big', [('Follow the ', 'w'), ('money.', 'oi')])],
 'deal': [(0.0, 'label', 'THE DECISION'), (0.12, 'big', [('No deal.', 'w')]), (0.55, 'sub', [('They keep 100%', 'p')])],
 'exit': [(0.0, 'label', 'AFTER THE TANK'),
          (0.12, 'sub', [('Power Cakes launch at Target', 'p')]),
          (0.45, 'big', [('2021: L Catterton', 'w')]),
          (0.75, 'sub', [('Majority stake · price undisclosed', 'p')])],
 'hook': [(0.0, 'big', [('$5M ask', 'w')]), (0.5, 'card', ('The best offer valued the company at', [('$1.4M', 'o')]))],
 'lesson': [(0.0, 'line', [('Dilution is', 'w')]), (0.18, 'line', [('permanent.', 'oi')]), (0.55, 'chips', ['Price it at the exit', 'Not today'])],
 'math': [(0.0, 'label', 'THE MATH'),
          (0.12, 'line', [('35% for $500K = ', 'w'), ('$1.4M', 'o')]),
          (0.4, 'line', [('50% for $500K = ', 'w'), ('$1M', 'o')]),
          (0.72, 'slam', [('vs. their $5M ask', 'oi')])],
 'offers': [(0.0, 'label', 'THE OFFERS'), (0.2, 'line', [('Robert: ', 'w'), ('$500K for 35%', 'o')]), (0.58, 'line', [('Barbara + Kevin: ', 'w'), ('$500K for 50%', 'o')])]}
