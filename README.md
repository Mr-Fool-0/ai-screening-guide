# AI-Based Fake Identity & Document Screening System

A beginner-built prototype that automatically checks identity and travel
documents (passports, visas, national IDs) for tampering and verifies that
the document photo matches the person presenting it — built for the
**Ministry of Home Affairs / Sashastra Seema Bal (SSB), Police II Division**
problem statement on border checkpoint document screening.

> Status: 🚧 Skeleton stage — UI and pipeline structure are built; the
> real OCR / tampering / face-matching logic is being added step by step.
> See [Roadmap](#roadmap) below.

---

## What this project does

Border checkpoints check thousands of documents a day, mostly by hand. This
app aims to speed that up by automatically:

1. Reading the text on a document (OCR)
2. Checking that dates and formats look valid
3. Checking the image for signs of tampering
4. Comparing the document photo to the person's face
5. Combining all of this into one simple risk score: **Safe / Needs Review / Flagged**

## Demo

Run the app locally and upload any passport/visa/ID image to see the
current skeleton flow (upload → view → placeholder results for each step).

## Tech stack

| Purpose | Tool |
|---|---|
| App interface | [Streamlit](https://streamlit.io) |
| Programming language | Python 3 |
| Reading text from images | Tesseract OCR (`pytesseract`) |
| Image processing / tampering checks | OpenCV |
| Face comparison | `face_recognition` |
| Image handling | Pillow |

## Project structure

```
.
├── app.py                   # Main Streamlit app
├── requirements.txt         # Python dependencies
├── .streamlit/
│   └── config.toml          # Custom theme settings
└── README.md                # You are here
```

## Getting started

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> Note: `pytesseract` and `face_recognition` also need system-level
> installs (Tesseract OCR binary, and `cmake`/`dlib` for face_recognition).
> If installation fails, search "install tesseract [your OS]" or
> "install face_recognition [your OS]" for a quick guide.

### 4. Run the app
```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`.

## Roadmap

This project follows a 6-week, milestone-based build plan:

| Milestone | What it proves |
|---|---|
| 1. Skeleton app | Upload and display an image |
| 2. Text comes out | OCR extracts and shows text |
| 3. Rules run | Basic validation (e.g. expiry date check) |
| 4. Tamper check runs | Flags at least one type of image tampering |
| 5. Face check runs | Compares two photos, shows a match % |
| 6. Full pipeline + score | All checks combine into one risk verdict |

Full details, diagrams, and a week-by-week learning plan are in the project
roadmap document (`AI_Document_Screening_Roadmap.pdf`).

## Team

| Role | Responsibility |
|---|---|
| OCR & data extraction | Extracts text fields from document images |
| Tampering detection | Detects signs of digital or physical editing |
| Face verification | Matches document photo to the presented person |
| App & coordination | Builds the UI, connects modules, leads the team |

## Limitations (current stage)

- This is a learning/prototype project, not a certified security system
- Tampering detection currently covers basic, common forgery patterns only
- Face matching accuracy depends on photo quality and lighting
- Not yet connected to any official document/blacklist databases

## License

Add your chosen license here (e.g. MIT) before sharing this repository publicly.
