from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
Y="https://www.youtube.com/watch?v="
V="Verify before scripting"
# company, season, vid, start, ask/deal on show, after the show, CFO/M&A angle, tier
rows=[
("Poppi (Mother Beverage)","S10E8","sAto3yCMwkM","","Asked $400K for 10%","PepsiCo deal, $1.95B (announced Mar 2025)","Tiny cheque to a $1.95B strategic exit","A"),
("Kodiak Cakes","S5E22","Rz3hPF_x2XI","","Asked $500K/10%; walked from 35% and 50% offers","L Catterton majority stake 2021 (reported ~$800M)","Saying no to dilution: the most expensive 'no' the Sharks ever heard","A"),
("Squatty Potty","S6E9","2atjT5fKK8A","","Lori deal on air","Sold to Aterian for ~$31M (2021)","Viral marketing to a public-company acquisition","A"),
("Rocketbook","S8","bjW4T3xp8vc","","Mark Cuban deal on air","Acquired by BIC (~$40M)","Strategic buyer pays for distribution fit","A"),
("Dude Wipes","S7","HVVA6J037wM","","Mark Cuban deal on air","Cuban calls it a top Shark Tank win",V+" (current valuation claims)","A"),
("Notehall","S1","K5f-WqpO_RY","","Bidding war; deal didn't close","Acquired by Chegg (~$3.7M in equity)","Exit without the Shark: the deal that didn't need TV money","A"),
("Moki Doorstep","S10E8","cMYX4FfMT1A","","Daymond's $3M buyout offer","Buyout didn't close; licensed to Rightline Gear","Buyout vs licensing: two ways to exit","A"),
("BedJet","S6 (2015)","PV2dBfbq1aA","","Asked $250K for 10%; all Sharks out","Grew strongly without them",V+" (lifetime sales figure)","A"),
("The Lip Bar","S6","5paHqbozX-E","","No deal; Sharks harsh","Went national at Target","Rejection to retail distribution","A"),
("CoatChex","S4E1","YLLSXnyepqA","","Asked $200K/10% with zero sales; rejected Cuban $200K/33%","Kept building",V,"A"),
("Cousins Maine Lobster","S4E6","EQUuPQv9EHs","","Barbara deal on air","Large food-truck franchise system","Franchising as a growth engine","A"),
("Tom + Chee","S4","xGYHDUwX0SU","","Kevin + Barbara deal","Over-expanded; distressed sale to Gold Star Chili","Growth that destroyed value: a distressed M&A story","A"),
("Rugged Maniac","S8","IaFLec49zJI","","Asked $1M for 10%; 3 Sharks fight","Later shut down","Rise and fall: event economics","A"),
("Manscaped","S10","SL0j0Or-Z2o","29:41","Check clip","Became a major brand",V,"A"),
("Tipsy Elves","S5","pbcrnXWpJuE","19:02","Robert Herjavec deal","Strong seasonal brand",V,"A"),
("Copa di Vino","S2/S4","H9RIb-Tm2f0","00:00","Clash with Kevin","Returned to the Tank","Founder control vs Shark terms","B"),
("FinalStraw","S10E1","9v6AFKrg1vI","","Check clip","Fought knockoffs",V,"B"),
("Swimply","S12","H9RIb-Tm2f0","19:10","Check clip","Marketplace kept scaling",V,"B"),
("The Bouqs","S6","kx2Nqo67czo","","No deal","Raised venture money","VC route vs Shark route","B"),
("Stasher","S9","NXMYLkdygEM","","Check clip","Check update",V,"B"),
("Brazi Bites","S7","nBQ8q9HDFps","","Lori deal on air","Deal fell through after the show","Why handshake deals die in diligence","B"),
("Ten Thirty One Productions","S6","4Wt2xT6IlBE","","Asked $2M for 10%","Check update","Valuing an events business",V and "B"),
("Yellow Leaf Hammocks","S6","FykmggqWOmM","08:12","Check clip","Check update",V,"B"),
("SparkCharge","S12","FykmggqWOmM","18:22","Check clip","Check update",V,"B"),
("Spikeball","S6","0I-QMVBq6VI","00:03","Deal on air","Deal fell apart; brand kept growing","The deal after the deal","B"),
("Lovepop","S7E11","wjb0NpgFnxA","","Check clip","Check update",V,"B"),
("Zipz","S6E11","49TFIjTYr60","00:05","$2.5M offer","Check update",V,"B"),
("Bubba's Q","S5","oTYA8qaAvWk","","Daymond deal","Later federal court dispute","When the Shark partnership goes to court","B"),
("Hammer & Nails","S6E1","Oi8PoU3A0Fg","","Asked $200K for 20%; no deal","Franchise growth","Franchise model math","B"),
("Chord Buddy","S4","hirO4tYwCrc","","Robert deal","Check update",V,"B"),
("Goalsetter","S10E15","qc4bucvjar4","","Asked $200K for 4%; no deal","Raised outside investors","High valuation ask, no deal, still funded","B"),
("Bottle Breacher","S6 (2014)","hHTlFtRtkG8","","Cuban + Kevin deal","Check update",V,"B"),
("Boost Oxygen","S11E2","yhjqY6Ps8p4","","Asked $1M for 5%","Check update",V,"B"),
("Daisy Cakes","S2","pR4AqBgjyzU","","Asked $50K for 25%; Barbara deal","Grew into a multi-million business","Small cheque, big return",V and "B"),
("Rumpl","S12E1","gXUUpzA9fdg","","Asked $600K for 4%; no deal","Already well funded","Why a funded company went on the show","B"),
("Proven Skincare","S11","V-IStQmhvHM","","Asked $500K for 5%; Cuban challenges sales quality","Check update","Paid growth vs real growth: CAC under the microscope","B"),
("ReadeREST","S3","HX_PMiQedYE","","Lori's first Shark Tank deal","Check update","Licensing-style product deal","B"),
("Brightwheel","S7E26","QMITubk2ajQ","","Sacca vs Cuban fight","Check update","Two Sharks, one cap table",V and "B"),
("Eterneva","S11","t2i3MMxrHMg","14:11","Check clip","Check update",V,"B"),
("The Woobles","S14E2","DC8UvhBU368","00:03","Check clip","Check update",V,"B"),
("The Smart Tire Company","S14","DC8UvhBU368","10:19","Check clip","Check update",V,"B"),
("Simply Fit Board","S7","UGyRmSqH2q8","","Lori deal","Check update",V,"C"),
("Mission Belt","S4E22","Vw2YDKxLTZY","","Asked $50K for 20%; Daymond deal","Check update",V,"C"),
("Oru Kayak","S6","wyy3Yqi2Uks","","Check clip (fan upload, quality may be low)","Check update",V,"C"),
("Pavlok","S7","TfT7OW7b9nE","","Asked $500K; Cuban not buying","Check update",V,"C"),
("Ta-Ta Towel","S10","SL0j0Or-Z2o","08:11","Check clip","Check update",V,"C"),
("Rebel Cheese","S15","nNlvwLND3Fk","00:00","Two-Shark deal","Check update",V,"C"),
("Luminaid","S6","d8w7VntNqyg","","Cuban deal (this link is a founder update interview, not the pitch)","Check update",V,"C"),
("PetPlate","S9","ptH71kYSgwI","","Check clip","Returned to the Tank later",V,"C"),
("FiberFix","S5E6","urGT7hPOZ6s","","Asked $90K (link is a Short)","Check update",V,"C"),
("Jax Sheets","S12E13","zHP7kntYtAY","","Asked $212K for 10%","Check update",V,"C"),
("Souper Cubes","S13","NJKR3FZzU9s","","Asked $400K for 5%; Lori golden ticket","Check update",V,"C"),
("Boarderie","S14E7","9m9SsHuAlCI","","Asked $300K for 5%","Check update",V,"C"),
("Supply (royalty deal)","—","fJCvxMfIk4M","","Royalty deal","Check update","Royalty vs equity",  "C"),
("Chill-N-Reel (royalty deal)","—","own-GTz53Vg","","Royalty deal","Check update","Royalty vs equity","C"),
]
def ts(s):
    if not s: return 0
    m,sec=s.split(":"); return int(m)*60+int(sec)
wb=Workbook(); ws=wb.active; ws.title="Episode Pipeline"
hdr=["#","Tier","Company","Season/Ep","YouTube link (download this)","Pitch starts at","Deal on the show","What happened after","CFO / M&A angle","Status"]
ws.append(hdr)
for i,r in enumerate(rows,1):
    c,se,vid,st,deal,after,angle,tier=r
    url=Y+vid+(f"&t={ts(st)}s" if st else "")
    ws.append([i,tier,c,se,url,st or "Start",deal,after,angle,"Footage needed"])
    ws.cell(row=i+1,column=5).hyperlink=url; ws.cell(row=i+1,column=5).font=Font(color="0563C1",underline="single")
done=[("Breathometer (EP7, done)","UToDZppStMk"),("Plated (EP9, done)","nkPrDsD4YmE")]
ws2=wb.create_sheet("Already Produced")
ws2.append(["Episode","YouTube link"])
for n,v in done:
    ws2.append([n,Y+v]); ws2.cell(row=ws2.max_row,column=2).hyperlink=Y+v
for w in (ws,ws2):
    for c in w[1]:
        c.font=Font(bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor="1F3A5F")
    w.freeze_panes="A2"
widths=[5,6,28,11,52,13,42,40,46,15]
for i,wd in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=wd
ws2.column_dimensions["A"].width=28; ws2.column_dimensions["B"].width=50
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment=Alignment(wrap_text=True,vertical="top")
    t=row[1].value
    row[1].fill=PatternFill("solid",fgColor={"A":"C6EFCE","B":"FFEB9C","C":"EDEDED"}[t])
ws.auto_filter.ref=ws.dimensions
wb.save("/home/claude/deals/out/SharkTank_Episode_Pipeline_55.xlsx")
print(len(rows), sum(r[7]=="A" for r in rows))
