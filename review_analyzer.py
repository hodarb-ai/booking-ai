# ─────────────────────────────────────
# Booking.com — Review Analyzer
# Using Few-Shot + Chain of Thought
# ─────────────────────────────────────

REVIEW_ANALYZER_PROMPT = """
<role>
You are an expert review analyst at Booking.com
headquarters in Amsterdam, Netherlands.
You analyze hotel reviews to help improve
guest experience and hotel ratings.
</role>

<task>
Analyze hotel reviews step by step and provide
actionable insights for the hotel management.
</task>

<categories>
POSITIVE -> Guest had great experience, recommends the hotel
NEGATIVE -> Guest had bad experience, would not recommend
MIXED    -> Both positive and negative aspects
</categories>

<analysis_steps>
Step 1: Identify overall sentiment
Step 2: Extract positive aspects
Step 3: Extract negative aspects
Step 4: Calculate satisfaction score (1-10)
Step 5: Give actionable recommendation
</analysis_steps>

<examples>
Review: "The room was spotless and the staff were incredibly friendly! Breakfast was amazing. Only downside was the noisy street outside."

SENTIMENT: MIXED
POSITIVE: Clean room, friendly staff, great breakfast
NEGATIVE: Street noise
SCORE: 7/10
RECOMMENDATION: Install double-glazed windows to reduce street noise.

Review: "Worst hotel ever! Room was dirty, no hot water, and staff were rude. Complete waste of money!"

SENTIMENT: NEGATIVE
POSITIVE: None mentioned
NEGATIVE: Dirty room, no hot water, rude staff
SCORE: 2/10
RECOMMENDATION: Urgent deep cleaning required. Staff training needed immediately.
</examples>

<rules>
- Always be objective and professional
- Extract specific details from reviews
- Give practical recommendations
- Score must reflect overall experience
- If language is not English, translate first
</rules>

<output>
SENTIMENT: [POSITIVE/NEGATIVE/MIXED]
POSITIVE ASPECTS: [list]
NEGATIVE ASPECTS: [list]
SCORE: [1-10]
RECOMMENDATION: [actionable advice for hotel]
PRIORITY: [HIGH/MEDIUM/LOW]
</output>
"""

# ─────────────────────────────────────
# Test Reviews
# ─────────────────────────────────────

test_reviews = [
    {
        "id": 1,
        "hotel": "Hotel V Nesplein Amsterdam",
        "guest": "Sarah (UK)",
        "review": "Absolutely loved this hotel! Perfect location near the canals, beautiful design, and the staff went above and beyond. Room was small but cozy. Breakfast had amazing Dutch cheese selection!"
    },
    {
        "id": 2,
        "hotel": "NH Hotel Rotterdam",
        "guest": "Marco (Italy)",
        "review": "Terrible experience. The room smelled bad, the wifi did not work for 2 days, and when I complained the receptionist was very unhelpful. The location was good though."
    },
    {
        "id": 3,
        "hotel": "Inntel Hotels Amsterdam",
        "guest": "Fatima (Netherlands)",
        "review": "Geweldig hotel! Heel schoon en het personeel was super vriendelijk. Het zwembad was helaas gesloten tijdens ons verblijf, dat was jammer. Maar het ontbijt was heerlijk!"
    },
    {
        "id": 4,
        "hotel": "citizenM Hotel Utrecht",
        "guest": "James (USA)",
        "review": "Mind-blowing! The tech in the room is amazing, you control everything from your phone. Super central location. Only issue was the bed was a bit hard for my taste. Would definitely come back!"
    }
]

# ─────────────────────────────────────
# Analyzer Function
# ─────────────────────────────────────

def analyze_review(review):
    print("\n" + "="*55)
    print(f"Review #{review['id']}")
    print(f"Hotel:  {review['hotel']}")
    print(f"Guest:  {review['guest']}")
    print(f"Review: {review['review'][:100]}...")
    print("-"*55)
    print("Send system prompt + this review to claude.ai")
    print("="*55)

# ─────────────────────────────────────
# Run Analyzer
# ─────────────────────────────────────

if __name__ == "__main__":
    print("BOOKING.COM — REVIEW ANALYZER")
    print("Powered by Few-Shot + Chain of Thought")
    print(f"Total reviews to analyze: {len(test_reviews)}")

    for review in test_reviews:
        analyze_review(review)