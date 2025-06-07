# main.py

import sys
from patterns import lower_triangle, upper_triangle, pyramid

def print_pattern(title: str, pattern: list[str]):
    print(f"\n{title}")
    print("-" * len(title))
    for line in pattern:
        print(line)

def get_positive_integer(prompt: str = "Enter size (positive integer): ") -> int:
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                raise ValueError("Value must be positive.")
            return n
        except ValueError as ve:
            print(f"Invalid input: {ve}. Try again.\n")
            continue

def main():
    print("Pattern Generator")
    print("=================")

    n = get_positive_integer()

    patterns: dict[str, list[str]] = {
        "Lower Triangle": lower_triangle(n),
        "Upper Triangle": upper_triangle(n),
        "Pyramid": pyramid(n)
    }

    seen_titles: set[str] = set()

    for title, pattern in patterns.items():
        if title in seen_titles:
            continue  # avoid duplicate
        print_pattern(title, pattern)
        seen_titles.add(title)

    # Tuple example
    summary: tuple[str, int] = ("Patterns Generated", len(patterns))
    print(f"\nSummary: {summary[0]} = {summary[1]}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting.")
        sys.exit(0)
