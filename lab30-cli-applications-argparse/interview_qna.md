# 📘 Interview Q&A – Lab 30: CLI Applications with argparse

1. **What is a CLI application?**  
   A CLI application allows users to interact with a program using terminal commands.

2. **Which Python module is commonly used for CLI parsing?**  
   The built-in argparse module.

3. **What does ArgumentParser do?**  
   It defines the CLI program and handles argument parsing and validation.

4. **What is an optional argument in argparse?**  
   An argument that is not mandatory, usually prefixed with --.

5. **How do you access parsed arguments?**  
   Through the object returned by `parser.parse_args()`.

6. **What happens if no arguments are passed?**  
   The script runs with default behavior.

7. **What is the purpose of --help?**  
   It displays automatically generated usage and help information.

8. **Why is argparse preferred over sys.argv?**  
   It provides validation, help messages, and cleaner code.

9. **Does argparse support type conversion?**  
   Yes, it converts inputs based on the specified type.

10. **Where are CLI tools commonly used?**  
    In automation scripts, DevOps tooling, and security utilities.
