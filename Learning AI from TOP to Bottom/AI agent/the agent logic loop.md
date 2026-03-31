

## Core Python Logic
This is the `test_run_1.py` code that allows the AI to think, act, and remember:

```python
# The main function that starts our AI agent. You give it a 'query' (your question or command).
def agent_loop(query):
    
    # 1. THE MEMORY: We create the chat history. It starts with just your initial question.
    messages = [{"role": "user", "content": query}]
    
    # 2. THE ENGINE: This is an infinite loop. It will keep running until the AI decides it is finished.
    while True:
        
        # 3. THE REQUEST: We send the chat history AND our list of "TOOLS" to Anthropic's server.
        response = client.messages.create(
            model=MODEL,
            system=SYSTEM,
            messages=messages,
            tools=TOOLS, # This is the crucial part that gives the AI 'hands'
            max_tokens=8000,
        )
        
        # 4. We receive the AI's reply and immediately save it into our chat history memory.
        messages.append({"role": "assistant", "content": response.content})
        
        # 5. THE EXIT CONDITION: We check *why* the AI stopped generating text. 
        if response.stop_reason != "tool_use":
            return 
            
        # 6. TOOL EXECUTION: If the AI decided it needs to run a command 
        results = [] 
        
        # 7. We scan through the AI's response to find the specific tool it wants to use...
        for block in response.content:
            if block.type == "tool_use":
                
                # 8. THE MAGIC: We execute the command and get the output.
                output = run_bash(block.input["command"])
                
                # 9. We package the terminal's text output into a format the AI can read.
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                })
                
        # 10. THE INJECTION: We append the raw terminal output back into the history.
        # This is where the AI "remembers" what the computer told it!
        messages.append({"role": "user", "content": results})
        
        # 11. The loop immediately restarts, and the AI reads the terminal output.
```

## The "Invisible Conversation" Explained
The "Invisible Conversation" is the internal feedback loop that happens **after** the user types a prompt but **before** the AI gives its final answer. 

Unlike a standard chatbot (which only remembers what the human said), an AI Agent has a "Third Voice" in its memory: **The Computer.**

- **The Reasoning Phase**: The AI thinks about the user's request and decides it needs a tool (like a Bash terminal).
- **The Execution Phase**: The code runs the command on the computer.
- **The Injection Phase (The Magic)**: The result of that command is "injected" back into the chat history (Line 49). The user doesn't see this yet!
- **The Reaction Phase**: The AI reads the new tool result, "learns" from it, and either runs another command or finally answers the user.
