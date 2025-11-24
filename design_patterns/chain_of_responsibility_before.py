
# ==============================================
# Before Pattern: Chain of Responsibility
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how spam filtering logic looked BEFORE applying
#   the Chain of Responsibility pattern. A single large function
#   contains multiple if/elif checks for different spam rules.
#   Adding a new rule requires modifying this big function,
#   violating the Open–Closed Principle.
# ==============================================


# -----------------------------
# Email Model (simple container)
# -----------------------------
class Email:
    def __init__(self, sender, text, has_attachment=False):
        self.sender = sender
        self.text = text
        self.has_attachment = has_attachment


# -----------------------------
# BEFORE Chain of Responsibility
# -----------------------------
# A single messy function that handles ALL filtering rules.
# Adding new spam checks makes this function grow endlessly.
# -----------------------------

def process_email(email: Email):
    # Rule 1 — keyword filter
    if "buy now" in email.text.lower() or "free money" in email.text.lower():
        print("Rejected: Spam keywords detected.")
        return

    # Rule 2 — sender blacklist
    blacklist = {"spam@evil.com", "bot@ads.net"}
    if email.sender in blacklist:
        print("Rejected: Sender is blacklisted.")
        return

    # Rule 3 — suspicious attachment
    if email.has_attachment:
        print("Rejected: Suspicious attachment detected.")
        return

    # No rule handled it
    print("Accepted: Email delivered to inbox.")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Before Chain of Responsibility Example ---\n")

    emails = [
        Email("user@example.com", "Hello, buy now!"),
        Email("spam@evil.com", "Normal message here"),
        Email("friend@mail.com", "Check this out", has_attachment=True),
        Email("boss@company.com", "Meeting at 3 PM"),  # only this passes
    ]

    for e in emails:
        print(f"Processing email from: {e.sender}")
        process_email(e)
        print()

    print(
        "\nProblem: All rules are hardcoded into ONE place.\n"
        "Adding, removing, or reordering spam filters requires editing\n"
        "this large function. This tightly couples all rules together."
    )


# -----------------------------
# Example Output
# -----------------------------
# Processing email from: user@example.com
# Rejected: Spam keywords detected.
#
# Processing email from: spam@evil.com
# Rejected: Sender is blacklisted.
#
# Processing email from: friend@mail.com
# Rejected: Suspicious attachment detected.
#
# Processing email from: boss@company.com
# Accepted: Email delivered to inbox.
#
# ==============================================
# History
# ==============================================
# The Chain of Responsibility pattern was formalized in the GoF book (1994),
# but the concept existed much earlier in GUI systems and operating systems.
# Event-handling systems passed user actions (clicks, keypresses) up a chain
# of widgets until one handled them. Early email filters also used sequential
# rule checks where each rule could accept or reject a message. The pattern
# emerged as a clean way to decouple senders from receivers and to allow
# multiple handlers to process a request in sequence.
# ==============================================
