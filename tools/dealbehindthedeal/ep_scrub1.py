import json, sys
sys.path.insert(0, "/home/claude/ep1v6")
from beats import BEATS
SRC = "/home/claude/st/src.mp4"
VO = "/home/claude/st/vo_final.wav"
VO_END = 108.22
TAIL = 0.6
EPLABEL = "DEAL BEHIND THE DEAL · EP1"
ORDER = [b[0] for b in BEATS]
TEXT = {b[0]: b[1] for b in BEATS}
BT = {"hook": 0.0, "walkin": 6.57, "ask": 13.67, "demo": 25.28, "kevin": 31.90, "lowball": 42.93, "jumpin": 50.18,
      "miss": 55.10, "climb": 63.88, "final": 72.12, "lesson": 81.64, "cta": 97.22}
SIL = json.loads("[" + open("/home/claude/ep1v6/sil_final.txt").read().strip().rstrip(",") + "]")
COLD_SHOTS = [(682.0, 10.0, "full")]
SHOTS = {
    "hook":    [(691.9, 4.6, "full"), (0.5, 3.16, "full")],
    "walkin":  [(3.66, 5.0, "full"), (17.0, 2.83, "full")],
    "ask":     [(19.83, 7.2, "fit"), (29.7, 3.0, "full"), (139.3, 2.24, "full")],
    "demo":    [(46.3, 4.0, "full"), (71.8, 3.25, "full")],
    "kevin":   [(171.1, 6.7, "full"), (330.2, 4.98, "fit")],
    "lowball": [(262.8, 3.3, "full"), (449.3, 4.58, "full")],
    "jumpin":  [(366.0, 1.75, "fit"), (421.1, 1.75, "fit"), (359.0, 1.76, "full")],
    "miss":    [(287.4, 5.8, "fit"), (533.2, 3.26, "fit")],
    "climb":   [(592.0, 2.6, "fit"), (604.2, 2.6, "fit"), (613.7, 2.6, "fit"), (625.7, 2.67, "full")],
    "final":   [(656.8, 3.0, "full"), (670.4, 2.0, "full"), (689.6, 2.88, "full")],
    "lesson":  [(692.5, 3.27, "full"), (182.9, 4.97, "fit"), (540.9, 3.9, "full")],
    "cta":     [(700.8, 8.2, "full"), (117.5, 3.2, "fit"), (120.6, 3.55, "fit")],
}
CALLOUTS = {
 "cold":    [(0.05, "label", "THE MOMENT THE DEAL CLOSED"), (0.55, "slam", [("DEAL.", "oi")])],
 "hook":    [(0.0, "big", [("$200K offer", "w")]), (0.45, "line", [("became a ", "w"), ("$1M deal.", "oi")])],
 "walkin":  [(0.0, "label", "OCTOBER 2012 · SCRUB DADDY")],
 "ask":     [(0.0, "label", "THE ASK"), (0.05, "big", [("$100K for 10%", "w")]), (0.6, "card", ("In plain English, the company is worth", [("$1M", "o")]))],
 "demo":    [(0.1, "line", [("No argument.", "w")]), (0.45, "line", [("Let the product ", "w"), ("talk.", "oi")])],
 "kevin":   [(0.0, "label", "KEVIN GOES FIRST"), (0.08, "big", [("$100K for 50%", "w")]), (0.45, "card", ("That values the company at", [("$200K", "o")])),
             (0.8, "sub", [("80% below the ask", "p")])],
 "lowball": [(0.0, "slam", [("THE LOWBALL.", "oi")]), (0.5, "sub", [("How badly do you need this deal?", "p")])],
 "jumpin":  [(0.0, "label", "THEN THE OTHER SHARKS"), (0.15, "chips", ["Daymond", "Lori", "Daymond again"])],
 "miss":    [(0.1, "line", [("Same sponge.", "w")]), (0.32, "line", [("Same numbers.", "w")]), (0.7, "slam", [("COMPETITION.", "oi")])],
 "climb":   [(0.0, "label", "IMPLIED VALUE, BID BY BID"), (0.3, "chips", ["$300K", "$600K", "$700K", "$800K"])],
 "final":   [(0.0, "label", "THE FINAL DEAL"), (0.08, "big", [("$200K for 20%", "w")]), (0.4, "card", ("Exactly his ask", [("$1M", "o")])),
             (0.75, "sub", [("5x the first offer", "p")])],
 "lesson":  [(0.05, "line", [("One buyer sets the price.", "w")]), (0.3, "line", [("Several buyers ", "w"), ("fight over it.", "oi")]),
             (0.65, "chips", ["Run a process"])],
 "cta":     [(0.0, "label", "SELLING YOUR BUSINESS SOMEDAY?"), (0.1, "line", [("Put more than one buyer", "w")]), (0.25, "line", [("in the room.", "oi")]),
             (0.75, "sub", [("Next: Kevin's royalty offer", "p")])],
}
