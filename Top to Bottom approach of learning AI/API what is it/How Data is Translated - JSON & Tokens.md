When a user types a message, it undergoes a massive transformation before the AI can understand it.

- **Step 1: Text to JSON:** The user's text is wrapped in a structured data envelope (JSON) that includes metadata like timestamps, user IDs, and chat history.
    
- **Step 2: Tokenization (The Math Translation):** Neural networks do not read English. The API unpacks the JSON and translates the text into **tokens** (arrays of numerical IDs).
    
- **Step 3: Processing & Reversing:** The AI runs those numbers through its mathematical weights (like a massive version of $y = f(Wx + b)$) to predict new output numbers. The API catches these numbers, translates them back into text, packages them into a new JSON envelope, and sends them to the user's screen.
