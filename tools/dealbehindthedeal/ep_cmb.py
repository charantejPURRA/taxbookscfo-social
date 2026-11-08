import json, os
SRC = "/home/claude/deals/coffeemeetsbagel.mp4"
VO = "/home/claude/deals/vo/cmb_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP8"
ORDER = ["hook", "ask", "offer", "math", "why", "cost", "verdict", "lesson", "cta"]
_b = "/home/claude/deals/vo/cmb_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {
 "hook": "Mark Cuban said he was out. Then he offered thirty million dollars, for the whole company. They said no. Without blinking.",
 "ask": "2015. Three sisters: Dawoon, Arum and Soo Kang. Coffee Meets Bagel, a dating app built for women. They ask for five hundred thousand, for five percent. That says: we're worth ten million.",
 "offer": "The Sharks push back on the numbers. One by one, they're out. Then Mark comes back. Thirty million dollars. All of it.",
 "math": "Think about that. Three times their own valuation. Cash. No dilution. No more risk. In M&A terms, that's a full exit at a big premium.",
 "why": "They said no because they believed they were building the next Match. After the show, they raised nearly twenty million dollars from investors to chase it.",
 "cost": "But here's what most people miss. Every round they raised meant selling more of the company. Thirty million for one hundred percent... versus a smaller piece of something bigger. That's the real trade.",
 "verdict": "Was it the right call? The founders say yes. The answer depends on what their shares are worth today, and that number isn't public.",
 "lesson": "The lesson: an offer isn't just a price. Weigh it against the risk, the dilution, and the years it takes to beat it.",
 "cta": "This is TaxBooks C F O. Before you sign a deal, follow the money.",
}
# Mark's comeback -> the sisters' answer
COLD_SHOTS = [(669.0, 7.0, "fit"), (676.0, 4.0, "fit")]
SHOTS = {
 "hook":    [(673.0, 2.0, "full"), (677.0, 2.0, "full"), (687.0, 3.0, "fit")],
 "ask":     [(4.6, 2.3, "full"), (18.4, 2.3, "full"), (87.4, 2.3, "fit"), (102.0, 3.0, "fit"), (106.0, 3.5, "fit"), (163.3, 2.5, "fit")],
 "offer":   [(193.2, 2.0, "full"), (184.0, 2.0, "full"), (147.2, 2.0, "full"), (568.2, 2.0, "full"), (625.0, 2.5, "full"), (669.0, 3.0, "full")],
 "math":    [(680.0, 2.0, "full"), (59.8, 2.3, "full"), (673.0, 2.0, "full")],
 "why":     [(62.1, 2.3, "full"), (66.7, 2.3, "full"), (69.0, 2.3, "full"), (71.3, 2.3, "full"), (691.0, 3.0, "fit")],
 "cost":    [(559.0, 2.3, "full"), (611.9, 2.3, "full"), (539.0, 2.0, "full"), (225.4, 2.3, "full")],
 "verdict": [(665.0, 2.5, "full"), (676.0, 2.5, "fit"), (694.0, 2.5, "fit")],
 "lesson":  [(513.0, 2.2, "full"), (655.6, 2.2, "full"), (593.5, 2.2, "full")],
 "cta":     [(687.5, 2.0, "fit"), (692.0, 2.5, "fit")],
}
CALLOUTS = {
 "cold":    [(0.04, "label", "MARK CUBAN, AFTER SAYING HE WAS OUT"), (0.3, "big", [("$30M", "o")]), (0.55, "line", [("for ", "w"), ("100%", "oi")])],
 "hook":    [(0.0, "big", [("$30M offer", "w")]), (0.55, "slam", [("They said no.", "oi")])],
 "ask":     [(0.0, "label", "THE ASK · 2015 · COFFEE MEETS BAGEL"), (0.25, "big", [("$500K for 5%", "w")]),
             (0.65, "card", ("In plain English, the company is worth", [("$10M", "o")]))],
 "offer":   [(0.0, "label", "THE SHARKS"), (0.1, "line", [("Out. Out. Out.", "w")]), (0.6, "big", [("Mark: ", "w"), ("$30M", "o")]), (0.85, "sub", [("for all of it", "p")])],
 "math":    [(0.0, "label", "THE NAPKIN MATH"), (0.1, "big", [("3x", "o"), (" their own price", "w")]), (0.4, "chips", ["Cash", "No dilution", "No risk"]),
             (0.75, "sub", [("A full exit at a premium", "p")])],
 "why":     [(0.0, "label", "WHY THEY SAID NO"), (0.1, "line", [("\"The next Match.\"", "oi")]), (0.55, "card", ("Raised from investors after the show", [("~$20M", "o")]))],
 "cost":    [(0.0, "label", "WHAT MOST PEOPLE MISS"), (0.15, "line", [("Every round = ", "w"), ("dilution.", "oi")]),
             (0.55, "line", [("100% of $30M", "w")]), (0.7, "line", [("vs. a slice of ", "w"), ("something bigger", "o")])],
 "verdict": [(0.0, "label", "THE VERDICT"), (0.15, "line", [("Founders: ", "w"), ("right call.", "o")]), (0.55, "sub", [("Today's share value isn't public.", "p")])],
 "lesson":  [(0.0, "line", [("An offer isn't just a ", "w"), ("price.", "oi")]), (0.4, "chips", ["Risk", "Dilution", "Time"])],
 "cta":     [(0.0, "label", "BEFORE YOU SIGN A DEAL"), (0.15, "big", [("Follow the ", "w"), ("money.", "oi")])],
}
