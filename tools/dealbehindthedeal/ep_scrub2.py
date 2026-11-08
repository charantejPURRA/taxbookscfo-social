import json
SRC = "/home/claude/st/src.mp4"
VO = "/home/claude/ep2/vo.wav"
VO_END = 73.30
TAIL = 0.6
EPLABEL = "DEAL BEHIND THE DEAL · EP2"
ORDER = ["hook", "what", "math", "margin", "scale", "exit", "lesson", "cta"]
BT = {"hook": 0.0, "what": 8.86, "math": 18.44, "margin": 28.51, "scale": 38.64, "exit": 48.99, "lesson": 60.11, "cta": 71.23}
TEXT = {
 "hook": "Kevin offered him a hundred thousand dollars, and let him keep one hundred percent of his company. It may have been the most expensive offer in the room.",
 "what": "It's called a royalty. Kevin doesn't buy a single share. Instead, he gets paid on every sponge sold, whether the company makes a profit or not.",
 "math": "Fifty cents a sponge, until his hundred thousand is paid back. That's just two hundred thousand sponges. Then ten cents a sponge... forever.",
 "margin": "Ten cents sounds small. But this sponge cost about a dollar to make. That ten cents comes off the top, before payroll, before rent, before a single ad.",
 "scale": "Now picture fifty million sponges a year. That's five million dollars a year to Kevin. Every year. For one hundred-thousand-dollar check.",
 "exit": "And here's what a buyer of your business sees. A royalty that never ends doesn't disappear when you sell. Buyers treat it like debt. They cut your price, or make you buy it out first.",
 "lesson": "So never compare offers by the size of the check. Compare what each one costs you over time. Royalties, earn-outs, revenue shares. Read the structure, not the headline.",
 "cta": "This is TaxBooksCFO.",
}
SIL = json.loads("[" + open("/home/claude/ep2/sil.txt").read().strip().rstrip(",") + "]")
COLD_SHOTS = [(455.0, 7.0, "fit")]
SHOTS = {
 "hook":   [(441.5, 2.9, "full"), (446.5, 1.5, "full"), (665.0, 1.4, "full"), (666.5, 1.4, "full"), (449.39, 3.2, "full")],
 "what":   [(641.0, 2.9, "full"), (91.0, 2.6, "full"), (46.3, 3.8, "full")],
 "math":   [(79.99, 2.9, "full"), (462.0, 1.4, "fit"), (463.5, 1.4, "fit"), (465.0, 1.4, "fit"), (466.5, 1.4, "fit"), (444.5, 1.9, "full")],
 "margin": [(98.3, 3.4, "full"), (155.7, 3.7, "full"), (106.3, 3.6, "full")],
 "scale":  [(207.15, 3.1, "full"), (287.4, 3.0, "fit"), (117.5, 1.9, "fit"), (71.8, 3.4, "full")],
 "exit":   [(694.0, 1.7, "full"), (648.0, 4.9, "fit"), (533.2, 4.2, "fit")],
 "lesson": [(529.64, 3.5, "full"), (540.91, 2.6, "full"), (262.8, 3.3, "full"), (640.0, 0.9, "full")],
 "cta":    [(700.84, 2.5, "full")],
}
CALLOUTS = {
 "cold":   [(0.05, "label", "KEVIN'S OFFER, ON THE SHOW"), (0.5, "slam", [("A royalty.", "oi")])],
 "hook":   [(0.0, "big", [("$100K", "w")]), (0.3, "line", [("He keeps ", "w"), ("100%.", "o")]), (0.65, "sub", [("The most expensive offer in the room?", "p")])],
 "what":   [(0.0, "label", "IT'S CALLED A ROYALTY"), (0.15, "line", [("No shares.", "w")]), (0.45, "line", [("Paid on ", "w"), ("every sponge.", "oi")]),
            (0.75, "sub", [("Profit or not", "p")])],
 "math":   [(0.0, "label", "THE TERMS"), (0.05, "line", [("50¢ a sponge until repaid", "w")]), (0.35, "sub", [("= just 200,000 sponges", "p")]),
            (0.6, "line", [("Then 10¢ a sponge", "w")]), (0.82, "slam", [("FOREVER.", "oi")])],
 "margin": [(0.0, "label", "WHERE THE 10¢ COMES FROM"), (0.15, "card", ("Cost to make one sponge, about", [("$1", "o")])),
            (0.55, "chips", ["Before payroll", "Before rent", "Before ads"])],
 "scale":  [(0.0, "label", "THE NAPKIN MATH"), (0.08, "line", [("50M sponges a year", "w")]), (0.35, "big", [("$5M a year", "o")]),
            (0.75, "sub", [("for one $100K check", "p")])],
 "exit":   [(0.0, "label", "WHAT A BUYER SEES"), (0.15, "line", [("A royalty that never ends", "w")]), (0.4, "slam", [("= debt.", "oi")]),
            (0.7, "chips", ["Lower price", "Buy it out first"])],
 "lesson": [(0.05, "line", [("Don't compare checks.", "w")]), (0.25, "line", [("Compare ", "w"), ("cost over time.", "oi")]),
            (0.55, "chips", ["Royalties", "Earn-outs", "Revenue shares"]), (0.85, "sub", [("Read the structure, not the headline.", "p")])],
 "cta":    [(0.0, "label", "BEFORE YOU SIGN A DEAL"), (0.15, "big", [("Follow the ", "w"), ("money.", "oi")])],
}
