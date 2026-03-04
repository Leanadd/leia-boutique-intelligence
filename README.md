# LÉIA AI Suite — Boutique Intelligence Platform

AI-powered internal tools for a luxury jewelry maison — RAG chatbot &amp; analytics dashboard

> **Luxury retail meets artificial intelligence** — A product case study simulating AI-powered internal tools for a high jewelry maison.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-Llama%203.3%2070B-blueviolet)
![RAG](https://img.shields.io/badge/Architecture-RAG-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

---

## Context & Product Vision

**LÉIA** is a fictional Parisian high jewelry and Swiss watchmaking house. This project simulates the AI tools a Product Manager might design and ship for a luxury retail company with boutiques across Paris, Geneva, New York, and Hong Kong.

### Product Vision — The Augmented Advisor

LÉIA was designed from the ground up with a specific brand DNA: **jewelry as emancipation**. 
3 Jewerly and 1 Watch Collections:
At LÉIA, femininity is vast. Powerful with Amazon. Poetic with Hatching. Boundless with Eclipse. A piece of jewelry is never assigned — it is chosen.
Not jewelry as status, not jewelry as gift, jewelry as a mirror of identity, a tool for becoming. Collections are built around human experiences (transformation, power, fluidity) rather than gender. The Eclipse collection was specifically created for non-binary and gender-fluid individuals. 

This brand philosophy directly shaped the AI product decisions.

A generic RAG assistant retrieves product specs. That's not enough in luxury.

**LÉIA's assistant helps advisors tell the story of each piece** — why it was designed, what emotion it was meant to evoke, which client journey it speaks to. The goal is not to replace the human advisor but to augment them: turning them from salespeople into 
**curators of experience** — translators between the brand's values and each client's personal aspirations.

> *"The advisor doesn't dictate, they illuminate. They don't push a product, they help the client recognize themselves in a piece."*

This is the paradox the AI is designed to resolve: luxury retail needs to feel deeply human and spontaneous, while being perfectly consistent and informed. The augmented advisor is the answer — someone who can hold a meaningful conversation about identity and transformation, and instantly access the exact product knowledge or client insight that makes that conversation land.

In a market where consumers increasingly ask not *"is this for a man or a woman?"* but *"what emotion does this piece evoke in me?"* — the advisor who can answer that question with confidence and depth wins the relationship.

---

### The problem

The luxury sector is undergoing a fundamental shift. Online experiences now influence over 78% of all luxury purchases, and brands are under pressure to deliver interactions that are **hyperpersonalized, emotionally resonant, and consistent** — whether in-store, online, or across both. Consumers are willing to spend up to 20% more for experiences tailored to their tastes. The bar for in-store excellence has never been higher.

Yet the teams responsible for delivering that experience: boutique advisors, CRM, after-sales, marketing, are working with knowledge that is scattered across intranets, PDFs, SharePoint, training decks, and emails. The phygital promise breaks down at the most critical moment: when an advisor is standing in front of a client and doesn't have the right answer.

The result:

- **Lost time** — advisors search manually mid-client interaction
- **Inconsistent answers** — different boutiques, different versions of the truth
- **Degraded client experience** — the luxury promise breaks down at the point of service
- **No visibility on field needs** — management can't see what questions are being asked or where knowledge gaps exist

This is the gap LÉIA AI Suite is designed to close: **bringing the omnichannel intelligence layer inside the boutique**, so advisors can deliver the hyper-personalized, expert experience that modern luxury clients expect, in real time, every time.

### The product response

The goal was to go beyond a simple chatbot demo and think through **who the users are**, **what problems they face daily**, and **how AI can solve them** — the way a PM would.

Rather than "building a chatbot," I defined the business problem first, then designed two tools to address it:

| Tool                        | What it solves                     | For whom |
| 🤖 **RAG Chatbot** | Instant, reliable access to internal knowledge — grounded in brand documents, adapted by role | Boutique advisors, CRM, after-sales, marketing, product teams |
| 📊 **Analytics Dashboard** | Unified view of sales, client, and collection performance — turning raw data into actionable insights | Boutique managers, CRM team |

Together they create a **single source** for both operational knowledge and business performance — and a feedback loop where usage patterns reveal what the field actually needs

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
