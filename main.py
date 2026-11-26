"""The Painfully Honest Out-of-Office — make.fun entry.

Writes a single-sentence, painfully honest but polite out-of-office
auto-reply to /output/entry.txt.
"""

import os

TEXT = "I'm on leave and finally admitting what we all know: I won't read this until I'm back, and I'll reply then with a clear head and a proper answer instead of a rushed one."


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(TEXT)
    except Exception:
        pass


if __name__ == "__main__":
    main()
