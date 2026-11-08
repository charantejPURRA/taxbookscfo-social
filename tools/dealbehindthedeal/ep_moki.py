import json, os
SRC = "/home/claude/deals/moki.mp4"
VO = "/home/claude/deals/vo/moki_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP16"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/moki_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': "What happened after the cameras stopped? Public reports conflict, so we won't guess. The math holds either way.",
 'ask': "Season ten. Zach and Alyssa Brown, a firefighter and an E R nurse. Moki Doorstep: a step that hooks onto your car's door latch. They ask for one hundred fifty thousand, for five percent. A "
        'three million dollar company.',
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': "Zach says he'd rather sell. Daymond: three million dollars, for one hundred percent. They accept on the spot.",
 'exit': 'A full buyout in the Tank. Rare. But what is a company worth when most of its value is one contract?',
 'hook': 'They had a licensing deal worth three million dollars. Then a Shark offered to buy the whole company... for three million.',
 'lesson': "The lesson: when you sell a royalty stream, price it in today's dollars. A guarantee paid over seven years is not cash in hand.",
 'math': "Three million spread over seven years is not three million today. At a ten percent discount rate, it's worth about two point one million now. The royalty on top is the upside, and in a "
         'buyout, the buyer gets it.',
 'offers': 'Zach says a licensing deal guarantees three million over seven years, plus a twelve and a half percent royalty. Daymond offers four hundred fifty thousand, for twenty percent.'}
COLD_SHOTS = [(378.0, 3.5, 'fit'), (429.5, 4.0, 'fit')]
SHOTS = {'after': [(462.0, 2.5, 'fit'), (468.0, 2.5, 'fit'), (390.0, 2.5, 'fit')],
 'ask': [(19.5, 3.5, 'fit'), (6.0, 2.5, 'fit'), (156.0, 2.5, 'fit'), (24.5, 3.0, 'fit')],
 'cta': [(444.0, 1.5, 'full'), (48.0, 2.0, 'fit')],
 'deal': [(432.0, 2.5, 'full'), (429.5, 3.0, 'fit'), (480.0, 2.5, 'fit')],
 'exit': [(456.0, 2.5, 'fit'), (114.0, 2.5, 'fit'), (78.0, 2.5, 'fit')],
 'hook': [(132.0, 2.5, 'full'), (430.0, 2.5, 'fit'), (474.0, 2.0, 'full')],
 'lesson': [(408.0, 2.5, 'full'), (420.0, 2.0, 'full'), (252.0, 2.0, 'fit')],
 'math': [(330.0, 2.5, 'full'), (270.0, 2.5, 'full'), (210.0, 2.5, 'full')],
 'offers': [(318.0, 2.5, 'full'), (342.0, 2.5, 'full'), (366.0, 2.5, 'full'), (378.0, 3.0, 'fit')]}
CALLOUTS = {'after': [(0.0, 'label', 'AFTER THE CAMERAS'), (0.25, 'big', [('Reports conflict.', 'w')]), (0.6, 'sub', [('The math holds either way', 'p')])],
 'ask': [(0.0, 'label', 'THE ASK · SEASON 10 · MOKI DOORSTEP'),
         (0.25, 'sub', [("A step that hooks on your car's door latch", 'p')]),
         (0.45, 'big', [('$150K for 5%', 'w')]),
         (0.72, 'card', ('In plain English, the company is worth', [('$3M', 'o')]))],
 'cold': [(0.04, 'label', 'THE OFFERS, ON THE SHOW'), (0.16, 'line', [('$450K for ', 'w'), ('20%', 'o')]), (0.62, 'slam', [('Then: $3M for 100%.', 'oi')])],
 'cta': [(0.0, 'label', 'BEFORE YOU SIGN A DEAL'), (0.15, 'big', [('Follow the ', 'w'), ('money.', 'oi')])],
 'deal': [(0.0, 'label', 'THE DEAL ON TV'), (0.12, 'big', [('$3M for 100%', 'o')]), (0.6, 'sub', [('Accepted on the spot', 'p')])],
 'exit': [(0.0, 'label', 'THE QUESTION'), (0.2, 'line', [("What's a company worth", 'w')]), (0.45, 'line', [('when its value is ', 'w'), ('one contract?', 'oi')])],
 'hook': [(0.0, 'big', [('$3M license', 'w')]), (0.5, 'card', ('Then a Shark offered for the whole company', [('$3M', 'o')]))],
 'lesson': [(0.0, 'line', [('Price a royalty in', 'w')]), (0.18, 'line', [("today's ", 'w'), ('dollars.', 'oi')]), (0.55, 'chips', ['A guarantee ≠ cash', 'Discount the future'])],
 'math': [(0.0, 'label', 'THE MATH (ILLUSTRATIVE)'),
          (0.12, 'line', [('$3M over 7 years', 'w')]),
          (0.4, 'line', [('At 10% discount: ', 'w'), ('≈$2.1M today', 'o')]),
          (0.72, 'slam', [('Royalty upside goes to the buyer', 'oi')])],
 'offers': [(0.0, 'label', 'ON AIR'),
            (0.15, 'line', [('License: ', 'w'), ('$3M over 7 yrs', 'o')]),
            (0.4, 'sub', [('+ 12.5% royalty', 'p')]),
            (0.7, 'line', [('Daymond: ', 'w'), ('$450K for 20%', 'o')])]}
