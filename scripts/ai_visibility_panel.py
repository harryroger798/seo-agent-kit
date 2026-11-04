#!/usr/bin/env python3
"""Create a 30-prompt AI visibility panel and a weekly log template.

This script does not call AI engines. It creates the panel and the log;
you run the prompts manually or through your connected MCP tools.

Usage:
  python scripts/ai_visibility_panel.py --brand "Alias Browser" --out data/ai-panel.csv
"""

import argparse
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_PROMPTS = [
    "what is the best {category} for {audience}",
    "how do I choose a {category}",
    "best {category} in {market}",
    "{category} vs alternatives",
    "is {brand} good for {audience}",
    "{brand} pricing and plans",
    "{brand} alternatives",
    "how does {brand} compare to competitors",
    "what should I look for in a {category}",
    "common mistakes with {category}",
    "how much does a {category} cost",
    "is {category} worth it",
    "best free {category}",
    "best {category} for small business",
    "best {category} for beginners",
    "how to set up a {category}",
    "how long does {category} take",
    "what is the safest {category}",
    "best {category} with support",
    "best {category} for India",
    "best {category} for the US",
    "can I trust {brand}",
    "what do reviews say about {brand}",
    "who is {brand} for",
    "what makes {brand} different",
    "does {brand} work for {audience}",
    "cheapest {category} that still works",
    "premium {category} worth the price",
    "how to migrate to {brand}",
    "how to cancel {brand}",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brand", required=True)
    parser.add_argument("--category", default="SEO tool")
    parser.add_argument("--audience", default="small teams")
    parser.add_argument("--market", default="India")
    parser.add_argument("--out", default="data/ai-panel.csv")
    args = parser.parse_args()

    path = args.out if os.path.isabs(args.out) else os.path.join(ROOT, args.out)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["id", "prompt", "engine", "cited", "position", "sentiment", "competitors", "date", "notes"])
        for i, template in enumerate(DEFAULT_PROMPTS, 1):
            prompt = template.format(brand=args.brand, category=args.category, audience=args.audience, market=args.market)
            writer.writerow([i, prompt, "", "", "", "", "", "", ""])

    log_path = path.replace(".csv", "-log.csv")
    if not os.path.exists(log_path):
        with open(log_path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["date", "prompt_id", "engine", "cited", "position", "sentiment", "competitors", "notes"])

    print(f"Wrote {path}")
    print(f"Log template: {log_path}")
    print("Run each prompt in ChatGPT, Gemini, Perplexity, and AI Mode; fill the log weekly.")


if __name__ == "__main__":
    main()
