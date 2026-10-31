# The AEO, GEO and SEO Field Guide

For Rey. Version 1, 31 Oct 2026.

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
