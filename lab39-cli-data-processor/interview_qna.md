# 📘 Interview Q&A – Lab 39: CLI Data Processor

1. **What is the purpose of this project?**  
   To build a real-world CLI tool that fetches and processes API data.

2. **Which library is used for HTTP requests?**  
   requests.

3. **Why is argparse used?**  
   To parse command-line arguments cleanly.

4. **Why is logging preferred over print()?**  
   Logging provides timestamps, severity levels, and better debugging.

5. **What does response.raise_for_status() do?**  
   It raises errors for HTTP failures.

6. **How is JSON validation handled?**  
   Using response.json() inside try/except.

7. **What happens if the API request fails?**  
   The error is logged and the program exits gracefully.

8. **Why is exception handling important in CLI tools?**  
   To prevent crashes and ensure reliability.

9. **What real-world systems use similar tools?**  
   DevOps pipelines, data ingestion systems, monitoring tools.

10. **Why is this lab considered a capstone project?**  
    It integrates multiple Python concepts into one practical tool.
