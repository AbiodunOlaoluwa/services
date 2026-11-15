"""Builds the static pages. Run: python3 build.py (writes index.html and */index.html)."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "mate.olaoluwa@gmail.com"
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'


def page(*, slug, title, description, body):
    up = "" if slug == "" else "../"
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>
<div class="page">
<header class="site">
  <a href="{up or './'}">Olaoluwa Abiodun</a>
  {MAIL}
</header>
<main>
{body.strip()}
</main>
<footer class="site">
  <a href="{up}privacy/">Privacy notice</a>. These pages don't use cookies or tracking.
</footer>
</div>
</body>
</html>
"""


def write(slug, html):
    out = ROOT / slug / "index.html" if slug else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out.relative_to(ROOT))


ME = '<img src="../assets/olaoluwa.jpg" alt="Olaoluwa Abiodun" width="112" height="112">'

# ---------------------------------------------------------------- lettings
LETTINGS = page(
    slug="lettings",
    title="Missed enquiry checks for letting agents",
    description="Find the portal enquiries that never reached your CRM, and answer the ones that arrive when the office is closed.",
    body=f"""
<h1>Find the portal enquiries that never reached your CRM</h1>
<p class="intro">I build small systems for letting agents that check the enquiries from Rightmove, Zoopla, OnTheMarket and your website against your CRM, flag the ones that went missing, and send a first reply when the office is closed.</p>

<h2>Where enquiries go missing</h2>
<p>A portal changes the layout of its emails, and the parser that feeds your CRM stops recognising them. The emails keep arriving, nothing lands in the CRM, and nobody notices until a landlord asks why their flat has had no interest.</p>
<p>A forwarding rule breaks. Nothing errors; the portal simply goes quiet.</p>
<p>An applicant enquires at 8pm on a Friday. By Monday morning they've booked a viewing with the agent who replied first.</p>

<h2>What I build</h2>
<h3>A watchdog for missing enquiries</h3>
<p>Every few minutes (how often depends on what your CRM allows) it looks up each new enquiry in your CRM. Anything still missing after a set time, 15 minutes in the demo, becomes an alert with the original email attached, and a portal that goes quiet for much longer than usual is flagged too.</p>
<figure>
<img src="../assets/watchdog-sample.jpg" width="1185" height="757" alt="The watchdog demo: a list of the day's portal enquiries with the time each one reached the CRM, one Zoopla enquiry marked missing, and two alerts, one for the missing Zoopla enquiry and one saying OnTheMarket has gone quiet.">
<figcaption>The demo on a made-up Tuesday for an agency in Leeds, with HubSpot as the example CRM. One Zoopla enquiry hasn't arrived, and OnTheMarket has gone quiet. <a href="https://abiodunolaoluwa.github.io/enquiry-watchdog/">You can try it here</a>.</figcaption>
</figure>
<p>Each week you get one line per portal: enquiries received, and how many reached the CRM. It can't see enquiries that never reached your inbox at all, such as a phone call nobody logged.</p>

<h3>A first reply when the office is closed</h3>
<p>When the office is closed, the applicant gets a reply within minutes asking the questions you choose, for example move-in date, budget, pets and when they could view. Every draft is checked on the server against your rules before it goes out, such as never confirming a viewing, a price or availability, never discussing deposits, and passing complaints and landlord messages straight to a person. If a draft breaks a rule, it gets one rewrite; if that fails too, nothing is sent and the enquiry goes to your team with a note. <a href="https://reply-desk-8rzb.onrender.com">There's a demo of the reply side here</a>.</p>

<h2>How we'd start</h2>
<ol>
<li><strong>You tell me your setup.</strong> Reply with the portals you list on and the CRM you use, and I'll send a one-page plan for your agency: what I'd check, what I'd need, and what it would cost. It's free, and I don't need any access for it.</li>
<li><strong>A one-week check, if the plan makes sense.</strong> Also free. You give me read-only access to the inbox your portal emails land in and a CRM export for the same week, under a short data agreement, and I send back how many enquiries each portal sent, how many reached the CRM, how long the first reply took, and anything that went missing.</li>
<li><strong>The build.</strong> A fixed price agreed before I start, usually between £1,500 and £3,500, and usually two to three weeks of work on the accounts and CRM you already use.</li>
<li><strong>A monthly care plan.</strong> I keep an eye on it, fix it when a portal changes its emails, make small changes, and send a one-page report each month. It's £250 to £500 a month, and you can cancel with a month's notice.</li>
</ol>

<h2>Your data</h2>
<p>Where possible the software runs in your own accounts, and where it can't, on a small server set up in your agency's name that you can switch off. I work with the least access the job needs, you can revoke it at any time, and when the check ends I remove my access, delete anything I exported, and confirm it in writing. I sign a data processing agreement before I touch anything.</p>
<p>Nothing replies on your behalf until you've approved how it speaks, and it can run in draft-only mode for as long as you like.</p>

<h2>Who you'd be working with</h2>
<div class="me">{ME}
<p>I'm Olaoluwa Abiodun, an engineer based in Lagos, Nigeria, working UK hours (Lagos is an hour ahead of London in winter and level with it in summer). I built Rentyx, a property-management platform, end to end, including an assistant that answered tenants' and landlords' WhatsApp messages under rules the server checked before anything went out, handing anything unclear to me.</p>
<p>You'd be one of my first agency clients, which is why the plan and the check are free and the build price is fixed.</p>
</div>

<h2>Questions</h2>
<h3>Which CRMs does it work with?</h3>
<p>I haven't worked with every lettings CRM, so I check what yours allows (an API, an email-in address or exports) before I quote.</p>
<h3>What if a reply goes wrong?</h3>
<p>It only sends replies that pass your rules, and anything they don't cover goes to a person. You can start in draft-only mode, where your team approves every reply.</p>
<h3>Why are you in Lagos?</h3>
<p>That's where I live. The work is all online, and my day overlaps yours.</p>

<p class="signoff">If it sounds useful, email me at {MAIL} with your agency's name, the portals you list on and the CRM you use, and I'll send the one-page plan within two working days.</p>
<p>Olaoluwa</p>
""",
)

# ---------------------------------------------------------------- recruitment
RECRUITMENT = page(
    slug="recruitment",
    title="Sourcing for independent recruitment agencies",
    description="People who fit your live roles, with verified work emails and a first line drafted for your consultant to approve.",
    body=f"""
<h1>People who fit your live roles, with verified work emails and a first line drafted</h1>
<p class="intro">I've spent two years in recruiting, and I build the sourcing side for small agencies: people who fit a live role, found in public sources, with work emails verified and a first line drafted for your consultant to approve.</p>

<h2>Where I'm coming from</h2>
<p>Most of my recruiting has been sourcing for early-stage US startups. I've contacted about 1,000 candidates through personalised four-step email sequences, contributed to five placements, and contributed to the workflows that found candidates' contact details and drafted each email's opening line. Finding people who fit, finding an email that works, and writing a first line that doesn't read like a template are the parts I build for agencies.</p>

<h2>What I build</h2>
<h3>Sourcing for a live role</h3>
<p>You send the brief and choose the sources. For engineering or construction that might be company team pages, project announcements, public professional registers and conference speaker lists. You set the criteria (must-haves, nice-to-haves, location), and the list shows which ones each person meets and where that came from, so your consultant can check it and change the criteria.</p>
<h3>Verified work emails</h3>
<p>The address is worked out from the company's own email pattern, then verified with an email-checking service, which confirms the mail server accepts that address. It can't promise the person reads it. If no address verifies, the person is listed without one rather than guessed. On an outreach list I built for my own project, this took bounces from 12.3% to 2.9%.</p>
<h3>One record per person</h3>
<p>The same person found on two sites becomes one record, so nobody gets two messages from you.</p>
<h3>A draft first line for each person</h3>
<p>Based on something they actually did, like a project they delivered or a talk they gave. Your consultant approves, edits or bins it. Nothing sends on its own.</p>

<p>Here's one row of a sample, with a made-up person:</p>
<div class="table-wrap"><table>
<tr><th>Person</th><th>Fits because</th><th>Work email</th><th>Draft first line</th></tr>
<tr><td data-label="Person">Priya N., Senior Site Manager, Northgate Build Ltd (made up)</td><td data-label="Fits because">Must-have: 5+ years running school or hospital builds (company news page, March 2026: led a £12m school extension in Leeds). Location: West Yorkshire (team page).</td><td data-label="Work email">Verified</td><td data-label="Draft first line">"Saw that the Leeds school extension finished on time in March, which can't have been easy over winter."</td></tr>
</table></div>
<p>The sourcing and matching side <a href="https://lead-engine-yqxv.onrender.com">runs on sample data here</a>.</p>

<h2>How we'd start</h2>
<ol>
<li><strong>A free sample.</strong> Send me a link to one of your public job adverts. Within three working days you get a spreadsheet of up to ten people who fit, each with the criteria they meet and where that came from, a verified work email where one exists, and a draft first line. You keep the spreadsheet, and I delete my copy within a week of sending it. A short data agreement covers it.</li>
<li><strong>The build.</strong> Set up for your sectors and the system you use, at a fixed price agreed before I start, usually between £1,500 and £3,500 and two to three weeks of work.</li>
<li><strong>A monthly care plan.</strong> I keep the sources working as sites change, tune the criteria with your feedback, and send a short monthly report. It's £250 to £500 a month, and you can cancel with a month's notice.</li>
</ol>

<h2>Your data</h2>
<p>Candidate data ends up in your systems, not mine. I sign a data processing agreement before any work starts, and you decide who gets contacted and what they're sent.</p>

<h2>Who you'd be working with</h2>
<div class="me">{ME}
<p>I'm Olaoluwa Abiodun, an engineer based in Lagos, Nigeria, working UK hours. Alongside recruiting, I built Rentyx, a property-management platform, end to end.</p>
<p>You'd be one of my first agency clients, which is why the sample is free and the build price is fixed.</p>
</div>

<h2>Questions</h2>
<h3>Does it work with our ATS?</h3>
<p>I'll work with the system you already use, and check what it allows before I quote.</p>
<h3>Which sources won't you use?</h3>
<p>Any site whose terms don't allow it. You see the source of every name.</p>

<p class="signoff">If you'd like to see a sample, email me at {MAIL} with a link to one of your job adverts and the sector you recruit for, and I'll put it together within three working days.</p>
<p>Olaoluwa</p>
""",
)

# ---------------------------------------------------------------- white-label
WHITE_LABEL = page(
    slug="white-label",
    title="White-label build help for automation agencies",
    description="The code-heavy part of a client build, done under your name: custom steps, awkward APIs, scrapers and LLM steps with checks.",
    body=f"""
<h1>The code-heavy part of a client build, done under your name</h1>
<p class="intro">Your team keeps the workflow in n8n or Make. When a step needs real code, like a custom node, an awkward API, a scraper or an LLM step that needs rules around it, I write that piece, document it, and hand it back under your brand.</p>

<h2>The kind of thing I pick up</h2>
<ul>
<li>A client's API that rate-limits, paginates oddly and fails at 2am, so the flow needs retries, logging and a way to replay what failed.</li>
<li>A scraper with checks that tell you when the source site has changed, instead of quietly returning nothing.</li>
<li>An LLM step whose drafts have to pass fixed checks before anything is sent.</li>
</ul>

<h2>Two things I've built that look like agency work</h2>
<p><strong>Lead Engine</strong> pulls firms from directories with different page layouts, keeps a field only when it can quote it from the page, merges the same firm found in two places, and picks up where it stopped after a failure. <a href="https://lead-engine-yqxv.onrender.com">Demo</a>.</p>
<p><strong>Reply Desk</strong> answers inbound messages with a model, but every draft has to pass checks on the server. A draft that fails gets one rewrite and is then held for a person, and there's a kill switch and a daily cap. <a href="https://reply-desk-8rzb.onrender.com">Demo</a>.</p>
<p>I also built search over legal texts that quotes the paragraph it relied on, or refuses: <a href="https://cite-desk.onrender.com">Cite Desk</a>.</p>

<h2>How we'd work</h2>
<ol>
<li><strong>Send me five lines describing the piece, or a redacted export of the workflow.</strong> No client data needed. Within two working days you get a free scope, the approach I'd take, and a fixed quote.</li>
<li><strong>One fixed piece first,</strong> typically a single code step, integration or small service, delivered in under a week with a README and tests, so you can judge the work without committing to more.</li>
<li><strong>Your conventions.</strong> My code sits where your team can see it: a code node inside the workflow, or a small service in your account that the workflow calls. I follow your repo, naming and documentation, write handover notes your team can maintain, and fix bugs in my code free for 30 days after handover.</li>
<li><strong>Then per project, or a monthly block of hours,</strong> whichever suits your pipeline.</li>
</ol>

<h2>Who you'd be working with</h2>
<div class="me">{ME}
<p>I'm Olaoluwa Abiodun, an engineer based in Lagos, Nigeria, on UK and European hours. I'm code-first (TypeScript, Python, PostgreSQL) and built Rentyx, a property-management platform, end to end. I work inside n8n and Make when the job needs it, and your team stays the experts on those tools. My code is on <a href="https://github.com/AbiodunOlaoluwa">GitHub</a>.</p>
</div>

<h2>Questions</h2>
<h3>Will you contact our client?</h3>
<p>Only if you ask me to.</p>
<h3>Who owns the code?</h3>
<p>You or your client, on payment.</p>
<h3>What about NDAs and client data?</h3>
<p>I'll sign your NDA and a sub-processor agreement, and I don't need client data to quote.</p>

<p class="signoff">If there's a piece your team would rather not build, email me at {MAIL} and I'll reply within two working days with a free scope and a fixed quote.</p>
<p>Olaoluwa</p>
""",
)

# ---------------------------------------------------------------- index
INDEX = page(
    slug="",
    title="Olaoluwa Abiodun",
    description="Software engineer in Lagos building and looking after small systems for letting agents, recruitment agencies and automation agencies.",
    body="""
<h1>Olaoluwa Abiodun</h1>
<p class="intro">I'm a software engineer in Lagos, Nigeria, working UK and European hours. I build small systems for three kinds of business and then look after them. Each one starts with something free and small, so you can judge the work before you pay for anything.</p>
<ul>
<li><a href="lettings/">For letting and estate agents</a>: find the portal enquiries that never reached your CRM, and answer the ones that arrive after hours.</li>
<li><a href="recruitment/">For recruitment agencies</a>: people who fit your live roles, with verified work emails and a first line drafted.</li>
<li><a href="white-label/">For automation and CRM agencies</a>: the code-heavy part of a client build, done under your name.</li>
</ul>
<p>My code is on <a href="https://github.com/AbiodunOlaoluwa">GitHub</a>.</p>
""",
)


def privacy():
    src = (ROOT / "copy-privacy.md").read_text()
    body = src.split("Updated: 15 November 2026", 1)[1]
    html, items = ["<h1>Privacy notice</h1>", '<p class="intro">How I handle the details of people I contact about my work, and what you can ask me to do with them. Last updated 15 November 2026.</p>'], []

    def flush():
        if items:
            html.append("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>")
            items.clear()

    for line in body.strip().split("\n"):
        line = line.strip()
        if line.startswith("- "):
            items.append(line[2:])
            continue
        flush()
        if line.startswith("## "):
            html.append(f"<h2>{line[3:]}</h2>")
        elif line:
            html.append(f"<p>{line}</p>")
    flush()
    out = "\n".join(html)
    out = out.replace(EMAIL, MAIL)
    out = out.replace("(ico.org.uk)", '(<a href="https://ico.org.uk/make-a-complaint/">ico.org.uk</a>)')
    out = out.replace("(ndpc.gov.ng)", '(<a href="https://ndpc.gov.ng">ndpc.gov.ng</a>)')
    return page(slug="privacy", title="Privacy notice: Olaoluwa Abiodun",
                description="How Olaoluwa Abiodun handles the personal details of people he contacts about his work.",
                body=out)


if __name__ == "__main__":
    write("", INDEX)
    write("lettings", LETTINGS)
    write("recruitment", RECRUITMENT)
    write("white-label", WHITE_LABEL)
    write("privacy", privacy())
