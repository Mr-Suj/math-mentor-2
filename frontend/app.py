import streamlit as st
import requests

TEXT_API = "http://localhost:8000/solve_text"
IMAGE_API = "http://localhost:8000/solve_image"
AUDIO_API = "http://localhost:8000/solve_audio"

st.set_page_config(
    page_title="AI Math Mentor",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Math Mentor")
st.caption("Solve JEE-style math problems using AI")

st.divider()

# Create tabs
tab1, tab2, tab3 = st.tabs(["✍ Text Question", "📷 Image Question", "🎤 Audio Question"])


# -------------------------
# TEXT TAB
# -------------------------

with tab1:

    question = st.text_input(
        "Enter your math problem",
        placeholder="Example: Find derivative of x^2 + 3x"
    )

    if st.button("Solve", key="solve_text"):

        if question.strip() == "":
            st.warning("Please enter a question")
        else:

            with st.spinner("Solving problem..."):

                response = requests.post(
                    TEXT_API,
                    json={"question": question}
                )

                if response.status_code != 200:
                    st.error(response.text)
                else:

                    result = response.json()

                    st.success("Solution generated")

                    st.subheader("Final Answer")
                    st.code(result["solution"])

                    st.subheader("Explanation")
                    st.write(result["explanation"])

                    st.subheader("Verification")
                    st.json(result["verification"])


# -------------------------
# IMAGE TAB
# -------------------------

with tab2:

    uploaded_image = st.file_uploader(
        "Upload a math problem image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

    if uploaded_image and st.button("Solve", key="solve_image"):

        with st.spinner("Extracting text and solving..."):

            response = requests.post(
                IMAGE_API,
                files={"file": uploaded_image}
            )

            if response.status_code != 200:
                st.error(response.text)
            else:

                result = response.json()

                st.success("Problem solved")

                st.subheader("Extracted Question")
                st.write(result["extracted_question"])

                st.subheader("Final Answer")
                st.code(result["solution"])

                st.subheader("Explanation")
                st.write(result["explanation"])

                st.subheader("Verification")
                st.json(result["verification"])


# -------------------------
# AUDIO TAB
# -------------------------

with tab3:

    uploaded_audio = st.file_uploader(
        "Upload an audio question",
        type=["wav", "mp3", "m4a"]
    )

    if uploaded_audio is not None:
        st.audio(uploaded_audio)

    if uploaded_audio and st.button("Solve", key="solve_audio"):

        with st.spinner("Transcribing audio and solving..."):

            response = requests.post(
                AUDIO_API,
                files={"file": uploaded_audio}
            )

            if response.status_code != 200:
                st.error(response.text)
            else:

                result = response.json()

                st.success("Problem solved")

                st.subheader("Transcribed Question")
                st.write(result["transcribed_question"])

                st.subheader("Final Answer")
                st.code(result["solution"])

                st.subheader("Explanation")
                st.write(result["explanation"])

                st.subheader("Verification")
                st.json(result["verification"])


# st.sidebar.title("About")
# st.sidebar.info(
# """
# AI Math Mentor

# Features:
# - Multimodal input
# - RAG retrieval
# - Multi-agent reasoning
# - Verification layer
# - Human-in-the-loop
# """
# )

st.sidebar.title("About")

st.sidebar.markdown("""
### 🚀 Project Overview
AI Math Mentor is an **AI-powered system that solves JEE-style mathematics problems** using a **multi-agent architecture and multimodal input processing**.

Users can submit problems through **text, images, or audio**, and the system automatically extracts, reasons, solves, verifies, and explains the solution.

---

### ⚙️ Core Capabilities

🧩 **Multimodal Input**
- Text problems
- Image-based questions (OCR)
- Spoken math queries (Speech-to-Text)

🧠 **Multi-Agent Reasoning**
- Problem parsing agent  
- Strategy planning agent  
- Mathematical solver agent  
- Verification agent

📚 **Retrieval Augmented Generation (RAG)**
- Vector search using **BGE embeddings**
- Knowledge base of mathematical concepts
- Context-aware reasoning

🔢 **Symbolic Math Engine**
- Powered by **SymPy**
- Performs algebraic manipulation and verification

🧾 **Solution Verification Layer**
- Mathematical validation of results
- Reduces hallucinations

💾 **Learning & Memory**
- Stores solved problems
- Improves reasoning over time

🧑‍🏫 **Human-in-the-Loop (HITL)**
- Allows correction of incorrect solutions
- System learns from feedback


""")

st.sidebar.markdown("---")

st.sidebar.caption("Built with ❤️ using AI, RAG, and Multi-Agent Systems")
