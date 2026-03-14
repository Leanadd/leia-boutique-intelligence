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
**multi-persona RAG chatbot** that gives every team instant access to brand knowledge,
**analytics dashboard** that turns sales and client data into actionable insights.


## Product Roadmap  
### 1. Discovery — Problem Identification & User Needs

**"What are the real issues that luxury retail teams face on a daily basis, 
and what can be improved?"**

An analysis of the operational reality of a multi-boutique luxury maison revealed 
three main friction points:

**For field teams (boutique advisors, after-sales):**
- No instant access to product knowledge, brand storytelling, or policies just before or during 
  client interactions 
- Training is provided at onboarding and updated only at each new collection release, 
  leaving gaps in between
- Information scattered across PDFs, emails, training decks, and intranets with no 
  single place to turn to mid-conversation
- No tool to quickly adjust the depth of an answer 

**For office teams (CRM, marketing, product):**
- No unified view of sales performance, client behavior, or collection trends
- Time wasted searching scattered systems when a question arises
- Remote coordination with field teams is slow — no way to answer their questions 
  in real time, creating bottlenecks on both sides
- Personalization at scale is impossible: client data exists but can't be translated 
  into actionable recommendations for advisors in the moment

**For the organization:**
- Inconsistent messaging across boutiques and countries, with no guarantee that 
  brand DNA is being conveyed accurately at every touchpoint
- Knowledge gaps are invisible 
- A wrong answer on warranty, materials, or policy is a brand trust failure

### 2. Problem Statement 

> Brand knowledge and performance data are scattered across systems, making it 
> harder for teams to deliver the seamless, personalized experience that defines luxury. 
> The goal: augment every team member with the right information, at the right moment, in the right format.

### 3. Product Vision

#### The brand as a design constraint

LÉIA was designed from scratch as the fictional company this project is built 
around and its brand DNA directly shaped every product decision.

Founded in 2013, the year France legalized marriage equality, LÉIA was built 
around one core idea: **jewelry as emancipation**, as a mirror of identity.

This translates into four distinct collections, each celebrating a different 
facet of that vision:

| Collection | Philosophy |
|-----------|------------|
|  **Amazon** | Unapologetic feminine power — bold, visible, commanding |
|  **Hatching** | Quiet strength — delicate but unbreakable, soft yet architectural |
|  **Eclipse** | Beyond definition — designed for non-binary and gender-fluid individuals |
|  **Vanta** | Tech minimalism — time reimagined, function without decoration |

> *"At LÉIA, femininity is vast. Powerful with Amazon. Poetic with Hatching. 
> Boundless with Eclipse. A piece of jewelry is never assigned — it is chosen."*

This matters for the AI product. 
The assistant doesn't just retrieve specs, it helps advisors tell the story of each piece in a way that resonates with each client's identity and aspirations. 
The **augmented advisor** becomes a curator of experience, translating brand values into deeply personal moments.

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
| `boutique_innovation.txt` | Two phygital retail concepts designed for LÉIA: 
The **Chrysalis Room** : a private in-store space reserved for clients living 
a significant life transition (coming out, divorce, career milestone), equipped 
with adaptive lighting, sound, and a digital memory capsule linked to their 
purchase.
The **Constellation Wall** : a live interactive installation 
displaying anonymized client stories, creating a visible community inside 
the boutique |
| `after_sales_policy.txt` | Warranty, repairs, returns, trade-in program |
| `care_instructions.txt` | Material-specific care by metal, stone, and product type |
| `leia_products.csv` | 42 products — materials, prices, gemstones, craftsmanship |
| `purchase_history.csv` | 186 transactions across 4 boutiques |
| `client_profiles.csv` | VIP tiers, preferences, purchase history per client |


### 4. OKRs

**Objective 1 — Empower field and office teams with instant, reliable access 
to brand knowledge**

| Key Result | Target |
|-----------|--------|
| KR1 | Reduce average time to find product or policy information from ~5 min to <30 sec |
| KR2 | Deliver consistent, brand-accurate answers across all 5 user personas |
| KR3 | Cover 100% of knowledge base documents in RAG retrieval |

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
| 🤖 **RAG Chatbot** | Instant access to brand knowledge, adapted by role and context | Boutique advisors, CRM, after-sales, marketing, product teams |
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
| 🛍️ Boutique Advisor | Quick ref during client interaction | Concise, bullet points, 50-100 words |
| 📞 Customer Service | After-sales policy & repair info | Clear, step-by-step, policy-accurate |
| 🎨 Marketing / Brand | Storytelling & brand positioning | Rich, narrative, 150-250 words |
| 📈 CRM Manager | Client insights & purchase patterns | Data-focused, analytical |
| 🔧 Product Team | Materials, craftsmanship, specs | Technical, detailed |

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

Thinking like a PO, here are the features I'd prioritize in a next sprint:

- [ ] **Client 360 view** — merge chatbot + dashboard so advisors can pull a client profile mid-conversation
- [ ] **Real-time CRM sync** — replace static CSVs with a live database (Supabase or Airtable)
- [ ] **Conversation memory** — persist chat history per advisor session
- [ ] **Alert system** — flag dormant VIP clients who haven't purchased in 6+ months
- [ ] **Multi-language support** — French / English / Cantonese for HK boutique
- [ ] **Feedback loop** — advisors rate chatbot answers to fine-tune retrieval quality over time

---

## 💡 Why this project / About me

I built this project to demonstrate product thinking applied to AI tooling — not just the technical implementation, but the upstream decisions: who are the users, what are their pain points, and how does the product design reflect that.

My background is in [your background here]. I'm looking for **Product Owner / Product Manager** roles where I can sit at the intersection of user needs, business goals, and technical feasibility.

📬 [LinkedIn](https://linkedin.com/in/your-profile) · [Email](mailto:your@email.com)

---

## ⚠️ Disclaimer

LÉIA is a fictional brand created for this portfolio project. All data (clients, transactions, products) is synthetic. No real personal data was used.

---

*Built with curiosity and a lot of Streamlit reruns.*
