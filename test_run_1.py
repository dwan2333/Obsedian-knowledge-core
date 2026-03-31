# The main function that starts our AI agent. You give it a 'query' (your question or command).
def agent_loop(query):
    
    # 1. THE MEMORY: We create the chat history. It starts with just your initial question.
    messages = [{"role": "user", "content": query}]
    
    # 2. THE ENGINE: This is an infinite loop. It will keep running until the AI decides it is finished.
    while True:
        
        # 3. THE REQUEST: We send the chat history AND our list of "TOOLS" to Anthropic's server.
        # This tells the AI: "Here is the conversation, and by the way, you have permission to use a Bash terminal."
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
        # If the stop reason is NOT "tool_use", it means the AI just typed a normal text answer to you. 
        # We break the loop and finish.
        if response.stop_reason != "tool_use":
            return 
            
        # 6. TOOL EXECUTION: If we reach this line, the AI decided it needs to run a command 
        # before it can answer you. We create an empty list to store the terminal outputs.
        results = [] 
        
        # 7. We scan through the AI's response to find the specific tool it wants to use...
        for block in response.content:
            if block.type == "tool_use":
                
                # 8. THE MAGIC: We extract the exact bash command the AI wrote (like 'ls' or 'cat file.py'), 
                # and we literally execute it on your computer's real terminal using a helper function.
                output = run_bash(block.input["command"])
                
                # 9. We package the terminal's text output into a specific format that the AI can read.
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                })
                
        # 10. THE INJECTION: We append the raw terminal output back into the chat history as a "User" message.
        messages.append({"role": "user", "content": results})
        
        # 11. The loop immediately restarts at Step 2. 
        # The AI reads the terminal output we just injected, thinks about it, and decides its next move!
