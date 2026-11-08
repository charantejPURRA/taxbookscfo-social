import json, os
SRC = "/home/claude/deals/poppi.mp4"
VO = "/home/claude/deals/vo/poppi_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP11"
ORDER = ['hook', 'ask', 'offers', 'deal', 'exit', 'math', 'after', 'lesson', 'cta']
_b = "/home/claude/deals/vo/poppi_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {'after': 'And read the fine print. PepsiCo said three hundred million of that price was expected tax benefits. Net purchase price: one point six five billion.',
 'ask': "2018. Allison and Stephen Ellsworth. Mother Beverage: a sparkling apple cider vinegar drink. They ask for four hundred thousand, for ten percent. That's a four million dollar company.",
 'cta': 'This is TaxBooks C F O. Before you sign a deal, follow the money.',
 'deal': 'Same four hundred thousand... but for twenty five percent. The valuation drops from four million to one point six. They take it.',
 'exit': 'Mother becomes Poppi. And in 2025, PepsiCo buys it. Headline price: one point nine five billion dollars.',
 'hook': 'They asked for four hundred thousand dollars. Six years later, PepsiCo agreed to pay one point nine five billion.',
 'lesson': "The lesson: don't just fight the valuation. Price the partner. And every headline number has a net number underneath it.",
 'math': "Run it. The deal they almost didn't like valued the company at one point six million. The exit valued it at more than a thousand times that. Giving up twenty five percent instead of ten "
         'barely mattered.',
 'offers': 'Kevin calls the valuation insane, and goes out. Only one Shark makes an offer: guest Shark Rohan Oza.'}
# Cold open: the founders pitch -> Rohan's offer caption on screen
COLD_SHOTS = [(48.0, 6.0, "fit"), (464.0, 4.0, "fit")]
SHOTS = {
 "hook":   [(56.0, 2.0, "full"), (466.0, 2.5, "fit"), (484.0, 2.0, "full")],
 "ask":    [(4.0, 3.0, "fit"), (60.0, 2.5, "full"), (64.0, 2.5, "full"), (276.0, 3.0, "fit")],
 "offers": [(352.0, 2.5, "full"), (364.0, 2.5, "full"), (124.0, 3.0, "full"), (444.0, 2.5, "full")],
 "deal":   [(456.0, 3.0, "full"), (463.6, 3.0, "fit"), (480.0, 2.5, "full")],
 "exit":   [(244.0, 2.5, "fit"), (292.0, 2.5, "fit"), (360.0, 2.5, "fit")],
 "math":   [(208.0, 2.5, "full"), (156.0, 2.5, "full"), (432.0, 2.5, "full")],
 "after":  [(104.0, 2.5, "full"), (240.0, 2.5, "full"), (68.0, 2.5, "fit")],
 "lesson": [(448.0, 2.5, "full"), (400.0, 2.0, "full"), (172.0, 2.0, "full")],
 "cta":    [(484.0, 1.5, "full"), (488.0, 2.0, "full")],
}
CALLOUTS = {
 "cold":   [(0.04, "label", "THE ASK, ON THE SHOW"), (0.16, "line", [("$400K for ", "w"), ("10%", "o")]), (0.62, "slam", [("They got 25%.", "oi")])],
 "hook":   [(0.0, "big", [("$400K", "w")]), (0.5, "card", ("Six years later, PepsiCo agreed to pay", [("$1.95B", "o")]))],
 "ask":    [(0.0, "label", "THE ASK · 2018 · MOTHER BEVERAGE"), (0.25, "sub", [("Sparkling apple cider vinegar", "p")]), (0.45, "big", [("$400K for 10%", "w")]),
            (0.72, "card", ("In plain English, the company is worth", [("$4M", "o")]))],
 "offers": [(0.0, "label", "THE OFFERS"), (0.25, "line", [("Kevin: ", "w"), ("out.", "oi")]), (0.6, "line", [("Rohan Oza: ", "w"), ("one offer.", "oi")])],
 "deal":   [(0.0, "label", "THE DEAL THEY TOOK"), (0.12, "big", [("$400K for ", "w"), ("25%", "o")]), (0.6, "sub", [("Valuation: $4M → $1.6M", "p")])],
 "exit":   [(0.0, "label", "2025 · PEPSICO"), (0.15, "sub", [("Mother → Poppi", "p")]), (0.4, "big", [("$1.95B", "o")])],
 "math":   [(0.0, "label", "THE MATH"), (0.12, "line", [("Deal valuation: ", "w"), ("$1.6M", "o")]), (0.4, "line", [("Exit: ", "w"), ("$1.95B", "o")]),
            (0.72, "slam", [("1,000x+", "oi")])],
 "after":  [(0.0, "label", "THE FINE PRINT"), (0.15, "line", [("Tax benefits: ", "w"), ("$300M", "o")]), (0.55, "big", [("Net: $1.65B", "w")])],
 "lesson": [(0.0, "line", [("Don't just fight", "w")]), (0.18, "line", [("the valuation. Price the ", "w"), ("partner.", "oi")]),
            (0.55, "chips", ["Who you take it from", "What the buyer nets"])],
 "cta":    [(0.0, "label", "BEFORE YOU SIGN A DEAL"), (0.15, "big", [("Follow the ", "w"), ("money.", "oi")])],
}
