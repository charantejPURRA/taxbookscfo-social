import json, os
SRC = "/home/claude/deals/coatchex.mp4"
VO = "/home/claude/deals/vo/coatchex_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP19"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/coatchex_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': "Derek later said he didn't regret it, and that he'd had offers at higher valuations.",
 'ask': '2012. The season four premiere. Derek Pacque, fresh out of Indiana University. CoatChex: a ticketless coat check system. He asks for two hundred thousand, for ten percent. A two million '
        'dollar company.',
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': 'He calls his co-founder, a venture capital professor. Then he says no. He counters at twenty percent. Mark walks.',
 'exit': 'CoatChex later rebranded as Chexology, and kept building.',
 'hook': "He hadn't sold a single system. And he still turned down two hundred thousand dollars from Mark Cuban.",
 'lesson': 'The lesson: valuation follows evidence. If you want a higher number, bring revenue, not projections.',
 'math': "Mark's offer valued the company at about six hundred thousand. Derek wanted two million. The gap wasn't greed. It was proof. With no customers, the buyer sets the price.",
 'offers': "He'd made about fifty thousand dollars checking coats himself. But no venue had bought the system yet. Most Sharks go out. Then Mark: two hundred thousand... for thirty three percent."}
COLD_SHOTS = [(608.0, 3.5, 'fit'), (762.5, 3.5, 'fit')]
SHOTS = {'after': [(528.0, 2.5, 'full'), (720.0, 2.5, 'full'), (786.0, 2.0, 'fit')],
 'ask': [(92.5, 3.5, 'fit'), (156.0, 2.5, 'fit'), (120.0, 2.5, 'fit'), (101.0, 3.0, 'fit')],
 'cta': [(216.0, 1.5, 'fit'), (684.0, 2.0, 'fit')],
 'deal': [(640.0, 3.5, 'fit'), (762.5, 3.0, 'fit'), (738.0, 2.5, 'full')],
 'exit': [(774.0, 2.5, 'fit'), (708.0, 2.5, 'fit'), (168.0, 2.5, 'fit')],
 'hook': [(150.0, 2.5, 'fit'), (402.0, 2.5, 'full'), (378.0, 2.0, 'full')],
 'lesson': [(462.0, 2.5, 'full'), (444.0, 2.0, 'full'), (534.0, 2.0, 'full')],
 'math': [(594.0, 2.5, 'full'), (480.0, 2.5, 'full'), (360.0, 2.5, 'full')],
 'offers': [(306.0, 2.5, 'full'), (252.0, 2.5, 'full'), (324.0, 2.5, 'full'), (608.0, 3.0, 'fit')]}
CALLOUTS = {'after': [(0.0, 'label', 'LATER'), (0.25, 'line', [('No regrets.', 'w')]), (0.55, 'sub', [('Says he had higher-valuation offers', 'p')])],
 'ask': [(0.0, 'label', 'THE ASK · 2012 · COATCHEX'),
         (0.25, 'sub', [('Ticketless coat check', 'p')]),
         (0.45, 'big', [('$200K for 10%', 'w')]),
         (0.72, 'card', ('In plain English, the company is worth', [('$2M', 'o')]))],
 'cold': [(0.04, 'label', 'THE OFFER, ON THE SHOW'), (0.16, 'line', [('Mark: $200K for ', 'w'), ('33%', 'o')]), (0.62, 'slam', [('He said no.', 'oi')])],
 'cta': [(0.0, 'label', 'BEFORE YOU SIGN A DEAL'), (0.15, 'big', [('Follow the ', 'w'), ('money.', 'oi')])],
 'deal': [(0.0, 'label', 'THE CALL'), (0.12, 'sub', [('Phones his professor / co-founder', 'p')]), (0.4, 'line', [('Counters: ', 'w'), ('20%', 'o')]), (0.72, 'slam', [('Mark walks.', 'oi')])],
 'exit': [(0.0, 'label', 'AFTER THE TANK'), (0.25, 'big', [('Chexology', 'w')]), (0.6, 'sub', [('Rebranded and kept building', 'p')])],
 'hook': [(0.0, 'big', [('0 systems sold', 'w')]), (0.5, 'card', ("He still turned down Mark Cuban's", [('$200K', 'o')]))],
 'lesson': [(0.0, 'line', [('Valuation follows', 'w')]), (0.18, 'line', [('evidence.', 'oi')]), (0.55, 'chips', ['Bring revenue', 'Not projections'])],
 'math': [(0.0, 'label', 'THE MATH'),
          (0.12, 'line', [("Mark's offer: ", 'w'), ('~$600K', 'o')]),
          (0.4, 'line', [("Derek's ask: ", 'w'), ('$2M', 'o')]),
          (0.72, 'slam', [("No customers = buyer's price", 'oi')])],
 'offers': [(0.0, 'label', 'THE NUMBERS'),
            (0.15, 'line', [('Coat-check revenue: ', 'w'), ('~$50K', 'o')]),
            (0.42, 'line', [('Systems sold: ', 'w'), ('0', 'oi')]),
            (0.72, 'line', [('Mark: ', 'w'), ('$200K for 33%', 'o')])]}
