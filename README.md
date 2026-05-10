# ⚡ PM Copilot — AI-Powered PRD Generator

> Turn your product problem into a structured, senior-PM-quality PRD in under 30 seconds.

![PM Copilot](https://img.shields.io/badge/Built%20with-Gemini%20LLM-purple?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🎯 The Problem

Writing PRDs is one of the biggest time sinks for product teams.

A good PRD requires:
- Structured problem definition
- User personas and stories
- Success metrics with baselines
- Solution trade-offs
- Risk assessment
- Open questions with owners

Most PMs spend 2-4 hours on a single PRD. A lot of that time is structure and formatting — not actual thinking.

**PM Copilot handles the structure. You focus on the thinking.**

---

## 🚀 What It Does

PM Copilot takes structured product inputs and generates a full PRD including:

| Section | What you get |
|---|---|
| 🎯 Problem Statement | Refined, structured, with root cause hypothesis |
| 👥 User Personas | 2-3 detailed personas with goals and frustrations |
| 📋 User Stories | 6-8 MoSCoW-prioritised stories with acceptance criteria |
| 📊 Success Metrics | Primary, secondary, and guardrail KPIs with baselines |
| 💡 Proposed Solutions | 3 options with pros, cons, effort, and recommendation |
| 🚫 Out of Scope | Clear boundaries to prevent scope creep |
| ⚠️ Risks & Edge Cases | 6 risks with likelihood, impact, and mitigation |
| ❓ Open Questions | 5-6 blockers with owners and deadlines |

---

## 🖥️ Demo

**Input:**
> "Our mobile banking app loses 60% of users during KYC onboarding. Users abandon when asked to upload multiple documents."

**Output:** A complete 8-section PRD in under 30 seconds — ready to share with your engineering team.

---

## 🛠️ Tech Stack

- **LLM:** Google Gemini 1.5 Flash
- **UI:** Streamlit
- **Deployment:** Docker + Google Kubernetes Engine (GKE)
- **Language:** Python 3.9+

---

## ⚙️ Setup & Run Locally

### Prerequisites
- Python 3.9+
- Google Gemini API key (free from [aistudio.google.com](https://aistudio.google.com))

### Installation

```bash
# Clone the repo
git clone https://github.com/ManaskrJha/pm-copilot.git
cd pm-copilot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Add your API key
When the app opens, paste your Gemini API key in the input field on the main page.

Get your free key at [aistudio.google.com](https://aistudio.google.com) → Get API Key → Create API Key.

---

## 🚀 Deploy on Streamlit Cloud (Free)

1. Fork this repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. In **Advanced Settings → Secrets** add:
```toml
GEMINI_API_KEY = "your_actual_key_here"
```
5. Deploy — live in 2 minutes

---

## 📁 Project Structure

---

## 💡 How to Use

1. Enter your **Gemini API key** in the input field
2. Describe your **product problem** in 2-3 sentences
3. Fill in **user context**, **success metrics**, and **constraints**
4. Choose your **PRD depth** — Quick, Standard, or Deep Dive
5. Click **Generate PRD**
6. Download as TXT or Markdown

---

## 🧠 Why I Built This

I'm a product professional working on B2B enterprise products in FinTech. PRD writing was consistently the most time-consuming part of my workflow — not because the thinking was hard, but because the structure took forever.

I wanted a tool that handles the scaffolding so I could focus on the actual product decisions — the trade-offs, the user empathy, the prioritization.

PM Copilot is that tool. It's opinionated, structured, and built for PMs who think deeply about problems.

---

## 📄 License

MIT — free to use, modify, and distribute.

---


