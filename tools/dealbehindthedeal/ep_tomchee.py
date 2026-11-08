import json, os
SRC = "/home/claude/deals/tomchee.mp4"
VO = "/home/claude/deals/vo/tomchee_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP21"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/tomchee_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': 'On TV, the deal valued Tom plus Chee at two million dollars. The exit went through the bank.',
 'ask': '2013. Trew Quackenbush and Corey Ward. Tom plus Chee: grilled cheese and tomato soup from Cincinnati. They ask for six hundred thousand, for ten percent. A six million dollar company.',
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': 'Six hundred thousand, for thirty percent. They take it.',
 'exit': 'But after the show, Mark dropped out, and Barbara cut her stake. The chain pushed into franchising, fast.',
 'hook': "Two Sharks agreed to put in six hundred thousand dollars. Four years later, the bank seized the company's assets.",
 'lesson': 'The lesson: growth funded with debt has a deadline. Before you expand, know your runway, and who gets paid first.',
 'math': "Then the debt came due. Tom plus Chee couldn't repay a loan, and the lender seized its assets. In September 2017, Gold Star Chili bought them from the lender. Terms not disclosed. By then, "
         'it was down to twenty three locations.',
 'offers': 'Kevin tears into the menus and the logo. Then they reveal two corporate stores did one and a half million dollars last year. Barbara offers three hundred thousand for fifteen percent, if '
           'another Shark joins. Mark joins.'}
COLD_SHOTS = [(2.5, 3.0, 'fit'), (80.0, 3.0, 'fit')]
SHOTS = {'after': [(44.0, 2.5, 'fit'), (96.0, 2.5, 'fit'), (50.0, 2.5, 'fit')],
 'ask': [(16.0, 2.5, 'fit'), (14.0, 2.0, 'fit'), (86.0, 2.5, 'fit'), (88.0, 2.5, 'fit')],
 'cta': [(58.0, 1.5, 'fit'), (102.0, 2.0, 'fit')],
 'deal': [(12.0, 2.0, 'fit'), (56.0, 2.5, 'fit'), (64.0, 2.5, 'fit')],
 'exit': [(30.0, 2.5, 'fit'), (34.0, 2.5, 'fit'), (84.0, 2.5, 'fit')],
 'hook': [(80.0, 2.5, 'fit'), (6.0, 2.0, 'fit'), (100.0, 2.0, 'fit')],
 'lesson': [(72.0, 2.5, 'fit'), (74.0, 2.0, 'fit'), (94.0, 2.0, 'fit')],
 'math': [(92.0, 2.5, 'fit'), (60.0, 2.5, 'fit'), (24.0, 2.5, 'fit')],
 'offers': [(4.0, 2.0, 'fit'), (26.0, 2.5, 'fit'), (8.0, 2.0, 'fit'), (78.0, 2.5, 'fit')]}
CALLOUTS = {'after': [(0.0, 'label', 'ON TV vs. AT THE EXIT'), (0.2, 'line', [('Valued at ', 'w'), ('$2M', 'o')]), (0.55, 'big', [('Exit: via the bank', 'w')])],
 'ask': [(0.0, 'label', 'THE ASK · 2013 · TOM + CHEE'),
         (0.25, 'sub', [('Grilled cheese + tomato soup, Cincinnati', 'p')]),
         (0.45, 'big', [('$600K for 10%', 'w')]),
         (0.72, 'card', ('In plain English, the company is worth', [('$6M', 'o')]))],
 'cold': [(0.04, 'label', 'THE DEAL, ON THE SHOW'), (0.16, 'line', [('$600K for ', 'w'), ('30%', 'o')]), (0.62, 'slam', [('Four years later: the lender.', 'oi')])],
 'cta': [(0.0, 'label', 'BEFORE YOU SIGN A DEAL'), (0.15, 'big', [('Follow the ', 'w'), ('money.', 'oi')])],
 'deal': [(0.0, 'label', 'THE DEAL'), (0.12, 'big', [('$600K for ', 'w'), ('30%', 'o')]), (0.6, 'sub', [('Mark + Barbara', 'p')])],
 'exit': [(0.0, 'label', 'AFTER THE SHOW'),
          (0.15, 'line', [('Mark: ', 'w'), ('dropped out', 'oi')]),
          (0.45, 'line', [('Barbara: ', 'w'), ('cut her stake', 'oi')]),
          (0.75, 'sub', [('Fast franchising push', 'p')])],
 'hook': [(0.0, 'big', [('$600K', 'w')]), (0.5, 'card', ('Four years later, the lender seized', [('the assets', 'o')]))],
 'lesson': [(0.0, 'line', [('Debt-funded growth', 'w')]), (0.18, 'line', [('has a ', 'w'), ('deadline.', 'oi')]), (0.55, 'chips', ['Know your runway', 'Who gets paid first'])],
 'math': [(0.0, 'label', 'THE DEBT'),
          (0.12, 'line', [('Loan not repaid → ', 'w'), ('assets seized', 'o')]),
          (0.45, 'line', [('Sept 2017: ', 'w'), ('Gold Star Chili', 'o')]),
          (0.75, 'sub', [('Bought from the lender · 23 locations · terms undisclosed', 'p')])],
 'offers': [(0.0, 'label', 'THE OFFERS'),
            (0.15, 'line', [('Two stores: ', 'w'), ('$1.5M sales', 'o')]),
            (0.45, 'line', [('Barbara: ', 'w'), ('$300K for 15%', 'o')]),
            (0.75, 'sub', [('If another Shark joins → Mark', 'p')])]}
