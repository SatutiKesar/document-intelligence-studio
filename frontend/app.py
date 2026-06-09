# # import streamlit as st
# # import requests

# # # 1. Page Configuration & Layout
# # st.set_page_config(
# #     page_title="Document Intelligence Platform",
# #     page_icon="🤖",
# #     layout="wide"
# # )

# # # 2. Premium Custom CSS Styles (With Maximum Readability Overrides)
# # st.markdown("""
# #     <style>
# #     /* Change the main app background to a deep premium tech navy gradient */
# #     .stApp {
# #         background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
# #         color: #ffffff !important;
# #     }
    
# #     /* FORCE ALL CHAT MESSAGE TEXT TO BE SOLID WHITE & HIGHER READABILITY */
# #     [data-testid="stChatMessage"] p, 
# #     [data-testid="stChatMessage"] span, 
# #     [data-testid="stChatMessage"] li,
# #     .stMarkdown p {
# #         color: #ffffff !important;
# #         font-size: 1.1rem !important; /* Slightly larger font size to read from afar */
# #         font-weight: 500 !important;   /* Slightly bolder weight for clean presentation */
# #         line-height: 1.6 !important;
# #     }
    
# #     /* Style headers with bright tech colors */
# #     h1 {
# #         color: #38bdf8 !important; /* Cyber Cyan */
# #         font-weight: 800 !important;
# #         font-family: 'Inter', sans-serif;
# #     }
# #     h3 {
# #         color: #cbd5e1 !important; /* Lighter slate gray */
# #     }
    
# #     /* Clean up borders and give buttons an interactive glow */
# #     .stButton>button {
# #         background: linear-gradient(90deg, #0284c7 0%, #0369a1 100%) !important;
# #         color: white !important;
# #         border: none !important;
# #         border-radius: 8px !important;
# #         font-weight: bold !important;
# #         transition: all 0.3s ease;
# #         box-shadow: 0 4px 12px rgba(3, 105, 161, 0.3);
# #     }
# #     .stButton>button:hover {
# #         transform: translateY(-2px);
# #         box-shadow: 0 6px 20px rgba(3, 105, 161, 0.5);
# #     }
    
# #     /* Darken sidebar background to look premium */
# #     [data-testid="stSidebar"] {
# #         background-color: #0b0f19 !important;
# #         border-right: 1px solid #334155;
# #     }
# #     [data-testid="stSidebar"] p {
# #         color: #cbd5e1 !important; /* Keeps sidebar description visible but secondary */
# #     }
    
# #     /* Adjust divider lines */
# #     hr {
# #         border-color: #334155 !important;
# #     }
# #     </style>
# # """, unsafe_allow_html=True)

# # # The target web address where your Uvicorn FastAPI server is running
# # # BACKEND_URL = "http://127.0.0.1:8000"
# # BACKEND_URL = "http://backend:8000/chat"

# # # 3. Sidebar Layout & Infrastructure Monitor
# # with st.sidebar:
# #     st.markdown("<h2 style='color:#38bdf8;'>🛠️ Core Infrastructure</h2>", unsafe_allow_html=True)
# #     st.write("Control panel interface to monitor running backend microservices.")
# #     st.write("---")
    
# #     st.markdown("### Data Operations")
# #     if st.button("🚀 Process & Index System", use_container_width=True):
# #         with st.spinner("Verifying vector matrix..."):
# #             st.success("✅ Connection to Backend Active!")
            
# #     st.write("---")
# #     st.markdown("⚡ **Engine Status:** `Running` (Port 8000)")
# #     st.markdown("🤖 **Model Architecture:** `Gemini-2.5-Flash`")
# #     st.markdown("📦 **Vector Database:** `ChromaDB`")

# # # 4. Main Workspace Presentation
# # st.title("⚡ Document Intelligence Studio")
# # st.subheader("Enterprise Contextual Retrieval-Augmented Generation Engine")
# # st.write("---")

# # # 5. Interactive Chat Engine (Session History State tracking)
# # if "messages" not in st.session_state:
# #     st.session_state.messages = []

# # # Loop and render prior conversations sequentially inside modern UI containers
# # for message in st.session_state.messages:
# #     with st.chat_message(message["role"]):
# #         st.markdown(message["content"])

# # # Accept user queries input form
# # if user_query := st.chat_input("Ask something about your document schemas..."):
# #     # Render user prompt onto the dashboard instantly
# #     with st.chat_message("user"):
# #         st.markdown(user_query)
# #     st.session_state.messages.append({"role": "user", "content": user_query})

# #     # Network round-trip processing wrapper
# #     with st.chat_message("assistant"):
# #         with st.spinner("FastAPI routing network loop execution..."):
# #             try:
# #                 # Packages your variable with the key 'message' to match main.py perfectly!
# #                 payload = {"message": str(user_query)}
                
# #                 # Send HTTP POST request to your FastAPI backend
# #                 response = requests.post(
# #                     f"{BACKEND_URL}/chat", 
# #                     json=payload,
# #                     headers={"Content-Type": "application/json"}
# #                 )
                
# #                 if response.status_code == 200:
# #                     # Extract the answer text string
# #                     answer = response.json().get("response", "No response key found.")
# #                     st.markdown(answer)
# #                     st.session_state.messages.append({"role": "assistant", "content": answer})
# #                 else:
# #                     # Renders backend diagnostic errors on-screen if formatting slips
# #                     st.error(f"Backend rejection error: {response.status_code}\n\nDetails: {response.text}")
                    
# #             except Exception as e:
# #                 st.error(f"Could not connect to FastAPI server. Ensure Uvicorn is active! Error: {e}")


import streamlit as st
import requests

# 1. Page Configuration & Layout
st.set_page_config(
    page_title="Document Intelligence Platform",
    page_icon="🤖",
    layout="wide"
)

# 2. Premium Custom CSS Styles
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
    
    # 🎯 TARGET FIXED: Yeh button ab asli mein backend ke data parsing logic ko hit karega
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