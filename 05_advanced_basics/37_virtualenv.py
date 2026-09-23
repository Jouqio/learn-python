"""
Topic: Virtual Environments
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Virtual environments isolate a project's dependencies from the system Python and from other projects.

# ============================================
# 2. EXAMPLE
# ============================================

print("python -m venv .venv          # create a virtual environment")
print(".venv\\Scripts\\activate         # activate on Windows")
print("source .venv/bin/activate       # activate on Linux/macOS")
print("pip install -r requirements.txt # install project dependencies")
print("deactivate                     # leave the virtual environment")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Write the command to create a virtual environment named .venv.
# EXERCISE 2 (easy): Write the activation command for your operating system.
# EXERCISE 3 (easy): Write the command to freeze installed packages into requirements.txt.
# EXERCISE 4 (medium): Explain why each project should have its own virtual environment.
# EXERCISE 5 (medium): Write the command to deactivate the current virtual environment.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a short setup guide (as a multi-line string) for a new contributor to this repository, from cloning to running the first script.


# ============================================
# 5. SUMMARY
# ============================================
# Virtual environments prevent dependency conflicts between projects and keep your global Python clean.
