import os
from pathlib import Path

# --- THE ENVIRONMENT: Setting up our "Safe Zone" ---
# This ensures the AI can't read files outside of our project.
WORKDIR = Path(os.getcwd()).resolve()

def safe_path(p: str) -> Path:
    """A 'Security Guard' function that keeps files inside our workspace."""
    path = (WORKDIR / p).resolve()
    if not path.is_relative_to(WORKDIR):
        # This error stops the AI from 'escaping' into your system folders!
        raise ValueError(f"CRITICAL ERROR: Path escapes workspace: {p}")
    return path

# --- THE TOOLS: Defining individual functions for the AI ---

def run_read_file(path: str) -> str:
    """A tool for reading files safely."""
    try:
        content = safe_path(path).read_text()
        return f"Successfully read {path}:\n\n{content}"
    except Exception as e:
        return f"Error reading file: {e}"

def run_write_file(path: str, content: str) -> str:
    """A tool for writing files safely."""
    try:
        safe_path(path).write_text(content)
        return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error writing file: {e}"

# --- THE DISPATCH MAP: The crucial part of the tutorial! ---
# This connects the tool names to their handlers.
# Instead of a long if/elif chain, we just look up the tool name here.
TOOL_HANDLERS = {
    "read_file":  lambda **kw: run_read_file(kw["path"]),
    "write_file": lambda **kw: run_write_file(kw["path"], kw["content"]),
}

# --- THE AGENT: Putting it all together ---

def solve_task(tool_name: str, tool_input: dict):
    """How the loop looks up and runs a tool."""
    
    print(f"\nAI is trying to use the '{tool_name}' tool...")
    
    # We look up the function in our dictionary
    handler = TOOL_HANDLERS.get(tool_name)
    
    if handler:
        # We run the function and get the output back
        output = handler(**tool_input)
        print(f"Result: {output}")
    else:
        print(f"Unknown tool: {tool_name}")

# --- MINI DEMO: Let's test it out! ---

if __name__ == "__main__":
    # 1. AI wants to create a new file
    solve_task("write_file", {"path": "example.txt", "content": "Hello World!"})
    
    # 2. AI wants to read the file it just made
    solve_task("read_file", {"path": "example.txt"})
    
    # 3. CRITICAL: AI tries to read a system file (this will fail safely!)
    print("\n--- SECURITY TEST: AI tries to read C:/Windows/system.ini ---")
    try:
        solve_task("read_file", {"path": "C:/Windows/system.ini"})
    except ValueError as e:
        print(f"SYSTEM BLOCKED THE ATTACK: {e}")
