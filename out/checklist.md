# AEO, GEO and SEO Practitioner Checklist

Every task from first look to long-term care. Use with the Field Guide (part numbers in brackets).

## 0. Scope the job

Agree on what you will do and how success is measured, before you touch anything. [Guide part 4, step 0]

### Inputs

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 0.1 | Write down the business model | Business potential decides which keywords and prompts matter | Kick-off call; their site; sales deck | What they sell, to whom, where, average deal size, main conversion |
| 0.2 | Build the fact sheet | You grade AI answers against it | Primary sources only (own site, filings, official releases); source URL and date per fact | 8 to 30 facts, each with a source; client confirms in writing |
| 0.3 | Write the one-line positioning and 3 proof points | AI repeats what the web repeats; one clear line wins | Ramonov's pattern: the one thing + proof + proof + proof | Client approves the line |
| 0.4 | List 3 to 5 business competitors and 3 search competitors | You benchmark against both | Ask the client; check who ranks and who AI names | Names and domains listed |
| 0.5 | Set markets and languages | AI answers change by country | Ask the client | Countries and languages written down |
| 0.6 | Collect customer voice | Real questions beat guessed ones | Sales calls, support tickets, reviews (theirs and competitors'), Reddit, forums | At least 20 real questions or complaints in the buyer's words |
| 0.7 | Get access | Most fixes and all real data need it | Search Console, GA4, Bing Webmaster Tools, CMS, DNS or Cloudflare, Google Business Profile, social profiles | Each item has an owner and a yes or no |
| 0.8 | Agree scope, price, timeline and what you will not do | Protects you and the client | Short proposal or statement of work | Signed or approved in writing |
| 0.9 | Map the brand's names (entities) | Each name can win or lose on its own | Main brand, sub-brands, products, named features, own metrics, key people; plus the topics each should own | List saved with topics per name |

## 1. Inspect (the audit)

Where does the brand stand today? Go in gate order: reached, read, trusted, chosen, credited. [Guide part 4, step 1]

### 1A. Business baseline

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1A.1 | Record 12 months of organic traffic | You need the before numbers | Search Console, GA4, or a suite estimate | Trend saved with dates of big changes |
| 1A.2 | List top pages and top queries, branded versus unbranded | Shows what already works and how much demand the brand has | Search Console performance report | Top 20 pages and queries saved |
| 1A.3 | Record conversions by channel | Business impact is the real goal | GA4 | Conversions per channel per month saved |

### 1B. Crawl and index (technical SEO)

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1B.1 | Homepage and key pages return 200 | A failing page cannot rank or be cited | Browser, Screaming Frog | No errors on key pages |
| 1B.2 | One preferred host | Duplicate versions split signals | Try http, https, www and non-www | All reach one version in one redirect |
| 1B.3 | robots.txt allows Googlebot and Bingbot to key pages | Blocked pages are not crawled | Read site.com/robots.txt; Search Console | Key pages allowed |
| 1B.4 | No noindex on pages that should rank | Common mistake after a redesign | Screaming Frog; view source; check X-Robots-Tag header | No noindex on key pages |
| 1B.5 | XML sitemap exists, listed in robots.txt, submitted | Helps engines find pages | Open the sitemap; Search Console and Bing | Loads, lists key pages, has lastmod, submitted |
| 1B.6 | Canonical tags are correct | Tells engines the preferred URL | Screaming Frog | Each page points to itself or the right page |
| 1B.7 | No broken internal links | Wastes crawl; frustrates users | Screaming Frog | Internal links return 200 |
| 1B.8 | No redirect chains | Each hop loses time and signal | Screaming Frog | No internal link passes 2 or more redirects |
| 1B.9 | No orphan pages | Pages without internal links are hard to find | Crawl plus sitemap comparison | Every sitemap page has an internal link |
| 1B.10 | Key pages within 3 clicks of the homepage | Deep pages get less attention | Crawl depth report | Key pages at depth 3 or less |
| 1B.11 | Indexing status checked | Shows what Google actually stored | Search Console, Pages report | No key page excluded without a reason |
| 1B.12 | Core Web Vitals on mobile | Slow pages rank, convert and get fetched worse | PageSpeed Insights | LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less |
| 1B.13 | Mobile friendly | Google indexes the mobile version | PageSpeed Insights; a real phone | Viewport set, text readable, no overlap |
| 1B.14 | HTTPS everywhere | Security and trust | Crawl for http links and mixed content | All pages on HTTPS |

### 1C. AI access (technical AEO)

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1C.1 | AI search and user bots allowed | They fetch pages at answer time | Read robots.txt for OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User | All allowed |
| 1C.2 | Training-bot policy is a choice | Blocking every AI bot also removes the site from live answers | Check GPTBot, ClaudeBot, Google-Extended, CCBot; ask the owner | Rules match what the owner wants |
| 1C.3 | No firewall block for AI bots | A 403 or challenge page blocks bots even when robots.txt allows them | curl with a bot user agent; Cloudflare settings; logs for proof | No 403 or challenge for AI bots |
| 1C.4 | Cloudflare AI settings checked | Cloudflare can block AI bots by default | Cloudflare dashboard | No block the owner did not choose |
| 1C.5 | Main text in raw HTML | ChatGPT's crawler does not run JavaScript | Turn JavaScript off; view source; search for a key sentence | Key text visible without JavaScript |
| 1C.6 | No facts hidden in images, PDFs, tabs or pop-ups | Hidden facts are often missed | Read the page as plain text | Key facts are in HTML text |
| 1C.7 | Agent readiness scan (optional) | Newer signals; nice to have | isitagentready.com | Score noted; no critical blocker |
| 1C.8 | llms.txt (optional) | Not used by major AI companies so far | Open site.com/llms.txt | Noted; never sold as a fix |

### 1D. On-page SEO

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1D.1 | One main topic per key page; no cannibalization | Two pages fighting for one keyword both lose | Suite: pages ranking for the same keyword | One page per main keyword |
| 1D.2 | Intent match (3 Cs) | Wrong page type will not rank | Search the keyword; compare type, format, angle | Matches most top results |
| 1D.3 | Title tags | A strong ranking and click signal | Screaming Frog | Unique, about 60 characters, topic included |
| 1D.4 | Meta descriptions | Affects clicks (Google rewrites many) | Screaming Frog | Unique and descriptive |
| 1D.5 | URL slugs | Readable URLs help people and bots | Crawl list | Short words with hyphens |
| 1D.6 | Heading order | Structure helps people and AI chunking | Screaming Frog; browser extension | One H1; H2 and H3 in order |
| 1D.7 | Content gap against the top 3 pages | Missing subtopics lose | Suite content gap or page intersection | Common subtopics covered or listed as tasks |
| 1D.8 | Internal links | Pass authority and context | Crawl; site search for related pages | Key pages link to and from related pages |
| 1D.9 | Images | Accessibility, image search, speed | Crawl for missing alt; check file size | Alt text, readable names, compressed |
| 1D.10 | Readability | Easy text keeps readers and is easy to quote | Hemingway App | About grade 6 to 8 |
| 1D.11 | Open Graph tags | Better social sharing | View source; sharing debuggers | og:title, og:description, og:image |
| 1D.12 | Schema markup valid | Helps machines read facts (hygiene, not a citation switch) | Rich Results Test; Schema Markup Validator | Valid types for each page type |

### 1E. Content for AI answers

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1E.1 | Question headings | Match how buyers ask | Review the 10 to 20 key pages | 30% or more of H2 and H3 are real questions |
| 1E.2 | Answer first (BLUF) | Humans and AI weigh the start most | Read the first sentences under each heading | First 1 to 2 sentences answer the heading |
| 1E.3 | Sections stand alone | AI lifts chunks, not pages | Cover-the-page test | No 'This' or 'As mentioned' openers |
| 1E.4 | Entities named | Names give AI something to connect | Search for 'our tool', 'it', 'we' | Brand, products, people named |
| 1E.5 | Specific facts, no vague claims | Specific facts get quoted; vague ones do not | Look for numbers, dates, conditions | Claims carry numbers or examples |
| 1E.6 | Sources cited | Trust and quotability | Check claims and stats for links | Every stat has a source |
| 1E.7 | Named authors with credentials | E-E-A-T | Check bylines and author pages | Real people on key pages |
| 1E.8 | Tables in HTML; rows stand alone | Tables are easy to quote | View source | Each row carries its own labels |
| 1E.9 | FAQ with real questions | Direct answers to buyer questions | Review key pages | FAQ on key pages |
| 1E.10 | Freshness | AI favours recently updated pages | Visible dates; change history | Key pages updated with real changes in 30 to 90 days |
| 1E.11 | Page formats present | AI looks for these when buyers compare | Site search | Best-of, vs, alternatives, pricing, FAQ, facts page exist or are listed |
| 1E.12 | Original ideas carry the brand name | Unnamed ideas get absorbed without credit | Read key pages | Own frameworks named with the brand |

### 1F. Entity and positioning

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1F.1 | Organization (or Person, CollegeOrUniversity, LocalBusiness) schema | Tells machines who the brand is | Rich Results Test | Name, URL, logo, sameAs present |
| 1F.2 | sameAs lists only own profiles | Wrong links confuse the entity | Open each sameAs URL | No partner, client or press links |
| 1F.3 | About page complete | The main source of identity facts | Read it | Founders, leaders, address, year, what they do |
| 1F.4 | One name form | Mixed names split the entity | Titles, schema, text | Same spelling everywhere |
| 1F.5 | No contradictions | AI picks one at random or mixes them | Compare year, phone, email, address across pages | All match |
| 1F.6 | Facts or FAQ page | Fills gaps before AI fills them with fiction | Check the site | Answers the fact-sheet questions with specific values |
| 1F.7 | People pages | Experts are entities too | Check the site | Founders and experts have bios and profile links |
| 1F.8 | Wikidata and Wikipedia status | Knowledge graphs feed AI | Search Wikidata; check the official site link | Status noted; never edit for the client |
| 1F.9 | Lookalike brands found | Name clashes steal answers | Search the name; read AI answers | Lookalikes listed with a plan |
| 1F.10 | Positioning on the site | Consistency builds the association | Homepage title and meta, About page, schema description | The one-liner or its key words appear |
| 1F.11 | Positioning on every profile | Ramonov: repeat it everywhere | LinkedIn headline and company page, X, Instagram, YouTube, directories, podcast bios | Same line everywhere |
| 1F.12 | Source-of-truth grid | Shows which source spreads wrong facts | 8 to 10 facts x 7 sources; mark wrong cells | Grid built; worst source named |

### 1G. Authority and links

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1G.1 | Referring domains and domain rating against the top 3 pages | Links still drive rankings and retrieval | Ahrefs or Semrush | Gap per target keyword known |
| 1G.2 | Link quality review | Relevant, authoritative, followed, in-body links count most | Backlink report | Strengths and risks noted |
| 1G.3 | Spam or risk check | Bad links can hurt | Look for spikes and unrelated sites | No unexplained spam pattern |
| 1G.4 | Unlinked mentions listed | Easy outreach wins | Suite mentions tool; web search | List saved |
| 1G.5 | Competitor linkable points | Shows why others earn links | Anchor text report of competing pages | Top reasons listed (stats, lists, tools) |

### 1H. Off-site presence and reputation

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1H.1 | Cited domains for the category | These are the sources AI trusts | From the prompt runs (1K) | Top 10 domains; brand present and correct or not |
| 1H.2 | Best-of lists and comparisons in the niche | AI leans on them | Search 'best', 'top', 'vs', 'alternatives' | Pages missing the brand listed |
| 1H.3 | Review sites | Trust and AI sources | G2, Capterra, Trustpilot, Google, industry sites | Profiles claimed, facts right, reviews answered |
| 1H.4 | Reddit and Quora threads | Often cited and part of training data | Search the niche; check which threads rank | Relevant threads listed |
| 1H.5 | YouTube presence | YouTube is heavily cited by Google AI | Search niche topics on YouTube and Google | Brand videos on search topics, or a gap noted |
| 1H.6 | News, podcasts, associations, directories | More independent voices | Web search; Listen Notes | Presence noted |

### 1I. Local presence (if relevant)

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1I.1 | Google Business Profile | Main local source | Search the business on Google Maps | Right name, address, phone, category, hours, photos; reviews answered |
| 1I.2 | Bing Places and Apple Business Connect | Feed Copilot, Bing and Apple Maps | Search each | Claimed and correct |
| 1I.3 | NAP consistency on directories | Mismatches confuse engines | BrightLocal or Whitespark; manual search | Same name, address, phone everywhere |
| 1I.4 | Location pages | Answer 'near me' and area questions | Site review | One useful page per location |

### 1J. Keyword and prompt research

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1J.1 | Seeds and modifiers listed | The start of every keyword list | 10 short seeds; commercial, informational and tool modifiers | List saved |
| 1J.2 | Keyword ideas pulled | Real searches with volume | Keyword tool, phrase match with modifiers | Idea list with volume |
| 1J.3 | Competitor top pages mined | Finds keywords without your seeds | Suite top pages report for search competitors | Extra ideas added |
| 1J.4 | Each target passes the tests | Only worthwhile, winnable keywords | Demand, traffic potential, business potential 0 to 3, intent (3 Cs), difficulty (4 questions) | Targets scored |
| 1J.5 | AI filter applied | Some keywords no longer give clicks | Search each; full AI answer = mention target, not click target | Click and mention targets split |
| 1J.6 | Tool and transactional keywords found | AI cannot replace a tool, so clicks stay | Modifiers: calculator, checker, template, price, buy | List saved |
| 1J.7 | Keyword map built | One main keyword per page avoids cannibalization | Sheet: page, main keyword, related keywords | Every key page mapped; new pages listed |

### 1K. AI visibility and Brand Truth baseline

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1K.1 | Build the prompt set | A fixed set makes results comparable | Branded, unbranded, comparison, problem, should-not-recommend; from customer voice | 40 to 100+ prompts, 40%+ unbranded |
| 1K.2 | Run prompts on the main platforms | Each platform differs | Tracker, API or logged-out browser in the right country | AI Overviews, AI Mode, ChatGPT, Gemini, Perplexity, Claude covered |
| 1K.3 | Log every run | Proof and repeatability | Sheet: prompt, platform, date, country, search on or off, answer, cited URLs | Every row complete |
| 1K.4 | Score visibility and share of voice | Shows the gap against competitors | Named and cited, named only, cited only, not visible | Scores per platform and per topic |
| 1K.5 | Brand Truth test | Wrong facts cost trust and sales | About 30 fact questions, 3+ runs, graded against the fact sheet | Accuracy per platform; wrong facts listed |
| 1K.6 | A person checks the grades | Machine grades need review | Spot-check 10%+ and every 'Invented' | Reviewed and noted |
| 1K.7 | Narrative and tone | Being named wrongly is a gap too | Compare AI wording with the positioning | Narrative gap noted |

### 1L. Measurement setup

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1L.1 | Search Console and Bing Webmaster Tools verified | Core data | Verify both | Data flowing |
| 1L.2 | GA4 AI traffic channel | See AI referrals | Channel group with an AI referrer regex | Channel shows in reports |
| 1L.3 | 'How did you hear about us?' with AI options | Captures invisible AI influence | Forms, sign-up, checkout | Live and recorded |
| 1L.4 | Conversions tracked | Business impact | GA4 key events | Main conversions counted |
| 1L.5 | Bing AI Performance report reviewed | Shows Copilot and Bing AI citations | Bing Webmaster Tools | Baseline saved |
| 1L.6 | AI bot visits (optional) | Shows what AI reads | Server logs or Cloudflare | Baseline saved |

### 1M. Compliance basics (checks, not legal advice)

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1M.1 | Privacy policy and terms linked | Trust and legal basics | Footer | Both present |
| 1M.2 | Cookie consent where required | Law in many markets | Visit as a new user | Banner before non-essential cookies where needed |
| 1M.3 | Accessibility basics | Users, law and better structure | Page language, alt text, form labels, heading order, contrast, keyboard (WCAG 2.2 AA target) | No basic failures |
| 1M.4 | Reviews and testimonials are real | FTC rule on fake reviews | Ask how reviews are gathered | Real; incentives disclosed |
| 1M.5 | Paid and affiliate links disclosed | Law and Google rules | Check rel attributes and visible notes | rel=sponsored and a visible disclosure |

### 1N. Competitors

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 1N.1 | Light audit of 2 to 3 competitors | Shows what to copy and where to beat them | Repeat 1D to 1K at small scale | 'They have X, we do not' list |

## 2. Diagnose

Turn findings into causes and a ranked list. [Guide part 4, step 2]

### Causes and priorities

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 2.1 | Group findings by gate | Fix the earliest broken gate first | Discovery, retrieval, selection, inclusion, representation | Each finding has a gate |
| 2.2 | Fill the six brand gaps | Shows the whole picture | Visibility, narrative, topic, format, web mentions, demand | Each gap has evidence and a severity |
| 2.3 | Find root causes | One bad source can cause many wrong answers | Group wrong answers by the source behind them | Root causes named |
| 2.4 | Score every fix | Do the most valuable work first | Impact x confidence / effort; Truth Risk Score for wrong facts | Ranked list |
| 2.5 | Label each fix Fix, Build or Influence | Different owners and timelines | Ahrefs' split | Every fix labelled |
| 2.6 | Place the site on a maturity level (optional) | Clients understand 'you are here, next is there' | Invisible, Crawlable, Structured, Answer-Ready, Agent-Native | Level and next level stated |
| 2.7 | Mark quick wins | Early proof builds trust | Pages that rank and need an update; big lists that miss the brand | Quick wins flagged in the list |

## 3. Suggest

Hand over a plan people can act on. [Guide part 4, step 3]

### Deliverables

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 3.1 | One-page summary | Decision makers read one page | Scores, 3 to 5 findings, 5 top fixes, limits | Fits on one page in plain words |
| 3.2 | Full audit with evidence | Proof for every claim | Screenshots, URLs, answers | Every finding has evidence |
| 3.3 | Fix list with owners and 'done when' | Clear tasks get done | What, why, who, time, access, done when | Every top fix complete |
| 3.4 | 30-day and 90-day plan | Sets the order and the rerun date | Own site, then knowledge graph and profiles, then off-site and measurement | Plan with dates and rerun questions |
| 3.5 | State the limits | Honest reports keep trust | What was not tested, runs made, answers vary | Limits section present |
| 3.6 | List what you need from the client | Unblocks the work | Access, approvals, facts to confirm | List sent |
| 3.7 | Start the four records | Make every later report provable | Visibility baseline per platform; prompt map; cited-URL log; hypothesis, test and change log | All four exist |

## 4. Implement

Build the fixes in order: unblock, identity, content, new pages, earn, local, measurement. [Guide part 4, step 4]

### 4A. Unblock (technical)

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 4A.1 | Allow AI search bots; fix firewall blocks | Opens the door to live answers | robots.txt; Cloudflare rules | Retest passes |
| 4A.2 | Fix noindex, canonicals, redirects, broken links | Clean crawl and index | CMS; server; redirect map | Recrawl clean |
| 4A.3 | Server-side render key text | Bots without JavaScript can read it | Developer task | Raw HTML shows key text |
| 4A.4 | Speed up slow templates | Better rankings and fetching | Caching, image compression, developer fixes | Core Web Vitals pass |
| 4A.5 | Submit sitemap; turn on IndexNow if supported | Faster discovery | Search Console, Bing, CMS plugin | Submitted and active |

### 4B. Identity (entity)

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 4B.1 | Organization or Person schema with correct sameAs | Clear entity | JSON-LD; validate | Valid and only own profiles |
| 4B.2 | About and facts pages complete | Official answers to fact questions | Write from the fact sheet | Published and linked |
| 4B.3 | Fix contradictions and name forms | One truth everywhere | Edit pages | Recheck passes |
| 4B.4 | Align profiles and the positioning line | Consistency across the web | LinkedIn, socials, directories, Google Business Profile | Same line everywhere |
| 4B.5 | Prepare Wikidata or Wikipedia requests | Knowledge graphs feed AI | Write the request with sources; follow each site's rules | Request ready; no direct client edits |
| 4B.6 | Start a claims register | Keeps facts current | Claim, wording, evidence URL, owner, check date, recheck trigger | Register live with an owner |

### 4C. Rewrite key pages

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 4C.1 | Rewrite sections with the 5-part pattern | Makes passages quotable | Question heading, answer first, detail, evidence, no broken references | Top 10 pages rewritten |
| 4C.2 | Add tables, FAQs and named authors | Easy to quote; E-E-A-T | Edit pages | Live on key pages |
| 4C.3 | Name original frameworks with the brand | Keeps credit | Edit pages; reuse in social and talks | Named and repeated |
| 4C.4 | Refresh with real updates | Freshness | New data, examples, dates | Changes logged |

### 4D. Build missing pages

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 4D.1 | Best-of, vs and alternatives pages | Match buyer comparison questions | Honest tables; state own weaknesses | Published for top competitors |
| 4D.2 | Pricing, FAQ, facts, glossary pages | Direct answers | Write from the fact sheet | Published |
| 4D.3 | Tools or calculators where they fit | AI cannot replace a tool, so clicks stay | Developer or no-code tool | Live and indexed |
| 4D.4 | Case studies with numbers | Proof that AI and buyers trust | Customer, baseline, change, result | At least 3 published |
| 4D.5 | Original data or research | The strongest link and citation asset | Survey, benchmark, internal data | One study published with the brand name |

### 4E. Earn mentions (off-site)

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 4E.1 | Prospect list by reason | Personal pitches at scale | Cited pages, lists missing the brand, unlinked mentions, outdated stats | Segments with 10+ vetted prospects each |
| 4E.2 | Vet prospects | Only worthwhile, relevant sites | Live, relevant, still has the issue, has traffic, right language | Vetted list |
| 4E.3 | Write one email per segment | Personal without starting from zero | Write to one person, then extract merge fields; subject, reason, why you, pitch, conversation starter; under 120 words | Templates approved |
| 4E.4 | Test on a small batch first | Proves the pitch before scaling | 10 to 20 prospects per segment | Reply and win rate measured |
| 4E.5 | Community answers | Reddit and forums are cited | Honest, disclosed, useful replies | Answers posted where they fit |
| 4E.6 | Video plan | YouTube is heavily cited | Search-hit topics; keyword title; description; timestamps; say the keyword | First videos live |
| 4E.7 | PR and expert sourcing | Independent voices | Real news only; journalist requests; podcasts | Pitches sent; results logged |

### 4F. Local

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 4F.1 | Clean up Google Business Profile, Bing Places, Apple | Main local sources | Edit listings | All correct |
| 4F.2 | Fix NAP on directories | Consistency | BrightLocal, Whitespark or manual | All match |
| 4F.3 | Review request routine | Reviews drive local trust | After each job or sale; never fake or buy | Routine running |

### 4G. Measurement

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 4G.1 | Finish every 1L item | Prove the work | See 1L | All live |
| 4G.2 | Keep a change log | Shows what caused what | Date, page, change, reason | Every change logged |

## 5. Measure and report

Did it work? Report ranges and trends. [Guide part 4, step 5]

### Monthly report

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 5.1 | Rerun the same prompt set | Comparable over time | Same prompts, platforms, country | New scores beside the baseline |
| 5.2 | Rerun Brand Truth (quarterly or after big fixes) | Accuracy over time | Same questions, 3+ runs | Accuracy change reported |
| 5.3 | SEO numbers | The base still matters | Rankings, organic traffic, branded search, conversions | Trend charts |
| 5.4 | AI referrals, bot visits, self-reported discovery | Three views of AI impact | GA4, logs or Cloudflare, forms | All three reported |
| 5.5 | What we did, what changed, what is next | Tells the story | Change log plus results | Report sent |

## 6. Maintain

Keep it healthy. [Guide part 4, step 6]

### Cadence

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 6.1 | Weekly: bots, site errors, AI-cited 404s | Catch breakage fast | robots.txt, site audit, logs; redirect invented URLs that get traffic | Checked weekly |
| 6.2 | Monthly: visibility rerun, 2 to 3 page refreshes, mentions, follow-ups, report | Steady progress | See step 5 | Done monthly |
| 6.3 | Quarterly: full audit, competitor audit, Brand Truth rerun | Catch bigger shifts | Repeat steps 1 to 3 | Done quarterly |
| 6.4 | On any change: update facts page, schema, profiles, claims register | Stop new wrong facts | Same week as the change | Updated within a week |

## 7. Improve

Grow beyond the fixes. [Guide part 4, step 7]

### Growth

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 7.1 | Expand topic coverage (fan-out) | Win more of the sub-questions | Map sub-questions of top prompts | New sections or pages each month |
| 7.2 | Yearly original research | Links, citations, brand association | Survey or benchmark with the brand name | Published |
| 7.3 | Video and community programs | Formats AI cites | Monthly plan | Running |
| 7.4 | Experiments with a hypothesis log | Learn what works for this brand | Change one thing; compare on the same prompts | Results logged |
| 7.5 | Review platform mix | Buyers move between tools | Ask customers; check referrals | Priorities updated |
| 7.6 | Buyer journey study (advanced) | Shows where the brand drops out before purchase | Prompts per stage (problem, search, shortlist, compare, approve) and buyer role | Drop-off stage found and fixed |

## 8. Your own practice

Build yourself as an expert. [Guide parts 7 and 8]

### Skills and business

| # | Task | Why | How | Done when |
|---|---|---|---|---|
| 8.1 | Finish the three Ahrefs courses | The base method | Ahrefs Academy | Done; AEO exam passed |
| 8.2 | One full case study with numbers | Proof wins clients | Own site or a willing client | Before and after published |
| 8.3 | Templates ready | Speed and quality | Audit, one-page summary, fix list, monthly report, outreach email | All saved |
| 8.4 | SOPs for repeat tasks | Systems beat heroics | Write as you work | SOP per phase |
| 8.5 | First automations | Bridge to marketing automation | Prompt runs, monthly report, 404 alerts in n8n | Three automations live |
| 8.6 | Packages and prices | Easy to buy | Snapshot, audit, sprint, retainer | Written down |
| 8.7 | Stay current | AI search changes monthly | Ahrefs blog, Google Search Central, vendor docs; recheck figures | Monthly review habit |
