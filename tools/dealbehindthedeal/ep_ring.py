import json, os
# EP3 Ring (DoorBot). BT / VO_END / SIL are filled once the narration is generated (beats split on [long pause]).
SRC = "/home/claude/deals/ring.mp4"
VO = "/home/claude/deals/vo/ring_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP3"
ORDER = ["hook", "ask", "demo", "out", "kevin", "counter", "walk", "after", "math", "lesson", "cta"]
_b = "/home/claude/deals/vo/ring_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {
 "hook": "He walked away from the only offer in the room. Five years later, Amazon bought his company for a reported billion dollars. Walking away... was the smartest thing he did.",
 "ask": "2013. Jamie Siminoff walks in with a video doorbell called DoorBot. He asks for seven hundred thousand dollars, for ten percent. In plain English: my company is worth seven million dollars.",
 "demo": "He even built a front door on the set. Someone rings the bell, and your phone rings, wherever you are.",
 "out": "But the Sharks see risk. One by one, they're out.",
 "kevin": "Then Kevin makes the only offer. Seven hundred thousand dollars, as a royalty. Ten percent of every sale, until he's paid back. Then seven percent... forever.",
 "counter": "Jamie counters with something smarter. Make it a loan: seven hundred thousand at ten percent interest, plus three percent of the company. A loan ends. A royalty never does.",
 "walk": "Kevin says no. Jamie walks out with nothing.",
 "after": "Except he walks out owning one hundred percent of his company. He renames it Ring. Raises money from investors who share his vision. And in 2018, Amazon buys Ring for a reported billion dollars.",
 "math": "Now imagine seven percent of every Ring doorbell sold, paid to someone else, forever. Every future buyer would have priced that in.",
 "lesson": "The lesson for every owner: the wrong deal is worse than no deal. Don't sell your future to fix today's problem.",
 "cta": "This is TaxBooks C F O. Before you sign a deal, follow the money.",
}
# Kevin's offer with the show's on-screen terms (10% royalty -> 7%, + 5% equity)
COLD_SHOTS = [(450.0, 11.9, "fit")]
SHOTS = {
 "hook":    [(540.0, 2.9, "fit"), (553.0, 1.5, "full"), (297.0, 2.5, "fit"), (436.0, 2.0, "full")],
 "ask":     [(1.0, 3.9, "fit"), (8.0, 1.9, "full"), (40.0, 3.5, "fit"), (45.0, 2.9, "fit")],
 "demo":    [(79.0, 2.5, "fit"), (91.0, 2.5, "fit"), (88.0, 2.0, "fit"), (112.0, 1.9, "fit"), (119.0, 2.5, "fit")],
 "out":     [(163.0, 1.9, "full"), (314.0, 1.9, "full"), (329.0, 1.9, "full"), (333.0, 1.9, "full")],
 "kevin":   [(420.0, 2.5, "full"), (450.0, 3.0, "fit"), (454.5, 3.5, "fit"), (459.0, 2.9, "fit")],
 "counter": [(481.0, 2.9, "full"), (485.0, 5.9, "fit"), (466.0, 2.5, "full")],
 "walk":    [(506.0, 2.5, "full"), (514.0, 2.5, "full"), (540.0, 2.9, "fit")],
 "after":   [(553.0, 1.5, "full"), (555.0, 4.0, "fit"), (559.0, 3.9, "fit"), (297.0, 2.5, "fit")],
 "math":    [(119.0, 3.5, "fit"), (424.0, 2.0, "full"), (439.0, 2.0, "full")],
 "lesson":  [(528.0, 2.0, "fit"), (468.0, 2.0, "full"), (334.0, 1.9, "fit")],
 "cta":     [(541.0, 1.9, "fit"), (553.0, 1.5, "full")],
}
CALLOUTS = {
 "cold":    [(0.04, "label", "KEVIN'S OFFER, ON THE SHOW"), (0.14, "line", [("10% royalty. Then 7%.", "w")]), (0.55, "slam", [("Forever.", "oi")])],
 "hook":    [(0.0, "big", [("Walked away.", "w")]), (0.45, "card", ("Five years later, Amazon reportedly paid", [("$1B", "o")]))],
 "ask":     [(0.0, "label", "THE ASK · 2013 · DOORBOT"), (0.08, "big", [("$700K for 10%", "w")]), (0.62, "card", ("In plain English, the company is worth", [("$7M", "o")]))],
 "demo":    [(0.0, "label", "THE PRODUCT"), (0.15, "line", [("Doorbell rings.", "w")]), (0.5, "line", [("Your phone rings.", "oi")])],
 "out":     [(0.0, "label", "THE SHARKS"), (0.3, "big", [("Out. Out. Out.", "w")])],
 "kevin":   [(0.0, "label", "KEVIN'S OFFER"), (0.04, "big", [("$700K", "w"), (" · royalty", "p")]),
             (0.35, "sub", [("10% of sales until he's paid back", "w")]), (0.62, "line", [("Then 7%", "w")]), (0.85, "slam", [("FOREVER.", "oi")])],
 "counter": [(0.0, "label", "JAMIE'S COUNTER"), (0.05, "line", [("Loan: $700K at 10%", "w")]), (0.3, "sub", [("+ 3% equity", "p")]),
             (0.62, "card", ("A loan ends. A royalty", [("never does.", "oi")]))],
 "walk":    [(0.0, "label", "NO DEAL"), (0.35, "big", [("$0", "w")])],
 "after":   [(0.0, "label", "AFTER THE SHOW (REPORTED)"), (0.08, "big", [("100%", "o"), (" ownership", "w")]),
             (0.3, "chips", ["DoorBot becomes Ring"]), (0.7, "card", ("2018, Amazon buys Ring for a reported", [("$1B", "o")]))],
 "math":    [(0.0, "label", "THE NAPKIN MATH"), (0.1, "line", [("7% of every doorbell", "w")]), (0.38, "line", [("paid to someone else.", "oi")]),
             (0.7, "sub", [("Every buyer prices that in.", "p")])],
 "lesson":  [(0.0, "line", [("The wrong deal is worse", "w")]), (0.2, "line", [("than ", "w"), ("no deal.", "oi")]),
             (0.6, "sub", [("Don't sell your future to fix today's problem.", "p")])],
 "cta":     [(0.0, "label", "BEFORE YOU SIGN A DEAL"), (0.15, "big", [("Follow the ", "w"), ("money.", "oi")])],
}
