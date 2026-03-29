It is crucial to understand the difference between the tools you build and the services you rent.

- **FastAPI (Your Backend):** This is a Python web framework. You use it to build your _own_ custom API—the "storefront." This server handles your user logins, pulls your database info (like live-stream transcripts), and enforces your app's specific business rules.
    
- **The AI API (e.g., OpenAI, Anthropic):** This is the "wholesale warehouse" of intelligence. Your FastAPI server sends a secure request behind the scenes to the AI company's API, paying fractions of a cent per word to rent their model's computational power (Inference).
    
- **The Flow:** User $\rightarrow$ Frontend $\rightarrow$ Your FastAPI Server $\rightarrow$ AI Company's Server $\rightarrow$ (And back again).