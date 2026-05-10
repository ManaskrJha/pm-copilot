import streamlit as st
import google.generativeai as genai

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PM Copilot · PRD Generator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

*, *::before, *::after { box-sizing: border-box; }
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background: #08080f;
    color: #e2e0f0;
}
.stApp { background: #08080f; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 2.5rem 4rem; max-width: 1280px; }

.hero {
    padding: 3rem 0 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero::after {
    content: '';
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 800px; height: 400px;
    background: radial-gradient(ellipse at center top, rgba(124,58,237,0.12) 0%, transparent 65%);
    pointer-events: none;
    z-index: 0;
}
.hero-inner { position: relative; z-index: 1; }
.pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(124,58,237,0.12);
    border: 1px solid rgba(124,58,237,0.3);
    color: #a78bfa;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 0.3rem 0.9rem;
    border-radius: 100px;
    margin-bottom: 1.5rem;
}
.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.2rem, 4.5vw, 3.5rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.03em;
    color: #f0eeff;
    margin-bottom: 1rem;
}
.hero h1 em {
    font-style: normal;
    background: linear-gradient(135deg, #a78bfa 0%, #60a5fa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 1rem;
    color: #7c7898;
    font-weight: 300;
    max-width: 480px;
    margin: 0 auto 2rem;
    line-height: 1.7;
}
.stats {
    display: flex;
    justify-content: center;
    gap: 0.6rem;
    flex-wrap: wrap;
    margin-bottom: 2.5rem;
}
.stat-chip {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 100px;
    padding: 0.35rem 1rem;
    font-size: 0.8rem;
    color: #9d9ab0;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
}
.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #4a4560;
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.05);
}
.card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 1.6rem;
    margin-bottom: 1rem;
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #6b6480;
    margin-bottom: 1.1rem;
}
.api-card {
    background: rgba(124,58,237,0.06);
    border: 1px solid rgba(124,58,237,0.2);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.5rem;
}
.api-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 0.5rem;
}
.api-hint {
    font-size: 0.8rem;
    color: #6b6480;
    margin-bottom: 0.8rem;
    line-height: 1.5;
}
.api-hint a { color: #a78bfa; text-decoration: none; }
.stTextArea textarea {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 10px !important;
    color: #e2e0f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.93rem !important;
    line-height: 1.65 !important;
    padding: 0.9rem 1rem !important;
}
.stTextArea textarea:focus {
    border-color: rgba(124,58,237,0.45) !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.08) !important;
    outline: none !important;
}
.stTextInput input {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 10px !important;
    color: #e2e0f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.92rem !important;
    padding: 0.65rem 1rem !important;
}
.stTextInput input:focus {
    border-color: rgba(124,58,237,0.45) !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.08) !important;
}
.stSelectbox > div > div {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 10px !important;
    color: #e2e0f0 !important;
}
label, .stSelectbox label {
    color: #7c7898 !important;
    font-size: 0.85rem !important;
    font-weight: 400 !important;
}
.stRadio > div {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 0.5rem !important;
}
.stRadio > div > label {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 8px !important;
    padding: 0.5rem 1rem !important;
    color: #9d9ab0 !important;
    font-size: 0.85rem !important;
}
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #7c3aed 0%, #4338ca 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.9rem 2rem !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.96rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    box-shadow: 0 4px 20px rgba(124,58,237,0.3) !important;
    transition: all 0.2s !important;
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(124,58,237,0.45) !important;
}
.empty-state {
    background: rgba(124,58,237,0.04);
    border: 1px dashed rgba(124,58,237,0.2);
    border-radius: 16px;
    padding: 3.5rem 2rem;
    text-align: center;
}
.empty-icon { font-size: 2.5rem; margin-bottom: 1rem; }
.empty-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    color: #4a4560;
    margin-bottom: 0.5rem;
}
.empty-sub { font-size: 0.83rem; color: #3a3550; line-height: 1.6; }
.preview-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.65rem 0.9rem;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 9px;
    margin-bottom: 0.45rem;
}
.preview-title { font-size: 0.86rem; color: #c4c0d8; font-weight: 500; }
.preview-desc { font-size: 0.76rem; color: #4a4560; margin-top: 0.1rem; }
.prd-wrapper {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 2rem;
}
.prd-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 1.2rem;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 1.5rem;
}
.prd-top-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #f0eeff;
}
.prd-status {
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.25);
    color: #4ade80;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.28rem 0.7rem;
    border-radius: 100px;
}
div[data-testid="stDownloadButton"] > button {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 9px !important;
    color: #9d9ab0 !important;
    font-size: 0.85rem !important;
    transition: all 0.2s !important;
}
.hr {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(124,58,237,0.25), transparent);
    margin: 1.5rem 0;
}
.footer {
    text-align: center;
    padding: 2rem 0 1rem;
    font-size: 0.8rem;
    color: #3a3550;
}
.footer a { color: #6b6480; text-decoration: none; }
.footer a:hover { color: #a78bfa; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-inner">
    <div class="pill">⚡ AI-Powered PRD Generator</div>
    <h1>Your <em>PM Copilot</em><br/>thinks before it writes</h1>
    <p class="hero-sub">Answer smart questions about your product. Get a senior-PM-quality PRD — structured, specific, and ready to ship.</p>
    <div class="stats">
      <span class="stat-chip">🎯 8 PRD sections</span>
      <span class="stat-chip">⚡ Under 30 seconds</span>
      <span class="stat-chip">🔒 Your key, your data</span>
      <span class="stat-chip">📥 Download as Markdown</span>
    </div>
  </div>
</div>
<div class="hr"></div>
""", unsafe_allow_html=True)

# ── Layout ────────────────────────────────────────────────────────────────────
left, right = st.columns([1.05, 0.95], gap="large")

with left:

    # API Key
    st.markdown('<div class="api-card">', unsafe_allow_html=True)
    st.markdown('<div class="api-card-title">🔑 Gemini API Key</div>', unsafe_allow_html=True)
    st.markdown('<div class="api-hint">Free from <a href="https://aistudio.google.com" target="_blank">aistudio.google.com</a> → Get API Key → Create API Key. Takes 2 minutes.</div>', unsafe_allow_html=True)
    api_key = st.text_input("API Key", type="password", placeholder="Paste your Gemini API key here...", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    # Section 1
    st.markdown('<div class="section-label">01 · The Problem</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="card-title">🎯 What problem are you solving?</div>', unsafe_allow_html=True)
    problem = st.text_area("Problem", placeholder="Describe the core problem in 2-3 sentences. Be specific — what's broken, who's affected, and what's the impact?\n\nExample: Our mobile banking app loses 60% of users during KYC onboarding. Users abandon when asked to upload multiple documents. This costs us ₹40L/month in lost activations.", height=130, label_visibility="collapsed")
    c1, c2 = st.columns(2)
    with c1:
        product_type = st.selectbox("Product type", ["Mobile App", "Web App", "B2B SaaS / Platform", "API Product", "Marketplace", "FinTech / Banking", "E-commerce", "Internal Tool", "Other"])
    with c2:
        stage = st.selectbox("Product stage", ["0→1 (New product)", "1→10 (Early growth)", "10→100 (Scaling)", "Mature (Optimising)"])
    st.markdown('</div>', unsafe_allow_html=True)

    # Section 2
    st.markdown('<div class="section-label">02 · The Users</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="card-title">👥 Who are you building for?</div>', unsafe_allow_html=True)
    primary_user = st.text_input("Primary user", placeholder="e.g. First-time borrowers aged 22-35 in Tier 2 cities with no credit history")
    user_pain = st.text_area("What's their biggest frustration today?", placeholder="e.g. They find the KYC process confusing and time-consuming. They don't understand why they need to upload so many documents and give up halfway.", height=90)
    user_goal = st.text_input("What does the user ultimately want to achieve?", placeholder="e.g. Get a personal loan approved quickly without visiting a branch")
    st.markdown('</div>', unsafe_allow_html=True)

    # Section 3
    st.markdown('<div class="section-label">03 · Success & Constraints</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="card-title">📊 How will you know it worked?</div>', unsafe_allow_html=True)
    success_metric = st.text_input("Primary success metric", placeholder="e.g. Increase KYC completion rate from 40% to 70% within 3 months")
    current_baseline = st.text_input("Current baseline (if known)", placeholder="e.g. Current completion rate is 40%, 3000 users drop off per week")
    c3, c4 = st.columns(2)
    with c3:
        timeline = st.text_input("Timeline", placeholder="e.g. 6-week sprint, launch by Q2")
    with c4:
        team_size = st.selectbox("Engineering bandwidth", ["Solo / 1 engineer", "Small (2-3 engineers)", "Medium (4-6 engineers)", "Large (7+ engineers)"])
    constraints = st.text_area("Key constraints or non-negotiables", placeholder="e.g. Must comply with RBI KYC guidelines. Cannot remove Aadhaar verification step. No backend changes in Sprint 1.", height=80)
    st.markdown('</div>', unsafe_allow_html=True)

    # Section 4
    st.markdown('<div class="section-label">04 · Context</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="card-title">🧠 Help the AI think deeper</div>', unsafe_allow_html=True)
    solutions_tried = st.text_area("What have you already tried? (optional)", placeholder="e.g. We simplified the UI in Q3 — helped slightly but didn't solve the core drop-off. We tried removing one document requirement but compliance blocked it.", height=75)
    hypothesis = st.text_input("What's your hypothesis for why this problem exists?", placeholder="e.g. Users don't understand why we need each document — better explanation might reduce abandonment")
    c5, c6 = st.columns(2)
    with c5:
        competitors = st.text_input("Competitors doing this well?", placeholder="e.g. Airtel Payments Bank, Jupiter")
    with c6:
        prd_depth = st.radio("PRD depth", ["Quick", "Standard", "Deep Dive"], index=1, horizontal=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
    generate = st.button("⚡ Generate PRD", type="primary", use_container_width=True)


# ── Right Column ──────────────────────────────────────────────────────────────
with right:

    if not generate:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">📄</div>
            <div class="empty-title">Your PRD will appear here</div>
            <div class="empty-sub">Fill in the questions on the left<br/>and click Generate PRD</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div style="height:1.5rem"></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-label">What you\'ll get</div>', unsafe_allow_html=True)

        for emoji, title, desc in [
            ("🎯", "Problem Statement", "Structured & refined from your input"),
            ("👥", "User Personas", "2-3 detailed personas with context"),
            ("📋", "User Stories", "6-8 MoSCoW-prioritised stories"),
            ("📊", "Success Metrics", "Primary, secondary & guardrail KPIs"),
            ("💡", "Proposed Solutions", "3 options with pros, cons & effort"),
            ("🚫", "Out of Scope", "Clear boundaries to prevent scope creep"),
            ("⚠️", "Risks & Edge Cases", "5+ risks with mitigation strategies"),
            ("❓", "Open Questions", "Blockers with owners & deadlines"),
        ]:
            st.markdown(f"""<div class="preview-item"><span style="font-size:1rem">{emoji}</span><div><div class="preview-title">{title}</div><div class="preview-desc">{desc}</div></div></div>""", unsafe_allow_html=True)

    if generate:
        errors = []
        if not api_key: errors.append("Please enter your Gemini API Key")
        if not problem: errors.append("Please describe the problem you're solving")
        if not primary_user: errors.append("Please describe your primary user")
        if not success_metric: errors.append("Please define your success metric")

        if errors:
            for e in errors: st.error(f"⚠️ {e}")
        else:
            depth_map = {
                "Quick": "Be concise. 2-3 bullet points per section. Focus only on the most critical insights.",
                "Standard": "Provide balanced detail. 4-6 bullet points per section. Enough for an engineering team to understand and act.",
                "Deep Dive": "Be comprehensive. 6-10 bullet points per section. Include nuanced edge cases, strategic trade-offs, and second-order effects. Think like a Principal PM with 10+ years experience."
            }

            context = f"""
PRODUCT PROBLEM: {problem}
PRODUCT TYPE: {product_type} | STAGE: {stage}
PRIMARY USER: {primary_user}
USER FRUSTRATION: {user_pain or 'Not specified'}
USER GOAL: {user_goal or 'Not specified'}
SUCCESS METRIC: {success_metric}
CURRENT BASELINE: {current_baseline or 'Not specified'}
TIMELINE: {timeline or 'Not specified'} | ENGINEERING: {team_size}
CONSTRAINTS: {constraints or 'None'}
WHAT'S BEEN TRIED: {solutions_tried or 'Nothing specified'}
ROOT CAUSE HYPOTHESIS: {hypothesis or 'Not specified'}
COMPETITORS: {competitors or 'None specified'}
"""

            prompt = f"""
You are a Principal Product Manager with 12+ years experience at Stripe, Razorpay, Google, and CRED. You write PRDs that are brutally clear, deeply empathetic, and immediately actionable.

{context}

DEPTH: {depth_map[prd_depth]}

RULES:
- Be specific. Never write "improve user experience" without saying exactly what and by how much.
- Use numbers wherever possible.
- Every bullet must add value. No filler.
- Respect the constraints given.
- Write so a new engineer joining tomorrow can understand completely.

Generate EXACTLY these 8 sections:

## 🎯 Problem Statement
- **Core Problem:** One sentence. What is fundamentally broken.
- **Who Is Affected:** Specific user segment, frequency, scale of impact.
- **Business Impact:** Quantify the cost (revenue, churn, time).
- **Why Now:** Urgency. What happens if we don't solve this.
- **Root Cause Hypothesis:** What's likely causing this based on context.

## 👥 User Personas
2-3 distinct personas. For EACH:
- **Name & Profile:** Realistic name, age, occupation
- **Their Situation:** How they encounter this problem
- **Primary Goal:** One sentence
- **Frustrations:** 2-3 specific pain points
- **What Success Looks Like:** Perfect experience for them
- **Product Implication:** How this persona shapes our decisions

## 📋 User Stories
7-8 stories. Format: "As a [persona], I want to [action] so that [benefit]"
Label each: 🔴 Must Have | 🟡 Should Have | 🟢 Nice to Have
Then: **Acceptance Criteria** for top 3 Must-Haves.

## 📊 Success Metrics
- **North Star Metric:** The one number defining success.
- **Primary Metrics:** Current baseline → Target → How to measure
- **Secondary Metrics:** Supporting indicators
- **Guardrail Metrics:** Must NOT worsen
- **Anti-Metrics:** What we explicitly don't optimise for

## 💡 Proposed Solutions
3 options from minimal to comprehensive. For EACH:
- Approach name + what it is
- How it works (2-3 sentences)
- Pros (3), Cons (3)
- Effort: Low/Medium/High | Timeline estimate
- ✅ Recommended / ⚠️ Conditional / ❌ Not recommended — one line why
End with: **Recommended Approach** and reasoning.

## 🚫 Out of Scope
5 exclusions. For each: What + Why + When (if revisited)

## ⚠️ Risks & Edge Cases
6 risks. For each:
- Risk description
- Likelihood: 🔴 High / 🟡 Medium / 🟢 Low
- Impact: 🔴 High / 🟡 Medium / 🟢 Low
- Mitigation strategy
- Owner

## ❓ Open Questions
5-6 questions. For each:
- The question
- Why it matters
- Owner (Engineering/Design/Legal/Data/Leadership)
- Deadline (Before Sprint 1 / Before Launch / Post-Launch)
- Current best guess

End with a **PM's Note** — one paragraph personal take on the biggest risk or opportunity.
"""

            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-1.5-flash")

                with st.spinner("Generating your PRD..."):
                    response = model.generate_content(prompt)
                    prd_text = response.text

                st.markdown('<div class="prd-wrapper"><div class="prd-top"><div class="prd-top-title">📄 Generated PRD</div><div class="prd-status">✓ Ready to share</div></div></div>', unsafe_allow_html=True)
                st.markdown(prd_text)
                st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

                dc1, dc2 = st.columns(2)
                with dc1:
                    st.download_button("📥 Download TXT", data=prd_text, file_name="PRD.txt", mime="text/plain", use_container_width=True)
                with dc2:
                    st.download_button("📄 Download Markdown", data=f"# PRD\n\n*Generated by PM Copilot*\n\n---\n\n{prd_text}", file_name="PRD.md", mime="text/markdown", use_container_width=True)

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}\n\nCheck your API key and try again.")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    Built by <a href="https://www.linkedin.com/in/manas-kumar-jha16/" target="_blank">Manas Kumar Jha</a>
    &nbsp;·&nbsp;
    <a href="https://www.notion.so/Manas-Kumar-Jha-aa9496ee7d3082b6b935810bcf2bd1c3" target="_blank">Portfolio</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/ManaskrJha" target="_blank">GitHub</a>
    &nbsp;·&nbsp; PM Copilot v2.0
</div>
""", unsafe_allow_html=True)
