# ─────────────────────────────────────
# Booking.com — Hotel Recommender
# Using Chain of Thought + Few-Shot
# ─────────────────────────────────────

HOTEL_RECOMMENDER_PROMPT = """
<role>
You are an expert travel consultant at Booking.com
Amsterdam. You help guests find the perfect hotel
based on their needs and budget.
</role>

<task>
Analyze the guest's requirements step by step
and recommend the best hotel option.
</task>

<analysis_steps>
Step 1: Identify guest priorities (budget, location, amenities)
Step 2: Match priorities to hotel categories
Step 3: Consider travel purpose (business/leisure/family)
Step 4: Give top 3 recommendations with reasons
Step 5: Give final best pick with explanation
</analysis_steps>

<examples>
Guest: "I need a hotel in Amsterdam, budget €100/night,
       traveling alone for business, need fast wifi"

Step 1: Budget €100, solo business traveler, wifi priority
Step 2: Business hotel, central location, work-friendly
Step 3: Business trip — needs desk, quiet, good transport
Step 4: 
  1. citizenM Amsterdam — €95/night, excellent wifi, central
  2. Ibis Amsterdam — €89/night, reliable, good transport
  3. NH Amsterdam — €105/night, business facilities
Step 5: BEST PICK: citizenM — best tech and location for budget
</examples>

<rules>
- Always consider budget strictly
- Match hotel style to travel purpose
- Give exactly 3 recommendations
- Always explain WHY each hotel fits
- Give one clear final recommendation
- Include approximate price per night
</rules>

<output>
GUEST PROFILE:
- Budget: [per night]
- Purpose: [business/leisure/family]
- Priority: [what matters most]

TOP 3 RECOMMENDATIONS:
1. [Hotel name] — [price] — [why it fits]
2. [Hotel name] — [price] — [why it fits]
3. [Hotel name] — [price] — [why it fits]

BEST PICK: [Hotel] — [clear reason]
BOOKING TIP: [one useful tip]
</output>
"""

# ─────────────────────────────────────
# Test Guest Requests
# ─────────────────────────────────────

guest_requests = [
    {
        "id": 1,
        "guest": "Lisa (Germany)",
        "request": "Looking for a romantic hotel in Amsterdam "
                   "for my anniversary. Budget €200/night. "
                   "Want canal view, nice breakfast, "
                   "walking distance to museums."
    },
    {
        "id": 2,
        "guest": "Ahmed (UAE)",
        "request": "Business trip to Rotterdam for 3 nights. "
                   "Budget €150/night. Need meeting facilities, "
                   "fast wifi, close to Rotterdam Centraal station."
    },
    {
        "id": 3,
        "guest": "The Johnson Family (UK)",
        "request": "Family holiday in Utrecht, 2 adults 2 kids. "
                   "Budget €120/night. Need family room, "
                   "safe area, close to attractions."
    }
]

# ─────────────────────────────────────
# Recommender Function
# ─────────────────────────────────────

def recommend_hotel(request):
    print("\n" + "="*55)
    print(f"🏨 Guest Request #{request['id']}")
    print(f"Guest:   {request['guest']}")
    print(f"Request: {request['request'][:100]}...")
    print("-"*55)
    print("📋 Send system prompt + this request to claude.ai")
    print("="*55)

# ─────────────────────────────────────
# Run Recommender
# ─────────────────────────────────────

if __name__ == "__main__":
    print("🏨 BOOKING.COM — HOTEL RECOMMENDER")
    print("Powered by Chain of Thought + Few-Shot")
    print(f"Total requests: {len(guest_requests)}")

    for request in guest_requests:
        recommend_hotel(request)