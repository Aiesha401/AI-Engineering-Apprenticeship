# Day 1

## What did I build?

Today I built the foundation for my AI Engineering workspace. I organized my project structure, installed and configured Python correctly, set up VS Code, created a virtual environment (`venv`), and prepared my project for future development.



## What did I learn?

Today I learned that setting up a development environment is an important part of software engineering.

I learned about:
- Python installation and how Windows finds Python using the PATH environment variable.
- The difference between `python` and `py`.
- What `pip` is and why it is used.
- Why virtual environments (`venv`) are necessary.
- Why every project should have its own isolated environment.
- Why files like `.gitignore`, `README.md`, and `requirements.txt` are important.
- The difference between creating files in File Explorer and VS Code.



## Biggest challenge today

The biggest challenge was that Python was installed on my computer, but Windows couldn't recognize the `python` command. This prevented me from creating my virtual environment initially.



## How did I solve it?

Instead of reinstalling Python immediately, I learned how to debug the problem.

I discovered that:
- Python was installed correctly.
- The Microsoft App Execution Alias was intercepting the `python` command.
- Disabling the `python.exe` and `python3.exe` App Installer aliases fixed the issue.
- After that, Python and pip worked correctly, and I was able to create and activate my virtual environment successfully.



## What surprised me?

I was surprised that we didn't write any AI code today.

Instead, I realized how much work goes into preparing a professional development environment before writing a single line of application code.

I also learned that debugging the environment is a real engineering skill, not just an annoying setup step.



## One thing I still don't understand

I understand that a virtual environment creates an isolated workspace, but I still want to understand **how it works internally**.

Questions I have:
- How does the virtual environment use the global Python installation while keeping packages separate?
- Why does it create another `python.exe`?
- What exactly changes when I activate the virtual environment?