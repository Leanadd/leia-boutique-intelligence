# LÉIA AI Suite — Boutique Intelligence Platform

AI-powered internal tools for a luxury jewelry maison — RAG chatbot &amp; analytics dashboard

> **Luxury retail meets artificial intelligence** — A product case study simulating AI-powered internal tools for a high jewelry maison.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-Llama%203.3%2070B-blueviolet)
![RAG](https://img.shields.io/badge/Architecture-RAG-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

---

## Context

LÉIA is a fictional Parisian high jewelry and Swiss watchmaking house with worldwide boutiques. 
This project simulates the AI tools a Product Manager might design for a luxury retail company to enhance customer experience and empower both field and office teams to make better, faster decisions. 

Two tools were designed and built: 
**multi-persona RAG chatbot** gives every team instant access to brand knowledge, and helps boutique advisors turn client insights into personalized, on-brand interactions in seconds
**analytics dashboard** that turns sales and client data into actionable insights.


## Product Roadmap  
### 1. Discovery — Problem Identification & User Needs

**"What are the real issues that luxury retail teams face on a daily basis, 
and what can be improved?"**

An analysis of the operational reality of a multi-boutique luxury maison revealed 
three main friction points:

**For field teams (boutique advisors, after-sales):**
- No instant access to product knowledge, brand storytelling, or policies during client interactions, with information scattered across PDFs, emails, training decks, and intranets, leaving no single place to turn mid‑conversation.
- Training is provided at onboarding and updated only at each new collection release, 
  leaving gaps in between
- The real bottleneck is the gap between knowing and acting: advisors have context but no support to turn it into a 
  confident, personalized interaction at the right moment
  -They also need guidance on how to rebound in front of a client, from greetings to tailored recommendations, with on‑brand insights delivered instantly.

**For office teams (CRM, marketing, product):**
- Struggle with fragmented sales and client data, making personalization at scale difficult. 
- They lack a unified view of performance and
- Cannot provide real‑time answers to field teams, creating bottlenecks on both sides.

**For the organization:**
- Inconsistent messaging across boutiques and countries, with no guarantee that 
  brand DNA is being conveyed accurately at every touchpoint
- Knowledge gaps are invisible 
- A wrong answer on warranty, materials, or policy is a brand trust failure

### 2. Problem Statement 

> Brand knowledge and performance data remain fragmented, leaving teams without a unified view to guide them
> and a real‑time support to turn context into confident, personalized interactions.
> The goal: empower every persona with the right information and discourse at the right moment, ensuring luxury experiences stay seamless and true to brand DNA.


### 3. Product Vision

#### The brand as a design constraint

The assistant doesn't just retrieve specs, it helps advisors tell the story of each piece in a way that resonates with each client's identity and aspirations. 
The **augmented advisor** becomes a curator of experience, translating brand values into deeply personal moments.

LÉIA was designed from scratch as the fictional company this project is built 
around and its brand DNA directly shaped every product decision.

Founded in 2013, the year France legalized marriage equality, LÉIA was built 
around one core idea: **jewelry as emancipation, as a mirror of identity**, as a mirror of identity.

The maison expresses this vision through four collections:

| Collection | Philosophy |
|-----------|------------|
|  **Amazon** | Unapologetic feminine power — bold, visible, commanding |
|  **Hatching** | Quiet strength — delicate but unbreakable, soft yet architectural |
|  **Eclipse** | Beyond definition — designed for non-binary and gender-fluid individuals |
|  **Vanta** | Tech minimalism — time reimagined, function without decoration |

> *"At LÉIA, femininity is vast. Powerful with Amazon. Poetic with Hatching. 
> Boundless with Eclipse. A piece of jewelry is never assigned — it is chosen."*

---

#### Market trends that informed the vision

Three structural shifts in luxury retail shaped the product direction:

**Hyper-personalization as the new standard**
Consumers are willing to spend up to 20% more for personalized interactions. 
Online experiences now influence over 78% of all luxury purchases. The 
in-store advisor is the last and most powerful personalization lever 
a brand has.

**The phygital imperative**
Brands are using AI and connected experiences to make physical stores as 
intelligent as digital channels — from real-time product intelligence to 
experiential retail concepts that blend physical and digital touchpoints.


**Omnichannel consistency at scale**
With online luxury purchases forecast to reach 30% of market share, brand 
consistency across every touchpoint is non-negotiable. An advisor in Hong Kong 
and an advisor in Paris must tell the same story — with the same accuracy, 
the same emotional depth, the same brand voice.

---

#### Knowledge architecture

Eight documents were structured into a queryable knowledge base, covering every dimension of the brand a team member might need:

| Document | What it enables |
|----------|----------------|
| `brand_story.txt` | Brand DNA, values, founding story, collection philosophy |
| `boutique_guidelines.txt` | Service standards, client journey, advisor training |
| `after_sales_policy.txt` | Warranty, repairs, returns, trade-in program |
| `care_instructions.txt` | Material-specific care by metal, stone, and product type |
| `leia_products.csv` | 42 products — materials, prices, gemstones, craftsmanship |
| `purchase_history.csv` | 186 transactions across 4 boutiques |
| `client_profiles.csv` | VIP tiers, preferences, purchase history per client |

**`boutique_innovation.txt`** — Two original phygital retail concepts:
- **Chrysalis Room** — a private in-store space with programmable environment 
  (lighting, scent, sound) and an encrypted digital memory capsule tied to 
  each purchase
- **Constellation Wall** — a touchscreen installation displaying real client 
  stories across all global boutiques, filterable by collection, theme, and city


### 4. OKRs

**Objective 1 — Empower field and office teams with instant, reliable access 
to brand knowledge**

| Key Result | Target |
|-----------|--------|
| KR1 | Reduce average time to find product or policy information from ~5 min to <30 sec |
| KR2 | Deliver consistent, brand-accurate answers across all 5 user personas |
| KR3 | Cover 100% of knowledge base documents in RAG retrieval |
| KR4 | Enable advisors to prepare personalized client outreach in <1 min using client data |

**Objective 2 — Give managers and office teams actionable visibility on 
business performance**

| Key Result | Target |
|-----------|--------|
| KR1 | Deliver a unified view of revenue, clients, and collections across all boutiques |
| KR2 | Enable filtering by city, collection, VIP tier, and date range |
| KR3 | Surface top clients, advisor performance, and product trends in a single view |

**Objective 3 — Build a scalable knowledge system that improves over time**

| Key Result | Target |
|-----------|--------|
| KR1 | Establish a modular knowledge base that can be updated without touching the code |
| KR2 | Identify knowledge gaps through usage patterns and dashboard insights |
| KR3 | Document a clear iteration roadmap based on observed user needs |

### 5. The Product Response

Two complementary tools designed to address the identified needs : 
one for knowledge access, one for performance visibility.

| Tool | What it solves | For whom |
|------|---------------|----------|
| 🤖 **RAG Chatbot** | Instant access to brand knowledge, adapted by role and context, and for boutique advisors, turns client data into personalized outreach in seconds | Boutique advisors, CRM, after-sales, marketing, product teams |
| 📊 **Analytics Dashboard** | Unified view of sales, clients, and collection performance | Boutique managers, CRM team |

Together they create a **single source of truth** and a feedback loop where usage patterns reveal what teams actually need, informing future iterations of both tools.

---

## 🤖 Feature 1 — Multi-Persona RAG Chatbot

A knowledge base assistant grounded in LÉIA's internal documents (brand story, product catalog, boutique guidelines, after-sales policy, care instructions).

### What makes it different from a generic chatbot

The same question gets a **different answer depending on who is asking** — because a boutique advisor needs a fast 3-line answer during a client interaction, while a marketing manager needs the full brand narrative.

**5 personas, 5 response styles:**

| Persona | Use case | Response style |
|---------|----------|----------------|
| 🛍️ Boutique Advisor | Quick ref during client interaction **or** personalized outreach preparation based on client profile | Concise, bullet points, 50-100 words |
| 📞 Customer Service | After-sales policy & repair info | Clear, step-by-step, policy-accurate |
| 🎨 Marketing / Brand | Storytelling & brand positioning | Rich, narrative, 150-250 words |
| 📈 CRM Manager | Client insights & purchase patterns | Data-focused, analytical |
| 🔧 Product Team | Materials, craftsmanship, specs | Technical, detailed |

**Clienteling in action — two advisor use cases:**

| Question type | Example | Response |
|--------------|---------|----------|
| Product info | "Materials of the Möbius Ring?" | Bullet points — metal, stone, price, key feature |
| Client outreach | "Sophie arrives tomorrow, how do I prepare?" | Client profile summary + product suggestion based on her history |

> If a client is not found in the knowledge base, the assistant says so clearly — 
> it never invents data.

### Architecture

```
User query
    │
    ▼
RAG retrieval (top-k chunks from knowledge base)
    │
    ▼
Persona-specific system prompt + context injection
    │
    ▼
Llama 3.3 70B via Hugging Face Router
    │
    ▼
Grounded, role-appropriate answer
```

### Stack
- **LLM:** `meta-llama/Llama-3.3-70B-Instruct` via Hugging Face Inference API
- **RAG:** Custom knowledge base built from internal brand documents
- **Frontend:** Streamlit
- **Retrieval:** Top-15 chunks with source attribution

---

## 📊 Feature 2 — Analytics Dashboard

An interactive business intelligence dashboard for boutique managers and the CRM team.

### Key views

- **Revenue by collection** — which collections drive the most revenue
- **Revenue by city** — performance comparison across boutiques
- **VIP tier distribution** — Member / Gold / Platinum / Diamond breakdown
- **Top 5 best-selling products** — global and per-city
- **Purchases over time** — monthly trend line
- **Top clients by spending** — ranked table with preferences
- **Advisor performance** — sales count, revenue, average transaction
- **Collection insights** — avg price and product count per collection

### Filters
All views are filterable by: **City** · **VIP Tier** · **Collection** · **Date range**

### Stack
- **Data:** CSV files (42 products, 186 transactions, client profiles)
- **Visualization:** Plotly Express + Plotly Graph Objects
- **Frontend:** Streamlit

---

## 🗂️ Project Structure

```
leia-ai-suite/
│
├── README.md
├── requirements.txt
├── .env.example
│
├── app.py                     # Chatbot v1 — basic version
├── app_rag.py                 # Chatbot v2 — RAG + multi-persona
├── dashboard_analytics.py    # Analytics dashboard
│
└── knowledge_base/
    ├── brand_story.txt
    ├── boutique_guidelines.txt
    ├── boutique_innovation.txt
    ├── after_sales_policy.txt
    ├── care_instructions.txt
    ├── leia_products.csv
    ├── purchase_history.csv
    └── client_profiles.csv
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/leia-ai-suite.git
cd leia-ai-suite
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
```bash
cp .env.example .env
# Add your Hugging Face token to .env
```

### 4. Run the chatbot
```bash
streamlit run app_rag.py
```

### 5. Run the dashboard
```bash
streamlit run dashboard_analytics.py
```

---

## 📦 Requirements

```
streamlit
requests
pandas
plotly
python-dotenv
langchain          # or your RAG implementation
```

> See `requirements.txt` for full list with pinned versions.

---

## 🔭 Roadmap — What I'd build next

Here are the features I'd prioritize in a next sprint:

**Machine Learning & Behavioral Analytics layer** 
- [ ] **Clienteling assistant** — enable advisors to prepare personalized client outreach in seconds: "Sophie arrives tomorrow, how do I prepare?" → client 
  profile summary + conversation starter + product suggestion based on her history
- [ ]**Behavioral analysis** — analyze purchase history, expressed preferences, and social media interactions to build rich client profiles and detect emerging taste signals 
- [ ] **Sales forecasting** — predict collection and boutique performance for the coming months 
- [ ] **Retrieval ranking** — train a ranking model on advisor feedback to continuously improve chatbot answer quality over time

**Improve the chatbot** 
- [ ] **Conversation memory** — persist context within a session so advisors can ask follow-up questions without repeating themselves
- [ ] **Feedback loop** — advisors rate answers (👍/👎) to track response quality and improve retrieval over time 
- [ ] **Multi-language support** — French, English, Cantonese for the Hong Kong boutique
- [ ] **Knowledge gap tracking** — analyze chatbot query patterns to identify where information is missing or unclear

**Bigger picture** 
- [ ] **Connect the two tools** — an advisor mid-conversation could pull live dashboard insights directly in the chatbot.

**Improve the dashboard** 
- [ ] **Real-time data sync** — replace static CSVs with a live database (Supabase or Airtable) 

---

## Why this project / About me

I built this project to demonstrate product thinking applied to AI tooling, and my ability to connect technical workflows with user needs. 

Fascinated by new technologies and AI, I bring a hybrid background in law and business, enriched by roles across account management, partnerships, marketing, and operations in tech organizations from startups to multinationals. 

My clear goal is to move into operational and strategic roles leading innovative, AI‑driven projects. What motivates me most is shaping vision, structuring roadmaps, building solutions, and ensuring they create real impact, with adaptability and fast learning as my foundation.


📬 [LinkedIn](https://www.linkedin.com/in/leana-dardano/) · [Email](mailto:dardano.leana@email.com)

---

## Disclaimer

LÉIA is a fictional brand created for this portfolio project. All data (clients, transactions, products) is synthetic. No real personal data was used.

---

*Built with curiosity and a lot of Streamlit reruns.*
