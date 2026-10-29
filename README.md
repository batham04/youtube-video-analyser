# 🎬 YouTube Video Analyser

An AI-powered YouTube video summarization application built with **Python, Streamlit, Agno, and Groq**. It helps users understand YouTube videos through structured, AI-generated summaries without needing to watch every minute.

🚀 **Live Demo:** [Try YouTube Video Analyser](https://batham04-youtube-video-analyser-ui-zzpzl8.streamlit.app/)

## ✨ Features

- **YouTube Video Analysis:** Submit a YouTube video URL for analysis.
- **AI-Powered Summarization:** Generate clear, structured summaries of video content.
- **Detailed Insights:** Organize information into key concepts, important points, and conclusions.
- **Beginner-Friendly Explanations:** Make complex topics easier to understand.
- **Interactive Web Interface:** Use a simple interface built with Streamlit.
- **Agent-Based Workflow:** Use Agno to connect the language model with YouTube analysis tools.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| Agno | AI agent framework |
| Groq | Language model inference |
| YouTubeTools | Access supported YouTube video content |
| python-dotenv | Local environment variable management |

## 🏗️ Project Structure

```text
YOUTUBE_VIDEO_ANALYSER/
│
├── ui.py                 # Streamlit user interface
├── video_analyser.py     # YouTube analysis agent
├── requirements.txt      # Python dependencies
├── .gitignore            # Files excluded from Git
└── README.md             # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible version supported by your dependencies
- Git
- A Groq API key
- Access to the required YouTube video captions or content

### 1. Clone the repository

```bash
git clone https://github.com/batham04/youtube-video-analyser.git
cd youtube-video-analyser
```

### 2. Create a virtual environment

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use the environment's Python executable directly instead.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get an API key from [Groq Console](https://console.groq.com/).

**Security:** Never commit your `.env` file or expose your API key in source code.

### 5. Run the application

```bash
python -m streamlit run ui.py
```

Open the local URL displayed in your terminal, usually:

`http://localhost:8501`

## 📖 How to Use

1. Open the application.
2. Paste a valid YouTube video URL into the input field.
3. Click **Analyze Video**.
4. Wait for the AI agent to process the available video content.
5. Read the generated summary and insights.

The analysis depends on the video's accessible captions and the capabilities of the configured model and tools.

## ☁️ Deployment

This application is deployed using **Streamlit Community Cloud**.

🌐 **Live Application:** [YouTube Video Analyser](https://batham04-youtube-video-analyser-ui-zzpzl8.streamlit.app/)

To deploy your own instance:

1. Push the project to GitHub.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository.
4. Set `ui.py` as the application entrypoint.
5. Configure `GROQ_API_KEY` in the app's Streamlit Secrets settings.
6. Deploy the application.

## ⚠️ Limitations

- Some YouTube videos may not provide accessible transcripts or captions.
- Very long transcripts may exceed the selected language model's input limits.
- Model availability, API quotas, and rate limits depend on the Groq account and selected model.
- Summary quality depends on the available transcript and model output.
- The application requires an internet connection to access external services.

## 🔮 Future Improvements

- [ ] Add timestamp-based summaries and chapter navigation.
- [ ] Support multiple summary lengths and formats.
- [ ] Add key takeaways and revision questions.
- [ ] Implement transcript chunking for long videos.
- [ ] Add interactive question answering about video content.
- [ ] Support exporting summaries to Markdown or PDF.
- [ ] Improve error handling and user feedback.

## 🔐 Security

- Store API keys in environment variables or Streamlit Secrets.
- Keep `.env`, `.venv/`, and other private files out of Git.
- Never publish API credentials in logs, screenshots, or repository commits.

## 🤝 Contributing

Contributions and suggestions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Commit and push your changes.
5. Open a pull request.

## 👩‍💻 Author

**Vaishnavi Batham**

- GitHub: [@batham04](https://github.com/batham04)
- Project Repository: [youtube-video-analyser](https://github.com/batham04/youtube-video-analyser)

---

If you find this project useful, consider giving the repository a ⭐.

**Built with Python, AI, and Streamlit.**
