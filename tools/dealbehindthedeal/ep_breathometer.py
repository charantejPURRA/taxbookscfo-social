import json, os
SRC = "/home/claude/deals/breathometer.mp4"
VO = "/home/claude/deals/vo/breathometer_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP7"
ORDER = ["hook", "ask", "bid", "fomo", "ftc", "cuban", "lesson", "cta"]
_b = "/home/claude/deals/vo/breathometer_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {
 "hook": "All five Sharks bought in. One million dollars. Four years later, the government said the product didn't do what it promised.",
 "ask": "2013. Charles Yim. Breathometer: a breathalyzer that plugs into your phone. He pours the Sharks champagne, and asks for two hundred fifty thousand, for ten percent. A two and a half million dollar company.",
 "bid": "Then the bidding starts. Mark offers five hundred thousand. Kevin, Robert and Lori go to seven fifty. Daymond wants in too. He calls his CFO... and takes all five. One million dollars, for thirty percent.",
 "fomo": "Look at what just happened. The price went up because everyone wanted in. Nobody stopped to ask the only question that mattered: does it actually work?",
 "ftc": "In 2017, the FTC said Breathometer knew its devices often under-reported blood alcohol, while advertising them as accurate. The app was shut down. Customers were offered full refunds. The company settled without admitting the claims.",
 "cuban": "Mark Cuban later called it his worst Shark Tank investment ever.",
 "lesson": "In real M&A, this is why diligence exists. A buyer doesn't just buy revenue. They buy every promise the company ever made. Hype raises the price. It never lowers the risk.",
 "cta": "This is TaxBooks C F O. Before you sign a deal, follow the money.",
}
# "All five Sharks" caption -> the champagne toast
COLD_SHOTS = [(527.0, 7.5, "fit"), (650.5, 6.5, "fit")]
SHOTS = {
 "hook":   [(59.4, 2.2, "full"), (143.0, 2.2, "full"), (651.4, 2.5, "fit")],
 "ask":    [(2.2, 2.0, "full"), (33.0, 3.0, "fit"), (94.6, 2.2, "full"), (39.6, 2.2, "fit"), (191.4, 2.0, "full"), (207.0, 3.0, "fit")],
 "bid":    [(269.6, 2.5, "fit"), (352.5, 3.5, "fit"), (379.6, 2.5, "fit"), (554.6, 3.0, "fit"), (561.2, 2.0, "full"), (529.0, 3.5, "fit")],
 "fomo":   [(241.0, 2.2, "fit"), (245.4, 2.2, "full"), (274.0, 2.2, "fit"), (230.0, 2.0, "full")],
 "ftc":    [(180.4, 2.2, "full"), (184.8, 2.2, "full"), (191.4, 2.2, "full"), (359.8, 2.5, "full"), (397.2, 2.5, "full"), (96.8, 2.0, "full")],
 "cuban":  [(257.0, 2.0, "full"), (283.0, 2.0, "full"), (508.0, 2.0, "full")],
 "lesson": [(627.2, 2.2, "full"), (589.8, 2.2, "full"), (622.8, 2.2, "full"), (399.4, 2.2, "full")],
 "cta":    [(596.4, 2.0, "full"), (658.0, 2.0, "fit")],
}
CALLOUTS = {
 "cold":   [(0.04, "label", "THE ONLY ALL-FIVE-SHARK DEAL, 2013"), (0.16, "line", [("$1M for ", "w"), ("30%", "o")]), (0.62, "slam", [("Cheers.", "oi")])],
 "hook":   [(0.0, "big", [("5 Sharks. ", "w"), ("$1M.", "o")]), (0.5, "card", ("Four years later, the FTC said the product", [("didn't deliver.", "oi")]))],
 "ask":    [(0.0, "label", "THE ASK · 2013 · BREATHOMETER"), (0.2, "sub", [("A breathalyzer for your phone", "p")]), (0.45, "big", [("$250K for 10%", "w")]),
            (0.72, "card", ("In plain English, the company is worth", [("$2.5M", "o")]))],
 "bid":    [(0.0, "label", "THE BIDDING WAR"), (0.06, "line", [("Mark: ", "w"), ("$500K", "o")]), (0.22, "line", [("Kevin, Robert, Lori: ", "w"), ("$750K", "o")]),
            (0.4, "line", [("Daymond: ", "w"), ("in.", "o")]), (0.55, "chips", ["He calls his CFO"]), (0.8, "slam", [("$1M for 30%", "oi")])],
 "fomo":   [(0.0, "label", "WHAT JUST HAPPENED"), (0.1, "line", [("Price went ", "w"), ("up.", "oi")]), (0.55, "card", ("Nobody asked", [("does it work?", "oi")]))],
 "ftc":    [(0.0, "label", "2017 · FEDERAL TRADE COMMISSION"), (0.08, "line", [("Under-reported blood alcohol", "w")]), (0.25, "sub", [("while advertised as accurate (FTC complaint)", "p")]),
            (0.5, "chips", ["App shut down", "Full refunds"]), (0.78, "sub", [("Settled without admitting the allegations", "p")])],
 "cuban":  [(0.0, "label", "MARK CUBAN, LATER"), (0.15, "slam", [("\"My worst investment.\"", "oi")])],
 "lesson": [(0.0, "label", "THE M&A LESSON"), (0.1, "line", [("Buyers don't just buy revenue.", "w")]), (0.32, "line", [("They buy every ", "w"), ("promise.", "oi")]),
            (0.68, "card", ("Hype raises the price. It never lowers", [("the risk.", "oi")]))],
 "cta":    [(0.0, "label", "BEFORE YOU SIGN A DEAL"), (0.15, "big", [("Follow the ", "w"), ("money.", "oi")])],
}
