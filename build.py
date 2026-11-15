"""Builds the static offer pages. Run: python3 build.py (writes index.html, */index.html)."""
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "mate.olaoluwa@gmail.com"
FONTS = ("https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600"
         "&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600"
         "&family=Public+Sans:wght@400;500;600&display=swap")


def page(*, slug, ink, title, description, topline_right="", masthead, body, glance=""):
    up = "" if slug == "" else "../"
    glance_html = f'<aside class="glance" aria-label="At a glance">{glance}</aside>' if glance else ""
    body_html = (f'<div class="body"><div class="prose">{body}</div>{glance_html}</div>' if glance
                 else f'<div class="body"><div class="prose doc">{body}</div></div>')
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body data-ink="{ink}">
<a class="skip" href="#main">Skip to the content</a>
<div class="sheet">
  <header class="topline">
    <a href="{up or './'}">Olaoluwa Abiodun &middot; software engineer, Lagos</a>
    {topline_right or f'<a href="mailto:{EMAIL}">{EMAIL}</a>'}
  </header>
  <main id="main">
    <div class="masthead">{masthead}</div>
    {body_html}
  </main>
  <footer class="foot">
    <span>Olaoluwa Abiodun, sole trader, Lagos, Nigeria &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
    <span><a href="{up}privacy/">Privacy notice</a> &middot; No cookies or tracking on these pages</span>
  </footer>
</div>
</body>
</html>
"""


def meta(rows):
    return '<dl class="meta">' + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows) + "</dl>"


def glance(rows, button_text, subject, small):
    from urllib.parse import quote
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    return (f"<h2>At a glance</h2><dl>{dl}</dl>"
            f'<a class="button" href="mailto:{EMAIL}?subject={quote(subject)}">{button_text}</a>'
            f'<p class="small">{small}</p>')


def write(slug, html):
    out = ROOT / slug / "index.html" if slug else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out.relative_to(ROOT))


# ---------------------------------------------------------------- lettings
LETTINGS = page(
    slug="lettings", ink="lettings",
    title="Missed enquiry checks for letting agents",
    description="Find the portal enquiries that never reached your CRM, and answer the ones that arrive when the office is closed.",
    masthead=meta([("For", "Independent letting and estate agents"),
                   ("From", "Olaoluwa Abiodun, software engineer, Lagos"),
                   ("Start", "<strong>A free one-page plan</strong>, then a free two-week check")])
    + "<h1>Find the portal enquiries that never reached your CRM.</h1>"
    + '<p class="deck">I build small systems for letting agents that check the enquiries from Rightmove, Zoopla, OnTheMarket and your website against your CRM, flag the ones that went missing, and send a first reply when the office is closed.</p>',
    body="""
<section class="clause"><h2>Where enquiries go missing</h2>
<ul class="lede-list">
<li>A portal changes the layout of its emails, and the parser that feeds your CRM stops recognising them. The emails keep arriving, nothing lands in the CRM, and nobody notices until a landlord asks why their flat has had no interest.</li>
<li>A forwarding rule breaks. Nothing errors; the portal simply goes quiet.</li>
<li>An applicant enquires at 8pm on a Friday. By Monday morning they've booked a viewing with the agent who replied first.</li>
</ul></section>

<section class="clause"><h2>What I build</h2>
<div class="item"><h3>The watchdog</h3>
<p>Every few minutes (how often depends on what your CRM allows) it looks up each new enquiry in your CRM. Anything still missing after a set time, 15 minutes in the demo, becomes an alert with the original email attached, and a portal that goes quiet for much longer than usual is flagged too. This is what an alert looks like, on sample data:</p>
<figure class="exhibit" aria-label="Example alert, sample data">
<div class="label"><b>Missing from the CRM</b><span>Sample data &middot; <span class="t">Tue 13:05</span></span></div>
<p>3 Zoopla enquiries in a row haven't reached your CRM. Every Zoopla enquiry since <span class="t">12:40</span> is missing, while the other portals are fine. The emails are still arriving, so the parser has most likely stopped recognising them.</p>
</figure>
<p>Each week you get one line per portal: enquiries received, and how many reached the CRM. It can't see enquiries that never reached your inbox at all, such as a phone call nobody logged.</p>
<a class="demo" href="https://abiodunolaoluwa.github.io/enquiry-watchdog/">Try the watchdog on sample data</a></div>

<div class="item"><h3>The out-of-hours first reply</h3>
<p>When the office is closed, the applicant gets a reply within minutes asking the questions you choose, for example move-in date, budget, pets and when they could view. Every draft is checked on the server against your rules before it goes out, such as never confirming a viewing, a price or availability, never discussing deposits, and passing complaints and landlord messages straight to a person. If a draft breaks a rule, it gets one rewrite; if that fails too, nothing is sent and the enquiry goes to your team with a note.</p>
<a class="demo" href="https://reply-desk-8rzb.onrender.com">See the reply demo</a></div>
</section>

<section class="clause"><h2>How we'd start</h2>
<ol class="schedule">
<li><div><h3>Tell me your setup <span class="cost">Free</span></h3><p>Reply with the portals you list on and the CRM you use, and I'll send a one-page plan for your agency: what I'd check, what I'd need, and what it would cost. No access needed for this.</p></div></li>
<li><div><h3>A two-week check, if the plan makes sense <span class="cost">Free</span></h3><p>Read-only access to the inbox your portal emails land in, plus a CRM export for the same fortnight, under a short data agreement. You get back how many enquiries each portal sent, how many reached the CRM, how long the first reply took, and anything that went missing.</p></div></li>
<li><div><h3>A fixed-price build <span class="cost">&pound;1,500 to &pound;3,500</span></h3><p>Usually two to three weeks, on the accounts and CRM you already use.</p></div></li>
<li><div><h3>A monthly care plan <span class="cost">&pound;250 to &pound;500 a month</span></h3><p>I keep an eye on it, fix it when a portal changes its emails, make small changes, and send a one-page report each month. Cancel with a month's notice.</p></div></li>
</ol></section>

<section class="clause"><h2>Your data</h2>
<p>Where possible the software runs in your own accounts, and where it can't, on a small server set up in your agency's name that you can switch off. I work with the least access the job needs, you can revoke it at any time, and when the free check ends I remove my access, delete anything I exported, and confirm it in writing. I sign a data processing agreement before I touch anything.</p>
<p>Nothing replies on your behalf until you've approved how it speaks, and it can run in draft-only mode for as long as you like.</p></section>

<section class="clause"><h2>Who you'd be working with</h2>
<p>I'm Olaoluwa Abiodun, an engineer based in Lagos, Nigeria, working UK hours (Lagos is an hour ahead of London in winter and level with it in summer). I built Rentyx, a property-management platform, end to end, including an assistant that answered tenants' and landlords' WhatsApp messages under rules the server checked before anything went out, handing anything unclear to me.</p>
<p>You'd be one of my first agency clients, which is why the check is free and the build price is fixed.</p></section>

<section class="clause"><h2>Questions</h2>
<dl class="faq">
<dt>Which CRMs does it work with?</dt><dd>I haven't worked with every lettings CRM, so I check what yours allows (an API, an email-in address or exports) before I quote.</dd>
<dt>What if a reply goes wrong?</dt><dd>It only sends replies that pass your rules, and anything they don't cover goes to a person. You can start in draft-only mode, where your team approves every reply.</dd>
<dt>Why are you in Lagos?</dt><dd>That's where I live. The work is all online, and my day overlaps yours.</dd>
</dl></section>

<div class="close"><p>Email me with your agency's name, the portals you list on and the CRM you use. I'll send the one-page plan within two working days.</p>
<a class="button" href="mailto:mate.olaoluwa@gmail.com?subject=One-page%20plan%20for%20our%20agency">Email Olaoluwa</a></div>
""",
    glance=glance([("For", "Independent letting and estate agents"),
                   ("First step", "A one-page plan for your agency within two working days. Free, no access needed."),
                   ("Then", "A free two-week check, then a fixed-price build of two to three weeks"),
                   ("Price", "Build &pound;1,500 to &pound;3,500<br>Care plan &pound;250 to &pound;500 a month"),
                   ("Hours", "UK working hours, from Lagos")],
                  "Ask for the one-page plan", "One-page plan for our agency",
                  "Tell me the portals you list on and the CRM you use."),
)

# ---------------------------------------------------------------- recruitment
RECRUITMENT = page(
    slug="recruitment", ink="recruitment",
    title="Sourcing for independent recruitment agencies",
    description="People who fit your live roles, with verified work emails and a first line drafted for your consultant to approve.",
    masthead=meta([("For", "Independent recruitment agencies"),
                   ("From", "Olaoluwa Abiodun, software engineer, Lagos"),
                   ("Start", "<strong>A free sample</strong> for one of your public job adverts")])
    + "<h1>People who fit your live roles, with verified work emails and a first line drafted.</h1>"
    + '<p class="deck">I\'ve spent two years in recruiting, and I build the sourcing side for small agencies: people who fit a live role, found in public sources, with work emails verified and a first line drafted for your consultant to approve.</p>',
    body="""
<section class="clause"><h2>Where I'm coming from</h2>
<p>Most of my recruiting has been sourcing for early-stage US startups: I've contacted about 1,000 candidates through personalised four-step email sequences, contributed to five placements, and contributed to the workflows that found candidates' contact details and drafted each email's opening line. Finding people who fit, finding an email that works, and writing a first line that doesn't read like a template are the parts I build for agencies.</p></section>

<section class="clause"><h2>What I build</h2>
<div class="item"><h3>Sourcing for a live role</h3>
<p>You send the brief and choose the sources. For engineering or construction that might be company team pages, project announcements, public professional registers and conference speaker lists. You set the criteria (must-haves, nice-to-haves, location), and the list shows which ones each person meets and where that came from, so your consultant can check it and change the criteria.</p></div>
<div class="item"><h3>Verified work emails</h3>
<p>The address is worked out from the company's own email pattern, then verified with an email-checking service, which confirms the mail server accepts that address. It can't promise the person reads it. If no address verifies, the person is listed without one rather than guessed. On an outreach list I built for my own project, this took bounces from 12.3% to 2.9%.</p></div>
<div class="item"><h3>One record per person</h3>
<p>The same person found on two sites becomes one record, so nobody gets two messages from you.</p></div>
<div class="item"><h3>A draft first line for each person</h3>
<p>Based on something they actually did, like a project they delivered or a talk they gave. Your consultant approves, edits or bins it. Nothing sends on its own.</p></div>

<figure class="sample" aria-label="One row of a sample, fictional person">
<div class="label">One row of a sample &middot; fictional person</div>
<dl>
<dt>Person</dt><dd>Priya N., Senior Site Manager, Northgate Build Ltd (fictional)</dd>
<dt>Fits because</dt><dd>Must-have: 5+ years running school or hospital builds (company news page, March 2026: led a &pound;12m school extension in Leeds). Location: West Yorkshire (team page).</dd>
<dt>Work email</dt><dd>Verified</dd>
<dt>Draft first line</dt><dd>"Saw that the Leeds school extension finished on time in March, which can't have been easy over winter."</dd>
</dl>
</figure>
<a class="demo" href="https://lead-engine-yqxv.onrender.com">See the sourcing and matching on sample data</a>
</section>

<section class="clause"><h2>How we'd start</h2>
<ol class="schedule">
<li><div><h3>A free sample <span class="cost">Free</span></h3><p>Send me a link to one of your public job adverts. Within three working days you get a spreadsheet of up to ten people who fit, each with the criteria they meet and where that came from, a verified work email where one exists, and a draft first line. You keep the spreadsheet, and I delete my copy within a week of sending it. A short data agreement covers it.</p></div></li>
<li><div><h3>A fixed-price build <span class="cost">&pound;1,500 to &pound;3,500</span></h3><p>Set up for your sectors and the system you use, usually two to three weeks.</p></div></li>
<li><div><h3>A monthly care plan <span class="cost">&pound;250 to &pound;500 a month</span></h3><p>I keep the sources working as sites change, tune the criteria with your feedback, and send a short monthly report. Cancel with a month's notice.</p></div></li>
</ol></section>

<section class="clause"><h2>Your data</h2>
<p>Candidate data ends up in your systems, not mine. I sign a data processing agreement before any work starts, and you decide who gets contacted and what they're sent.</p></section>

<section class="clause"><h2>Who you'd be working with</h2>
<p>I'm Olaoluwa Abiodun, an engineer based in Lagos, Nigeria, working UK hours. Alongside recruiting, I built Rentyx, a property-management platform, end to end. You'd be one of my first agency clients, which is why the sample is free and the build price is fixed.</p></section>

<section class="clause"><h2>Questions</h2>
<dl class="faq">
<dt>Does it work with our ATS?</dt><dd>I'll work with the system you already use, and check what it allows before I quote.</dd>
<dt>Which sources won't you use?</dt><dd>Any site whose terms don't allow it. You see the source of every name.</dd>
</dl></section>

<div class="close"><p>Email me a link to one of your job adverts and tell me the sector you recruit for. I'll put the sample together within three working days.</p>
<a class="button" href="mailto:mate.olaoluwa@gmail.com?subject=Free%20sourcing%20sample">Email Olaoluwa</a></div>
""",
    glance=glance([("For", "Independent recruitment agencies"),
                   ("First step", "Up to ten people for one of your public job adverts, within three working days. Free."),
                   ("Then", "A fixed-price build of two to three weeks, set up for your sectors"),
                   ("Price", "Build &pound;1,500 to &pound;3,500<br>Care plan &pound;250 to &pound;500 a month"),
                   ("Hours", "UK working hours, from Lagos")],
                  "Ask for a free sample", "Free sourcing sample",
                  "Send a link to one public job advert."),
)

# ---------------------------------------------------------------- white-label
WHITE_LABEL = page(
    slug="white-label", ink="white-label",
    title="White-label build help for automation agencies",
    description="The code-heavy part of a client build, done under your name: custom steps, awkward APIs, scrapers and LLM steps with checks.",
    masthead=meta([("For", "Automation and CRM agencies"),
                   ("From", "Olaoluwa Abiodun, software engineer, Lagos"),
                   ("Start", "<strong>A free scope and fixed quote</strong> within two working days")])
    + "<h1>The code-heavy part of a client build, done under your name.</h1>"
    + '<p class="deck">Your team keeps the workflow in n8n or Make. When a step needs real code, like a custom node, an awkward API, a scraper or an LLM step that needs rules around it, I write that piece, document it, and hand it back under your brand.</p>',
    body="""
<section class="clause"><h2>The kind of thing I pick up</h2>
<ul class="lede-list">
<li>A client's API that rate-limits, paginates oddly and fails at 2am, so the flow needs retries, logging and a way to replay what failed.</li>
<li>A scraper with checks that tell you when the source site has changed, instead of quietly returning nothing.</li>
<li>An LLM step whose drafts have to pass fixed checks before anything is sent.</li>
</ul></section>

<section class="clause"><h2>Two things I've built that look like agency work</h2>
<div class="item"><h3>Lead Engine</h3>
<p>Pulls firms from directories with different page layouts, keeps a field only when it can quote it from the page, merges the same firm found in two places, and picks up where it stopped after a failure.</p>
<a class="demo" href="https://lead-engine-yqxv.onrender.com">Lead Engine demo</a></div>
<div class="item"><h3>Reply Desk</h3>
<p>Answers inbound messages with a model, but every draft has to pass checks on the server. A draft that fails gets one rewrite and is then held for a person, and there's a kill switch and a daily cap.</p>
<a class="demo" href="https://reply-desk-8rzb.onrender.com">Reply Desk demo</a></div>
<p>I also built search over legal texts that quotes the paragraph it relied on, or refuses: <a href="https://cite-desk.onrender.com">Cite Desk</a>.</p>
</section>

<section class="clause"><h2>How we'd work</h2>
<ol class="schedule">
<li><div><h3>Send me five lines, or a redacted workflow export <span class="cost">Free</span></h3><p>No client data needed. Within two working days you get a scope, the approach I'd take, and a fixed quote.</p></div></li>
<li><div><h3>One fixed piece first <span class="cost">Fixed quote</span></h3><p>Typically a single code step, integration or small service, delivered in under a week with a README and tests, so you can judge the work without committing to more.</p></div></li>
<li><div><h3>Your conventions</h3><p>My code sits where your team can see it: a code node inside the workflow, or a small service in your account that the workflow calls. Your repo, naming and documentation, with handover notes your team can maintain, and I fix bugs in my code free for 30 days after handover.</p></div></li>
<li><div><h3>Then per project, or a monthly block of hours</h3><p>Whichever suits your pipeline.</p></div></li>
</ol></section>

<section class="clause"><h2>Who you'd be working with</h2>
<p>I'm Olaoluwa Abiodun, an engineer based in Lagos, Nigeria, on UK and European hours. I'm code-first (TypeScript, Python, PostgreSQL) and built Rentyx, a property-management platform, end to end. I work inside n8n and Make when the job needs it, and your team stays the experts on those tools. My code is on <a href="https://github.com/AbiodunOlaoluwa">GitHub</a>.</p></section>

<section class="clause"><h2>Questions</h2>
<dl class="faq">
<dt>Will you contact our client?</dt><dd>Only if you ask me to.</dd>
<dt>Who owns the code?</dt><dd>You or your client, on payment.</dd>
<dt>What about NDAs and client data?</dt><dd>I'll sign your NDA and a sub-processor agreement, and I don't need client data to quote.</dd>
</dl></section>

<div class="close"><p>Email me the piece your team would rather not build. I'll reply within two working days with a free scope and a fixed quote.</p>
<a class="button" href="mailto:mate.olaoluwa@gmail.com?subject=Scope%20and%20quote%20request">Email Olaoluwa</a></div>
""",
    glance=glance([("For", "Automation and CRM agencies"),
                   ("First step", "A free scope and fixed quote within two working days. No client data needed."),
                   ("Then", "One fixed piece, usually under a week, with a README and tests"),
                   ("After", "Per project, or a monthly block of hours"),
                   ("Hours", "UK and European hours, from Lagos")],
                  "Ask for a scope and quote", "Scope and quote request",
                  "Five lines on the piece you need is enough."),
)

# ---------------------------------------------------------------- index
INDEX = page(
    slug="", ink="neutral",
    title="Olaoluwa Abiodun: small systems for small teams",
    description="Software engineer in Lagos building and looking after small systems for letting agents, recruitment agencies and automation agencies.",
    masthead=meta([("From", "Olaoluwa Abiodun, software engineer, Lagos"), ("Hours", "UK and European working hours")])
    + "<h1>Small systems for three kinds of business, built and then looked after.</h1>"
    + '<p class="deck">Each one starts with something free and small, so you can judge the work before you pay for anything.</p>',
    body="""
<ul class="offers">
<li><a href="lettings/"><span class="who">Letting and estate agents</span><span class="what">Find the portal enquiries that never reached your CRM</span><span class="go">Read &rarr;</span></a></li>
<li><a href="recruitment/"><span class="who">Recruitment agencies</span><span class="what">People who fit your live roles, with verified work emails</span><span class="go">Read &rarr;</span></a></li>
<li><a href="white-label/"><span class="who">Automation and CRM agencies</span><span class="what">The code-heavy part of a client build, under your name</span><span class="go">Read &rarr;</span></a></li>
</ul>
""",
)


def privacy():
    import re
    src = (ROOT / "copy-privacy.md").read_text()
    body = src.split("Updated: 15 November 2026", 1)[1]
    html, items = [], []

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
    out = out.replace("mate.olaoluwa@gmail.com", f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
    out = out.replace("(ico.org.uk)", '(<a href="https://ico.org.uk/make-a-complaint/">ico.org.uk</a>)')
    out = out.replace("(ndpc.gov.ng)", '(<a href="https://ndpc.gov.ng">ndpc.gov.ng</a>)')
    return page(
        slug="privacy", ink="neutral", title="Privacy notice: Olaoluwa Abiodun",
        description="How Olaoluwa Abiodun handles the personal details of people he contacts about his services.",
        masthead=meta([("From", "Olaoluwa Abiodun, sole trader, Lagos, Nigeria"), ("Updated", "15 November 2026")])
        + "<h1>Privacy notice</h1>"
        + '<p class="deck">How I handle the details of people I contact about my work, and what you can ask me to do with them.</p>',
        body=out,
    )


if __name__ == "__main__":
    write("", INDEX)
    write("lettings", LETTINGS)
    write("recruitment", RECRUITMENT)
    write("white-label", WHITE_LABEL)
    write("privacy", privacy())
