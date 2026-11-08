"""Captions for EP11–EP21 (handover 7-part order). Run to write nov_captions.json."""
import json

SERIES = ("Deal Behind the Deal · EP{ep}. We don't recap the pitch. We follow the money.\n"
          "Buying or selling a business? Talk with an advisor at taxbookscfo.com")
DISC = "Commentary and analysis. Not affiliated with or endorsed by Shark Tank or ABC."
CORE = "#SharkTank #MergersAndAcquisitions #Valuation #DealMaking #CFO"

E = {
"poppi": dict(ep=11, file="TaxBooksCFO_EP11_Poppi", date="2026-11-20T19:30:00",
  hook="They asked for $400K. Six years later, PepsiCo agreed to pay $1.95B.",
  deal="Mother Beverage (now Poppi) asked $400K for 10%, a $4M valuation. Kevin called it insane. Only guest Shark Rohan Oza offered: same $400K, for 25%. They took it, at a $1.6M valuation.",
  out="In 2025 PepsiCo bought Poppi for $1.95B. PepsiCo said $300M of that was expected tax benefits, so the net price was $1.65B.",
  lesson="Don't just fight the valuation. Price the partner. And every headline number has a net number underneath it.",
  q="Would you have taken 25% from the right partner over 10% from nobody? Yes or no?",
  tags="#Poppi #PepsiCo #Acquisition #StartupFunding",
  yt="$400K Deal to a $1.95B PepsiCo Exit #SharkTank #Shorts",
  yttags=["shark tank","poppi","pepsico","acquisition","valuation"],
  li="Every acquisition has two prices: the headline and the net.\n\nPoppi (then Mother Beverage) took $400K for 25% on Shark Tank, a $1.6M valuation. In 2025 PepsiCo agreed to pay $1.95B. PepsiCo also said $300M of that was expected tax benefits, putting the net price at $1.65B.\n\nTwo takeaways for owners: the partner can matter more than the valuation, and a headline price needs to be read down to what actually changes hands."),
"kodiak": dict(ep=12, file="TaxBooksCFO_EP12_KodiakCakes", date="2026-11-21T11:00:00",
  hook="The best offer valued Kodiak Cakes at $1.4M. They said no.",
  deal="They asked $500K for 10%, a $5M valuation. Robert offered $500K for 35%. Barbara and Kevin together offered $500K for 50%. They turned down both.",
  out="Two months later they launched Power Cakes at Target. In 2021, L Catterton bought a majority stake (price undisclosed), and the founders kept a minority stake.",
  lesson="Dilution is permanent. Price equity at the exit, not today.",
  q="Would you have taken $500K for 35%? Yes or no?",
  tags="#KodiakCakes #PrivateEquity #Dilution #Founders",
  yt="They Said No to $500K. Then Private Equity Came. #SharkTank #Shorts",
  yttags=["shark tank","kodiak cakes","private equity","dilution","valuation"],
  li="Equity you sell cheap is the most expensive money you will ever raise.\n\nKodiak Cakes asked $500K for 10% on Shark Tank. The offers implied $1M to $1.4M valuations. The founders declined both, kept 100%, and kept control of when and to whom they would sell. In 2021, L Catterton acquired a majority stake (terms undisclosed) with the founders staying on as minority owners.\n\nBefore accepting dilution, model what that stake is worth at the exit."),
"squatty": dict(ep=13, file="TaxBooksCFO_EP13_SquattyPotty", date="2026-11-22T11:00:00",
  hook="Squatty Potty sold for about $31M. Only about $19M was cash.",
  deal="They asked $350K for 5%, a $7M valuation. Kevin offered $350K for 10%; Lori matched. Bobby countered at $500K; Lori said no. They took Lori's $350K for 10%, a $3.5M valuation.",
  out="In May 2021, Aterian bought the business. Its filings show about $30.8M total: about $19M cash at closing, about $8M for transition services, and an earn-out of up to about $4M.",
  lesson="A deal price is a stack, not a number. Ask how much lands at closing.",
  q="Would you accept an earn-out as part of your sale price? Yes or no?",
  tags="#SquattyPotty #EarnOut #SellingABusiness #DealStructure",
  yt="$31M Exit, Only $19M in Cash #SharkTank #Shorts",
  yttags=["shark tank","squatty potty","earn out","selling a business","deal structure"],
  li="A purchase price is a stack, not a number.\n\nWhen Aterian acquired Squatty Potty in 2021, its filings show roughly $30.8M in total consideration: about $19M in cash at closing, about $8M for transition services, and an earn-out of up to about $4M tied to targets. The business had about $16.8M in trailing revenue and $4.7M in operating income.\n\nIf you're selling, model each layer: what's guaranteed, what's contingent, and when it's paid."),
"rocketbook": dict(ep=14, file="TaxBooksCFO_EP14_Rocketbook", date="2026-11-23T19:30:00",
  hook="Every Shark passed on Rocketbook. Three years later, BIC paid $40M.",
  deal="They asked $400K for 10%, a $4M valuation, with $2.2M in sales already. Barbara called it a gimmick. Kevin and Mark went out. No offers.",
  out="In December 2020, BIC bought 100% of Rocketbook for $40M: 10x the valuation the Sharks wouldn't pay.",
  lesson="Strategic buyers pay for fit, not just profit. Know who needs what you've built.",
  q="Have you mapped who would strategically need your business? Yes or no?",
  tags="#Rocketbook #BIC #StrategicBuyer #Acquisition",
  yt="Zero Shark Offers. Then BIC Paid $40M. #SharkTank #Shorts",
  yttags=["shark tank","rocketbook","bic","strategic buyer","acquisition"],
  li="Financial investors price your cash flow. Strategic buyers price what you do for them.\n\nRocketbook got zero offers on Shark Tank at a $4M valuation. In 2020, BIC acquired 100% of the company for $40M, a way into digital writing for a pen maker.\n\nBefore you go to market, list the buyers who need your product, customers or capability. They are often the ones who pay the premium."),
"notehall": dict(ep=15, file="TaxBooksCFO_EP15_Notehall", date="2026-11-24T19:30:00",
  hook="They shook on Barbara's $90K. Then walked away. Chegg bought them less than two years later.",
  deal="Notehall asked $90K for 10%. Kevin offered $90K for 35%. Barbara offered $90K for 25%, and they shook on it. Weeks after the episode aired, they walked away from the deal.",
  out="In June 2011, Chegg bought Notehall: $3.7M in equity per the SEC filing, plus undisclosed cash. Barbara's deal had valued it at $360K.",
  lesson="A handshake on TV is not a closed deal. Until it's signed, both sides can walk.",
  q="Should a handshake deal be binding? Yes or no?",
  tags="#Notehall #Chegg #TermSheet #Startups",
  yt="They Walked Away From Barbara. Chegg Bought Them. #SharkTank #Shorts",
  yttags=["shark tank","notehall","chegg","term sheet","startup"],
  li="A handshake is the start of a deal, not the end of one.\n\nNotehall shook on $90K for 25% with Barbara Corcoran on Shark Tank, then walked away weeks after the episode aired. In 2011, Chegg acquired the company for $3.7M in equity (per the SEC filing) plus undisclosed cash, and hired both founders.\n\nUntil the definitive agreement is signed, both sides still have choices. Plan accordingly."),
"moki": dict(ep=16, file="TaxBooksCFO_EP16_MokiDoorstep", date="2026-11-25T19:30:00",
  hook="A $3M licensing deal. Then a $3M offer for the whole company.",
  deal="Moki Doorstep asked $150K for 5%. On air, the founder said a licensing deal guaranteed $3M over seven years plus a 12.5% royalty. Daymond offered $450K for 20%, then $3M for 100%. They accepted on the spot.",
  out="What happened after the cameras stopped? Public reports conflict, so we won't guess. The math holds either way: at a 10% discount rate (illustrative), $3M paid over 7 years is worth about $2.1M today.",
  lesson="Price a royalty stream in today's dollars. A guarantee paid over years is not cash in hand.",
  q="Would you sell your company for the face value of a future contract? Yes or no?",
  tags="#MokiDoorstep #Licensing #Royalties #TimeValueOfMoney",
  yt="$3M Over 7 Years Is Not $3M #SharkTank #Shorts",
  yttags=["shark tank","moki doorstep","licensing","royalty","time value of money"],
  li="A dollar in year seven is not a dollar today.\n\nOn Shark Tank, Moki Doorstep described a licensing deal guaranteeing $3M over seven years plus a 12.5% royalty, then accepted a $3M offer for 100% of the company. At an illustrative 10% discount rate, $3M paid evenly over seven years is worth about $2.1M today.\n\nWhen a business's value sits in a contract, discount the cash flows before you set a price."),
"bedjet": dict(ep=17, file="TaxBooksCFO_EP17_BedJet", date="2026-11-26T11:00:00",
  hook="He left Shark Tank with $0. The next day, Mattress Firm signed on.",
  deal="BedJet asked $250K for 10%, a $2.5M valuation, with no sales yet and about $50K raised on Kickstarter. Lori felt brushed off and went out. Every Shark followed. No deal.",
  out="The day after the episode aired, Mattress Firm announced it would sell BedJet. The unit economics he pitched: $98 to make, $499 to sell, about an 80% gross margin before shipping and retailer cuts.",
  lesson="Investors buy the person as much as the margin. How you answer is part of the price.",
  q="Do you think founder attitude should change a valuation? Yes or no?",
  tags="#BedJet #GrossMargin #UnitEconomics #Negotiation",
  yt="No Deal, Then Mattress Firm Called #SharkTank #Shorts",
  yttags=["shark tank","bedjet","unit economics","gross margin","negotiation"],
  li="In any negotiation, how you answer is part of the price.\n\nBedJet's founder pitched strong unit economics on Shark Tank ($98 to make, $499 retail, roughly 80% gross margin before shipping and retailer cuts) but lost the room. No deal. The day after the episode aired, Mattress Firm announced it would carry the product.\n\nInvestors price the operator as well as the margin. Retail buyers price the product. Prepare for both."),
"lipbar": dict(ep=18, file="TaxBooksCFO_EP18_TheLipBar", date="2026-11-27T19:30:00",
  hook="A Shark called them cockroaches. Three years later, they were at Target.",
  deal="The Lip Bar asked $125K for 20%, a $625K valuation. Kevin called the colors clown makeup. Robert disliked the branding. No offers.",
  out="Melissa Butler cold-called a Target buyer. The Lip Bar launched on Target.com in 2016 and in Target stores in 2018, and later announced a launch in 3,000 CVS stores.",
  lesson="Equity is the most expensive money you can raise. Get distribution without selling ownership when you can.",
  q="Would you rather land a retailer or an investor first? Retailer = yes, investor = no.",
  tags="#TheLipBar #Target #Retail #Bootstrapping",
  yt="Called Cockroaches, Then Sold at Target #SharkTank #Shorts",
  yttags=["shark tank","the lip bar","target","retail distribution","equity"],
  li="Equity is the most expensive capital most founders ever raise.\n\nThe Lip Bar asked $125K for 20% on Shark Tank and got no offers. Instead, the founder cold-called a Target buyer: Target.com in 2016, Target stores in 2018, and later an announced launch in 3,000 CVS stores.\n\nA retailer buying inventory grows revenue without taking ownership. Run that option before you price your equity."),
}

def ig(n):
    e = E[n]
    return "\n\n".join([e["hook"], e["deal"], e["out"], e["lesson"],
        e["q"] + "\nSave this for your next term sheet.",
        SERIES.format(ep=e["ep"]), DISC, CORE + " " + e["tags"]])

def yt_desc(n):
    e = E[n]
    return "\n\n".join([e["hook"], e["lesson"], SERIES.format(ep=e["ep"]), DISC, "#SharkTank #Shorts #Business"])

def li(n):
    e = E[n]
    return "\n\n".join([e["li"], SERIES.format(ep=e["ep"]), DISC, "#MergersAndAcquisitions #Valuation #DealMaking #CFO"])

if __name__ == "__main__":
    out = {n: dict(ep=E[n]["ep"], file=E[n]["file"], date=E[n]["date"], ig=ig(n), yt_title=E[n]["yt"], yt_desc=yt_desc(n),
                   yt_tags=E[n]["yttags"], li=li(n)) for n in E}
    json.dump(out, open("nov_captions.json", "w"), indent=1)
    for n in out: print(n, len(out[n]["ig"]), len(out[n]["yt_title"]), len(out[n]["li"]))
