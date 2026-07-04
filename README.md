# 📊 AI Financial Research Assistant

An AI-powered financial research system built with **CrewAI**, **SerpAPI**, and Large Language Models (LLMs). The project automates company research by combining multiple AI agents that gather real-time information, analyze financial data, and generate a comprehensive research report.

Instead of manually collecting information from multiple sources, the AI agents collaborate to perform research and produce a structured report that can assist investors, analysts, or students.

---

# ✨ Features

* 🤖 Multi-agent workflow using CrewAI
* 🌐 Real-time company research using SerpAPI
* 📈 Financial analysis of companies
* 📝 Automatically generates a Markdown report
* 🔄 Sequential agent collaboration
* ⚡ Easy to configure using YAML
* 📂 Saves reports automatically

---

# 🛠 Tech Stack

* Python
* CrewAI
* CrewAI Tools
* SerpAPI
* OpenAI / Groq Compatible LLM
* Python Dotenv
* Pydantic

---

# 📂 Project Structure

```text
financial-researcher/
│
├── main.py
├── crew.py
├── requirements.txt
├── README.md
├── .env
│
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
│
└── output/
    └── report.md
```

---

# 🧠 Architecture

```text
                  User
                    │
                    ▼
             Financial Research Crew
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
 Research Agent          Analysis Agent
        │                       │
        ▼                       ▼
   SerpAPI Search        Financial Analysis
        │                       │
        └───────────┬───────────┘
                    ▼
        Generate Markdown Report
                    │
                    ▼
          output/report.md
```

---

# 🚀 Workflow

1. The user provides a company name.
2. The **Research Agent** searches the web for the latest information using SerpAPI.
3. The **Analysis Agent** evaluates the research and prepares a detailed financial analysis.
4. The final report is generated and saved as `output/report.md`.

---

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/Zenitsu1Codes/CrewAI-Financial-Research-Assistant.git

cd CrewAI-Financial-Research-Assistant
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key

SERPAPI_API_KEY=your_serpapi_api_key

OPENAI_MODEL=gpt-4o-mini
```

If you are using Groq through an OpenAI-compatible endpoint:

```env
OPENAI_API_BASE=https://api.groq.com/openai/v1
```

---

# ▶️ Usage

Run the application:

```bash
python main.py
```

Example input:

```python
inputs = {
    "company": "Asian Paints"
}
```

The generated report will be saved to:

```text
output/report.md
```

---

# 📄 Example Report

The generated report may include:

* Company Overview
* Business Model
* Financial Performance
* Recent News
* Competitive Analysis
* Growth Opportunities
* Risks
* Investment Outlook
* Final Recommendation

---

# 📚 Learning Outcomes

This project demonstrates:

* Multi-Agent AI Systems
* CrewAI Framework
* Web Research Automation
* Financial Analysis using LLMs
* Prompt Engineering
* YAML-based Agent Configuration
* Sequential Task Execution
* Automated Report Generation

---

# 🔮 Future Improvements

* Stock price visualization
* Financial ratio analysis
* Yahoo Finance integration
* SEC filing analysis
* PDF report export
* Email report delivery
* Multi-company comparison
* Interactive Streamlit dashboard

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Harsh Asarsa**

AI • Python • CrewAI • Financial AI • Automation

If you found this project useful, consider giving it a ⭐ on GitHub.
