import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("AI Interview Coach")

st.header("Upload Resume")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    files = {"file": uploaded_file}

    response = requests.post(f"{API_URL}/upload-resume", files=files)

    if response.status_code == 200:

        data = response.json()

        st.success("Resume uploaded successfully!")

        # Show AI generated summary
        st.subheader("Resume Summary")

        st.write(data["summary"])

        # Save summary in session state
        st.session_state["resume_uploaded"] = True
        st.session_state["resume_summary"] = data["summary"]

    else:
        st.error("Upload failed")


if st.session_state.get("resume_uploaded"):

    st.header("Start Interview")

    # Automatically use resume summary as context
    context = st.session_state["resume_summary"]

    if st.button("Generate Question"):

        response = requests.post(
            f"{API_URL}/generate-question",
            json={"context": context}
        )

        question = response.json()["question"]

        st.session_state["question"] = question


if "question" in st.session_state:

    st.subheader("Interview Question")

    st.write(st.session_state["question"])

    answer = st.text_area("Your Answer")

    if st.button("Submit Answer"):

        response = requests.post(
            f"{API_URL}/evaluate-answer",
            json={
                "question": st.session_state["question"],
                "answer": answer
            }
        )

        evaluation = response.json()["evaluation"]

        st.subheader("AI Evaluation")

        st.write(evaluation)