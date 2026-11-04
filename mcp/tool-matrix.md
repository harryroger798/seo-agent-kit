# Tool matrix

| Tool | MCP | API | Auth | Fallback | Notes |
|---|---|---|---|---|---|
| **Ubersuggest** | Official connector | No public API | OAuth via MCP | CSV export | 37 SEO tools; start at the official MCP page |
| **AnswerThePublic** | Depends on client | Public API (plan-gated) | OAuth / API key | CSV export | Question mining, not volume |
| **SpyFu** | Community MCP | Official REST | API key (Pro/Team) | CSV export | Pay-as-you-go credits |
| **Mangools** | Depends on client | Official REST | `x-access-token` | CSV export | API spec on GitHub |
| **Google Search Console** | Community MCP | Official API | OAuth | CSV export | Read-only scope |
| **GA4** | Community MCP | Official API | OAuth | CSV export | AI Assistant channel added May 2026 |

## Connection checklist

- [ ] The server appears in the client’s tool list.
- [ ] A read-only call succeeds.
- [ ] The agent can name the exact tool and parameters.
- [ ] The secret is in `.env` or the client’s secret store, not the repo.
- [ ] The fallback is documented.

## When to use which

| Need | Best source | Why |
|---|---|---|
| Keyword volume / KD | Mangools KWFinder, Ubersuggest | Fast, cheap |
| Competitor organic pages | SpyFu, Mangools SiteProfiler | Historical data |
| Questions / fan-out | AnswerThePublic, GSC queries | Real language |
| SERP features / AIO | Mangools SERPChecker, manual | Feature context |
| Rankings / clicks | GSC | First-party truth |
| Conversions | GA4 | Outcome |
| AI citations | Prompt panel + GSC AI report | No single tool sees it all |

## Security

Never commit a real key. See `docs/03-credentials-and-security.md`.
