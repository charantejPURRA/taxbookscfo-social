import json, os
SRC = "/home/claude/deals/rocketbook.mp4"
VO = "/home/claude/deals/vo/rocketbook_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP14"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/rocketbook_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': "And the founders stayed with BIC. A pen company wasn't just buying notebooks. It was buying a way into digital writing.",
 'ask': '2017. Jake Epstein and Joe Lemay. Rocketbook: a reusable notebook that sends your handwriting to the cloud. They ask for four hundred thousand, for ten percent. A four million dollar '
        'company.',
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': 'No deal. Not one offer.',
 'exit': 'December 2020. BIC, the pen company, buys one hundred percent of Rocketbook. Price: forty million dollars.',
 'hook': 'Every Shark said no to this notebook. Three years later, BIC bought it for forty million dollars.',
 'lesson': "The lesson: a strategic buyer pays for fit, not just profit. Know who needs what you've built.",
 'math': "Four million on the ask. Forty million at the exit. Ten times the valuation the Sharks wouldn't pay, in about three and a half years.",
 'offers': "They've already sold two point two million dollars. Barbara calls it a gimmick and goes out. Kevin is out. Mark laughs, and goes out too."}
COLD_SHOTS = [(20.0, 4.0, 'fit'), (128.0, 4.0, 'fit')]
SHOTS = {'after': [(156.0, 2.5, 'fit'), (96.0, 2.5, 'full'), (276.0, 2.5, 'full')],
 'ask': [(22.0, 3.0, 'fit'), (32.0, 2.5, 'fit'), (52.0, 2.5, 'fit'), (28.5, 3.0, 'fit')],
 'cta': [(252.0, 1.5, 'fit'), (308.0, 2.0, 'fit')],
 'deal': [(224.0, 2.5, 'fit'), (260.0, 2.5, 'full'), (320.0, 2.0, 'fit')],
 'exit': [(36.0, 2.5, 'fit'), (92.0, 2.5, 'full'), (4.0, 2.5, 'fit')],
 'hook': [(88.0, 2.5, 'full'), (184.0, 2.0, 'full'), (268.0, 2.0, 'full')],
 'lesson': [(216.0, 2.5, 'full'), (240.0, 2.0, 'full'), (172.0, 2.0, 'fit')],
 'math': [(212.0, 2.5, 'full'), (148.0, 2.5, 'full'), (192.0, 2.5, 'full')],
 'offers': [(68.0, 2.5, 'fit'), (104.0, 2.5, 'full'), (132.0, 2.5, 'full'), (300.0, 2.5, 'full')]}
CALLOUTS = {'after': [(0.0, 'label', 'WHY BIC PAID'), (0.2, 'line', [('Not notebooks. ', 'w')]), (0.5, 'big', [('Digital writing.', 'w')])],
 'ask': [(0.0, 'label', 'THE ASK · 2017 · ROCKETBOOK'),
         (0.25, 'sub', [('Reusable notebook → cloud', 'p')]),
         (0.45, 'big', [('$400K for 10%', 'w')]),
         (0.72, 'card', ('In plain English, the company is worth', [('$4M', 'o')]))],
 'cold': [(0.04, 'label', 'THE ASK, ON THE SHOW'), (0.16, 'line', [('$400K for ', 'w'), ('10%', 'o')]), (0.62, 'slam', [('Every Shark said no.', 'oi')])],
 'cta': [(0.0, 'label', 'BEFORE YOU SIGN A DEAL'), (0.15, 'big', [('Follow the ', 'w'), ('money.', 'oi')])],
 'deal': [(0.0, 'label', 'THE RESULT'), (0.12, 'big', [('No deal.', 'w')]), (0.55, 'sub', [('Not one offer', 'p')])],
 'exit': [(0.0, 'label', 'DECEMBER 2020 · BIC'), (0.15, 'sub', [('100% of the company', 'p')]), (0.45, 'big', [('$40M', 'o')])],
 'hook': [(0.0, 'big', [('0 offers', 'w')]), (0.5, 'card', ('Three years later, BIC paid', [('$40M', 'o')]))],
 'lesson': [(0.0, 'line', [('Strategic buyers', 'w')]), (0.18, 'line', [('pay for ', 'w'), ('fit.', 'oi')]), (0.55, 'chips', ['Who needs what you built?', 'Not just profit'])],
 'math': [(0.0, 'label', 'THE MATH'), (0.12, 'line', [('The ask: ', 'w'), ('$4M', 'o')]), (0.4, 'line', [('The exit: ', 'w'), ('$40M', 'o')]), (0.72, 'slam', [('10x in ~3.5 years', 'oi')])],
 'offers': [(0.0, 'label', 'THE SHARKS'),
            (0.15, 'line', [('Sales so far: ', 'w'), ('$2.2M', 'o')]),
            (0.45, 'line', [('Barbara: ', 'w'), ('“gimmick.” Out.', 'oi')]),
            (0.75, 'line', [('Kevin, Mark: ', 'w'), ('out.', 'oi')])]}
