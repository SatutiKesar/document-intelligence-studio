import streamlit as st
import requests

# 1. Page Configuration & Layout
st.set_page_config(
    page_title="Document Intelligence Platform",
    page_icon="🤖",
    layout="wide"
)

# 2. Custom CSS Styles
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff !important;
    }
    [data-testid="stChatMessage"] p, 
    [data-testid="stChatMessage"] span, 
    [data-testid="stChatMessage"] li,
    .stMarkdown p {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
    }
    h1 {
        color: #38bdf8 !important;
        font-weight: 800 !important;
        font-family: 'Inter', sans-serif;
    }
    h3 {
        color: #cbd5e1 !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #0284c7 0%, #0369a1 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(3, 105, 161, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(3, 105, 161, 0.5);
    }
    [data-testid="stSidebar"] {
        background-color: #0b0f19 !important;
        border-right: 1px solid #334155;
    }
    [data-testid="stSidebar"] p {
        color: #cbd5e1 !important;
    }
    hr {
        border-color: #334155 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Base backend container URL
BACKEND_URL = "http://backend:8000"

# 3. Sidebar Layout & Infrastructure Monitor
with st.sidebar:
    st.markdown("<h2 style='color:#38bdf8;'>🛠️ Core Infrastructure</h2>", unsafe_allow_html=True)
    st.write("Control panel interface to monitor running backend microservices.")
    st.write("---")
    
    st.markdown("### Data Operations")
    
   
    if st.button("🚀 Process & Index System", use_container_width=True):
        with st.spinner("Processing PDFs and building vector database..."):
            try:
                res = requests.post(f"{BACKEND_URL}/ingest")
                if res.status_code == 200:
                    st.success("✅ Database Built Successfully!")
                else:
                    st.error(f"Ingest failed: {res.text}")
            except Exception as e:
                st.error(f"Could not connect to backend microservice: {e}")
            
    st.write("---")
    st.markdown("⚡ **Engine Status:** `Running` (Port 8000)")
    st.markdown("🤖 **Model Architecture:** `Gemini-2.5-Flash`")
    st.markdown("📦 **Vector Database:** `ChromaDB`")

# 4. Main Workspace Presentation
st.title("⚡ Document Intelligence Studio")
st.subheader("Enterprise Contextual Retrieval-Augmented Generation Engine")
st.write("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("Ask something about your document schemas..."):
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    with st.chat_message("assistant"):
        with st.spinner("FastAPI routing network loop execution..."):
            try:
                payload = {"message": str(user_query)}
                
                response = requests.post(
                    f"{BACKEND_URL}/chat", 
                    json=payload,
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    answer = response.json().get("response", "No response key found.")
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"Backend rejection error: {response.status_code}\n\nDetails: {response.text}")
                    
            except Exception as e:
                st.error(f"Could not connect to FastAPI server. Ensure Uvicorn is active! Error: {e}")
