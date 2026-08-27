import streamlit as st
from PIL import Image
import time

# ==========================================
# 1. PAGE SETUP & CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="AI Document Screening — Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Manage state for reset functionality and processing simulation
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0
if "has_processed" not in st.session_state:
    st.session_state.has_processed = False
if "last_uploaded_file" not in st.session_state:
    st.session_state.last_uploaded_file = None

# ==========================================
# 2. CUSTOM CSS STYLING
# ==========================================
st.markdown("""
<style>
    /* Header banner styling */
    .header-banner {
        background: linear-gradient(135deg, #0d9488 0%, #0284c7 100%);
        padding: 26px 32px;
        border-radius: 14px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(13, 148, 136, 0.15);
    }
    .header-banner h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 700;
        color: white !important;
    }
    .header-banner p {
        margin: 6px 0 0 0;
        font-size: 1.05rem;
        opacity: 0.92;
        color: #e0f2fe;
    }

    /* Horizontal Step Progress Bar */
    .step-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
        background: #ffffff;
        padding: 14px 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
    }
    .step-item {
        display: flex;
        align-items: center;
        font-size: 0.9rem;
        font-weight: 600;
    }
    .step-active {
        color: #0d9488;
    }
    .step-inactive {
        color: #94a3b8;
    }
    .step-bubble {
        width: 26px;
        height: 26px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 8px;
        font-size: 0.8rem;
    }
    .bubble-active {
        background: #0d9488;
        color: white;
    }
    .bubble-inactive {
        background: #e2e8f0;
        color: #64748b;
    }
    .step-divider {
        flex-grow: 1;
        height: 2px;
        background: #e2e8f0;
        margin: 0 10px;
    }
    .step-divider.active {
        background: #0d9488;
    }

    /* Status Badge */
    .verdict-badge {
        display: inline-block;
        padding: 8px 20px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 1.1rem;
        background-color: #dcfce7;
        color: #15803d;
        border: 1px solid #86efac;
    }

    /* Roadmap & Feature Card Pills */
    .scope-pill {
        display: inline-block;
        background-color: #e0f2fe;
        color: #0369a1;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png", width=64)
    st.title("Document Shield")
    st.caption("AI-Powered Verification Engine")

    st.divider()
    st.markdown("### 🧭 Navigation")
    current_page = st.radio(
        "Select View",
        ["🛡️ Document Screening", "📖 About & Future Scope"],
        label_visibility="collapsed"
    )

    st.divider()

    # Reset button (only active on Screening page)
    if current_page == "🛡️ Document Screening":
        if st.button("🔄 Reset Screening", use_container_width=True, type="secondary"):
            st.session_state.uploader_key += 1
            st.session_state.has_processed = False
            st.session_state.last_uploaded_file = None
            st.rerun()

    st.caption("Version 1.0.0 • Architecture Prototype")

# ==========================================
# 4. PAGE 1: DOCUMENT SCREENING
# ==========================================
if current_page == "🛡️ Document Screening":

    # Header Banner
    st.markdown("""
    <div class="header-banner">
        <h1>🛡️ AI Document Screening</h1>
        <p>Automated verification, tampering detection, and identity risk assessment</p>
    </div>
    """, unsafe_allow_html=True)

    # File Uploader
    uploaded_file = st.file_uploader(
        "Upload a document image (passport, visa, or ID)",
        type=["jpg", "jpeg", "png"],
        key=f"doc_uploader_{st.session_state.uploader_key}"
    )

    is_uploaded = uploaded_file is not None

    # Horizontal Step-Progress Indicator
    steps = [
        ("1", "Upload"),
        ("2", "OCR"),
        ("3", "Validation"),
        ("4", "Tampering Check"),
        ("5", "Face Match"),
        ("6", "Risk Score")
    ]

    step_html_items = []
    for i, (num, name) in enumerate(steps):
        active = is_uploaded or (i == 0)
        bubble_class = "bubble-active" if active else "bubble-inactive"
        text_class = "step-active" if active else "step-inactive"
        
        item = f'''
        <div class="step-item {text_class}">
            <div class="step-bubble {bubble_class}">{num}</div>
            <span>{name}</span>
        </div>
        '''
        step_html_items.append(item)

    progress_bar_html = '<div class="step-container">'
    for idx, item in enumerate(step_html_items):
        progress_bar_html += item
        if idx < len(step_html_items) - 1:
            div_class = "step-divider active" if is_uploaded else "step-divider"
            progress_bar_html += f'<div class="{div_class}"></div>'
    progress_bar_html += '</div>'

    st.markdown(progress_bar_html, unsafe_allow_html=True)

    # Main Content Area
    if is_uploaded:
        image = Image.open(uploaded_file)
        width, height = image.size
        file_size_kb = uploaded_file.size / 1024

        # Simulated Processing Spinner
        if st.session_state.last_uploaded_file != uploaded_file.name:
            with st.spinner("Analyzing document structure & executing pipeline checks..."):
                time.sleep(0.8)
            st.session_state.has_processed = True
            st.session_state.last_uploaded_file = uploaded_file.name

        # Side-by-Side Image Preview & Metadata
        st.subheader("📄 Uploaded Document Overview")
        col_img, col_info = st.columns([1.2, 1], gap="large")

        with col_img:
            st.image(
                image,
                caption=f"Document Preview: {uploaded_file.name}",
                use_container_width=True
            )

        with col_info:
            st.markdown("#### 📊 File Metadata")
            st.text_input("File Name", value=uploaded_file.name, disabled=True)

            m1, m2 = st.columns(2)
            with m1:
                st.metric(label="File Size", value=f"{file_size_kb:.1f} KB")
            with m2:
                st.metric(label="Resolution", value=f"{width} × {height} px")

            m3, m4 = st.columns(2)
            with m3:
                st.metric(label="Format", value=image.format or "JPEG/PNG")
            with m4:
                st.metric(label="Color Mode", value=image.mode)

            st.success("✅ Image loaded and verified successfully.")

        st.divider()

        # Pipeline Step Cards
        st.subheader("⚙️ Verification Pipeline Stages")

        # Step 1: OCR
        with st.container(border=True):
            c_left, c_right = st.columns([3, 1])
            with c_left:
                st.markdown("#### 📄 OCR Results (Text Extraction)")
                st.caption("Extracts key fields: Full Name, Document Number, Date of Birth, Expiration Date.")
            with c_right:
                st.badge("Coming Soon", icon="⏳")
            st.info("💡 OCR engine integration will extract and map all document key-value pairs here.")

        # Step 2: Rule Validation
        with st.container(border=True):
            c_left, c_right = st.columns([3, 1])
            with c_left:
                st.markdown("#### ✅ Rule Validation")
                st.caption("Validates machine-readable zones (MRZ), date logic, checksums, and required standard formats.")
            with c_right:
                st.badge("Coming Soon", icon="⏳")
            st.info("💡 Business rules & compliance validation algorithms will run here.")

        # Step 3: Tampering Check
        with st.container(border=True):
            c_left, c_right = st.columns([3, 1])
            with c_left:
                st.markdown("#### 🔍 Tampering & Forgery Check")
                st.caption("Analyzes noise patterns, font inconsistencies, pixel compression artifacts, and digital splicing.")
            with c_right:
                st.badge("Coming Soon", icon="⏳")
            st.info("💡 Deep learning computer vision model for anti-spoofing will be embedded here.")

        # Step 4: Face Match
        with st.container(border=True):
            c_left, c_right = st.columns([3, 1])
            with c_left:
                st.markdown("#### 🙂 Face Match")
                st.caption("Biometric facial embedding comparison between portrait photo and live selfie / database.")
            with c_right:
                st.badge("Coming Soon", icon="⏳")
            st.info("💡 Facial recognition and similarity scoring model will display comparison metrics here.")

        st.divider()

        # Final Results Report Card
        st.subheader("📑 Final Screening Report")

        with st.container(border=True):
            col_verdict, col_score = st.columns([1.5, 1], gap="medium")

            with col_verdict:
                st.markdown("### Risk Verdict")
                st.markdown(
                    '<div class="verdict-badge">🟢 SAFE — LOW RISK</div>',
                    unsafe_allow_html=True
                )
                st.write("")
                st.caption("All preliminary structural integrity and format checks passed successfully.")

            with col_score:
                st.markdown("### Risk Score")
                st.markdown("## **98 / 100**")
                st.caption("Confidence Level: **High (98.4%)**")

            st.markdown("#### 📋 Pipeline Verification Matrix")
            
            summary_data = [
                {"Check": "Image Upload & Decoding", "Status": "Passed", "Indicator": "✅ Pass"},
                {"Check": "OCR Text Extraction", "Status": "Ready for Model", "Indicator": "⏳ Placeholder"},
                {"Check": "Rule & Format Validation", "Status": "Ready for Rules", "Indicator": "⏳ Placeholder"},
                {"Check": "Digital Tampering Detection", "Status": "Ready for Model", "Indicator": "⏳ Placeholder"},
                {"Check": "Biometric Face Match", "Status": "Ready for Model", "Indicator": "⏳ Placeholder"},
            ]
            st.table(summary_data)

        # Celebration animation
        st.balloons()

    else:
        st.info("👆 **Get started**: Upload a document image (Passport, Visa, or ID) above to preview the screening pipeline.")

# ==========================================
# 5. PAGE 2: ABOUT & FUTURE SCOPE
# ==========================================
else:
    # About Header Banner
    st.markdown("""
    <div class="header-banner">
        <h1>📖 About Document Shield & Future Scope</h1>
        <p>Explore what our AI document screening system does and discover our technology roadmap</p>
    </div>
    """, unsafe_allow_html=True)

    tab_about, tab_scope, tab_use_cases = st.tabs([
        "💡 What Our App Does",
        "🚀 Future Scopes & Roadmap",
        "🏢 Target Industry Use Cases"
    ])

    # Tab 1: What Our App Does
    with tab_about:
        st.subheader("Mission & Core Capabilities")
        st.write(
            "**Document Shield** is an automated, AI-driven identity verification and fraud prevention platform. "
            "It is designed to inspect, validate, and verify official identification documents (such as passports, "
            "visas, driver's licenses, and national ID cards) in real-time."
        )

        st.divider()
        st.markdown("### 🧩 The 5 Core Verification Pillars")

        c1, c2 = st.columns(2)

        with c1:
            with st.container(border=True):
                st.markdown("#### 1. 🔍 High-Precision OCR & Parsing")
                st.write(
                    "Converts raw document pixels into structured, verifiable JSON data. "
                    "Extracts Machine Readable Zones (MRZ lines), Visual Inspection Zones (VIZ), "
                    "and 2D PDF417/QR barcodes with sub-second latency."
                )

            with st.container(border=True):
                st.markdown("#### 3. 🛡️ Forensic Tampering & Splicing Detection")
                st.write(
                    "Employs deep convolutional neural networks and error level analysis (ELA) "
                    "to spot altered numbers, copied fonts, Photoshop artifacts, and synthetic AI-generated portraits."
                )

        with c2:
            with st.container(border=True):
                st.markdown("#### 2. 📐 Comprehensive Rule & Expiry Logic")
                st.write(
                    "Applies international ICAO 9303 checksum checks, calculates expiration dates, "
                    "detects under-age applicants, and validates issuing state codes and security formats."
                )

            with st.container(border=True):
                st.markdown("#### 4. 👤 Biometric Facial Match")
                st.write(
                    "Extracts facial feature embeddings from the document portrait and compares them against "
                    "live selfie scans or government records with enterprise-grade cosine similarity thresholds."
                )

        with st.container(border=True):
            st.markdown("#### 5. 🎯 Dynamic Risk Scoring & Verdict Engine")
            st.write(
                "Aggregates signals from all upstream checks to compute a composite risk score (0–100) and provides "
                "an actionable verdict: **Safe (Pass)**, **Needs Manual Review**, or **Flagged (High Risk)**."
            )

    # Tab 2: Future Scopes & Roadmap
    with tab_scope:
        st.subheader("🚀 Technology Roadmap & Future Scopes")
        st.write(
            "Here is how Document Shield is planned to evolve from prototype to an enterprise-scale fraud prevention network:"
        )

        col_s1, col_s2 = st.columns(2)

        with col_s1:
            with st.container(border=True):
                st.markdown('<span class="scope-pill">Phase 2 — In Progress</span>', unsafe_allow_html=True)
                st.markdown("#### 🧠 Multi-Modal Vision-Language Models (VLMs)")
                st.write(
                    "Integrating state-of-the-art vision models for reasoning over complex layout anomalies, "
                    "watermark authentication, and multi-lingual document translation across 50+ languages."
                )

            with st.container(border=True):
                st.markdown('<span class="scope-pill">Phase 3 — Q3 Roadmap</span>', unsafe_allow_html=True)
                st.markdown("#### 📱 Mobile Liveness & Anti-Deepfake Defense")
                st.write(
                    "Adding interactive 3D passive liveness detection to block presentation attacks such as "
                    "printed masks, screen replays, and real-time deepfake video injection."
                )

            with st.container(border=True):
                st.markdown('<span class="scope-pill">Phase 4 — Q4 Roadmap</span>', unsafe_allow_html=True)
                st.markdown("#### 📡 NFC e-Passport Chip Cryptographic Auth")
                st.write(
                    "Direct cryptographic reading of contactless RFID/NFC chips embedded inside modern e-passports "
                    "for zero-fraud, tamper-proof government signature verification."
                )

        with col_s2:
            with st.container(border=True):
                st.markdown('<span class="scope-pill">Phase 5 — Upcoming</span>', unsafe_allow_html=True)
                st.markdown("#### 🌐 Global Watchlist, PEP & Sanctions Screening")
                st.write(
                    "Instant automated screening against Interpol, OFAC, AML compliance lists, and Politically Exposed "
                    "Persons (PEP) databases with real-time audit logging."
                )

            with st.container(border=True):
                st.markdown('<span class="scope-pill">Phase 6 — Upcoming</span>', unsafe_allow_html=True)
                st.markdown("#### 🔒 Zero-Knowledge Privacy & PII Redaction")
                st.write(
                    "Automated client-side and in-transit redaction of sensitive identifiers (SSN, national tax IDs) "
                    "to ensure full compliance with GDPR, HIPAA, and SOC2 regulations."
                )

            with st.container(border=True):
                st.markdown('<span class="scope-pill">Enterprise Scale</span>', unsafe_allow_html=True)
                st.markdown("#### ⚡ Batch Processing & Asynchronous Webhooks")
                st.write(
                    "High-throughput REST and gRPC endpoints capable of processing 10,000+ documents per minute "
                    "with real-time event webhooks for enterprise backends."
                )

    # Tab 3: Target Industry Use Cases
    with tab_use_cases:
        st.subheader("🏢 Where This Is Used")
        
        u1, u2, u3 = st.columns(3)
        with u1:
            with st.container(border=True):
                st.markdown("#### 💳 FinTech & Banking")
                st.write(
                    "Instant customer KYC onboarding, preventing loan identity theft, "
                    "and automated AML compliance."
                )
        with u2:
            with st.container(border=True):
                st.markdown("#### ✈️ Travel & Hospitality")
                st.write(
                    "Automated visa and passport pre-checks for airlines, hotel check-ins, "
                    "and border management portals."
                )
        with u3:
            with st.container(border=True):
                st.markdown("#### 🤝 Gig Economy & Sharing")
                st.write(
                    "Driver license checks for rideshare platforms, host verification, "
                    "and secure age verification."
                )
