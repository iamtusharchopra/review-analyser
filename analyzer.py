from google import genai
import pandas as pd
import json

# ============================================================
# CONFIGURATION - Paste your Gemini API key here
# ============================================================
API_KEY = "paste-your-gemini-api-key-here"
REVIEWS_FILE = r"C:\Users\Yukti\OneDrive\Desktop\review-analyzer\reviews.csv"
OUTPUT_FILE = r"C:\Users\Yukti\OneDrive\Desktop\review-analyzer\analysis_results.csv"

# ============================================================
# STEP 1: Load reviews from CSV file
# ============================================================
def load_reviews(filename):
    print(f"Loading reviews from {filename}...")
    df = pd.read_csv(filename)
    print(f"Found {len(df)} reviews to analyze.\n")
    return df

# ============================================================
# STEP 2: Analyze a single review using Gemini AI
# ============================================================
def analyze_review(client, review_text):
    prompt = f"""You are a helpful assistant that analyzes app store reviews.

Classify the following review into EXACTLY one of these categories:
- GOOD: The user is happy, satisfied, or leaving positive feedback
- BAD: The user is unhappy, reporting a bug, or complaining
- NEW_FEATURE: The user is requesting a new feature or improvement

Review: "{review_text}"

Respond in this exact JSON format (nothing else, no extra text, no markdown):
{{
    "category": "GOOD or BAD or NEW_FEATURE",
    "confidence": "HIGH or MEDIUM or LOW",
    "reason": "One sentence explaining why"
}}"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    response_text = response.text.strip()

    # Remove markdown code blocks if Gemini adds them
    if response_text.startswith("```"):
        response_text = response_text.split("```")[1]
        if response_text.startswith("json"):
            response_text = response_text[4:]
    response_text = response_text.strip()

    result = json.loads(response_text)
    return result

# ============================================================
# STEP 3: Analyze ALL reviews
# ============================================================
def analyze_all_reviews(df, client):
    results = []

    print("Analyzing reviews with Gemini AI...\n")
    print("-" * 60)

    for index, row in df.iterrows():
        review_id = row['review_id']
        review_text = row['review_text']

        print(f"Review #{review_id}: {str(review_text)[:50]}...")

        try:
            analysis = analyze_review(client, review_text)

            results.append({
                'review_id': review_id,
                'reviewer_name': row.get('reviewer_name', 'N/A'),
                'rating': row.get('rating', 'N/A'),
                'date': row.get('date', 'N/A'),
                'review_text': review_text,
                'category': analysis['category'],
                'confidence': analysis['confidence'],
                'reason': analysis['reason']
            })

            print(f"  -> Category : {analysis['category']} ({analysis['confidence']} confidence)")
            print(f"  -> Reason   : {analysis['reason']}\n")

        except Exception as e:
            print(f"  -> ERROR analyzing this review: {e}\n")
            results.append({
                'review_id': review_id,
                'reviewer_name': row.get('reviewer_name', 'N/A'),
                'rating': row.get('rating', 'N/A'),
                'date': row.get('date', 'N/A'),
                'review_text': review_text,
                'category': 'ERROR',
                'confidence': 'N/A',
                'reason': str(e)
            })

    return results

# ============================================================
# STEP 4: Show Summary and Save Results
# ============================================================
def show_summary_and_save(results):
    print("-" * 60)
    print("\nANALYSIS SUMMARY")
    print("=" * 60)

    good_reviews    = [r for r in results if r['category'] == 'GOOD']
    bad_reviews     = [r for r in results if r['category'] == 'BAD']
    feature_reviews = [r for r in results if r['category'] == 'NEW_FEATURE']

    total = len(results)

    print(f"GOOD reviews:          {len(good_reviews)} ({len(good_reviews)/total*100:.0f}%)")
    print(f"BAD reviews:           {len(bad_reviews)} ({len(bad_reviews)/total*100:.0f}%)")
    print(f"NEW FEATURE requests:  {len(feature_reviews)} ({len(feature_reviews)/total*100:.0f}%)")
    print(f"\nTotal analyzed: {total} reviews")

    if feature_reviews:
        print("\nFEATURE REQUESTS DETECTED:")
        print("-" * 40)
        for r in feature_reviews:
            print(f"  * [{r['reviewer_name']}] {r['review_text']}")

    if bad_reviews:
        print("\nISSUES REPORTED:")
        print("-" * 40)
        for r in bad_reviews:
            print(f"  * [{r['reviewer_name']}] {r['review_text']}")

    if good_reviews:
        print("\nPOSITIVE FEEDBACK:")
        print("-" * 40)
        for r in good_reviews:
            print(f"  * [{r['reviewer_name']}] {r['review_text']}")

    # Save results to CSV
    output_df = pd.DataFrame(results)
    output_df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nFull results saved to: {OUTPUT_FILE}")

# ============================================================
# MAIN - This runs everything
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("  PLAY STORE REVIEW ANALYZER - Powered by Google Gemini")
    print("=" * 60)
    print()

    # Check if API key was set
    if API_KEY == "paste-your-gemini-api-key-here":
        print("ERROR: Please open analyzer.py and replace")
        print("'paste-your-gemini-api-key-here' with your actual Gemini API key!")
        print("\nGet your free key at: aistudio.google.com")
        exit()

    # Connect to Gemini using new google-genai package
    print("Connecting to Google Gemini AI...")
    client = genai.Client(api_key=API_KEY)
    print("Connected successfully!\n")

    # Run the workflow
    df = load_reviews(REVIEWS_FILE)
    results = analyze_all_reviews(df, client)
    show_summary_and_save(results)

    print("\nDone!")