import streamlit as st
import requests

st.set_page_config(page_title="Offline CRM Agent", page_icon="🧾")
st.title("🧾 Offline CRM Agent")
st.subheader("Ask about invoices, customer payments, and more")

query = st.text_input("🔍 Enter your CRM/ERP question:")

if st.button("Get Answer"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Processing..."):
            try:
                response = requests.post("http://localhost:8000/query", json={"query": query})
                response.raise_for_status()
                data = response.json()

                raw_output = data.get("output", "No response.")

                # Handle nested dict (like LangChain returning {input, output})
                if isinstance(raw_output, dict):
                    answer_text = raw_output.get("output", "No response.")
                else:
                    answer_text = raw_output

                st.success("✅ Here's what I found:")
                st.markdown(f"""
                <div style="background-color:#f0f2f6;padding:20px;border-radius:10px;">
                    <strong>📨 Question:</strong> {query}<br><br>
                    <strong>💡 Answer:</strong><br>{answer_text}
                </div>
                """, unsafe_allow_html=True)

            except requests.exceptions.RequestException as e:
                st.error("❌ Server error. Please ensure the backend is running.")
                st.text(str(e))
            except Exception as e:
                st.error("❌ Unexpected error.")
                st.text(str(e))