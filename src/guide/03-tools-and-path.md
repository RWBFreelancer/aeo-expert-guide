---

## Part 5. Different kinds of clients

The steps stay the same. The focus changes.

| Client type | Focus | Watch out for |
|---|---|---|
| **B2B company or SaaS** | Comparisons, alternatives, pricing clarity, integrations, case studies with numbers, review sites (G2, Capterra), analyst and industry lists, LinkedIn | Long buying cycles: measure leads and self-reported discovery, not only traffic |
| **Industrial or distributor (many brands, territories)** | One clear entity per company and its relationship to the parent; location and territory pages; product and manufacturer pages; spec and "or equal" content engineers search for; tools such as calculators; trade show content; industry associations; Google Business Profile per location | Name confusion between sister companies; facts locked in PDFs and images |
| **University or school** | Program pages with facts in text (not graphics); faculty as Person entities with profiles; research and patents with good metadata; rankings and admissions sites; student forums and Reddit; accessibility | Many sub-brands; facts in PDFs; outdated program info on third-party sites |
| **Local business** | Google Business Profile, reviews, NAP consistency, local directories, location pages, Bing Places, Apple | Duplicate listings, old addresses, wrong categories |
| **Online store** | Product schema, product feeds (Google Merchant Center), reviews, "best X" lists, comparison pages, ChatGPT shopping | Thin product copy copied from the maker |
| **Person or personal brand** | Person schema, one positioning line on LinkedIn and every profile, podcasts, speaking, bylined articles, Wikidata (if notable) | Same-name people; old job titles on profiles |

The book has extra checklists for healthcare, legal, ecommerce, financial services, B2B and SaaS, local and publishing. Health, money and legal topics (called **YMYL**, "your money or your life") need extra care with expert authors and sources.

---

## Part 6. Tools: what experts use, and when

### 6.1 What job posts ask for

- **Google Analytics is the most-named tool in SEO job posts.** Semrush studied 3,900 Indeed SEO listings (Nov 2025): Google Analytics appeared in 33.5% of senior listings and 47.7% of other roles; Semrush in 6.1% and 9.6%. Semrush ran the study, so read it with that in mind.
- **Semrush and Ahrefs are the standard paid suites.** A separate analysis of 6,000+ SEO postings calls them "the undisputed kings of the SEO toolkit".
- **Screaming Frog and Search Console are table stakes.** US job guides list a keyword or link tool plus a technical crawler as the baseline.
- **AEO and GEO posts on Upwork (Oct 2026)** ask for Google Search Console, GA4, Screaming Frog, Ahrefs, Semrush and Bing Webmaster Tools; name AI trackers like Profound, Peec or Otterly "or similar"; and very often ask for **manual prompt testing**: a baseline of 20 to 30 buyer prompts across ChatGPT, Perplexity, Gemini and AI Overviews, with a repeatable log of prompts, platforms, dates, mentions and citations.

So the market wants: the free Google and Bing tools, one big suite, a crawler, a way to track AI answers, and a clean, repeatable method. The method matters more than the brand of tool.

### 6.2 Tools by job

Prices change often. They are entry prices seen in 2026 and are only a guide. Check the vendor's page before you buy.

**Free core (every client, always)**

| Tool | Use it for | When |
|---|---|---|
| Google Search Console | What Google indexes; queries, clicks, impressions; errors; sitemap submission. AI Overviews and AI Mode traffic is counted inside normal web search there | Day one of every job; weekly |
| Google Analytics 4 (GA4) | Traffic, sources, conversions; the AI traffic channel group | Day one; monthly reports |
| Google Tag Manager | Adding tracking without editing code | Setup |
| Bing Webmaster Tools | Bing index (which feeds Copilot and has fed ChatGPT search); IndexNow; the **AI Performance** report (public preview since Feb 2026) shows how often Copilot and Bing AI cite the site's pages | Day one; monthly |
| Google Business Profile, Bing Places, Apple Business Connect | Local listings | Local clients |
| PageSpeed Insights and Lighthouse | Speed and Core Web Vitals | Audit; after big changes |
| Rich Results Test and Schema Markup Validator | Check structured data | After any schema change |
| Google Trends | Seasonality and rising topics | Keyword research |
| Looker Studio | Free dashboards from GA4, Search Console, Sheets | Client reporting |
| isitagentready.com (Cloudflare) | Quick agent-readiness scan | Technical AEO audit |
| Hemingway App | Readability grade | Content reviews |
| Wikidata | Check entity facts | Entity audit |
| Ahrefs Webmaster Tools (free for sites you own) | Site audit and backlinks for verified sites | When the client verifies the site |

**All-in-one SEO suites (pick one; most agencies use Semrush or Ahrefs)**

| Tool | Strength | When |
|---|---|---|
| Semrush | Keywords, competitors, site audit, rank tracking, local add-on, AI Visibility Toolkit (sold alone at about $99 a month per domain on annual billing, per one review) | Keyword research, competitor research, audits |
| Ahrefs | Backlink data, Keywords Explorer, Content Explorer (prospecting), Site Explorer; Brand Radar for AI visibility | Link research, outreach prospecting, content gaps, AI mentions |
| Moz Pro, SE Ranking | Cheaper all-in-ones | Small budgets |
| Semdash | Budget suite (keywords, backlinks, some AI Overview data); Buzz Insider uses it | Small budgets |
| Similarweb | Market and traffic estimates | Competitive market sizing |

**Crawlers (technical audits)**

| Tool | When |
|---|---|
| Screaming Frog SEO Spider (free up to 500 URLs; paid licence above) | Every technical audit; custom searches across many pages (for example "does each page still mention X") |
| Sitebulb | Visual audits with explanations; good for client-friendly technical reports |
| Screaming Frog Log File Analyser | Reading server logs to see real bot visits, including AI bots |

**Rank tracking**: AccuRanker, SE Ranking, or the tracker inside Semrush or Ahrefs. Use for weekly keyword positions once targets are set.

**Content optimization**

| Tool | When |
|---|---|
| Surfer, Clearscope, Frase, MarketMuse | Briefs and content scoring against what ranks. Useful for topic coverage. Do not write to a "score"; write for the reader |
| Claude, ChatGPT | Drafting, outlines, rewriting to the answer-first pattern, schema drafts. A person always edits and fact-checks |

**AI visibility tracking (AEO-specific)**

| Tool | Notes (from 2026 reviews; check current terms) |
|---|---|
| Manual testing | Free. Logged-out browser, right country, fixed prompt list, a spreadsheet. Every Upwork AEO post expects you can do this |
| Otterly.AI | Cheapest entry (about $29 a month for 15 prompts, per one review) |
| Peec AI | Monitoring-first; about $95 a month for 50 prompts (sources differ) |
| Profound | Enterprise leader; custom pricing, often $399+ a month |
| Scrunch, AthenaHQ | Optimization platforms; AthenaHQ has a free tier |
| Semrush AI Visibility Toolkit, Ahrefs Brand Radar | Add-ons for teams already on those suites |
| ZeroRank | Tracks up to 17 AI tools with country per prompt; from $39 a month; has an API |
| DataForSEO | Pay-per-use API data (AI Overviews, AI Mode, ChatGPT and Gemini answers, LLM mentions, keywords, backlinks). For people who build their own tracker; $50 minimum top-up |

Expert view: compare tools on **prompt count, engines covered, country setting, and whether you get the full answer text and cited URLs**, not on the headline price.

**Local SEO**

| Tool | When |
|---|---|
| BrightLocal | All-in-one for agencies: listings, Google Business Profile audits, grid rank tracking, reviews, white-label reports |
| Whitespark | Citation finding and building; local rank tracking |
| Moz Local, Semrush Local | Automatic listing sync |

**Links, outreach and PR**

| Tool | When |
|---|---|
| Ahrefs or Semrush backlinks, Majestic | Link research and prospecting |
| Hunter.io, NeverBounce | Find and verify contact emails |
| BuzzStream, Pitchbox, Respona | Run outreach campaigns and follow-ups |
| Journalist request services (for example Qwoted, Featured, Source of Sources) | Expert quotes in media. Check which ones are active |
| Listen Notes | Find podcasts to pitch |

**Technical AEO and bots**: Cloudflare dashboard (AI crawler controls and bot analytics), server logs, `curl` (fetch a page as a bot from the command line), browser with JavaScript turned off.

**Reporting**: Looker Studio (free), AgencyAnalytics or Whatagraph (paid, white-label), Google Sheets.

**Automation (your bridge to marketing automation)**: n8n, Make, Zapier; the Search Console API, GA4 Data API, DataForSEO, Semrush API; Apify (scraping); Slack for alerts.

**Project management**: Notion, Trello or Asana, with SOPs (step-by-step instructions for repeat tasks) and a Kanban board (columns: brainstorm, prospecting, vetting, outreach, done).

### 6.3 Your starter kit

| Budget | Stack |
|---|---|
| $0 | Search Console, GA4, Bing Webmaster Tools, PageSpeed Insights, Rich Results Test, Screaming Frog free, Ahrefs Webmaster Tools (client sites), manual AI prompt testing in a sheet, Looker Studio, Hemingway |
| About $100 to $150 a month | Add one suite at entry level (Semrush or Ahrefs, or a budget suite) and one cheap AI tracker (Otterly or ZeroRank Starter) |
| Agency | Full suite, Screaming Frog licence, a local tool, an outreach tool, an AI tracker with more prompts, white-label reporting |

Rule: **one tool per job**. Many tools averaging different numbers is a common mess. Buzz Insider named this pain on 20 Oct.

---

## Part 7. Working as an independent expert

### 7.1 What to sell

| Package | What the client gets | Notes |
|---|---|---|
| Free or low-cost snapshot | A short AI visibility check on 20 to 100 prompts plus top technical blockers | Brandleap gives a free AI Visibility Index and a free technical report as lead offers |
| Full audit | Steps 1 to 3: audit, diagnosis, fix list, 30/90-day plan | Brandleap sells a custom Brand Truth audit at $299 |
| Implementation sprint | Step 4 for a set scope (for example technical + entity + 5 page rewrites) | Fixed price per scope |
| Retainer | Steps 5 to 7 monthly: tracking, refreshes, new pages, outreach, report | The steady income |
| Training | Teach a client's team the method | Good for agencies |

### 7.2 What to charge (directional only)

- Upwork's own guide puts beginners at about $10 to $25 an hour and lists a median of about $15 to $35 an hour for SEO experts on its cost page.
- Other 2026 rate guides put experienced freelancers at about $60 to $150 an hour, and senior experts with case studies at $200 or more.
- One analysis says AEO and GEO add about 15 to 25% to retainer prices since 2024, because the skill is scarce.

Treat these as rough. Your price rises with **proof**: case studies with before-and-after numbers.

### 7.3 When you grow into a team

Sam Oh's advice from the Advanced Link Building course: give each person one stage, so each gets very good at it.
- **Prospector:** finds opportunities and pitch angles. Needs SEO knowledge, research skill and creativity. Often doubles as project manager.
- **Vetter:** checks each prospect against a written standard. Needs attention to detail; no SEO background needed.
- **Outreach manager:** writes and sends emails and keeps relationships. Needs writing and people skills.

Support them with five things: clear roles, shared goals (for example new referring domains a month to money pages), SOPs, a project board, and a shared sheet for campaign data.

### 7.4 Win the work

- Answer the post's exact ask. Upwork AEO posts want a baseline of buyer prompts, a repeatable tracking method, technical and schema fixes, and monthly reporting.
- Show a one-page sample: one real brand, 20 prompts, 4 platforms, findings and 5 fixes.
- Ramonov's sales pattern: post useful AEO content on LinkedIn; offer a playbook; book an audit call; show the prospect their gaps against competitors. Lead with results, not jargon.

---

## Part 8. Your path: beginner to expert, then marketing automation

### 8.1 Twelve-week plan (about 5 to 8 hours a week)

| Weeks | Learn | Do |
|---|---|---|
| 1 to 2 | Ahrefs SEO Course for Beginners (keywords, on-page, links, technical) | Set up Search Console, GA4 and Bing Webmaster Tools on a site you control |
| 3 to 4 | Ahrefs AEO Course; parts 1 to 3 of this guide | Run 20 prompts about one brand on 4 platforms; log names and citations |
| 5 to 6 | Technical audits with Screaming Frog; robots.txt and bots; schema | Full technical and AI-access audit of one site |
| 7 to 8 | Content for answers; entity work; source-of-truth grid | Rewrite 3 sections answer-first; build a facts page and Organization schema |
| 9 to 10 | Ahrefs Advanced Link Building; digital PR | Build a prospect list of 30 pages, segment by reason, write 2 outreach templates |
| 11 to 12 | Measurement and reporting | A Looker Studio dashboard and a one-page monthly report; rerun the 20 prompts and compare |

Capstone: one full case study (before and after, with numbers) you can show clients.

### 8.2 Certificates

Certificates help a profile, but a real result helps more. Ahrefs' own blog argues that ranking a real site teaches more than any certificate.
- Free: Ahrefs Academy courses (the AEO course has a 50-question exam), Semrush Academy, Google Analytics certification (Google Skillshop), HubSpot SEO, Google Search Central documentation.
- Paid: Moz SEO Essentials (about $595).

### 8.3 Bridge to marketing automation

AEO and SEO have many repeat tasks. These are your first automations, and your portfolio for automation work:

| Task | Automation |
|---|---|
| Weekly AI prompt runs | n8n schedule → DataForSEO or a tracker API → sheet or database → scores |
| Monthly report | Search Console API + GA4 Data API + tracker data → Looker Studio or a PDF → email or Slack |
| Bot and 404 watch | Logs or Cloudflare → alert in Slack when an AI-cited URL returns 404 |
| Lost-mention watch | Mention tracker → alert → draft a correction request |
| Content brief | Top results + fan-out questions + facts page → draft brief for a writer |
| Outreach pipeline | Prospect sheet → email finder → verifier → CRM stages → follow-up reminders |
| Lead capture from calculators | Form before the result → CRM → sales alert |

Rule from the link-building course that also fits automation: build a **system** (structure, goals, SOPs, a project board, shared data), not one-off heroics.

---

## Part 9. Templates

Copy these. Change the words in [brackets].

### 9.1 One-page summary (for decision makers)

> **[Brand]: search and AI answer check, [date]**
>
> **Where you stand.** Readiness [score]/100 ([level]). Named in [x]% of [n] buyer questions across [platforms], [n] runs each. Competitors: [A] [x]%, [B] [x]%. AI tools state your key facts correctly [x]% of the time.
>
> **What we found.** (3 to 5 lines, plain words, each with its business effect.)
> 1. [Finding]. This means [effect on buyers or sales].
>
> **What to do first.** (5 fixes, each with owner and time.)
> 1. [Fix]: [owner], [time].
>
> **What this test did not cover.** [Platforms, countries, questions not tested.] AI answers change from run to run; we ran each question [n] times.
>
> **What we need from you.** [Access, facts to confirm, approvals.]

### 9.2 Fix card (one per fix)

| Field | Content |
|---|---|
| Fix | [Short name] |
| Why | [What is broken and what it costs] |
| Evidence | [URL, screenshot, answer] |
| Who | [Role or person] |
| Time | [Hours or days] |
| Access needed | [CMS, DNS, Search Console ...] |
| Steps | 1. ... 2. ... 3. ... |
| Done when | [A test anyone can check] |
| Rerun | [Which questions or checks to repeat afterwards] |

### 9.3 Prompt log (one row per answer)

`date | platform | model shown | country | logged in? | search on? | run # | prompt id | prompt | topic | brand named? | position | brand cited? | cited URLs | competitors named | answer text | grade (for fact questions) | notes`

### 9.4 Claims register (one row per approved fact)

`claim id | approved wording | evidence URL | owner | last checked | recheck trigger (for example new CEO, price change)`

### 9.5 Source-of-truth grid

| Fact | Own site | Wikipedia | Wikidata | LinkedIn | Business listings | Top third-party page | AI answers |
|---|---|---|---|---|---|---|---|
| Founded | [value] | [value] | ... | | | | |
| CEO | | | | | | | |
| Headquarters | | | | | | | |

Mark each wrong cell. The column with the most wrong cells is usually the first fix.

### 9.6 Change log

`date | page or asset | what changed | why | expected effect | checked on | result`

### 9.7 Outreach email (fill after you write one real email to one real person)

> **Subject:** [honest reason, for example "Your list of [category] tools"]
>
> Hi [first name],
>
> I read your [page title] and saw you list [competitors] for [use]. [Brand] is missing, and it is often the pick for [specific buyer] because [one concrete reason with a number].
>
> [One honest line: where it is not the best fit.]
>
> If useful, here is [a short summary, data, or free access] so you can check it yourself: [link].
>
> Would it be worth a look for your readers?
>
> [Name]

Keep it under 120 words. One email per reason segment. Test it on 10 to 20 people before the full list.

### 9.8 GA4 AI traffic channel

GA4 → Admin → Data display → Channel groups → copy the default group → add channel "AI traffic", condition **Session source matches regex**:

`.*(chatgpt\.com|chat\.openai\.com|perplexity\.ai|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai|deepseek\.com|grok\.com|meta\.ai).*`

Move it above "Referral" so it is matched first. Add new AI sites to the regex as they appear.

### 9.9 Monthly report outline

1. Headline: what changed this month, in one sentence.
2. Scores against last month and the baseline (readiness, AI visibility, accuracy, search).
3. Leads and conversions, with self-reported AI discovery.
4. What we did (from the change log).
5. What we learned (wins, misses, surprises).
6. Next month's plan.
7. Limits of the data.

---

## Part 10. Glossary

| Term | Meaning |
|---|---|
| AEO | Answer engine optimization: being named, correct and cited in AI answers |
| Anchor text | The clickable words of a link |
| Answer engine | An AI tool that writes answers (ChatGPT, Gemini, Perplexity, AI Overviews) |
| Backlink | A link from another site to yours |
| BLUF | Bottom line up front: the answer first |
| Canonical tag | Code that names the preferred URL among similar pages |
| Citation (AEO) | The answer links to a source page |
| Citation (local SEO) | A listing of the business's name, address and phone on another site |
| Claims register | A list of the brand's approved facts, each with a source, owner and check date |
| Core Web Vitals | Google's speed and stability metrics: LCP, INP, CLS |
| Crawler, bot | A program that visits and reads web pages |
| DR, domain rating | Ahrefs' score for the strength of a site's backlink profile (other tools have their own versions) |
| E-E-A-T | Experience, expertise, authoritativeness, trustworthiness |
| Entity | A thing with stable facts: a company, person, product, place |
| Fan-out | The hidden sub-searches an AI runs for one question |
| GEO | Generative engine optimization, a near-synonym of AEO |
| Index | A search engine's stored copy of the pages it knows |
| IndexNow | A protocol that tells search engines (Bing and others) about page changes at once |
| JSON-LD | The usual format for schema markup |
| Knowledge Graph | Google's database of entities and their links |
| llms.txt | A proposed file that summarizes a site for AI tools; not used by major AI companies so far |
| NAP | Name, address, phone |
| noindex | A tag that asks search engines not to store a page |
| Orphan page | A page with no internal links pointing to it |
| RAG | Retrieval-augmented generation: the AI searches while it answers |
| robots.txt | The file that tells bots where they may go |
| Schema markup | Code that labels page facts for machines |
| SERP | Search engine results page |
| Share of voice | How often a brand is named compared with competitors |
| Sitemap | A file that lists the pages you want found |
| Topical authority | Being known as a strong source on one subject |
| User agent | The name a bot or browser sends to identify itself |
| YMYL | "Your money or your life" topics (health, money, legal) that need extra trust |

---

## Part 11. Sources

- Ahrefs, SEO Course for Beginners (Sam Oh): https://ahrefs.com/academy/seo-training-course
- Ahrefs, Answer Engine Optimization course (Sam Oh): https://ahrefs.com/academy/aeo-course
- Ahrefs, Advanced Link Building course (Sam Oh): https://ahrefs.com/academy/link-building-course
- Ahrefs, Brand Gap Analysis report template and Link + Mentions Prospecting sheet (AEO course, lesson 2.1)
- Sabrina Ramonov, AI SEO for Beginners (video transcript)
- Rodrigo Stockebrand, *Answer Engine Optimization*, O'Reilly (July 2026); Brandleap AI Brand Truth sample (Mauna Loa, Oct 2026), AI Visibility Index (Hyperlite, Oct 2026), technical readiness example, 2026 AEO Playbook
- Semrush, "What 3,900 SEO Job Listings Reveal in 2026": https://www.semrush.com/blog/seo-job-market-study/
- The SEO Cube, "I Analyzed 6,000+ SEO Job Postings": https://theseocube.com/p/ai-impact-on-seo-jobs
- Upwork AEO and GEO job posts, Oct 2026 (for example https://www.upwork.com/freelance-jobs/apply/SEO-AIEO-GEO-Specialist-for-B2B-Cybersecurity-Company_~022114440878420894827/ and https://www.upwork.com/freelance-jobs/apply/SEO-and-Search-AEO-GEO-Specialist-White-Label-Partner-Driven-Agency_~022112563227619849015/)
- Upwork hourly rates guide: https://www.upwork.com/resources/upwork-hourly-rates ; Upwork SEO cost page: https://www.upwork.com/hire/seo-experts/cost/
- AI visibility tool pricing roundups (2026): https://www.elitecontentmarketer.com/best-ai-visibility-tools/ , https://ainora.lt/blog/best-ai-visibility-tracking-tools-2026
- Bing Webmaster Tools AI Performance report: https://searchengineland.com/bing-webmaster-tools-testing-new-ai-performance-report-468039
- Google, "AI features and your website": https://developers.google.com/search/docs/appearance/ai-features ; Google Search Central blog, May 2026: https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing
- Local SEO tools: https://searchatlas.com/blog/brightlocal-vs-whitespark/
- SEO certifications: https://ahrefs.com/blog/seo-certification , https://markampus.com/blog/semrush-certifications-worth-getting-2026/
