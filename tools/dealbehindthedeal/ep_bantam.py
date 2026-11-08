import json, os
SRC = "/home/claude/deals/bantam.mp4"
VO = "/home/claude/deals/vo/bantam_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP10"
ORDER = ["hook", "ask", "offers", "control", "growth", "exit", "math", "lesson", "cta"]
_b = "/home/claude/deals/vo/bantam_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {
 "hook": "Two Sharks wanted control of this bagel company, for two hundred seventy-five thousand dollars. A few years later, it sold for thirty-four million.",
 "ask": "Nick and Elyse Oleksak. Bantam Bagels: mini bagels, stuffed with cream cheese. They ask for two seventy-five, for eleven percent. A two and a half million dollar company.",
 "offers": "Barbara offers the same money, for fifty-one percent. Kevin wants fifty. That's not an investment. That's control. Then Lori offers thirty percent... and they make a deal with Lori.",
 "control": "In M&A terms, fifty-one percent means someone else runs your company. Fifty means you can't move without them. Keeping control kept every option open.",
 "growth": "With Lori, they land on QVC, then grocery freezers, then Starbucks.",
 "exit": "In 2018, T. Marzetti, owned by Lancaster Colony, buys Bantam for thirty-four million dollars, on sales of about twenty million a year.",
 "math": "That's roughly one point seven times sales. And if they'd given half to Barbara or Kevin, about seventeen million of that exit would have walked out the door.",
 "lesson": "The lesson: early money is the most expensive money. Never sell control just to get started.",
 "cta": "This is TaxBooks C F O. Before you sign a deal, follow the money.",
}
# Barbara's 51% offer -> Kevin's 50% offer (show captions)
COLD_SHOTS = [(201.0, 5.0, "fit"), (231.0, 5.0, "fit")]
SHOTS = {
 "hook":    [(208.5, 2.0, "full"), (213.0, 2.0, "full"), (300.0, 3.0, "fit")],
 "ask":     [(9.0, 2.5, "fit"), (27.0, 3.0, "fit"), (52.5, 2.0, "full"), (55.5, 2.0, "full"), (57.0, 1.5, "full"), (36.0, 3.0, "fit")],
 "offers":  [(202.5, 2.5, "fit"), (205.5, 1.5, "full"), (232.5, 3.0, "fit"), (249.0, 3.5, "fit"), (255.0, 2.0, "full")],
 "control": [(210.0, 2.0, "full"), (223.5, 2.0, "full"), (216.0, 2.0, "full"), (225.0, 2.0, "full")],
 "growth":  [(268.5, 1.5, "full"), (273.0, 1.5, "full"), (276.0, 1.5, "full"), (277.5, 1.5, "full")],
 "exit":    [(264.0, 1.5, "full"), (280.5, 2.5, "full"), (298.5, 2.5, "fit"), (301.5, 2.5, "fit")],
 "math":    [(295.5, 2.5, "full"), (304.5, 2.5, "full"), (312.0, 2.5, "full"), (316.5, 2.0, "fit")],
 "lesson":  [(265.5, 2.5, "fit"), (285.0, 2.5, "fit"), (292.5, 2.5, "full")],
 "cta":     [(321.0, 1.5, "full"), (313.5, 2.5, "fit")],
}
CALLOUTS = {
 "cold":    [(0.04, "label", "THE OFFERS, ON THE SHOW"), (0.1, "line", [("Barbara: ", "w"), ("51%", "o")]), (0.52, "line", [("Kevin: ", "w"), ("50%", "o")]),
             (0.75, "slam", [("Control.", "oi")])],
 "hook":    [(0.0, "big", [("$275K for control", "w")]), (0.55, "card", ("A few years later, it sold for", [("$34M", "o")]))],
 "ask":     [(0.0, "label", "THE ASK · BANTAM BAGELS"), (0.2, "sub", [("Mini bagels, stuffed", "p")]), (0.45, "big", [("$275K for 11%", "w")]),
             (0.72, "card", ("In plain English, the company is worth", [("$2.5M", "o")]))],
 "offers":  [(0.0, "label", "SAME MONEY, DIFFERENT DEALS"), (0.06, "line", [("Barbara: ", "w"), ("51%", "o")]), (0.2, "line", [("Kevin: ", "w"), ("50%", "o")]),
             (0.38, "slam", [("That's control.", "oi")]), (0.75, "line", [("Lori: ", "w"), ("30%", "o")])],
 "control": [(0.0, "label", "WHY THE PERCENT MATTERS"), (0.08, "line", [("51% ", "o"), ("= they run it", "w")]), (0.38, "line", [("50% ", "o"), ("= they can block it", "w")]),
             (0.7, "sub", [("Control kept every option open.", "p")])],
 "growth":  [(0.0, "label", "AFTER THE SHOW"), (0.12, "chips", ["QVC", "Grocery freezers", "Starbucks"])],
 "exit":    [(0.0, "label", "2018 · T. MARZETTI (LANCASTER COLONY)"), (0.1, "big", [("$34M", "o")]),
             (0.55, "card", ("On annual net sales of about", [("$20M", "w")]))],
 "math":    [(0.0, "label", "THE NAPKIN MATH"), (0.08, "big", [("~1.7x", "o"), (" sales", "w")]),
             (0.45, "card", ("Half the company to a Shark would have cost", [("~$17M", "oi")]))],
 "lesson":  [(0.0, "line", [("Early money is the most", "w")]), (0.2, "line", [("expensive ", "w"), ("money.", "oi")]),
             (0.55, "sub", [("Never sell control just to get started.", "p")])],
 "cta":     [(0.0, "label", "BEFORE YOU SIGN A DEAL"), (0.15, "big", [("Follow the ", "w"), ("money.", "oi")])],
}
