import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule

C = json.load(open("/home/claude/deals/master/captions.json"))
F = "Arial"
NAVY = "0B2545"; GOLD = "C9A227"; LIGHT = "EEF2F7"
thin = Side(style="thin", color="D0D7E2")
B = Border(left=thin, right=thin, top=thin, bottom=thin)
H = Font(name=F, bold=True, color="FFFFFF", size=10)
HF = PatternFill("solid", fgColor=NAVY)
N = Font(name=F, size=10)
WRAP = Alignment(wrap_text=True, vertical="top")

def sheet(ws, headers, rows, widths, title=None, note=None):
    r0 = 1
    if title:
        ws.cell(1, 1, title).font = Font(name=F, bold=True, size=14, color=NAVY)
        r0 = 2
        if note:
            ws.cell(2, 1, note).font = Font(name=F, italic=True, size=9, color="555555")
            r0 = 3
        r0 += 1
    for j, h in enumerate(headers, 1):
        c = ws.cell(r0, j, h); c.font = H; c.fill = HF; c.border = B
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for i, row in enumerate(rows, r0 + 1):
        for j, v in enumerate(row, 1):
            c = ws.cell(i, j, v); c.font = N; c.border = B; c.alignment = WRAP
            if (i - r0) % 2 == 0:
                c.fill = PatternFill("solid", fgColor=LIGHT)
    for j, w in enumerate(widths, 1):
        ws.column_dimensions[ws.cell(r0, j).column_letter].width = w
    ws.freeze_panes = ws.cell(r0 + 1, 1)
    return r0

wb = Workbook()

# ---------- Schedule ----------
ws = wb.active; ws.title = "Schedule"
ROOT = "Downloads/TaxBooksCFO_DealBehindTheDeal/"
sched = [
 (0, "2026-11-08", "Sun", "11:00 AM", "EP06", "GrooveBook: The Side Door", "Episodes/EP06_GrooveBook/TaxBooksCFO_EP6_GrooveBook_9x16.mp4", "none", "Weekend fill. Added Nov 7"),
 (1, "2026-11-11", "Wed", "7:30 PM", "EP03", "Ring: The Deal He Walked Away From", "04_Sat-Nov21_EP03_Ring_9x16.mp4", "@ring", "Daily run starts. Strongest hook"),
 (2, "2026-11-12", "Thu", "7:30 PM", "EP05", "Bombas: Negotiate What the Money Does", "05_Sun-Nov22_EP05_Bombas_9x16.mp4", "@bombas", ""),
 (3, "2026-11-13", "Fri", "7:30 PM", "EP08", "Coffee Meets Bagel: The $30M No", "07_Sat-Nov28_EP08_CoffeeMeetsBagel_9x16.mp4", "@coffeemeetsbagel", ""),
 (4, "2026-11-14", "Sat", "11:00 AM", "EP01", "Scrub Daddy: The Bidding War", "01_Sat-Nov14_EP01_ScrubDaddy_BiddingWar_9x16.mp4", "@scrubdaddy", "Scheduled in Meta Business Suite. Ends 'follow for part two'"),
 (5, "2026-11-15", "Sun", "11:00 AM", "EP02", "Scrub Daddy: Kevin's Royalty", "02_Sun-Nov15_EP02_ScrubDaddy_Royalty_9x16.mp4", "@scrubdaddy", "Part two, next day"),
 (6, "2026-11-16", "Mon", "7:30 PM", "EP09", "Plated: The $200M Panic Buy", "03_Wed-Nov18_EP09_Plated_9x16.mp4", "none", "Never tag Plated"),
 (7, "2026-11-17", "Tue", "7:30 PM", "EP07", "Breathometer: Hype vs. Diligence", "06_Wed-Nov25_EP07_Breathometer_9x16.mp4", "none", "Never tag Breathometer"),
 (8, "2026-11-18", "Wed", "7:30 PM", "EP10", "Bantam Bagels: Never Sell Control", "08_Sun-Nov29_EP10_BantamBagels_9x16.mp4", "none (account inactive)", "Caption includes 2022 discontinuation note"),
 (9, "2026-11-19", "Thu", "7:30 PM", "EP04", "Wicked Good: The Forever Royalty", "09_Sat-Dec05_EP04_WickedGood_9x16.mp4", "none", "Cutdowns EP4b/EP4c held in reserve"),
]
rows = [list(s[:7]) + [("Meta Business Suite" if s[4]=="EP01" else "Metricool"), "Scheduled", "Scheduled", "Scheduled", s[7], s[8]] for s in sched]
hdr = ["#", "Date", "Day", "Time (ET)", "Episode", "Title", "File (00_POST_QUEUE → same number in each platform folder)", "Scheduled via",
       "Instagram + Facebook", "YouTube Shorts", "LinkedIn page (12:15 PM)", "Tag", "Notes"]
r0 = sheet(ws, hdr, rows, [4, 11, 6, 10, 8, 34, 50, 14, 22, 14, 14, 18, 40],
           "Deal Behind the Deal: posting schedule",
           "Daily from Nov 11: weekdays 7:30 PM ET, weekends 11:00 AM ET. One reel per day. Status columns have dropdowns.")
dv = DataValidation(type="list", formula1='"Not started,Captions typed, waiting on video,Scheduled,Published,Skipped"', allow_blank=True)
ws.add_data_validation(dv)
last = r0 + len(rows)
dv.add(f"I{r0+1}:K{last}")
green = PatternFill("solid", fgColor="D9F2E3"); amber = PatternFill("solid", fgColor="FFF4CC")
for col in "IJK":
    rng = f"{col}{r0+1}:{col}{last}"
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'OR({col}{r0+1}="Scheduled",{col}{r0+1}="Published")'], fill=green))
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'{col}{r0+1}="Captions typed, waiting on video"'], fill=amber))
s = last + 2
ws.cell(s, 1, "Progress").font = Font(name=F, bold=True, color=NAVY)
for k, (lab, col) in enumerate([("Instagram + Facebook", "I"), ("YouTube Shorts", "J"), ("LinkedIn", "K")]):
    ws.cell(s + 1 + k, 2, lab).font = N
    c = ws.cell(s + 1 + k, 6, f'=COUNTIF({col}{r0+1}:{col}{last},"Scheduled")+COUNTIF({col}{r0+1}:{col}{last},"Published")')
    c.font = N
    ws.cell(s + 1 + k, 7, f'=F{s+1+k}&" of "&COUNTA({col}{r0+1}:{col}{last})&" scheduled or published"').font = N

# ---------- Already on the calendar ----------
ws2 = wb.create_sheet("Already Scheduled")
pre = [("2026-11-08", "Sun", "7:30 PM", "Reel", "Facebook + Instagram"),
       ("2026-11-09", "Mon", "11:00 AM", "Reel", "Facebook + Instagram"),
       ("2026-11-09", "Mon", "3:00 PM", "Reel", "Facebook + Instagram"),
       ("2026-11-09", "Mon", "7:30 PM", "Reel", "Facebook + Instagram"),
       ("2026-11-10", "Tue", "11:00 AM", "Reel", "Facebook + Instagram")]
sheet(ws2, ["Date", "Day", "Time (ET)", "Type", "Channels"], [list(p) for p in pre], [12, 6, 10, 8, 24],
      "Posts already scheduled before this series (left untouched)",
      "Read from Meta Business Suite > Content > Scheduled on Nov 7, 2026. The series starts after these.")

# ---------- Episodes ----------
ws3 = wb.create_sheet("Episodes")
eps = [
 ("EP01", "Scrub Daddy", "Bidding war", "Asked $100K / 10% ($1M). Kevin opened at 50%. Closed $200K / 20% with Lori", "Competition sets the price. Run a process", "@scrubdaddy (718K)", "Episodes/EP01_ScrubDaddy_BiddingWar", "Ready"),
 ("EP02", "Scrub Daddy", "Royalty structure", "Kevin: $100K, 50¢/unit to payback, then 10¢ forever", "Read the structure, not the headline", "@scrubdaddy (718K)", "Episodes/EP02_ScrubDaddy_Royalty", "Ready"),
 ("EP03", "Ring (DoorBot)", "Walking away", "Asked $700K / 10%. Kevin royalty, no deal. Amazon bought Ring (~$1B reported)", "The wrong deal is worse than no deal", "@ring (628K)", "Episodes/EP03_Ring", "Ready"),
 ("EP04", "Wicked Good Cupcakes", "Royalty in an exit", "$75K, 45¢/jar royalty, 100% kept. Later sold to Hickory Farms", "Price the royalty before you sign it", "none (no verified account)", "Episodes/EP04_WickedGood (+ Cutdowns)", "Ready + 2 cutdowns"),
 ("EP05", "Bombas", "Working capital", "Asked $200K / 5%. Closed 17.5% + inventory financing (Daymond)", "Negotiate what the money does", "@bombas (456K)", "Episodes/EP05_Bombas", "Ready"),
 ("EP06", "GrooveBook", "Licensing vs. selling + earn-out", "Asked $150K / 20%. Kevin offered $750K for 100%. Took Mark & Kevin: $150K for 80% of licensing rights. Shutterfly bought for $14.5M (incl. earn-out), shut 2022", "The headline price isn't the price", "none", "Episodes/EP06_GrooveBook", "Ready"),
 ("EP07", "Breathometer", "Due diligence", "All five Sharks: $1M / 30%. FTC settlement 2017", "Hype raises the price, never lowers the risk", "never tag", "Episodes/EP07_Breathometer", "Ready"),
 ("EP08", "Coffee Meets Bagel", "Turning down a buyout", "Asked $500K / 5% ($10M). Mark offered $30M for 100%. Declined", "Weigh an offer against risk, dilution, time", "@coffeemeetsbagel (477K)", "Episodes/EP08_CoffeeMeetsBagel", "Ready"),
 ("EP09", "Plated", "Strategic premium", "Deal fell apart post-show. Albertsons bought ~$200M (2017), $38M write-down, shut 2019", "Fear is not a valuation", "never tag", "Episodes/EP09_Plated", "Ready"),
 ("EP10", "Bantam Bagels", "Control", "Asked $275K / 11%. Barbara 51%, Kevin 50%. Lori deal. Sold to T. Marzetti $34M (2018), discontinued 2022", "Never sell control just to get started", "none (account inactive)", "Episodes/EP10_BantamBagels", "Ready"),
 ("EP11", "Kodiak Cakes", "—", "Skipped: footage not found", "—", "—", "—", "On hold"),
]
sheet(ws3, ["EP", "Company", "Theme", "The deal", "Lesson", "Tag", "Folder", "Status"], [list(e) for e in eps],
      [6, 20, 20, 52, 36, 22, 36, 18], "Episode library",
      "Each folder holds 9x16 (Reels/Shorts/TikTok), 1x1 (feed), 16x9 (X/YouTube/LinkedIn). Covers in /Covers.")

# ---------- Captions ----------
ws4 = wb.create_sheet("Captions")
order = ["EP01", "EP02", "EP03", "EP04", "EP05", "EP07", "EP08", "EP09", "EP10"]
sheet(ws4, ["EP", "Instagram + Facebook caption (as typed in Meta)", "X post (≤280, attach 16x9)", "LinkedIn page post (attach 1x1 or 16x9)"],
      [[e, C[e]["ig"], C[e]["x"], C[e]["li"]] for e in order], [6, 70, 45, 60],
      "Captions by platform", "Instagram/Facebook text is exactly what is in the Meta composer.")
for r in range(5, 5 + len(order)):
    ws4.row_dimensions[r].height = 300

# ---------- Collabs ----------
ws5 = wb.create_sheet("Collab Outreach")
col = [
 ("Scrub Daddy", "@scrubdaddy", "718K", "Instagram DM from @taxbookscfo", "Drafted", "Send after EP01 is live; offer Collab invite on EP02"),
 ("Ring", "@ring", "628K", "Instagram DM", "Drafted", "Corporate (Amazon). Low odds, tag still drives discovery"),
 ("Coffee Meets Bagel", "@coffeemeetsbagel", "477K", "Instagram DM", "Drafted", ""),
 ("Bombas", "@bombas", "456K", "Instagram DM", "Drafted", "Story is positive for them: good collab fit"),
 ("Wicked Good Cupcakes", "via Hickory Farms / email", "—", "Email", "Drafted", "Brand IG not verified"),
 ("GrooveBook founders", "TBD", "—", "Instagram / LinkedIn", "Not started", "After EP06 is built"),
 ("Breathometer / Plated", "—", "—", "—", "Do not contact", "Negative stories: never tag or pitch"),
]
r = sheet(ws5, ["Brand", "Handle", "Followers", "Channel", "Status", "Notes"], [list(c) for c in col],
          [22, 26, 10, 28, 14, 50], "Collab and co-post outreach", "Every DM is confirmed before sending.")
dv2 = DataValidation(type="list", formula1='"Not started,Drafted,Sent,Replied,Collab accepted,Declined,Do not contact"', allow_blank=True)
ws5.add_data_validation(dv2); dv2.add(f"E{r+1}:E{r+len(col)}")

# ---------- Rules ----------
ws6 = wb.create_sheet("Brand Rules")
rules = [
 ("Accounts", "TaxBooksCFO brand accounts only. Nothing on founders' personal profiles."),
 ("Budget", "$0. No boosts or ads. Visibility, not sales: referral marketing drives revenue."),
 ("Disclaimer", "Every caption: 'Commentary and analysis. Not affiliated with or endorsed by Shark Tank or ABC.'"),
 ("Tagging", "Tag only companies with a positive story. Never tag @SharkTankABC, Breathometer or Plated."),
 ("Cadence", "Max one series reel per day. Weekends (Sat/Sun 11 AM ET) are the anchor; one weekday evening (Wed 7:30 PM ET)."),
 ("Positioning", "Big 4 expertise for small businesses, brokers and the middle market. Series line: 'We don't recap the pitch. We follow the money.'"),
 ("CTA", "Buying or selling a business? Talk with an advisor at taxbookscfo.com"),
 ("Formats", "9x16 → Instagram/Facebook Reels, YouTube Shorts, TikTok · 1x1 → LinkedIn/Facebook feed · 16x9 → X, YouTube, LinkedIn"),
]
sheet(ws6, ["Rule", "Detail"], [list(x) for x in rules], [16, 110], "Brand rules for this series")

for w in wb.worksheets:
    w.sheet_view.showGridLines = False
wb.save("/mnt/user-data/outputs/TaxBooksCFO_DealBehindTheDeal_Master.xlsx")
print("saved")
