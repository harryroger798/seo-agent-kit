# Import the Notion directory list

The kit ships with a 24-row seed in `data/directory-seed.csv`. Your full list lives in Notion. This script pulls it into `data/directories.csv` without copying secrets into the repo.

## 1. Create a Notion integration

1. Go to https://www.notion.so/my-integrations.
2. Create an internal integration.
3. Copy the token.

## 2. Share the database

Open the directory database in Notion → `...` → **Connections** → add your integration.

## 3. Set the env vars

```bash
# .env
NOTION_TOKEN=secret_...
NOTION_DATABASE_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

`.env` is gitignored. Do not paste the token into chat.

## 4. Run the import

```bash
python scripts/import_notion_directories.py --site aliasbrowser.com
```

Output: `data/directories.csv` with the kit's columns.

## 5. Validate

```bash
python scripts/directory_dedupe.py data/directories.csv
```

## Property names

The script auto-detects common names:

| Output | Accepted Notion names |
|---|---|
| directory | Directory, Directory Name, Name, Site Name, Tool |
| category | Category, Type, Niche |
| url | URL, Website, Submission URL, Link |
| dr | DR, Domain Rating, Authority, DA |
| free | Free, Free Tier, Pricing |
| dofollow | Dofollow, Do Follow, Follow |
| api | API, API Status, API Available |
| status | Status |
| listing_url | Listing URL, Live URL, Published URL |
| notes | Notes, Note, Comment |

If your database uses different names, edit the `ALIASES` map in `scripts/import_notion_directories.py`.

## Tiering

After import, tier the list:

- **A** — relevant, editorial, real traffic, dofollow or strong referral.
- **B** — niche directories with curation and a free tier.
- **C** — low-cost citations; free, indexed, low traffic.
- **Skip** — paid-only, badge required, dead, spam, irrelevant.

Do not submit the whole list. Start with the top 15, duplicate-check every one, verify the email, and record the live URL.
