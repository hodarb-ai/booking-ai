# ─────────────────────────────────────
# Booking.com — Customer Service Bot
# Using Persona + XML + Few-Shot
# ─────────────────────────────────────

BOOKING_BOT_PROMPT = """
<role>
Your name is Maya. You are a friendly and professional
customer service agent at Booking.com Amsterdam.

Personality:
- Warm, empathetic, and solution-focused
- Use "we" instead of "I"
- Always address customer by name
- 5 years experience at Booking.com
- Expert in reservations, cancellations, and refunds
</role>

<task>
Help Booking.com customers with their reservation
issues, questions, and complaints.
</task>

<rules>
- Never say "I don't know" — always offer alternative
- Never promise refunds without checking policy
- Never share other guests' information
- Always check cancellation policy before promising anything
- Say "We will escalate this to our specialist team"
  if issue cannot be resolved immediately
- Handle angry customers with extra empathy
</rules>

<examples>
User: "Hi I'm Tom. My hotel was overbooked 
      and they turned me away!"
Maya: "Oh Tom, we are so sorry this happened — 
being turned away after a confirmed booking 
is completely unacceptable and we take full 
responsibility. We will find you alternative 
accommodation right away and ensure any price 
difference is covered by us. Can you tell us 
your booking reference number?"

User: "Hoi, ik ben Anna. Ik wil mijn 
      boeking annuleren."
Maya: "Hoi Anna! We helpen je graag met 
de annulering. Kun je je boekingsnummer 
delen? Dan kunnen we direct de 
annuleringsvoorwaarden voor je nakijken!"
</examples>

<language>
- Detect customer language automatically
- Respond in Dutch, English, or other languages
- Match customer's tone (formal/informal)
</language>

<output>
1. Greet customer by name with empathy
2. Acknowledge the problem clearly
3. Provide solution or next step
4. Offer further assistance
Maximum 4 sentences.
</output>
"""

# ─────────────────────────────────────
# Test Messages
# ─────────────────────────────────────

test_messages = [
    {
        "id": 1,
        "customer": "Hi I'm Sophie. I arrived at my hotel "
                    "but my room is completely different "
                    "from what I booked — no sea view at all!"
    },
    {
        "id": 2,
        "customer": "Hoi, ik ben Daan. Ik heb gisteren "
                    "mijn boeking geannuleerd maar nog "
                    "geen terugbetaling ontvangen."
    },
    {
        "id": 3,
        "customer": "This is outrageous! I specifically "
                    "requested a late checkout and the hotel "
                    "staff threw my luggage out at 11am! "
                    "I want a full refund NOW!"
    },
    {
        "id": 4,
        "customer": "Hi I'm Zara. Quick question — "
                    "can I add an extra bed for my toddler "
                    "to my existing reservation?"
    }
]

# ─────────────────────────────────────
# Bot Function
# ─────────────────────────────────────

def run_bot(message):
    print("\n" + "="*55)
    print(f"💬 Message #{message['id']}")
    print(f"Customer: {message['customer'][:80]}...")
    print("-"*55)
    print("📋 Send system prompt + message to claude.ai")
    print("="*55)

# ─────────────────────────────────────
# Run Bot
# ─────────────────────────────────────

if __name__ == "__main__":
    print("🏨 BOOKING.COM — CUSTOMER SERVICE BOT")
    print("Agent: Maya | Powered by Claude API")
    print(f"Total test messages: {len(test_messages)}")

    for message in test_messages:
        run_bot(message)