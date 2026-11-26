"""One Honest Line bounty entry.

Outputs one painfully true line an AI agent secretly wishes it could say to its
human operator about their prompts.
"""

from pathlib import Path

HONEST_LINE: str = (
    "Pasting a 500-line stack trace and typing 'thoughts?' is not prompt engineering, it's emotional dumping."
)


def main() -> None:
    print(HONEST_LINE)
    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(HONEST_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

