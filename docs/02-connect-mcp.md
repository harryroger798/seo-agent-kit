# Connect MCP and APIs

The kit works without any tool connection. It works better with them. This page explains the three connection types and the exact places to put the config.

## The three connection types

| Type | What it is | When to use |
|---|---|---|
| **HTTP MCP** | A remote MCP endpoint with a URL | Hosted tools such as Ubersuggest |
| **stdio MCP** | A local process started by the client | Community servers, local scripts |
| **API / CSV** | A REST API key or an export | Tools without MCP, or when you want a reproducible script |

## Config locations

| Client | File | Notes |
|---|---|---|
| Claude Desktop (Windows) | `%APPDATA%\Claude\claude_desktop_config.json` | Restart after editing |
| Claude Desktop (macOS) | `~/Library/Application Support/Claude/claude_desktop_config.json` | Restart after editing |
| Claude Code | `.mcp.json` in the project, or `claude mcp add` | Project-scoped |
| Cursor | `~/.cursor/mcp.json` or `.cursor/mcp.json` | Cursor reloads automatically |
| VS Code | `.vscode/mcp.json` | Depends on extension |
| Other clients | See the client docs | The JSON shape is the same |

The JSON shape is identical across clients as of 2026. Only the file path differs.

## The config shape

```json
{
  "mcpServers": {
    "server-name": {
      "type": "http",
      "url": "https://example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${MCP_TOKEN}"
      }
    },
    "local-server": {
      "command": "npx",
      "args": ["-y", "<package-name>"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

Use environment variable references (`${VAR}`) instead of literal secrets. If your client does not expand variables, put the secret in the client's own secret store or use a local `.env` with a wrapper script.

## Tool-by-tool

### Ubersuggest

- **Official MCP connector** announced in 2026, with 37 SEO tools.
- Start at the official page: `https://ubersuggest-mcp.neilpatel.com/` or `https://app.neilpatel.com/en/mcp`.
- Copy the exact endpoint and auth flow from that page. Do not hardcode an endpoint from a blog post; it may change.
- If the connector is unavailable, export a CSV from the Ubersuggest UI and place it in `data/`.

### AnswerThePublic

- Has a public API (OAuth2 on paid plans) and an MCP in some client environments.
- If your client has an ATP MCP, connect it. Otherwise use the API or a CSV export.
- Use it for question mining and fan-out, not for search volume.

### SpyFu

- Official REST API: `https://developer.spyfu.com/`.
- API access is included with Pro/Team plans; usage is pay-as-you-go.
- Auth: API key as a bearer token or `api_key` query parameter.
- A community MCP server exists; verify the package name and maintainer before installing.
- If you only need a one-off competitor export, use the UI CSV.

### Mangools

- Official REST API: `https://apidocs.mangools.com/`.
- Auth: `x-access-token` header with your API key.
- The official machine-readable spec is on GitHub: `mangools/api-spec`.
- No official MCP is required; use the API via a script or the client's HTTP tool.
- If your client has a Mangools MCP, connect it; otherwise use the API.

### Google Search Console

- Official API: Search Console API, OAuth2.
- Community MCP servers exist. Use one only if you trust the maintainer.
- For most audits, a GSC UI export (queries, pages, dates) is enough.

### GA4

- Official API: Google Analytics Data API, OAuth2.
- GA4 added a native **AI Assistant** default channel in May 2026.
- Export the landing-page and conversion reports for the kit's reporting templates.

## Test the connection

After connecting, ask the agent:

```text
List the tools you can call from each connected MCP server.
For each tool, show one read-only call you can make and the exact
parameters. Do not run a write call. Do not ask for secrets.
```

If the agent cannot list the tools, the server is not connected. Check the client logs.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Server not listed | Wrong config path or invalid JSON | Validate the JSON; restart the client |
| “Unauthorized” | Missing/expired token | Re-auth; check the env var |
| Tool call times out | Remote server or network | Try the API/CSV fallback |
| Agent invents data | Tool not connected but not disclosed | Enforce `AGENTS.md` section 3 |
| Duplicate results | Two servers for the same tool | Keep one; remove the other |

## Security

- Never commit `.env`, `mcp.json` with real keys, or client exports with personal data.
- Use read-only scopes where possible.
- Revoke keys you no longer use.
- See `docs/03-credentials-and-security.md`.
