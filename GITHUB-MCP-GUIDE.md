# GitHub MCP Server - Usage Prompt for LLMs

## Quick Start Prompt

**Copy this prompt to use GitHub MCP with any LLM:**

```
I have access to GitHub MCP server tools. Help me:

1. List all my Copilot Spaces
2. Get details of my "learn-mcp" space (owner: fvegiard)
3. Verify my GitHub repository fvegiard/learn-mcp is accessible

Use these tools:
- github-mcp-server-list_copilot_spaces
- github-mcp-server-get_copilot_space (name: "learn-mcp", owner: "fvegiard")
- github-mcp-server-get_file_contents (owner: "fvegiard", repo: "learn-mcp", path: "README.md")
```

## Available GitHub MCP Tools

### 1. **list_copilot_spaces**
Lists all your Copilot Spaces.

**Prompt**: `List all my Copilot Spaces`

### 2. **get_copilot_space**  
Get details of a specific space.

**Prompt**: `Get details of Copilot Space "learn-mcp" owned by "fvegiard"`

### 3. **search_code**
Search for code on GitHub.

**Prompt**: `Search GitHub for "FastMCP language:python"`

### 4. **get_file_contents**
Fetch file from GitHub repository.

**Prompt**: `Get the README.md file from fvegiard/learn-mcp repository`

### 5. **search_users**
Find GitHub users.

**Prompt**: `Search for GitHub user "fvegiard"`

## Common Use Cases

### Manage Your Copilot Space
```
Show me all my Copilot Spaces and their contents.
For my "learn-mcp" space, tell me how many documents are stored.
```

### Research Code Examples
```
Search GitHub for FastMCP server implementations with semantic search.
Fetch the best example and explain how it works.
```

### Sync Documentation
```
Check if my GitHub repository fvegiard/learn-mcp has the latest 
COPILOT-SPACE-DOC.md file. Compare it with my local version at
/home/francis-v/ai-stack/learn-mcp/COPILOT-SPACE-DOC.md
```

## Your Configuration

- **GitHub User**: fvegiard
- **Copilot Space**: learn-mcp  
- **Local MCP**: http://127.0.0.1:8001/mcp
- **Repository**: github.com/fvegiard/learn-mcp
- **Knowledge Base**: 801 AI engineering references

## Example Session

**You say**:
```
Connect to GitHub and show me my Copilot Space status
```

**LLM will**:
1. Call `github-mcp-server-list_copilot_spaces`
2. Call `github-mcp-server-get_copilot_space` with your space name
3. Show you the results with document count and size

