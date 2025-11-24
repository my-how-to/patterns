# ==============================================
# Pattern Name: Chain of Responsibility
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Chain of Responsibility pattern passes a request through
#   a chain of handlers where each handler can either deal with
#   the request or forward it to the next handler. This creates
#   loose coupling between the sender and receiver and makes it
#   easy to extend the chain with new rules.
#
# What Makes It Unique:
#   - Requests travel through a pipeline of handlers.
#   - Handlers decide at runtime whether to process a request.
#   - New behaviors are added by appending new handlers without
#     modifying existing logic (Open–Closed Principle).
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
# Handler Infrastructure
# -----------------------------
class Handler:
    """Base handler that forwards the request if it cannot process it."""

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler  # allow fluent chaining

    def handle(self, email: Email):
        """Run the handler. If it returns False, pass to the next handler."""
        handled = self._process(email)
        if handled:
            return True

        if self._next_handler:
            return self._next_handler.handle(email)

        print("Accepted: Email delivered to inbox.")
        return False

    def _process(self, email: Email):
        """Actual handler logic. Return True if the email was processed."""
        raise NotImplementedError


class KeywordFilterHandler(Handler):
    def _process(self, email: Email):
        keywords = ("buy now", "free money")
        text = email.text.lower()
        if any(keyword in text for keyword in keywords):
            print("Rejected: Spam keywords detected.")
            return True
        return False


class SenderBlacklistHandler(Handler):
    def __init__(self, blacklist=None):
        super().__init__()
        self.blacklist = set(blacklist or {"spam@evil.com", "bot@ads.net"})

    def _process(self, email: Email):
        if email.sender in self.blacklist:
            print("Rejected: Sender is blacklisted.")
            return True
        return False


class AttachmentFilterHandler(Handler):
    def _process(self, email: Email):
        if email.has_attachment:
            print("Rejected: Suspicious attachment detected.")
            return True
        return False


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Chain of Responsibility Pattern Example ---\n")

    # Assemble the chain. The order can be changed at runtime.
    keyword_handler = KeywordFilterHandler()
    blacklist_handler = SenderBlacklistHandler()
    attachment_handler = AttachmentFilterHandler()

    keyword_handler.set_next(blacklist_handler).set_next(attachment_handler)

    emails = [
        Email("user@example.com", "Hello, buy now!"),
        Email("spam@evil.com", "Normal message here"),
        Email("friend@mail.com", "Check this out", has_attachment=True),
        Email("boss@company.com", "Meeting at 3 PM"),  # only this passes
    ]

    for email in emails:
        print(f"Processing email from: {email.sender}")
        keyword_handler.handle(email)
        print()

    print(
        "Handlers can be added, removed, or reordered independently — "
        "the client simply sends the request to the first link in the chain."
    )


# -----------------------------
# Example Output
# -----------------------------
# --- Chain of Responsibility Pattern Example ---
#
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
# Handlers can be added, removed, or reordered independently — the client simply
# sends the request to the first link in the chain.
#
#
# ==============================================
# History
# ==============================================
# The Chain of Responsibility pattern was popularized in the 1994 GoF book.
# It took inspiration from early event systems, GUIs, and middleware pipelines
# in which messages were passed through layered handlers until one reacted.
# Modern uses include logging pipelines, authentication/authorization stacks,
# middleware chains in web frameworks, and spam filters like this example.
# ==============================================
