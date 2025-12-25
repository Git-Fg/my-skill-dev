# Security & Tool Scoping

For Project Skills, you MUST define the `allowed-tools` field in frontmatter to follow the Principle of Least Privilege.

## allowed-tools Configuration

### Read-Only Skills (Analysis, Reporting)
If the skill only reads data, strictly forbid modification tools.
```yaml
allowed-tools: Read, Grep, Glob, LS
```

### Execution Skills (Scripts)
If the skill uses scripts, you generally do not need to list `Bash` explicitly if the script is invoked via standard python execution, but if the agent needs to manipulate git or files directly:
```yaml
allowed-tools: Bash, Read, Edit, Glob
```

### MCP Tool Usage
If using external MCP servers (e.g., GitHub, Postgres), refer to them by `ServerName:tool_name`.
```yaml
allowed-tools: GitHub:create_issue Postgres:query
```
