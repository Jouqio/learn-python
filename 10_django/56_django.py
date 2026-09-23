"""
Topic: Django Introduction
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Django is a batteries-included web framework built on the MVT (Model-View-Template) pattern.

# ============================================
# 2. EXAMPLE
# ============================================

# Conceptual overview only - no server started here.
print("django-admin startproject mysite   # create a project")
print("python manage.py startapp blog     # create an app")
print("python manage.py runserver         # run dev server")
print("python manage.py makemigrations && python manage.py migrate")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Write the command to start a new Django project called 'mysite'.
# EXERCISE 2 (easy): Write the command to create an app called 'blog' inside that project.
# EXERCISE 3 (easy): List the 3 letters in MVT and what each stands for.
# EXERCISE 4 (medium): Write a minimal Django view function (as code) that returns an HttpResponse.
# EXERCISE 5 (medium): Write a minimal urls.py snippet mapping '/' to that view.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Sketch (as commented pseudocode) a Django model `Post` with title, content, and created_at fields, plus its matching URL and view.


# ============================================
# 5. SUMMARY
# ============================================
# Django structures a web app into models (data), views (logic), and templates (presentation), with an ORM and admin panel included.
