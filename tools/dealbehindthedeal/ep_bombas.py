import json, os
# EP5 Bombas. BT / VO_END / SIL are filled once the narration is generated (beats split on [long pause]).
SRC = "/home/claude/deals/bombas.mp4"
VO = "/home/claude/deals/vo/bombas_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP5"
ORDER = ["hook", "ask", "sharks", "offer", "counter", "deal", "why", "paid", "lesson", "cta"]
_b = "/home/claude/deals/vo/bombas_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {
 "hook": "They gave up three and a half times the equity they came in to sell... and it may be the best deal ever made in the Tank. Because the money wasn't the prize.",
 "ask": "2014. Two founders. One sock company: Bombas. Buy a pair, they donate a pair. They ask for two hundred thousand dollars for five percent. That says: we're worth four million.",
 "sharks": "The Sharks like the mission. Not the price. The founders come down to ten percent.",
 "offer": "Then Daymond, the man who built FUBU, makes his move. Twenty percent. That cuts their value to one million.",
 "counter": "They counter with something smarter than a number. Fifteen percent... plus a two hundred thousand dollar line of credit.",
 "deal": "Daymond lands at seventeen and a half percent, and he'll finance their inventory. Deal.",
 "why": "Here's what they understood. A sock company doesn't die from a low valuation. It dies from running out of cash between buying inventory and getting paid. Daymond's money fixed that gap.",
 "paid": "Bombas has reportedly passed one billion dollars in lifetime sales.",
 "lesson": "The lesson for every owner: don't just negotiate the price. Negotiate what the money does.",
 "cta": "This is TaxBooks C F O. Before you sign a deal, follow the money.",
}
# Daymond's final counter (on-screen caption: 17.5% + financing of inventory) -> the hug
COLD_SHOTS = [(575.0, 12.4, "fit"), (618.6, 4.4, "fit")]
SHOTS = {
 "hook":    [(585.0, 2.0, "full"), (620.0, 2.0, "fit"), (592.0, 2.0, "fit")],
 "ask":     [(14.0, 3.0, "fit"), (22.0, 3.0, "full"), (38.0, 3.0, "fit"), (42.0, 4.0, "fit")],
 "sharks":  [(180.0, 1.9, "full"), (338.0, 1.9, "full"), (360.0, 1.9, "full"), (448.0, 4.0, "fit")],
 "offer":   [(474.0, 2.5, "full"), (488.0, 4.0, "fit"), (500.0, 2.0, "full")],
 "counter": [(568.0, 2.0, "full"), (570.5, 4.0, "fit"), (576.0, 2.0, "full")],
 "deal":    [(579.5, 3.5, "fit"), (595.0, 2.0, "full"), (619.0, 3.0, "fit")],
 "why":     [(92.0, 2.5, "full"), (104.0, 2.5, "full"), (22.0, 2.0, "full"), (602.0, 2.0, "full"), (130.0, 2.0, "full")],
 "paid":    [(440.0, 2.5, "full"), (524.0, 2.5, "full")],
 "lesson":  [(552.0, 2.0, "full"), (224.0, 2.0, "full"), (586.0, 2.0, "full")],
 "cta":     [(616.0, 2.0, "fit"), (622.0, 2.5, "fit")],
}
CALLOUTS = {
 "cold":    [(0.04, "label", "DAYMOND'S FINAL COUNTER"), (0.14, "line", [("17.5%", "w")]), (0.45, "slam", [("+ the inventory.", "oi")])],
 "hook":    [(0.0, "big", [("5%", "w"), (" became ", "p"), ("17.5%", "o")]), (0.6, "sub", [("The money wasn't the prize.", "p")])],
 "ask":     [(0.0, "label", "THE ASK"), (0.05, "big", [("$200K for 5%", "w")]), (0.62, "card", ("In plain English, the company is worth", [("$4M", "o")]))],
 "sharks":  [(0.0, "label", "THE SHARKS"), (0.08, "line", [("Love the mission.", "w")]), (0.35, "line", [("Not the price.", "oi")]),
             (0.7, "sub", [("Founders drop to ", "w"), ("10%", "o")])],
 "offer":   [(0.0, "label", "DAYMOND'S OFFER"), (0.1, "big", [("20%", "w")]), (0.55, "card", ("Valuation falls to", [("$1M", "o")]))],
 "counter": [(0.0, "label", "THE COUNTER"), (0.3, "line", [("15%", "w")]), (0.6, "line", [("+ $200K line of credit", "oi")])],
 "deal":    [(0.0, "label", "THE DEAL"), (0.08, "big", [("17.5%", "o")]), (0.45, "sub", [("+ Daymond finances the inventory", "w")]),
             (0.85, "slam", [("Deal.", "oi")])],
 "why":     [(0.0, "label", "THE REAL PROBLEM"), (0.25, "line", [("Not valuation.", "w")]), (0.45, "line", [("Cash.", "oi")]),
             (0.62, "chips", ["Buy inventory", "Wait", "Get paid"])],
 "paid":    [(0.0, "label", "AFTER THE SHOW (REPORTED)"), (0.1, "big", [("$1B+", "o")]), (0.5, "sub", [("in lifetime sales", "w")])],
 "lesson":  [(0.0, "line", [("Don't just negotiate the price.", "w")]), (0.45, "line", [("Negotiate what the ", "w"), ("money does.", "oi")])],
 "cta":     [(0.0, "label", "BEFORE YOU SIGN A DEAL"), (0.15, "big", [("Follow the ", "w"), ("money.", "oi")])],
}
