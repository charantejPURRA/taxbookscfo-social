import json, os
SRC = "/home/claude/deals/groovebook.mp4"
VO = "/home/claude/deals/vo/groovebook_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP6"
ORDER = ["hook", "ask", "offers", "deal", "exit", "math", "after", "lesson", "cta"]
_b = "/home/claude/deals/vo/groovebook_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {
 "hook": "Kevin offered to buy the whole company for seven hundred fifty thousand dollars. Ten months later, it sold for fourteen and a half million.",
 "ask": "2014. Julie and Brian Whiteman. GrooveBook: a hundred phone photos, printed and mailed every month, for two ninety-nine. They ask for a hundred fifty thousand, for twenty percent. That's a seven hundred fifty thousand dollar company.",
 "offers": "Then the offers. Kevin: buy all of it. Lori and Robert: half of everything.",
 "deal": "They take Mark and Kevin's deal instead. Same hundred fifty thousand... but for eighty percent of the licensing rights. Not the company. They keep one hundred percent of the business.",
 "exit": "Ten months later, Shutterfly buys GrooveBook for fourteen and a half million dollars. Part of that price was an earn-out: money paid later, only if the business hits its targets.",
 "math": "Now run the other deals. Sell it all to Kevin: seven hundred fifty thousand. Give half to Lori and Robert: half the exit, gone. They gave away a side door... and kept the house.",
 "after": "And the twist. In 2022, Shutterfly shut GrooveBook down. Once you sell, the buyer decides what lives.",
 "lesson": "The lesson: the headline price isn't the price. Read the structure. What are you giving up, and when do you actually get paid?",
 "cta": "This is TaxBooks C F O. Before you sign a deal, follow the money.",
}
# Kevin's $750K-for-100% offer (show caption) -> the founders celebrating the deal they actually took
COLD_SHOTS = [(439.0, 8.5, "fit"), (775.0, 5.0, "fit")]
SHOTS = {
 "hook":   [(434.0, 2.0, "full"), (770.0, 2.0, "fit"), (779.0, 2.5, "fit")],
 "ask":    [(7.5, 3.0, "fit"), (45.0, 3.0, "fit"), (57.5, 2.0, "full"), (62.5, 2.5, "full"), (50.5, 3.0, "fit")],
 "offers": [(443.0, 3.5, "fit"), (626.0, 4.0, "fit")],
 "deal":   [(665.0, 5.5, "fit"), (676.0, 3.0, "full"), (777.0, 2.0, "fit")],
 "exit":   [(67.5, 2.5, "fit"), (322.5, 2.5, "full"), (312.5, 2.5, "full"), (80.0, 2.5, "fit")],
 "math":   [(300.0, 2.5, "full"), (627.5, 2.5, "fit"), (685.0, 2.5, "fit")],
 "after":  [(242.5, 2.5, "full"), (452.5, 3.0, "full"), (57.5, 2.0, "full")],
 "lesson": [(247.5, 2.0, "full"), (560.0, 2.0, "full"), (692.5, 2.0, "full")],
 "cta":    [(778.0, 1.5, "fit"), (782.5, 2.0, "fit")],
}
CALLOUTS = {
 "cold":   [(0.04, "label", "KEVIN'S OFFER, ON THE SHOW"), (0.16, "line", [("$750K for ", "w"), ("100%", "o")]), (0.62, "slam", [("They said no.", "oi")])],
 "hook":   [(0.0, "big", [("$750K", "w")]), (0.5, "card", ("Ten months later, it sold for", [("$14.5M", "o")]))],
 "ask":    [(0.0, "label", "THE ASK · 2014 · GROOVEBOOK"), (0.25, "sub", [("100 photos a month · $2.99", "p")]), (0.45, "big", [("$150K for 20%", "w")]),
            (0.72, "card", ("In plain English, the company is worth", [("$750K", "o")]))],
 "offers": [(0.0, "label", "THE OFFERS"), (0.25, "line", [("Kevin: ", "w"), ("all of it.", "oi")]), (0.6, "line", [("Lori & Robert: ", "w"), ("half.", "oi")])],
 "deal":   [(0.0, "label", "THE DEAL THEY TOOK"), (0.12, "big", [("80% of the ", "w"), ("license", "o")]), (0.45, "sub", [("Not the company.", "p")]),
            (0.72, "slam", [("They keep 100%.", "oi")])],
 "exit":   [(0.0, "label", "10 MONTHS LATER · SHUTTERFLY"), (0.08, "big", [("$14.5M", "o")]),
            (0.5, "card", ("Part of the price was an", [("earn-out", "oi")])), (0.75, "sub", [("Paid later, only if targets are hit", "w")])],
 "math":   [(0.0, "label", "THE OTHER DEALS"), (0.12, "line", [("Kevin's buyout: ", "w"), ("$750K", "o")]),
            (0.4, "line", [("Lori & Robert: ", "w"), ("half the exit", "o")]), (0.72, "slam", [("They kept the house.", "oi")])],
 "after":  [(0.0, "label", "2022"), (0.15, "big", [("Shut down.", "w")]), (0.55, "sub", [("Once you sell, the buyer decides what lives.", "p")])],
 "lesson": [(0.0, "line", [("The headline price", "w")]), (0.18, "line", [("isn't the ", "w"), ("price.", "oi")]),
            (0.5, "chips", ["What you give", "When you get paid"])],
 "cta":    [(0.0, "label", "BEFORE YOU SIGN A DEAL"), (0.15, "big", [("Follow the ", "w"), ("money.", "oi")])],
}
