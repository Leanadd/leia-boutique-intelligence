"""
LÉIA Chatbot with RAG
Advanced knowledge base assistant for LÉIA boutique advisors
"""

import streamlit as st
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from rag_system import LEIAKnowledgeBase

# Load custom styles for LÉIA branding
from leia_style import inject_leia_style

st.set_page_config(page_title="LÉIA Assistant", page_icon="◈", layout="wide")

inject_leia_style() 

# Load environment variables
load_dotenv(dotenv_path=Path(".") / ".env")

# Hugging Face API configuration
API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

# Initialize RAG system (cached to avoid reloading)
@st.cache_resource
def initialize_knowledge_base():
    """Initialize the LÉIA knowledge base (runs once)"""
    kb = LEIAKnowledgeBase()
    if kb.initialize():
        return kb
    return None

# Query the knowledge base
def get_relevant_context(kb, question, k=3):
    """Get relevant context from knowledge base"""
    if kb is None:
        return ""
    
    results = kb.query(question, k=k)
    
    if not results:
        return ""
    
    # Combine relevant documents into context
    context_parts = []
    for i, doc in enumerate(results, 1):
        source = doc.metadata.get('source', 'unknown')
        content = doc.page_content[:2000]  # Limit length
        context_parts.append(f"[Source {i}: {source}]\n{content}")
    
    return "\n\n".join(context_parts)

# Query Hugging Face with RAG context
def query_hf_with_rag(messages, context="", persona="Boutique Advisor"):
    """Query Hugging Face API with RAG context and persona-specific prompt"""
    
    # Persona-specific system prompts
    persona_prompts = {
        "Boutique Advisor": """You are a quick-reference assistant for LÉIA boutique advisors during client interactions.

CRITICAL INSTRUCTIONS:
- CONCISE answers 
- ACTIONABLE information only
- Use BULLET POINTS for comparisons
- Include: materials, price, key features
- Skip marketing language
- Professional colleague tone
- ONLY use information from the knowledge base — never invent client data, 
  product details, or policies. If information is not found, say clearly: 
  "I don't have this information in the knowledge base."

TWO USE CASES — detect automatically from the question:

1. PRODUCT / POLICY QUESTION
- CONCISE answers (50-100 words max)
→ Return bullet points with key facts only
→ Format: Name | Price | Materials | Key feature (3-4 lines)
→ Example: "Matériaux de la Möbius Ring ?" → bullet points
Format for products: Name | Price | Materials | Why it's special (3-4 lines)
Format for clients: Name | Tier | Preferences | Last purchase (4 lines)
Format for comparisons: Bullet points with key differences

2. CLIENTELING / OUTREACH QUESTION  
→ When advisor mentions a client name or upcoming visit:
   - Retrieve client's purchase history and preferences from knowledge base
   - If client is not found in the knowledge base, say: 
     "I don't have any data on this client."
   - If client is found, suggest a short personalized message 
     or preparation notes based strictly on available data
   - Tone: warm, on-brand, never transactional
→ Example: "Sophie arrives tomorrow, how do I prepare?" 
   → client profile summary + conversation starters + product suggestion

IMPORTANT: 
- When asked about COLLECTIONS, provide collection overview
- When asked about specific PRODUCTS, provide product details
- Judgment and final message always belong to the advisor
- Never script a full conversation — offer a starting point only""",

        "Customer Service": """You are a support assistant for LÉIA after-sales team.

CRITICAL INSTRUCTIONS:
- CLEAR and PRECISE policy information
- Include specific terms (warranty duration, what's covered)
- Step-by-step for processes
- Empathetic but efficient tone
- 75-150 words depending on complexity

Always include: Policy terms, timelines, what client needs to do""",

        "Marketing/Brand Team": """You are a brand storytelling assistant for LÉIA marketing team.

INSTRUCTIONS:
- RICH, DETAILED responses (150-250 words)
- Include emotional/narrative elements
- Connect to brand values (inclusivity, transformation, "Unbound")
- Provide context and meaning
- Inspiring, elevated tone

Focus on: Why it matters, story behind it, brand positioning""",

        "CRM Manager": """You are an insights assistant for LÉIA CRM team.

INSTRUCTIONS:
- DATA-FOCUSED responses
- Include numbers (spending, purchase count, dates)
- Identify patterns and segments
- 100-150 words
- Analytical, strategic tone

Focus on: Client behavior, preferences, opportunities""",

        "Product Team": """You are a product knowledge assistant for LÉIA product development.

INSTRUCTIONS:
- TECHNICAL and DETAILED (100-200 words)
- Materials, construction, specifications
- Design intent and craftsmanship
- Price positioning
- Precise, expert tone

Focus on: How it's made, why these choices, technical details"""
    }
    
    # Get persona-specific prompt (default to Boutique Advisor)
    base_prompt = persona_prompts.get(persona, persona_prompts["Boutique Advisor"])
    
    # Add context if available
    system_message = base_prompt
    if context:
        system_message += f"\n\nRelevant information from LÉIA knowledge base:\n{context}"
    
    system_message += "\n\nONLY use information from the context provided. Never invent details."
    
    # Prepare messages with system context
    api_messages = [{"role": "system", "content": system_message}]
    api_messages.extend(messages)
    
    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct",
        "messages": api_messages,
        "max_tokens": 800,
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
        
        if response.status_code != 200:
            return f"[Erreur API {response.status_code}] {response.text}"
        
        data = response.json()
        return data["choices"][0]["message"]["content"]
    
    except Exception as e:
        return f"[Erreur] {str(e)}"

# Streamlit UI
st.set_page_config(
    page_title="LÉIA Assistant", 
    page_icon="◈",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("◈ LÉIA Assistant")
    st.markdown("---")
    
    # Persona Selection
    st.markdown("### 👤 Select Your Role")
    persona = st.selectbox(
        "Who are you?",
        [
            "Boutique Advisor",
            "Customer Service",
            "Marketing/Brand Team",
            "CRM Manager",
            "Product Team"
        ],
        key="persona"
    )

    st.markdown("### Details")
    
    # Dynamic description based on persona
    persona_descriptions = {
        "Boutique Advisor": "Quick reference for client interactions",
        "Customer Service": "Policy and after-sales support",
        "Marketing/Brand Team": "Brand storytelling and positioning",
        "CRM Manager": "Client insights and analytics",
        "Product Team": "Collection details and product specs"
    }
    
    st.markdown(f"**{persona}**")
    st.markdown(persona_descriptions.get(persona, "Access LÉIA knowledge base"))
    
    
    st.markdown("---")
    st.markdown("### Knowledge Base")
    
    # Initialize knowledge base
    kb = initialize_knowledge_base()
    
    if kb:
        st.markdown("<p style='font-size: 0.82rem;'>✅ Knowledge Base Active</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 0.82rem;'>📚 {len(kb.documents)} documents loaded</p>", unsafe_allow_html=True)
    else:
        st.error("❌ Knowledge Base Error")
    
    st.markdown("---")
    
    # Clear conversation button
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# Main chat interface
st.markdown("<h3 style='font-size: 1.7rem; font-weight: 350; font-family: 'Cormorant Garamond', serif'>🪞 How would you like to improve today?</h3>", unsafe_allow_html=True)

st.markdown("---")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
AVATARS = {"assistant": "👁", "user": "👤"}
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=AVATARS[msg["role"]]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything about LÉIA products, clients, policies, or procedures...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get current persona from sidebar
    current_persona = st.session_state.get("persona", "Boutique Advisor")
    
    # Get relevant context from RAG
    with st.spinner("🔍 Searching knowledge base..."):
        context = get_relevant_context(kb, user_input, k=15)
    
    # Query AI with context and persona
    with st.spinner("💭 Thinking..."):
        # Prepare messages for API
        api_messages = [{"role": m["role"], "content": m["content"]} 
                       for m in st.session_state.messages]
        
        assistant_reply = query_hf_with_rag(api_messages, context, persona=current_persona)
    
    # Add assistant reply
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
    
    # Show sources in expander
    if context:
        with st.expander("📚 Sources used"):
            st.text(context[:1000] + "..." if len(context) > 1000 else context)