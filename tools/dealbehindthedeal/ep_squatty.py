import json, os
SRC = "/home/claude/deals/squatty.mp4"
VO = "/home/claude/deals/vo/squatty_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP13"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/squatty_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': 'In the twelve months before the deal, Squatty Potty did about sixteen point eight million in revenue, and four point seven million in operating income. The cash was about four times that '
          'profit.',
 'ask': '2014. Bobby and Judy Edwards. Squatty Potty. They ask for three hundred fifty thousand dollars, for five percent. A seven million dollar company.',
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': "They take Lori's deal. Three hundred fifty thousand, for ten percent. The valuation is cut in half, to three and a half million.",
 'exit': 'May 2021. Public company Aterian buys the business. On its books, total consideration: about thirty point eight million dollars.',
 'hook': 'A toilet stool company sold for about thirty one million dollars. But only nineteen million of it was cash.',
 'lesson': 'The lesson: a deal price is a stack, not a number. Cash, services, earn-outs. Ask how much actually lands at closing.',
 'math': 'Now break it down. About nineteen million in cash at closing. About eight million for transition services. And an earn-out of up to four million, paid only if the business hit its targets.',
 'offers': 'Kevin offers the money, for ten percent. Lori matches him. Bobby counters at five hundred thousand. Lori says no.'}
COLD_SHOTS = [(338.0, 3.5, 'fit'), (416.0, 4.0, 'fit')]
SHOTS = {'after': [(246.0, 2.5, 'full'), (222.0, 2.5, 'fit'), (360.0, 2.5, 'full')],
 'ask': [(38.0, 3.5, 'fit'), (90.0, 2.5, 'fit'), (300.0, 2.5, 'fit'), (314.0, 3.0, 'fit')],
 'cta': [(480.0, 1.5, 'fit'), (102.0, 2.0, 'fit')],
 'deal': [(498.0, 2.5, 'fit'), (492.0, 2.5, 'full'), (528.0, 2.5, 'fit')],
 'exit': [(96.0, 2.5, 'fit'), (60.0, 2.5, 'fit'), (516.0, 2.5, 'fit')],
 'hook': [(186.0, 2.5, 'fit'), (42.0, 2.5, 'fit'), (486.0, 2.0, 'full')],
 'lesson': [(438.0, 2.5, 'full'), (264.0, 2.0, 'full'), (354.0, 2.0, 'full')],
 'math': [(150.0, 2.5, 'full'), (432.0, 2.5, 'full'), (126.0, 2.5, 'full')],
 'offers': [(338.0, 3.0, 'fit'), (390.0, 2.5, 'full'), (426.0, 2.5, 'full'), (424.0, 3.0, 'fit')]}
CALLOUTS = {'after': [(0.0, 'label', 'WHAT THE BUYER PRICED'),
           (0.15, 'line', [('TTM revenue: ', 'w'), ('$16.8M', 'o')]),
           (0.4, 'line', [('Operating income: ', 'w'), ('$4.7M', 'o')]),
           (0.72, 'slam', [('Cash ≈ 4x profit', 'oi')])],
 'ask': [(0.0, 'label', 'THE ASK · 2014 · SQUATTY POTTY'),
         (0.25, 'sub', [('A toilet stool', 'p')]),
         (0.45, 'big', [('$350K for 5%', 'w')]),
         (0.72, 'card', ('In plain English, the company is worth', [('$7M', 'o')]))],
 'cold': [(0.04, 'label', 'THE OFFERS, ON THE SHOW'), (0.16, 'line', [('$350K for ', 'w'), ('10%', 'o')]), (0.62, 'slam', [('Sold for ~$31M.', 'oi')])],
 'cta': [(0.0, 'label', 'BEFORE YOU SIGN A DEAL'), (0.15, 'big', [('Follow the ', 'w'), ('money.', 'oi')])],
 'deal': [(0.0, 'label', 'THE DEAL THEY TOOK'), (0.12, 'big', [('Lori: $350K for ', 'w'), ('10%', 'o')]), (0.6, 'sub', [('Valuation: $7M → $3.5M', 'p')])],
 'exit': [(0.0, 'label', 'MAY 2021 · ATERIAN'), (0.2, 'big', [('~$30.8M', 'o')]), (0.55, 'sub', [('Total consideration, per its filings', 'p')])],
 'hook': [(0.0, 'big', [('~$31M', 'w')]), (0.5, 'card', ('But the cash at closing was', [('~$19M', 'o')]))],
 'lesson': [(0.0, 'line', [('A deal price is a', 'w')]), (0.18, 'line', [('stack, ', 'w'), ('not a number.', 'oi')]), (0.55, 'chips', ['Cash', 'Services', 'Earn-outs'])],
 'math': [(0.0, 'label', 'THE STACK'),
          (0.12, 'line', [('Cash at close: ', 'w'), ('~$19M', 'o')]),
          (0.38, 'line', [('Transition services: ', 'w'), ('~$8M', 'o')]),
          (0.64, 'line', [('Earn-out: ', 'w'), ('up to ~$4M', 'o')])],
 'offers': [(0.0, 'label', 'THE OFFERS'),
            (0.2, 'line', [('Kevin: ', 'w'), ('$350K for 10%', 'o')]),
            (0.5, 'line', [('Lori: ', 'w'), ('matches', 'oi')]),
            (0.75, 'sub', [('Counter at $500K → no', 'p')])]}
