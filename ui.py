
import streamlit as st
from video_analyser import build_youtube_agent

st.set_page_config(
    page_title="YouTube Video Analyser",
    page_icon="▶",
    layout="wide"
)

st.title("YouTube Video Analyser")
st.write("Enter a YouTube URL to generate an AI-powered summary.")

video_url = st.text_input(
    "YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

if st.button("Analyze Video", type="primary"):
    if not video_url.strip():
        st.warning("Please enter a YouTube URL.")
    else:
        with st.spinner("Analyzing video..."):
            try:
                agent = build_youtube_agent()

                response = agent.run(
                    f"Analyze this video: {video_url}"
                )

                st.subheader("Video Summary")
                st.markdown(response.content)

            except Exception as e:
                st.error(f"Analysis failed: {e}")
