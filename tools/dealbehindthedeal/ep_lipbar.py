import json, os
SRC = "/home/claude/deals/lipbar.mp4"
VO = "/home/claude/deals/vo/lipbar_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP18"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/lipbar_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': 'Later, The Lip Bar announced a launch in three thousand C V S stores.',
 'ask': '2015. Melissa Butler, a former Wall Street analyst. The Lip Bar: bold, vegan lipstick. One hundred twenty five thousand, for twenty percent. A six hundred twenty five thousand dollar '
        'company.',
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': 'No deal.',
 'exit': "So Melissa cold-called a Target buyer. The Lip Bar launched on Target's website in 2016, and in Target stores in 2018.",
 'hook': "A Shark said they'd be crushed like colorful cockroaches. Three years later, they were on the shelves at Target.",
 'lesson': 'The lesson: equity is the most expensive money you can raise. If you can get distribution without selling ownership, do that first.',
 'math': 'The CFO read: the Sharks wanted twenty percent of the company. Target bought inventory. One sells your equity. The other sells your product.',
 'offers': 'Kevin calls the colors clown makeup. Robert dislikes the branding. They all go out.'}
COLD_SHOTS = [(32.0, 3.5, 'fit'), (228.0, 4.0, 'fit')]
SHOTS = {'after': [(276.0, 2.5, 'fit'), (172.0, 2.5, 'fit'), (8.0, 2.5, 'fit')],
 'ask': [(25.5, 3.5, 'fit'), (36.0, 2.5, 'fit'), (148.0, 2.5, 'fit'), (32.5, 3.0, 'fit')],
 'cta': [(132.0, 1.5, 'fit'), (296.0, 2.0, 'fit')],
 'deal': [(260.0, 2.5, 'full'), (192.0, 2.5, 'full'), (292.0, 2.5, 'fit')],
 'exit': [(92.0, 2.5, 'fit'), (48.0, 2.5, 'fit'), (128.0, 2.5, 'fit')],
 'hook': [(208.0, 2.5, 'full'), (44.0, 2.5, 'fit'), (140.0, 2.0, 'full')],
 'lesson': [(152.0, 2.5, 'full'), (196.0, 2.0, 'full'), (168.0, 2.0, 'fit')],
 'math': [(180.0, 2.5, 'full'), (244.0, 2.5, 'full'), (280.0, 2.5, 'full')],
 'offers': [(220.0, 2.5, 'full'), (96.0, 2.5, 'full'), (184.0, 2.5, 'full'), (264.0, 2.5, 'full')]}
CALLOUTS = {'after': [(0.0, 'label', 'LATER'), (0.25, 'big', [('3,000 CVS stores', 'w')]), (0.65, 'sub', [('Announced launch', 'p')])],
 'ask': [(0.0, 'label', 'THE ASK · 2015 · THE LIP BAR'),
         (0.25, 'sub', [('Bold, vegan lipstick', 'p')]),
         (0.45, 'big', [('$125K for 20%', 'w')]),
         (0.72, 'card', ('In plain English, the company is worth', [('$625K', 'o')]))],
 'cold': [(0.04, 'label', 'THE ASK, ON THE SHOW'), (0.16, 'line', [('$125K for ', 'w'), ('20%', 'o')]), (0.62, 'slam', [('Zero offers.', 'oi')])],
 'cta': [(0.0, 'label', 'BEFORE YOU SIGN A DEAL'), (0.15, 'big', [('Follow the ', 'w'), ('money.', 'oi')])],
 'deal': [(0.0, 'label', 'THE RESULT'), (0.12, 'big', [('No deal.', 'w')])],
 'exit': [(0.0, 'label', 'THE COLD CALL'), (0.15, 'line', [('2016: ', 'w'), ('Target.com', 'o')]), (0.5, 'line', [('2018: ', 'w'), ('Target stores', 'o')])],
 'hook': [(0.0, 'big', [('“Cockroaches”', 'w')]), (0.5, 'card', ('Three years later, on the shelves at', [('Target', 'o')]))],
 'lesson': [(0.0, 'line', [('Equity is the most', 'w')]), (0.18, 'line', [('expensive ', 'w'), ('money.', 'oi')]), (0.55, 'chips', ['Distribution first', 'Ownership kept'])],
 'math': [(0.0, 'label', 'THE CFO READ'),
          (0.12, 'line', [('Sharks: ', 'w'), ('20% of the company', 'o')]),
          (0.45, 'line', [('Target: ', 'w'), ('bought inventory', 'o')]),
          (0.75, 'slam', [('Equity vs. revenue', 'oi')])],
 'offers': [(0.0, 'label', 'THE SHARKS'),
            (0.2, 'line', [('Kevin: ', 'w'), ('“clown makeup”', 'oi')]),
            (0.55, 'line', [('Robert: ', 'w'), ('not the branding', 'oi')]),
            (0.8, 'sub', [('All out', 'p')])]}
