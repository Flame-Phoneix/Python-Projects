Contributing to this repository
===============================

Thank you for your interest in contributing! This document explains how to report issues and submit changes so we can review them quickly.

1. Report Issues
-----------------
- Provide a clear, descriptive title.
- Describe the steps to reproduce the problem.
- Include expected vs actual behavior.
- Add environment details (OS, Python version) and any error messages.

2. Submit a Pull Request
------------------------
1. Fork the repository on GitHub.
2. Clone your fork:

   git clone https://github.com/<your-username>/Python-Projects.git

3. Create a topic branch:

   git checkout -b fix/short-description

4. Make your changes on the branch. Keep commits small and focused.
5. Run any available tests and linters locally.
6. Commit and push your branch:

   git add .
   git commit -m "Short, descriptive commit message"
   git push origin fix/short-description

7. Open a Pull Request against the repository's `main` branch. In the PR description, explain what you changed and why, and link any related issues.

3. Code Style
-------------
- Follow PEP 8 for Python code.
- Use meaningful names and add docstrings for public functions.
- Run formatting and linting tools if available (e.g., `black`, `flake8`).

4. Tests
--------
- If the repository includes tests, add tests for your changes.
- Run tests locally (commonly `pytest`). If no tests exist, describe how you validated your change in the PR.

5. Pull Request Checklist
-------------------------
- Target the `main` branch (or the branch specified by the maintainers).
- Ensure the test suite passes (if present).
- Include a clear description and changelog entry if appropriate.
- Keep the PR focused on a single issue or feature.

6. Code of Conduct
------------------
We expect contributors to be respectful and professional. If this repository includes a `CODE_OF_CONDUCT.md`, please follow it.

7. Questions
------------
If you're unsure about anything, open an issue or contact the maintainers through the repository's normal channels.

8. Adding New Projects
----------------------
- Add new projects as separate folders at the repository root (e.g., `my_project`).
- Use a short, lowercase name with underscores (no spaces).
- Include a `README.md` inside the project folder with: a short description, how to run it, required dependencies, and any sample input/output.
- If the project needs extra Python packages, either add them to the root `requirements.txt` or create a project-level `requirements.txt` and document how to install it.
- Keep assets in a clear subfolder (for example `assets/`, `images/`, or `data/`) inside the project folder.
- Add tests in a `tests/` folder or explain manual validation steps in the project's README.
- Update the top-level `Readme.md` to add the new project to the project list with a one-line description and a link to the project's README.
- Prefer small, self-contained projects and avoid changing unrelated files when adding a new project.

Thanks for contributing — your help improves this project!
