# The AEO, GEO and SEO Field Guide

For anyone who wants to learn and do SEO, AEO and GEO work. Version 1, 31 Oct 2026.

This is the one guide to use when you do SEO, AEO and GEO work for a client. It goes from first look to long-term care: inspect the brand, suggest fixes, build them, keep them healthy, and grow. It is written for a beginner, but it shows how an expert thinks at each step.

**How to use it**

- Read parts 1 to 3 once. They give you the mental model. Without it, the checklist is just a list.
- Use part 4 (the job, step by step) and the separate **Practitioner Checklist** on every client.
- Use part 6 (tools) to pick the right tool for each job.
- Use part 8 (your path) to grow from beginner to expert, and toward marketing automation.
- Use part 9 (templates) to write reports, logs and emails fast.
- The checklist lives beside this guide as `checklist.html` (tick boxes save in your browser) and `checklist.pdf`.

**About numbers in this guide.** Most figures come from one company's own study (often Ahrefs). They are written as "Ahrefs reports ...". They are not laws of nature. AI search changes month to month. Check a figure again before you put it in a client report.

---

## Part 1. The big picture

### 1.1 Three names, one practice

| Term | Plain meaning | Goal |
|---|---|---|
| **SEO** (search engine optimization) | Make pages rank in search results (Google, Bing) | Clicks from the list of blue links |
| **AEO** (answer engine optimization) | Make AI answer tools name the brand, describe it correctly, and cite its pages | Be in the answer itself |
| **GEO** (generative engine optimization) | Almost the same as AEO. The word stresses "generative" AI models | Same as AEO |

You will also see **LLMO** (large language model optimization) and **AI SEO**. They all point at the same work.

The AI answer tools are called **answer engines**: ChatGPT, Google AI Overviews and AI Mode, Gemini, Perplexity, Claude, Microsoft Copilot, Grok, DeepSeek and others.

**The key idea: AEO builds on SEO. It does not replace it.** Many answer engines search the web while they write. They pull from pages that search engines can find and trust. A site that cannot rank, or cannot be crawled, is rarely cited. So you learn SEO first, then add AEO on top.

### 1.2 Why it matters to a client

- **Fewer clicks from search.** Ahrefs reports that an AI Overview at the top of Google cut the click-through rate of the number one result by 58% (Dec 2025 data). The answer is on the page, so fewer people click.
- **Small but valuable AI traffic.** Ahrefs reports that in June 2025 AI search sent only 0.5% of its visits but 12.1% of its sign-ups. That is about 23 times the conversion rate of normal search. People who arrive from an AI answer have already been told why the brand fits.
- **Most AI impact is invisible.** Someone reads a brand name in ChatGPT, then types it into Google later. Analytics shows "direct" or "branded search", not "AI". So you must measure in new ways (part 4, step 5).
- **Google still sends far more traffic.** Ahrefs reports that Google sends about 210 times more traffic than the top AI tools combined. Do both. Do not drop SEO for AEO.

How an expert says it to a client: "Search is splitting into two games. In the old game you win a click. In the new game you win a mention. The same strong foundation wins both."

### 1.3 What "winning" looks like now

| Old (SEO) | New (AEO) |
|---|---|
| Rank position 1 to 10 | Named in the answer, described correctly, and cited |
| One page, one keyword | Many questions around a topic |
| Clicks | Mentions, citations, accuracy, then clicks and leads |
| Your site does most of the work | Other sites (reviews, lists, forums, news, Wikipedia, YouTube) do much of the work |
| Stable rankings | Answers that change from run to run |

---

## Part 2. How search engines work (the SEO base)

### 2.1 Crawl, index, rank

1. **Crawl.** Programs called **crawlers** (also bots or spiders) start from known pages and follow links to find more pages.
2. **Index.** The search engine stores a copy of each page it finds and understands. The **index** is that big library.
3. **Rank.** When someone searches, the engine picks the most useful pages from the index and orders them.

If a page is not crawled, it cannot be indexed. If it is not indexed, it cannot rank. If it cannot rank, most AI tools that use search will not find it either. That is why **technical SEO comes first**.

### 2.2 What makes a page rank

No one outside Google knows the exact formula. Google has given clues, and these factors are accepted by most experts:

- **Search intent match.** The page gives the type of answer people want. Look at the top results to learn this. Ahrefs teaches the **3 Cs**:
  - **Content type:** blog post, product page, category page, video, tool.
  - **Content format:** how-to, list, comparison, review, opinion.
  - **Content angle:** the hook, for example "for beginners", "2026", "cheap".
- **Backlinks.** A **backlink** is a link from another site to yours. Google treats it like a vote. Links from relevant, trusted pages count more. Google's original **PageRank** formula judges a page by the number and quality of pages that link to it.
- **Content depth.** The page answers the question fully. Depth is not length. A page about turning off a phone can be short and still win.
- **E-E-A-T.** Experience, expertise, authoritativeness and trustworthiness. This is Google's idea of quality: real authors, real experience, real evidence, a trusted site.
- **Page experience.** Fast, mobile friendly, secure (HTTPS), no annoying pop-ups.
- **Topical authority.** A site that covers one subject well often beats a bigger general site. Ahrefs shows a plumbing site outranking much stronger sites for "how to unclog a toilet".

### 2.3 One page ranks for many keywords

Ahrefs reports that the top page for a query ranks, on average, for about 1,000 other keywords in the top 10. So you do not stuff one exact phrase. You cover a topic well, and the page wins the many ways people ask about it.

### 2.4 Things that do not work (old SEO myths)

- Repeating the exact keyword many times (keyword stuffing).
- A fixed keyword count or a minimum word count.
- Buying links. It breaks Google's rules and can get a site penalized. Ahrefs asked 250 sites and found an average price of about $353 per link. They did not buy any.
- Hundreds of thin pages made only to catch keywords.

---

## Part 3. How AI answers work (the AEO layer)

### 3.1 Two sources of knowledge

An AI model knows a brand in two ways:

1. **Training memory.** What the model learned from a huge copy of the web, books, Reddit, YouTube transcripts and more. It is fixed until the next training round, often months later. If a brand launched last month, the memory does not know it.
2. **Live retrieval.** The tool searches the web while it answers, reads some pages, and writes from them. This is called **RAG** (retrieval-augmented generation). It changes as soon as the web changes.

Why it matters: you can change live retrieval in weeks (fix pages, earn mentions on cited pages). You change training memory only slowly, by being mentioned widely and consistently for a long time.

A real example from Brandleap's Mauna Loa audit: models were right 24% of the time from memory alone, and 72% of the time with search on. Fixing what search finds moves answers now. Memory catches up later.

### 3.2 The seven RAG stages (where a brand can drop out)

From Rodrigo Stockebrand's book *Answer Engine Optimization* (O'Reilly, 2026):

1. **User query.** The question as typed.
2. **Query understanding.** The tool rewrites the question and splits it into several smaller searches. This is **query fan-out**.
3. **Retrieval.** It pulls candidate pages or passages from an index.
4. **Ranking and reranking.** It orders candidates by relevance and trust.
5. **Context assembly.** It packs the best passages into the model's working memory.
6. **Generation.** The model writes the answer.
7. **Post-processing.** Citations, safety checks, formatting.

A brand can fail at any stage. A page that is never fetched fails at stage 3. A page that is fetched but vague fails at stage 4 or 6.

The same book gives a simpler content view, the **Five Gates**:

| Gate | Question | Typical fix |
|---|---|---|
| Discovery | Does the engine know the page exists? | Crawl access, sitemap, internal links, IndexNow |
| Retrieval | Does the page come back for the right question? | Topic coverage, the words buyers use, SEO |
| Selection | Is it chosen over competing passages? | Clear answer first, specifics, evidence, authority |
| Inclusion | Does the passage make it into the final answer? | Self-contained sections, quotable facts |
| Representation | Are the facts right, and is the brand credited? | Facts page, consistency across the web, entity markup |

Expert habit: find the gate where the brand drops out, and fix that gate first.

### 3.3 Query fan-out

When someone asks "plan a 5-day trip to Japan in November", the AI runs many hidden searches: best area to stay in Tokyo, weather in Kyoto in November, is the rail pass worth it, and so on. Ahrefs quotes research by Seer Interactive that an average prompt triggers about 9 to 11 fan-out searches, some up to 28.

What it means for you:
- A page that covers only the basics loses to a page that covers the whole topic.
- Ahrefs reports that over 95% of fan-out queries have zero search volume. Do not chase them as keywords. Use them to see **which subtopics** the AI thinks matter.

### 3.4 Answers are probabilities, not rankings

Ask the same question five times and you can get five different answers. The model adds some randomness, and the sources it finds change. Ahrefs reports that over 45% of AI Overview citations change when the overview refreshes, which happens about every two days on average.

So an expert never says "we rank number 2 in ChatGPT". An expert says "we were named in 34% of 300 answers across 3 runs". This is called **AI visibility** or **share of voice**, not ranking.

### 3.5 What raises the chance of being named

From Ahrefs' studies and the other sources:

- **Consensus.** When many sources say the same thing about a brand, AI repeats it. Ahrefs reports that branded web mentions had the strongest link to AI Overview visibility in a study of 75,000 brands (correlation 0.664), stronger than backlinks or domain rating. Mentions on pages with many links did even better (0.7).
- **Third-party pages.** Lists ("best X"), comparisons, reviews, Reddit threads, YouTube videos, Wikipedia, news. Ramonov says most brand mentions in AI come from sites the brand does not own.
- **Freshness.** Ahrefs reports AI-cited content is on average 25.7% fresher than what ranks in normal search. In one Ahrefs study of ChatGPT's top-cited pages that showed a date, 76.4% had been updated in the last 30 days (Sept 2025, 564 of 1,000 pages had a visible date). Refresh with real changes, not just a new date.
- **Authority and SEO.** Pages that rank well in Google have a head start, especially for AI Overviews and Perplexity. But the link is weakening. Ahrefs once found 76% of AI Overview citations came from top-10 pages; a newer study put it near 38%. And 14% of cited pages did not rank in the top 100 at all.
- **Format.** For "best ..." questions in ChatGPT, Ahrefs found 43.8% of cited pages were list posts (Dec 2025, 26,283 URLs). Comparisons, original data and clear how-tos also do well.
- **Specific facts.** Numbers, names, dates. Vague claims give the AI nothing to quote.

What does **not** seem to matter:
- **Length.** Ahrefs reports almost no link between word count and AI Overview citations (correlation 0.04). Over half of cited pages had under 1,000 words.
- **llms.txt.** A proposed file that summarizes a site for AI. No major AI company says it uses it. Fine to add, never sell it as a fix.
- **Schema as a magic switch.** Structured data helps machines read facts. The evidence that it raises AI citations is mixed. Treat it as hygiene.

### 3.6 Each platform is its own world

Ahrefs looked at the top 50 most-cited domains in AI Overviews, ChatGPT and Perplexity: only 7 appeared on all three (14% overlap).

| Platform | Where it gets facts | Tends to favour (Ahrefs data) | Check first |
|---|---|---|---|
| Google AI Overviews | Google's index + model | Established, authoritative sites; YouTube (about 5.6% of citations); Reddit | Normal SEO health, Search Console |
| Google AI Mode | Google's index + model | YouTube most cited; cites Quora far more than AI Overviews. Only 13.7% citation overlap with AI Overviews, though answers are 86% similar | Same as above, plus video and forums |
| ChatGPT | Memory + web search (Bing data has fed it) | Big publishers; median domain rating of top-cited pages is 90; only 8 to 10% overlap with Google's top 10 | OAI-SearchBot allowed; Bing Webmaster Tools; mentions on major publications |
| Perplexity | Live search on almost every question | Closest to Google: 28.6% of citations rank in Google's top 10 | PerplexityBot allowed; fresh, dated, answer-first pages |
| Claude | Memory + web search when on | Not studied as much | Claude-SearchBot and Claude-User allowed |
| Microsoft Copilot and Bing | Bing index + model | | Bing Webmaster Tools (it has an AI Performance report since Feb 2026), IndexNow, Bing Places |
| Gemini | Google's index + model | | Same as Google |

Expert rule: **fix the shared base first** (access, clean facts, answer-first content, trusted third-party sources). Then tune for one platform where the data shows a gap.

### 3.7 Three kinds of AI visibility

| Type | What happens | Value |
|---|---|---|
| Cited and linked | The answer links to the brand's page | Direct traffic; easy to measure |
| Mentioned, not linked | The brand name appears, no link | Word of mouth at scale; people search the name later; trains future models |
| Not visible | Not in the answer | The gap to fix |

Ahrefs reports that only about 28% of AI mentions carry a link. It varies by platform: Perplexity about 52%, AI Mode about 37%, ChatGPT about 27%, AI Overviews about 11%. So counting only clicks misses most of the value.

### 3.8 AI can repeat false facts

Ahrefs created a fake brand, planted three conflicting stories about it (a blog, Reddit, Medium), then asked eight AI tools. Gemini and Perplexity repeated the false facts in 37 to 39% of answers. ChatGPT stayed under 7% and cited the brand's official FAQ in 84% of answers.

The lesson: **"When AI has to choose between vague truth and specific fiction, it tends to choose the specific fiction."** Fill every fact gap with a specific, official page.

---

## Part 3b. How an expert thinks

These are the habits that separate an expert from someone who runs a tool and pastes the report.

1. **Business first.** A keyword or prompt matters only if winning it helps the business. Ahrefs scores **business potential** 0 to 3: 3 if the brand's product is the natural answer, 0 if it has nothing to do with the business.
2. **Intent decides the page.** Before you write, look at what already wins (the 3 Cs). Do not try to rank a blog post where Google shows only shops.
3. **Fix blockers before polish.** Order: can it be reached, then read, then trusted, then chosen. A beautiful page behind a robots block earns nothing.
4. **Measure before you change.** Take a dated **baseline** (scores, answers, rankings, traffic). Without it, you cannot prove your work helped.
5. **One answer is an anecdote.** Repeat AI tests (3 or more runs), keep the question set fixed, and report ranges. The book calls this the **confidence ladder**.
6. **The web decides who the brand is.** Your client's site is one voice. Lists, reviews, forums, news and knowledge graphs are many voices. Work on both.
7. **Specific beats vague.** Named people, products, places, numbers and dates. "Cut editing time by 40% in our 2026 test of 120 videos" beats "a great tool".
8. **Think in passages.** AI reads chunks, not whole pages. Every section should make sense alone, with the answer first.
9. **Know what is proven.** Sources disagree on llms.txt, schema, word count, LinkedIn headlines. Say what is proven, what is likely, and what is a guess.
10. **Prioritize by impact, confidence and effort.** Quick, safe, high-impact fixes first. Big bets get a test first (a small batch, then the full roll-out).
11. **Separate the scores.** Readiness, visibility, accuracy and SEO strength measure different things. A single blended number hides the cause.
12. **Honest limits.** Every report says what was not tested, how many runs were made, and that AI answers vary.
13. **Play the long game, ethically.** No bought links, no fake reviews, no spam, no editing Wikipedia for a client. These shortcuts burn the brand and you.
14. **Write for humans.** AI learned from what humans find useful. Content that serves a reader well is the content AI wants to cite.
15. **Systems beat heroics.** Experts use repeatable steps (SOPs), templates, checklists and automation. That is also your bridge to marketing automation.

### Questions an expert asks on every client

1. What does a win look like for this business, in money or leads?
2. Who is the buyer, and what do they ask before they buy?
3. Can engines reach and read the site at all?
4. What does the web say about this brand today, and who is saying it?
5. Where does the brand drop out: not found, not chosen, or described wrongly?
6. Which single change would move the most answers or rankings?
7. How will we know, in 90 days, that it worked?

### Common beginner mistakes

| Mistake | Do this instead |
|---|---|
| Running one AI prompt and reporting it as the result | Fixed prompt set, 3+ runs, report ranges |
| Starting with content before checking crawl and bot access | Unblock first |
| Chasing search volume | Check traffic potential, business potential and intent |
| Writing long pages to "be thorough" | Answer first, then depth; length set by the topic |
| Selling llms.txt or schema as the fix for AI visibility | Present them as hygiene; the big levers are access, content, consistency and mentions |
| Stating a tool's or study's number as fact | "Ahrefs reports ..." with the date |
| Fixing each wrong AI answer one by one | Find the source behind many wrong answers and fix that |
| Spamming outreach or forums | Personal, segmented outreach; honest, disclosed answers |
| No baseline, no change log | Record before you change; log every change |
| Reports full of jargon | Plain words and business impact for decision makers |


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
| Semdash | Budget suite (keywords, backlinks, some AI Overview data) | Small budgets |
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

Rule: **one tool per job**. Many tools that give different numbers for the same thing make a common mess.

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
