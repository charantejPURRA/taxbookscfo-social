import json, os
SRC = "/home/claude/deals/plated.mp4"
VO = "/home/claude/deals/vo/plated_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP9"
ORDER = ["hook", "ask", "deal", "fell", "exit", "why", "after", "lesson", "cta"]
_b = "/home/claude/deals/vo/plated_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {
 "hook": "A grocery giant paid a reported two hundred million dollars for a meal kit company. Two years later, it shut the service down.",
 "ask": "2014. Nick Taranto and Josh Hix. Plated: recipes and fresh ingredients, delivered. They ask for five hundred thousand, for four percent. A twelve and a half million dollar company.",
 "deal": "Mark offers five hundred thousand for five and a half percent, plus advisory shares. Handshake.",
 "fell": "But after the show, that deal fell apart. Months later, Kevin invested instead.",
 "exit": "Then 2017. Amazon buys Whole Foods, and grocers panic. Albertsons buys Plated for a reported two hundred million.",
 "why": "That's a strategic premium. Albertsons wasn't paying for profits. It was paying not to fall behind.",
 "after": "Then reality. In 2019, Albertsons wrote down thirty-eight million dollars on Plated, most of it the brand name itself. Months later, it ended the subscription service.",
 "lesson": "The lesson. For sellers: timing is value. Sell into the panic. For buyers: fear is not a valuation.",
 "cta": "This is TaxBooks C F O. Before you sign a deal, follow the money.",
}
# Mark's offer with the show's caption -> walking off with a deal
COLD_SHOTS = [(505.0, 8.0, "fit"), (552.5, 5.0, "fit")]
SHOTS = {
 "hook":   [(500.0, 2.5, "full"), (50.0, 2.5, "full"), (552.5, 2.5, "fit")],
 "ask":    [(2.5, 2.5, "full"), (15.0, 2.5, "fit"), (33.0, 3.0, "fit"), (37.5, 3.5, "fit"), (50.0, 2.5, "full"), (70.0, 2.5, "full")],
 "deal":   [(507.5, 3.5, "fit"), (515.0, 3.5, "fit"), (527.5, 2.0, "full"), (555.0, 2.5, "fit")],
 "fell":   [(485.0, 2.5, "full"), (480.0, 2.5, "full"), (495.0, 2.5, "full"), (360.0, 2.5, "full")],
 "exit":   [(72.5, 2.5, "full"), (22.5, 2.5, "fit"), (12.5, 2.5, "fit"), (67.5, 2.5, "full")],
 "why":    [(305.0, 2.5, "full"), (407.5, 2.5, "full"), (430.0, 2.5, "full")],
 "after":  [(367.5, 2.5, "full"), (290.0, 2.5, "full"), (302.5, 2.5, "full"), (65.0, 2.5, "full"), (465.0, 2.5, "full")],
 "lesson": [(547.5, 2.5, "full"), (540.0, 2.5, "full"), (577.5, 2.5, "full")],
 "cta":    [(562.5, 2.0, "fit"), (565.0, 2.5, "fit")],
}
CALLOUTS = {
 "cold":   [(0.04, "label", "MARK'S OFFER, ON THE SHOW"), (0.16, "line", [("$500K + advisory shares", "w")]), (0.62, "slam", [("Handshake.", "oi")])],
 "hook":   [(0.0, "big", [("~$200M", "o"), (" (reported)", "p")]), (0.55, "card", ("Two years later, the subscription", [("shut down.", "oi")]))],
 "ask":    [(0.0, "label", "THE ASK · 2014 · PLATED"), (0.2, "sub", [("Recipes + ingredients, delivered", "p")]), (0.45, "big", [("$500K for 4%", "w")]),
            (0.72, "card", ("In plain English, the company is worth", [("$12.5M", "o")]))],
 "deal":   [(0.0, "label", "MARK'S OFFER"), (0.1, "big", [("$500K for 5.56%", "w")]), (0.45, "sub", [("+ advisory shares", "p")]), (0.8, "slam", [("Handshake.", "oi")])],
 "fell":   [(0.0, "label", "AFTER THE CAMERAS"), (0.1, "line", [("Mark's deal: ", "w"), ("fell apart.", "oi")]), (0.55, "line", [("Kevin: ", "w"), ("invested.", "o")])],
 "exit":   [(0.0, "label", "2017"), (0.1, "line", [("Amazon buys Whole Foods.", "w")]), (0.35, "line", [("Grocers ", "w"), ("panic.", "oi")]),
            (0.6, "card", ("Albertsons buys Plated for a reported", [("$200M", "o")]))],
 "why":    [(0.0, "label", "THE STRATEGIC PREMIUM"), (0.1, "line", [("Not paying for profits.", "w")]), (0.45, "line", [("Paying not to ", "w"), ("fall behind.", "oi")])],
 "after":  [(0.0, "label", "2019 · ALBERTSONS SEC FILING"), (0.1, "big", [("$38.6M", "o"), (" write-down", "w")]), (0.38, "sub", [("Mostly the Plated brand name", "p")]),
            (0.7, "chips", ["Subscription ended"])],
 "lesson": [(0.0, "line", [("Sellers: ", "w"), ("timing is value.", "o")]), (0.5, "line", [("Buyers: ", "w"), ("fear is not a valuation.", "oi")])],
 "cta":    [(0.0, "label", "BEFORE YOU SIGN A DEAL"), (0.15, "big", [("Follow the ", "w"), ("money.", "oi")])],
}
