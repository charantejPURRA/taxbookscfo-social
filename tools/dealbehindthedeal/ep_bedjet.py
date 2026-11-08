import json, os
SRC = "/home/claude/deals/bedjet.mp4"
VO = "/home/claude/deals/vo/bedjet_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP17"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/bedjet_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': 'The Sharks priced the founder. The retailer priced the product.',
 'ask': '2015. Mark Aramli, an engineer. BedJet: a machine that heats and cools your bed. He asks for two hundred fifty thousand, for ten percent. A two and a half million dollar company.',
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': 'One by one, every Shark goes out. No deal.',
 'exit': 'But the day after the episode aired, Mattress Firm announced it would sell BedJet.',
 'hook': "He asked for two hundred fifty thousand dollars and left with nothing. The next day, America's largest mattress retailer signed him.",
 'lesson': 'The lesson: investors buy the person as much as the margin. In a negotiation, how you answer is part of the price.',
 'math': "Look at the unit economics he brought. Ninety eight dollars to make. Four ninety nine to sell. That's about an eighty percent gross margin, before shipping and retailer cuts.",
 'offers': "No sales yet. Production is six weeks away, with about fifty thousand dollars raised on Kickstarter. Then Lori feels brushed off... and she's out."}
COLD_SHOTS = [(40.0, 4.0, 'fit'), (180.0, 4.0, 'fit')]
SHOTS = {'after': [(256.0, 2.5, 'full'), (72.0, 2.5, 'fit'), (212.0, 2.5, 'full')],
 'ask': [(36.0, 3.5, 'fit'), (12.0, 2.5, 'fit'), (88.0, 2.5, 'fit'), (40.5, 3.0, 'fit')],
 'cta': [(308.0, 1.5, 'fit'), (96.0, 2.0, 'fit')],
 'deal': [(204.0, 2.5, 'full'), (288.0, 2.5, 'full'), (312.0, 2.5, 'full')],
 'exit': [(92.0, 2.5, 'fit'), (116.0, 2.5, 'fit'), (244.0, 2.5, 'fit')],
 'hook': [(68.0, 2.5, 'fit'), (184.0, 2.0, 'full'), (264.0, 2.5, 'fit')],
 'lesson': [(232.0, 2.5, 'full'), (268.0, 2.0, 'full'), (316.0, 2.0, 'full')],
 'math': [(16.0, 2.5, 'fit'), (24.0, 2.5, 'fit'), (164.0, 2.5, 'full')],
 'offers': [(124.0, 2.5, 'full'), (176.0, 2.5, 'full'), (192.0, 2.5, 'full'), (296.0, 2.5, 'fit')]}
CALLOUTS = {'after': [(0.0, 'line', [('Sharks priced the ', 'w'), ('founder.', 'oi')]), (0.5, 'line', [('Retail priced the ', 'w'), ('product.', 'oi')])],
 'ask': [(0.0, 'label', 'THE ASK · 2015 · BEDJET'),
         (0.25, 'sub', [('Heats and cools your bed', 'p')]),
         (0.45, 'big', [('$250K for 10%', 'w')]),
         (0.72, 'card', ('In plain English, the company is worth', [('$2.5M', 'o')]))],
 'cold': [(0.04, 'label', 'THE ASK, ON THE SHOW'), (0.16, 'line', [('$250K for ', 'w'), ('10%', 'o')]), (0.62, 'slam', [('He left with nothing.', 'oi')])],
 'cta': [(0.0, 'label', 'BEFORE YOU SIGN A DEAL'), (0.15, 'big', [('Follow the ', 'w'), ('money.', 'oi')])],
 'deal': [(0.0, 'label', 'THE RESULT'), (0.12, 'big', [('No deal.', 'w')]), (0.55, 'sub', [('Every Shark out', 'p')])],
 'exit': [(0.0, 'label', 'THE DAY AFTER AIRING'), (0.25, 'big', [('Mattress Firm', 'o')]), (0.6, 'sub', [('Announced it would sell BedJet', 'p')])],
 'hook': [(0.0, 'big', [('$0 from the Sharks', 'w')]), (0.5, 'card', ('The next day', [('Mattress Firm signed on', 'o')]))],
 'lesson': [(0.0, 'line', [('How you answer', 'w')]), (0.18, 'line', [('is part of the ', 'w'), ('price.', 'oi')]), (0.55, 'chips', ['Investors buy the person', 'And the margin'])],
 'math': [(0.0, 'label', 'UNIT ECONOMICS'), (0.12, 'line', [('Cost to make: ', 'w'), ('$98', 'o')]), (0.4, 'line', [('Price: ', 'w'), ('$499', 'o')]), (0.72, 'slam', [('≈80% gross margin', 'oi')])],
 'offers': [(0.0, 'label', 'THE PITCH'),
            (0.15, 'line', [('Sales: ', 'w'), ('none yet', 'oi')]),
            (0.4, 'line', [('Kickstarter: ', 'w'), ('~$50K', 'o')]),
            (0.7, 'line', [('Lori: ', 'w'), ('out.', 'oi')])]}
