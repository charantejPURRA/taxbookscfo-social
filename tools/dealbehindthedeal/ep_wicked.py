import json
SRC = "/home/claude/deals/wicked.mp4"
VO = "/home/claude/deals/vo/wicked_vo.wav"
VO_END = 73.11
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP4"
SIL = json.loads("[" + open("/home/claude/deals/vo/wicked_sil.txt").read().strip().rstrip(",") + "]")
ORDER = ["hook", "ask", "sharks", "offer", "counter", "paid", "exit", "lesson", "cta"]
BT = {"hook": 0.0, "ask": 7.75, "sharks": 19.75, "offer": 25.70, "counter": 36.35, "paid": 42.34,
      "exit": 50.16, "lesson": 62.94, "cta": 68.51}
TEXT = {
 "hook": "Kevin wanted fifty cents for every cupcake they would ever sell. Forever. They said yes... almost.",
 "ask": "2013. A mother and daughter sell cupcakes in a jar. They ask for seventy-five thousand dollars for twenty percent. That says: our company is worth three hundred seventy-five thousand.",
 "sharks": "The Sharks love the cupcakes. They hate the numbers. One by one, they're out.",
 "offer": "Then Kevin offers seventy-five thousand, with no equity. Instead, one dollar for every jar sold until he's paid back. Then fifty cents a jar... forever.",
 "counter": "They counter at forty cents, and settle at forty-five. They keep one hundred percent of their company.",
 "paid": "And it paid off. Sales reportedly passed forty million dollars. Kevin reportedly earned over a million in royalties.",
 "exit": "Then in 2021, Hickory Farms bought the company. And here's what every buyer asks: who pays a royalty that never ends? It's an invisible passenger. It comes with the company when you sell.",
 "lesson": "A royalty isn't good or bad. It's a cost. Price it before you sign it.",
 "cta": "This is TaxBooks C F O. Before you sign a deal, follow the money.",
}
# hallway moment, original audio + the show's own subtitles
COLD_SHOTS = [(475.0, 12.9, "fit")]
SHOTS = {
 "hook":    [(441.0, 1.9, "fit"), (445.0, 1.9, "fit"), (448.0, 3.4, "fit")],
 "ask":     [(69.0, 3.9, "fit"), (73.0, 2.9, "fit"), (101.0, 2.9, "full"), (109.0, 2.9, "full")],
 "sharks":  [(159.0, 2.9, "full"), (186.0, 1.9, "full"), (176.0, 1.9, "full")],
 "offer":   [(222.0, 1.9, "full"), (227.0, 1.9, "full"), (236.0, 1.9, "full"), (168.0, 1.9, "full"), (489.0, 1.9, "full"), (453.0, 0.9, "full")],
 "counter": [(537.0, 4.0, "fit"), (542.0, 1.9, "full")],
 "paid":    [(560.0, 2.9, "fit"), (261.0, 4.0, "full"), (330.0, 1.5, "full")],
 "exit":    [(381.0, 2.9, "fit"), (572.0, 3.9, "fit"), (326.0, 1.9, "fit"), (259.0, 1.9, "full"), (384.0, 2.9, "full")],
 "lesson":  [(154.0, 1.9, "full"), (181.0, 1.9, "full"), (171.0, 1.9, "full")],
 "cta":     [(552.0, 1.9, "fit"), (567.0, 3.9, "fit")],
}
CALLOUTS = {
 "cold":    [(0.04, "label", "THE HALLWAY, AFTER KEVIN'S OFFER"), (0.12, "line", [("50¢ a jar.", "w")]), (0.5, "slam", [("Forever.", "oi")])],
 "hook":    [(0.0, "big", [("$75K", "w")]), (0.2, "line", [("for 50¢ a jar, ", "w"), ("forever.", "oi")]), (0.72, "sub", [("They said yes... almost.", "p")])],
 "ask":     [(0.0, "label", "THE ASK"), (0.05, "big", [("$75K for 20%", "w")]), (0.62, "card", ("In plain English, the company is worth", [("$375K", "o")]))],
 "sharks":  [(0.0, "label", "THE SHARKS"), (0.08, "line", [("Love the cupcakes.", "w")]), (0.4, "line", [("Hate the numbers.", "oi")])],
 "offer":   [(0.0, "label", "KEVIN'S OFFER"), (0.04, "big", [("$75K", "w"), (" · 0% equity", "p")]),
             (0.3, "sub", [("$1 a jar until he's paid back", "w")]), (0.62, "line", [("Then 50¢ a jar", "w")]), (0.86, "slam", [("FOREVER.", "oi")])],
 "counter": [(0.0, "label", "THE COUNTER"), (0.05, "line", [("Counter: 40¢. Deal: ", "w"), ("45¢.", "o")]),
             (0.55, "sub", [("They keep ", "w"), ("100%", "o"), (" of the company", "w")])],
 "paid":    [(0.0, "label", "AFTER THE SHOW (REPORTED)"), (0.12, "big", [("$40M+", "o"), (" in sales", "w")]),
             (0.55, "card", ("Kevin's royalties, reportedly", [("$1M+", "o")]))],
 "exit":    [(0.0, "label", "2021 · HICKORY FARMS ACQUIRES IT"), (0.3, "line", [("Who pays a royalty", "w")]),
             (0.38, "line", [("that never ends?", "oi")]), (0.62, "chips", ["The invisible passenger"])],
 "lesson":  [(0.0, "line", [("A royalty isn't good or bad.", "w")]), (0.3, "line", [("It's a ", "w"), ("cost.", "oi")]),
             (0.6, "sub", [("Price it before you sign it.", "p")])],
 "cta":     [(0.0, "label", "BEFORE YOU SIGN A DEAL"), (0.15, "big", [("Follow the ", "w"), ("money.", "oi")])],
}
