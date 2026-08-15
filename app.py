import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

st.set_page_config(
    page_title="AI IT Help Desk",
    page_icon="🛠️",
    layout="centered"
)

st.title("AI IT Help Desk Assistant")
st.write(
    "Describe your technical problem and receive an AI-generated "
    "ticket classification and troubleshooting plan."
)

st.warning(
    "Never enter passwords, API keys, financial information, "
    "or other sensitive data."
)

issue = st.text_area(
    "Describe the IT issue:",
    placeholder="Example: My laptop connects to Wi-Fi, but websites will not load.",
    height=150
)

if st.button("Analyze Issue", type="primary"):
    if not issue.strip():
        st.error("Please describe an IT issue first.")
    else:
        with st.spinner("Analyzing the issue..."):
            try:
                response = client.responses.create(
                    model="gpt-5.6",
                    store=False,
                    instructions="""
You are an IT help-desk triage assistant.

Analyze the user's issue and return these exact sections:

Category:
Priority:
Likely Cause:
Troubleshooting Steps:
Escalation Recommendation:
Ticket Summary:

Use only Low, Medium, High, or Critical for priority.
Give safe, practical troubleshooting steps.
Never ask for passwords, API keys, or sensitive information.
Clearly state when a qualified technician should review the issue.
Do not claim certainty when the cause is unclear.
""",
                    input=issue
                )

                st.success("Analysis complete")
                st.markdown(response.output_text)                
                st.download_button(
                    label="Download Support Ticket",
                    data=response.output_text,
                    file_name="it_support_ticket.txt",
                    mime="text/plain",
                    on_click="ignore"
                )

            except Exception as error:
                st.error(f"Unable to analyze the issue: {error}")

