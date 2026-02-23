# review-analyser
An AI-powered Python tool that automatically reads Play Store app reviews and classifies each one as **Good**, **Bad**, or **New Feature Request** using Google Gemini AI.

---

## 💡 What It Does

Instead of manually reading hundreds of app reviews one by one, this tool does it all automatically in seconds. Just give it a CSV file of reviews and it will:

- ✅ Classify each review as **GOOD**, **BAD**, or **NEW FEATURE**
- 📊 Show a summary of how many reviews fall in each category
- 💾 Save all results to a new CSV file for easy viewing in Excel
- 🔍 List all bug reports and complaints so you can fix issues faster
- 💡 Highlight all feature requests so you know what users want next

---

## 🛠️ Built With

- **Python 3** — programming language
- **Google Gemini AI** (`gemini-2.5-flash`) — AI model that reads and understands reviews
- **Pandas** — for reading and saving CSV files
- **google-genai** — official Google library to connect to Gemini

---

## 📁 Project Files

| File | Description |
|---|---|
| `analyzer.py` | Main Python script that runs the analysis |
| `reviews.csv` | Input file containing the app reviews |
| `analysis_results.csv` | Output file generated after running the tool |

---

## ⚙️ How to Set Up

### 1. Install Python
Download and install Python from **python.org/downloads**
> ⚠️ During installation, check the box **"Add Python to PATH"**

### 2. Install Required Libraries
Open Command Prompt and run:
```
pip install google-genai pandas
```

### 3. Get a Free Gemini API Key
1. Go to **aistudio.google.com**
2. Sign in with your Google account
3. Click **"Get API Key"** → **"Create API Key"**
4. Copy the key

### 4. Add Your API Key to the Code
Open `analyzer.py` in Notepad and replace this line:
```python
API_KEY = "paste-your-gemini-api-key-here"
```
With your actual key:
```python
API_KEY = "AIzaSy..."
```

### 5. Add Your Reviews
Open `reviews.csv` and add your app reviews. The file must have these columns:
```
review_id, reviewer_name, rating, date, review_text, app_version
```

---

## ▶️ How to Run

Open Command Prompt, navigate to the project folder and run:
```
cd C:\Users\YourName\review-analyzer
python analyzer.py
```

---

## 📊 Sample Output

```
============================================================
  PLAY STORE REVIEW ANALYZER - Powered by Google Gemini
============================================================

Loading reviews from reviews.csv...
Found 25 reviews to analyze.

Analyzing reviews with Gemini AI...
------------------------------------------------------------
Review #1: This app has completely transformed how I manage...
  -> Category : GOOD (HIGH confidence)
  -> Reason   : User expresses strong satisfaction with the app.

Review #2: The app crashes every single time I try to upload...
  -> Category : BAD (HIGH confidence)
  -> Reason   : User reports a critical bug causing app crashes.

Review #3: Love the app! Would be amazing if you could add...
  -> Category : NEW_FEATURE (HIGH confidence)
  -> Reason   : User is requesting a dark mode feature.

------------------------------------------------------------

ANALYSIS SUMMARY
============================================================
GOOD reviews:          10 (40%)
BAD reviews:            8 (32%)
NEW FEATURE requests:   7 (28%)

Total analyzed: 25 reviews
```

---

## 📋 Input File Format

Your `reviews.csv` should look like this:

| review_id | reviewer_name | rating | date | review_text | app_version |
|---|---|---|---|---|---|
| 1 | John Smith | 5 | 2024-01-05 | Amazing app! | 3.2.1 |
| 2 | Jane Doe | 1 | 2024-01-06 | App keeps crashing | 3.2.1 |
| 3 | Bob Lee | 3 | 2024-01-07 | Please add dark mode | 3.2.1 |

---

## 🔒 Security Note

> ⚠️ **Never upload your real API key to GitHub!**
> Always replace your API key with `"paste-your-gemini-api-key-here"` before pushing code to GitHub.

---

## 🚀 Future Ideas


- [ ] Send email alerts when bad reviews spike
- [ ] Build a dashboard to visualize review trends
- [ ] Auto-generate reply suggestions for each review
- [ ] Schedule the analyzer to run every day automatically

---

## 👩‍💻 Author

Built by **Tushar Chopra** as a beginner AI automation project.

---

## 📄 License

This project is free to use and modify for personal and educational purposes.
