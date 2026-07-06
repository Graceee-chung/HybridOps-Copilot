import streamlit as st
from src.inference import analyze_ticket

st.set_page_config(
    page_title="AI IT Service Desk Copilot",
    layout="wide"
)

st.title("Hybrid-Local AI IT Service Desk Copilot")

st.write(
    "This local AI system classifies IT tickets, predicts priority, retrieves similar incidents, and generates troubleshooting recommendations."
)

ticket_text = st.text_area(
    "Enter an IT support ticket:",
    value="User cannot access Microsoft 365 account after password reset and MFA does not appear.",
    height=150
)

if st.button("Analyze Ticket"):
    with st.spinner("Running local AI pipeline..."):
        result = analyze_ticket(ticket_text)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Predicted Category")
        st.write(result["category"])

    with col2:
        st.subheader("Predicted Priority")
        st.write(result["priority"])

    st.subheader("Similar Historical Tickets")
    st.dataframe(result["similar_tickets"])

    st.subheader("Knowledge Base Sources")
    st.write(result["kb_sources"])

    st.subheader("Recommended Resolution")
    st.write(result["resolution"])