# LLM Security Helper

LLM Security Helper is a simple app that helps identify security problems in code or AI app designs. It uses a third-party LLM (like OpenAI) to analyze your input and give clear recommendations on fixing security issues. The app has two main modes:

1. Code Security Check – Finds vulnerabilities in code snippets (like SQL injection, hardcoded passwords, unsafe commands) and gives step-by-step fixes.  
2. GenAI Spec Risk Check – Reviews AI app specifications, finds potential security risks, and maps them to OWASP Top 10 for LLM applications and ATLAS threat categories with clear mitigations.

## How to Use

1. Open the `llm-security-helper` folder.  
2. Make sure you have Python 3.10 or higher installed.  
3. Copy `.env.example` to `.env` and put your OpenAI API key inside like this:


4. Run the app with Streamlit:


5. In the browser window, choose the analysis type: **Code Security Check** or **GenAI Spec Risk Check**.  
6. Paste your code snippet or AI app specification into the text box.  
7. Click **Analyze** and see the results.

## Example Inputs

*Code Security Check Example:*

```python
username = input("Username: ")
query = "SELECT * FROM users WHERE username = '" + username + "'"
cursor.execute(query)

**GenAI Spec Risk Check:**
A travel assistant app that can automatically book flights and hotels, stores user credit card information, and interacts with external APIs.

