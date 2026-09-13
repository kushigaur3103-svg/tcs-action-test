"""
Database query builder module with intentional SQL Injection vulnerability.
"""

import sqlite3
from flask import request


def find_user_by_id():
    """Fetches user record using untrusted query parameter in raw SQL string."""
    user_id = request.args.get("user_id")
    
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    
    # CWE-89: Tainted user input concatenated directly into raw SQL string
    query = "SELECT id, username, email FROM users WHERE id = " + user_id
    cursor.execute(query)
    
    return cursor.fetchone()
