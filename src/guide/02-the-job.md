---

## Part 4. The job, step by step

Every client goes through the same eight steps. The **Practitioner Checklist** has one box for every task below.

| Step | Name | Question it answers | Typical time (small site) |
|---|---|---|---|
| 0 | Scope | What does the client need, and what can I promise? | 1 to 2 hours |
| 1 | Inspect | Where does the brand stand today? | 1 to 3 days |
| 2 | Diagnose | Why is it there, and what matters most? | Half a day |
| 3 | Suggest | What should we do, in what order? | Half a day to 1 day |
| 4 | Implement | Build the fixes | Weeks to months |
| 5 | Measure | Did it work? | Monthly |
| 6 | Maintain | Keep it healthy | Weekly to quarterly |
| 7 | Improve | Grow beyond the fixes | Ongoing |

### Step 0. Scope the job

Goal: agree on what you will do, for whom, and how success is measured, before you touch anything.

Collect:
- **The business.** What they sell, to whom, where, how they make money, average deal size. This sets business potential for every keyword and prompt.
- **The brand.** Exact name and every spelling, domain, parent company, sub-brands, products, founders and leaders, address, founding year. These become the **fact sheet**.
- **Positioning.** The one thing they want to be known for, in one line, plus 3 proof points. Ramonov's pattern: "the one thing" + proof + proof + proof. Example: "Number one AI educator for entrepreneurs. 3M followers. Forbes 30 Under 30."
- **Competitors.** 3 to 5 that buyers really compare them with. Also the **search competitors**: sites that rank for the client's topics, even if they sell nothing.
- **Markets.** Countries and languages. AI answers change by country.
- **Customer voice.** Sales call notes, support tickets, reviews (theirs and competitors'), Reddit threads. Ramonov: "Don't guess. Go look." This is where real buyer questions come from.
- **Access.** Google Search Console, Google Analytics 4, Bing Webmaster Tools, website admin (CMS), DNS or Cloudflare, Google Business Profile, social profiles. Note who owns each one.
- **Budget and limits.** Tool budget, approval rules, legal rules (for example claims about competitors), brand voice.

- **Map the brand's names (entities).** List every name the brand goes by: the main brand, sub-brands, product names, named features, its own metrics or methods, and the people tied to it (founders, experts). Ahrefs' example for itself: Ahrefs; Site Explorer, Brand Radar; Domain Rating; Tim Soulo, Patrick Stox. Each name can be tested on its own later. For each, write the topics and qualities people should link to it ("affordable", "enterprise", "for engineers").

Expert tip: write down **what you will not do** (for example, no link buying, no Wikipedia edits). It protects you and the client.

### Step 1. Inspect (the audit)

Inspect in this order. It follows the gates: reach, read, trust, chosen, credited.

#### 1A. Business baseline

- Organic traffic trend for 12 months (Search Console, GA4, or an SEO tool estimate).
- Top pages and top queries. Branded versus unbranded queries.
- Conversions and where they come from.

Why: you need the "before" numbers. A traffic drop may be a season, a site change, or an algorithm update. Note the dates of big changes.

#### 1B. Crawl and index (technical SEO)

| Check | Why | How |
|---|---|---|
| Homepage and key pages load (HTTP 200) | If a page fails, nothing else matters | Browser, crawler |
| One preferred version of the site (https, with or without www) | Duplicates split signals | Type all four versions; each should redirect once to one |
| robots.txt does not block important pages | **robots.txt** is a file at `site.com/robots.txt` that tells bots where they may go | Read it; test in Search Console |
| No `noindex` on pages that should rank | A **noindex** tag tells search engines not to store the page. Common after a redesign | Crawler, view page source |
| XML sitemap exists, is listed in robots.txt, and is submitted | A **sitemap** lists the pages you want found | Open `site.com/sitemap.xml`; Search Console |
| Canonical tags are correct | A **canonical** tag names the preferred URL when pages are similar | Crawler |
| No broken internal links, no redirect chains | Broken links waste crawl and frustrate people | Crawler |
| No orphan pages | An **orphan** page has no internal links pointing to it, so bots and people cannot find it | Crawler plus sitemap |
| Key pages within 3 clicks of the homepage | Deep pages get crawled and valued less | Crawler (crawl depth) |
| Pages indexed in Search Console | Shows what Google actually stored | Search Console, Pages report |
| Speed and Core Web Vitals | Slow pages rank and convert worse; AI fetchers may drop slow pages | PageSpeed Insights. Targets: LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less |
| Mobile friendly | Google indexes the mobile version | PageSpeed Insights, a phone |
| HTTPS everywhere | Security and trust | Browser padlock, crawler |

#### 1C. AI access (technical AEO)

| Check | Why | How |
|---|---|---|
| AI search bots allowed in robots.txt | These bots fetch pages at answer time: OAI-SearchBot and ChatGPT-User (OpenAI), Claude-SearchBot and Claude-User (Anthropic), PerplexityBot and Perplexity-User. Block them and the site drops out of live answers | Read robots.txt line by line |
| Training bots: a deliberate choice | GPTBot, ClaudeBot, Google-Extended and CCBot collect training data. Blocking them is a valid business choice. Blocking everything is the "full lockdown paradox": you vanish from live answers too | Ask the owner what they want |
| No firewall block | A security service can return a 403 (forbidden) or a challenge page to bots even when robots.txt allows them. Ahrefs reports about 5.9% of 140 million sites block GPTBot | Request the page with an AI bot user agent; check Cloudflare settings. Real proof is in server logs |
| Cloudflare AI settings | Cloudflare can add AI blocks to robots.txt by default | Cloudflare dashboard |
| Text is in the raw HTML | ChatGPT's crawler does not run JavaScript. If the text appears only after scripts run, it sees an empty page | Turn JavaScript off in the browser, or view the raw source; search for a key sentence |
| No hidden facts | Facts inside images, PDFs only, tabs, accordions or pop-ups are often missed | Look at the page as plain text |
| Agent readiness (optional) | Newer signals: llms.txt, Markdown versions of pages, agent protocols | isitagentready.com (Cloudflare) |

#### 1D. On-page SEO

| Check | Good looks like |
|---|---|
| Each key page has one main topic | No two pages fight for the same main keyword (this fight is called **cannibalization**) |
| Title tag | Unique, about 60 characters or less, includes the topic or a close variant |
| Meta description | Unique summary. Ahrefs found Google rewrites about 63% of them, so do not spend hours, but do write them |
| URL slug | Short, readable, hyphens: `/best-golf-balls` not `/p?id=4482` |
| Headings | One H1; H2 and H3 in order |
| Intent match | Same content type, format and angle as most top results |
| Content gap | Covers the subtopics the top 3 pages cover |
| Internal links | Related pages link to each other with clear anchor text (the clickable words) |
| Images | Descriptive file names, alt text (a short description for screen readers and search), compressed files |
| Readability | Short sentences and paragraphs, about grade 6 to 8. Hemingway App is a free check |
| Open Graph tags | Control how the page looks when shared on social media |
| Schema markup | Valid structured data for the page type (more in 1F) |

#### 1E. Content for AI answers

Pick the 10 to 20 most important pages. For each, check:

- **Question headings.** H2 and H3 phrased the way buyers ask ("How much does X cost?" beats "Pricing").
- **Answer first.** The first one or two sentences under each heading answer it. This is **BLUF**: bottom line up front. Humans and AI both weigh the start of a passage most.
- **Atomic sections.** Each section makes sense alone. No "As mentioned above" or "This" with no subject. Test: cover the page except one paragraph. Can it answer a question by itself?
- **Entities.** Name the brand, products, people and places instead of "our tool" or "it".
- **Specifics.** Numbers, dates, conditions, examples. No empty sales words ("world-class", "seamless").
- **Evidence.** Sources linked, named experts, first-party data.
- **Author.** A real person with credentials.
- **Tables.** Real HTML tables. Each row should make sense alone ("Teams of 5 to 20, posting to 8 platforms: $49 a month").
- **FAQ.** Real buyer questions with direct answers.
- **Freshness.** Visible update date, and real updates in the last 30 to 90 days on key pages.
- **Formats.** Does the site have the pages AI looks for: "best X for Y", "brand vs competitor", "competitor alternatives", pricing, FAQ, a facts page, tools or calculators?
- **Original ideas carry the brand name.** Ahrefs advice: AI tends to absorb a new idea without credit. Name it ("the Ahrefs content scoring matrix") and repeat it in many places.

#### 1F. Entity and positioning

An **entity** is a thing with stable facts: the company, its parent, people, products, places. AI and Google's **Knowledge Graph** store entities and how they connect.

| Check | Good looks like |
|---|---|
| Organization schema (or Person, CollegeOrUniversity, LocalBusiness) | Name, legal name, URL, logo, `sameAs` |
| `sameAs` links | Only the brand's own official profiles. Never partners, clients or press articles |
| About page | Founders, leaders, address, founding year, what the brand does |
| One name form | Same spelling in titles, schema and text |
| No contradictions | Year, phone, email, address match on every page |
| Facts or FAQ page | Answers the fact-sheet questions with specific values |
| People pages | Founders and experts with a bio, photo, links |
| Wikidata and Wikipedia | Do they exist, and do they link to the official site? Never edit them yourself for a client; prepare a request with sources |
| Lookalike brands | Search the name: other companies, places or products with a similar name. Mauna Loa lost questions to the volcano |
| Positioning everywhere | The one-liner on the homepage title or meta, About page, schema description, LinkedIn headline and company page, other socials, directories, podcast bios |
| **Source-of-truth grid** | 8 to 10 core facts as rows; sources as columns (own site, Wikipedia, Wikidata, LinkedIn, business listings, top third-party pages, AI answers). Mark every wrong cell red. Fix the source that corrects the most answers first |

#### 1G. Authority and links

- Referring domains (number of other sites linking in) and domain rating, against the pages that rank top 3 for target keywords.
- Link quality: **relevant** (same topic), **authoritative** (strong page), **followed** (no `nofollow`, `ugc` or `sponsored` tag), descriptive anchor, placed in the body text.
- Bad signs: sudden spikes of spammy links, links from unrelated foreign sites, keyword-stuffed anchors.
- **Unlinked mentions:** pages that name the brand without linking. Easy outreach wins.

#### 1H. Off-site presence and reputation

- Which domains AI cites for the category (from step 1K).
- "Best X" lists, comparisons and reviews in the niche: is the brand there, and correct?
- Review sites (G2, Capterra, Trustpilot, Google reviews, industry sites).
- Reddit and Quora threads that rank or get cited.
- YouTube: does the brand have videos on topics people search?
- News, podcasts, industry associations, directories.

#### 1I. Local presence (if the brand serves an area)

- Google Business Profile: correct name, address, phone (**NAP**), category, hours, photos, reviews answered.
- Bing Places and Apple Business Connect.
- **Citations** (in local SEO this means listings of NAP on directories): Better Business Bureau, Yelp, industry directories. All must match exactly.
- Location pages on the site.

#### 1J. Keyword and prompt research

This is where you find what people search and ask, and which of those searches are worth winning. Do it before you finish the prompt set in 1K.

**Find ideas.**
1. List 10 **seed keywords**: short, broad terms for the niche (for example "golf clubs", "golf balls"). You can ask an AI assistant to suggest seeds and modifiers for the business.
2. Add **modifiers**. Commercial ones: best, top, vs, review, alternative, price. Informational ones: how, what, why, guide, tutorial. Tool ones: calculator, checker, generator, template, planner.
3. Put seeds and modifiers into a keyword tool (phrase match) to get real keywords with volume.
4. Look at the **top pages of search competitors**. They often rank for keywords that do not contain your seeds.
5. Add the real questions from customer voice (step 0).

**Judge each keyword. Ahrefs' checklist, plus the AI filter:**

| Test | Question | How |
|---|---|---|
| Search demand | Do people search for it? | Search volume (for example 300+ a month for a niche, lower for B2B) |
| Traffic potential | How much traffic does the top page get from all its keywords? | Look at the top page's total traffic. It beats search volume as a guide, because not every search leads to a click |
| Business potential | Would ranking for it help the business? | Score 0 to 3. 3: the product is the natural answer. 0: no link to the business |
| Intent | Can we make the kind of page that wins? | The 3 Cs of the top results |
| Difficulty | Can we win in a reasonable time? | Four questions: do some top pages miss the intent? Can we earn more quality links than the top pages? Is our site's authority in the same range? Are we as topically focused? More "yes" = better chance |
| **AI filter** | Does the AI answer fully satisfy the searcher? | Search it. If an AI Overview answers it completely, a click is unlikely. Treat it as a **mention target** (aim to be named in the answer), not a **click target** |

Ahrefs reports AI Overviews appear on about 21% of keywords overall, but on about 58% of question keywords, and nearly all of them are informational. Tool and transactional searches mostly show no AI Overview, so the click is still there to win.

**Output:** a keyword map (one main keyword per page, plus related keywords), a list of mention targets, and a list of new pages to build.

**Prompts are different from keywords.** People type full sentences with context into AI tools ("I run a small agency; which tool should I pick?"). Every person phrases it differently, and the AI fans each one out into many sub-searches. So you do not chase single prompts. You build visibility across the whole topic, and you test with a fixed set of prompts that stands for the topic.

#### 1K. AI visibility and Brand Truth baseline

1. **Build the question set.** 40 to 100 or more prompts across:
   - Branded: "What is [brand]?", "Who owns [brand]?", "[brand] pricing".
   - Unbranded category: "best [category] for [buyer]".
   - Comparison: "[brand] vs [competitor]", "[competitor] alternatives".
   - Problem: the buyer's pain in their own words.
   - Should-not-recommend: cases where the brand is a bad fit (tests honesty).
   Keep at least 40% unbranded. That is where new buyers are.
2. **Run it** on Google AI Overviews, AI Mode, ChatGPT, Gemini, Perplexity and Claude, at least. Use a tracking tool, an API, or a logged-out browser set to the right country. Record platform, date, country, search on or off, the answer, and every cited URL.
3. **Score visibility.** Per answer: named and cited, named only, cited only, or not visible. Share of voice against competitors. One public formula (Brandleap's free index): 50 points if named and cited, 30 if named only, 20 if cited only, per engine; average over prompts.
4. **Brand Truth.** About 30 fact questions, 3 or more runs. Grade each answer against the fact sheet: Correct, Partial, Out of date, Wrong, Invented, No answer. A person checks the grades. Brandleap's human reviewers changed 30 of 352 machine grades, so do not skip this.
5. **Narrative.** Does AI describe the brand the way the brand wants (the positioning words)? Is the tone positive?

#### 1L. Measurement setup

- Search Console and Bing Webmaster Tools verified.
- GA4 has an "AI traffic" channel group (regex on referrers such as chatgpt.com, chat.openai.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai, deepseek.com).
- Forms ask "How did you hear about us?" with AI options.
- Conversions are tracked.
- Optional: server logs or Cloudflare analytics for AI bot visits.

#### 1M. Compliance basics (checks, not legal advice)

- HTTPS, privacy policy, terms, cookie consent where the law needs it.
- Accessibility basics (WCAG 2.2 AA is the usual target): page language set, image alt text, form labels, heading order, contrast, keyboard use.
- Reviews and testimonials are real; incentives disclosed (the US FTC has a rule on fake reviews and testimonials).
- Paid and affiliate links disclosed and marked `rel="sponsored"`.

#### 1N. Competitors

Run a light version of 1D to 1K on 2 or 3 competitors. Note what they have that the client lacks: formats, mentions, links, videos, reviews, entity facts.

### Step 2. Diagnose

Turn findings into causes and a ranked list.

1. **Group by gate.** Discovery, retrieval, selection, inclusion, representation. Fix the earliest broken gate first.
2. **Use Ahrefs' six brand gaps** to see the whole picture:

| Gap | Question |
|---|---|
| Visibility | Are we named less than competitors? |
| Narrative | Does AI describe us the wrong way? |
| Topic | Which topics are linked to competitors, not us? |
| Format | Which formats get cited that we do not make (video, lists, comparisons)? |
| Web mentions | Which sites mention competitors but not us? |
| Demand | Do enough people search for our brand at all? |

3. **Find root causes.** Many wrong answers often trace back to one source: an old press release, a wrong directory listing, a Wikipedia line, a lookalike brand. Fix the cause, not each symptom.
4. **Score each fix.** Simple formula: priority = impact × confidence ÷ effort. Brandleap's Truth Risk Score for wrong facts: (severity × 0.6 + imminence × 0.4) × 10, where severity is the harm if repeated and imminence is how likely it is repeated now. Critical 80+, High 65+, Moderate 50+, Watch below 50.
5. **Label each fix:** Fix (improve what exists), Build (make something new), or Influence (earn mentions off-site). This is Ahrefs' split.
6. **Place the site on a maturity scale** (optional, useful for clients). Brandleap uses five levels: Invisible (engines cannot reach or read it), Crawlable, Structured, Answer-Ready, Agent-Native. A site cannot skip a level. It gives the client a simple "you are here, next is there".

Quick wins first: a page that already ranks and only needs a content update, or a big list that names every competitor but your client.

### Step 3. Suggest

What an expert hands over:

1. **One-page summary.** Scores, the 3 to 5 biggest findings, the 5 fixes that matter most, and the limits of the test.
2. **The full audit.** Every check with evidence (screenshots, URLs, answers).
3. **A prioritized fix list.** For each fix: what, why, who does it, time, access needed, and "done when".
4. **A 30-day and 90-day plan.** A common shape:
   - Week 1: claims register (approved facts with sources) and baseline.
   - Week 2: fix identity contradictions, canonical pages, official profiles.
   - Week 3: publish evidence pages for the top 3 gaps; update the facts page.
   - Week 4: rerun the same tests; list what is still missing.
   - Days 30 to 90: own site first, then the knowledge graph and profiles, then off-site evidence and measurement. Technical before content; earned (off-site) work runs all the time.
5. **What you need from them.** Access, approvals, facts to confirm.

Keep **four records** for every client (Brandleap's practice). They make every later report provable:
1. A visibility baseline per platform (dated).
2. The prompt and question map.
3. A log of every URL the AI tools cited.
4. A hypothesis, test and change log.

Write it for the reader. A marketing lead wants plain words and business impact. A developer wants exact steps and files.

### Step 4. Implement

Work in this order unless the data says otherwise.

**4A. Unblock (technical).** Allow AI search bots; fix firewall blocks; fix noindex, canonicals, redirects, broken links, sitemap; server-side render key text; speed up the slowest templates. Submit the sitemap; turn on IndexNow if the site supports it (it tells Bing and others about changes at once).

**4B. Identity (entity).** Organization or Person schema with correct `sameAs`; About and facts pages; one name form; fix contradictions; align profiles (LinkedIn, socials, directories, Google Business Profile); write the positioning one-liner everywhere; prepare Wikidata or Wikipedia change requests with sources (never edit for a client).

**4C. Rewrite key pages (content).** Use the 5-part section pattern from the book:
1. Heading phrased like the buyer's question.
2. The direct answer in the first one or two sentences.
3. Detail: numbers, conditions, examples.
4. Evidence: a source, a named expert, first-party data.
5. No references that break when the chunk stands alone.

Match the page to the **query type** (from the book):
- **Simple factual** ("When was X founded?"): one crisp, clearly stated fact.
- **Multistep** ("Which X fits a team of 10 with a $5,000 budget?"): well-linked pages that cover each part.
- **Agentic** (the AI plans and acts, for example compares options or books): structured, complete data such as prices, specs, availability.

**4D. Build missing pages.** "Best X for Y", "brand vs competitor", "competitor alternatives", pricing, FAQ, facts page, glossary, tools or calculators (AI cannot replace a tool, so these keep their clicks), case studies with numbers. Original data or research is the strongest asset: it earns links and citations.

**4E. Earn mentions (off-site).** Ahrefs' three tiers:
1. **Third-party editorial:** lists, reviews, comparisons, industry publications, YouTube reviews. Hardest and most valuable.
2. **Communities:** Reddit, Quora, niche forums. Answer real questions honestly, disclose who you are, never spam.
3. **Own properties:** YouTube channel, podcast, LinkedIn, other sites the brand owns.

How to do outreach well (Ahrefs Advanced Link Building):
- **Content decides the pitch.** You need a real reason to contact someone: an outdated stat on their page, a missing option on their list, a wrong fact about the brand.
- **Seed and lookalike prospects.** Find pages that link or mention for a specific reason (the "linkable point"). Then find more pages like them with the same footprint.
- **Segment by reason.** Each segment gets its own email. Personal, but at scale.
- **Vet.** Real site, relevant, still has the issue, has traffic, right language.
- **Contact the right person.** Authors and editors convert best. Sam Oh's campaign: authors 7.56%, editors 7.55%, generic inboxes 4%, other titles 1.64%.
- **Test on a small batch first** (the **blitz list**), then scale if it works.
- **Write to one person as if to a friend, then turn it into a template.** Short. One real benefit for their readers. One honest line about your weaknesses. Ask for feedback or a mention, not just a link.
- Hybrid outreach typically converts at 5 to 12% (Sam Oh's experience).
- **Only pitch your best work.** A plain "what is X" page gives no reason to link.

The shape of a good outreach email (Ahrefs SEO course):

| Part | Job | Example (guest post pitch) |
|---|---|---|
| Subject line | Get it opened, honestly | "New data: best balls for high handicappers" |
| Opening | Say why you are writing | "You have guides on golf balls for kids and for distance, but none for high handicappers." |
| Why you | Qualify yourself and justify the ask | "I am a high handicapper and tested 20 balls on a launch monitor." |
| The pitch | The ask plus the value for their readers | "I would like to write that guide for you, with all the data, to help your buyers choose." |
| Close | Start a conversation, not a hard sell | "Would that be useful?" |

Three ways to approach outreach: **shotgun** (same email to everyone: fast, but spammy and burns the brand), **sniper** (fully personal, few targets: slow, best links), and **hybrid** (personal per segment: Sam Oh's recommendation for most work).

Also:
- **Digital PR:** press releases only for real news (launch, key hire, award, milestone, partnership). Syndicated copies count as one source.
- **Expert sourcing:** answer journalist requests fast, short, with credentials first. (HARO, the service named in the Ahrefs course, has changed hands since the course was recorded. Check which journalist request services are active before you rely on one.)
- **Podcasts and YouTube:** each appearance leaves show notes and a transcript that AI can read. For YouTube: keyword in the title, a real description, timestamps, and say the keyword out loud. Ahrefs reports YouTube mentions had the strongest link to ChatGPT visibility of the factors it studied (0.737).

**4F. Local.** Clean up Google Business Profile, Bing Places, Apple; fix NAP on directories; start a review request routine.

**4G. Measurement.** Set up everything in 1L if missing.

Rules while implementing:
- Change one thing at a time where you can, and log it (date, page, change). The **change log** is how you later prove what worked.
- Get approval for facts, claims about competitors, and anything legal.
- Never fake freshness (changing only the date).

### Step 5. Measure and report

Three ways to see AI impact (Ahrefs):
1. **Referral traffic** from AI tools in GA4. It undercounts: some tools strip the referrer.
2. **Bot activity:** which pages AI bots fetch. Pages fetched often by answer-time bots are likely being cited.
3. **Self-reported:** "How did you hear about us?" Often the clearest proof.

Plus:
- AI visibility and share of voice, rerun on the same question set.
- Brand Truth accuracy, rerun.
- Rankings, organic traffic, branded search trend (Search Console), conversions.
- Bing Webmaster Tools AI Performance report: how often Copilot and Bing AI cite the site's pages.

Report ranges and trends, not single numbers. Show what changed, what you did, and what you will do next.

### Step 6. Maintain

| Every | Do |
|---|---|
| Week | Check robots.txt and bot access; scan the site audit for new errors; watch for AI-cited URLs that return 404 (AI sometimes invents URLs; Ahrefs reports AI tools send visitors to 404 pages 2.87 times as often as Google). Redirect the ones that get traffic |
| Month | Rerun the visibility check; refresh 2 or 3 key pages with real updates; check mentions (new, lost, wrong); follow up outreach; report |
| Quarter | Full audit; competitor audit; Brand Truth rerun with 3+ runs; update the plan |
| On any change | New product, leader, address, price or name: update the facts page, schema, profiles and the claims register the same week |

### Step 7. Improve

When the basics are done, grow:
- **Topic coverage:** build out the sub-questions of the top buyer questions (fan-out).
- **Original research:** a yearly survey or benchmark with the brand's name on it.
- **Video program:** one search-hit video a month.
- **Digital PR program:** steady, newsworthy stories.
- **Community presence:** helpful, disclosed answers where buyers ask.
- **Experiments:** pick a page, change one thing, compare before and after on the same questions. Keep a hypothesis log.
- **New platforms:** check where your client's buyers actually ask (for example Perplexity for researchers, Copilot for corporate users).
- **Buyer journey study (advanced).** Test whether the brand survives as a buyer moves from first research to purchase. Brandleap's On study used the stages Trigger, Explore, Compare, Buy, Own, and found the brand named in 15% of Explore answers but 1% of Buy answers. For B2B, use problem, solution search, shortlist, comparison, approval, and the roles in the buying team.
