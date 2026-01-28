"""
Database module for timer application
Handles all database operations including sessions, categories, and settings
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path


class Database:
    """Database handler for timer application"""
    
    def __init__(self, db_path="timer_data.db"):
        """Initialize database connection"""
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()
        self.init_default_data()
    
    def create_tables(self):
        """Create necessary database tables"""
        cursor = self.conn.cursor()
        
        # Sessions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                duration INTEGER NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Categories table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                color TEXT DEFAULT '#3366FF',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Settings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
        """)
        
        self.conn.commit()
    
    def init_default_data(self):
        """Initialize default categories and settings"""
        cursor = self.conn.cursor()
        
        # Default categories
        default_categories = [
            ("Uncategorized", "#808080"),
            ("Work", "#3366FF"),
            ("Study", "#FF6633"),
            ("Exercise", "#33CC33"),
            ("Reading", "#9933FF"),
            ("Project", "#FF3366"),
        ]
        
        for name, color in default_categories:
            cursor.execute("""
                INSERT OR IGNORE INTO categories (name, color)
                VALUES (?, ?)
            """, (name, color))
        
        # Default settings
        default_settings = {
            'idle_threshold': 60,
            'transparency': 0.8,
            'font_size': 72,
            'pause_hotkey': '<ctrl>+<alt>+p',
            'reset_hotkey': '<ctrl>+<alt>+r',
        }
        
        for key, value in default_settings.items():
            cursor.execute("""
                INSERT OR IGNORE INTO settings (key, value)
                VALUES (?, ?)
            """, (key, json.dumps(value)))
        
        self.conn.commit()
    
    # Session methods
    def add_session(self, category, duration, start_time, end_time):
        """Add a new session"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO sessions (category, duration, start_time, end_time)
            VALUES (?, ?, ?, ?)
        """, (category, duration, start_time.isoformat(), end_time.isoformat()))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_sessions(self, category=None, start_date=None, end_date=None):
        """Get sessions with optional filters"""
        cursor = self.conn.cursor()
        query = "SELECT * FROM sessions WHERE 1=1"
        params = []
        
        if category:
            query += " AND category = ?"
            params.append(category)
        
        if start_date:
            query += " AND date(start_time) >= ?"
            params.append(start_date)
        
        if end_date:
            query += " AND date(end_time) <= ?"
            params.append(end_date)
        
        query += " ORDER BY start_time DESC"
        
        cursor.execute(query, params)
        return cursor.fetchall()
    
    def update_session(self, session_id, duration):
        """Update a session duration"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE sessions
            SET duration = ?
            WHERE id = ?
        """, (duration, session_id))
        self.conn.commit()
    
    def delete_session(self, session_id):
        """Delete a session"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
        self.conn.commit()
    
    def get_statistics(self, category=None, days=7):
        """Get statistics for the last N days"""
        cursor = self.conn.cursor()
        
        query = """
            SELECT 
                category,
                COUNT(*) as session_count,
                SUM(duration) as total_duration,
                AVG(duration) as avg_duration,
                date(start_time) as date
            FROM sessions
            WHERE date(start_time) >= date('now', '-' || ? || ' days')
        """
        params = [days]
        
        if category:
            query += " AND category = ?"
            params.append(category)
        
        query += " GROUP BY category, date(start_time) ORDER BY date DESC"
        
        cursor.execute(query, params)
        return cursor.fetchall()
    
    def get_total_statistics(self):
        """Get total statistics by category"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT 
                category,
                COUNT(*) as session_count,
                SUM(duration) as total_duration,
                AVG(duration) as avg_duration
            FROM sessions
            GROUP BY category
            ORDER BY total_duration DESC
        """)
        return cursor.fetchall()
    
    # Category methods
    def get_categories(self):
        """Get all categories"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM categories ORDER BY name")
        return cursor.fetchall()
    
    def add_category(self, name, color="#3366FF"):
        """Add a new category"""
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO categories (name, color)
                VALUES (?, ?)
            """, (name, color))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None
    
    def update_category(self, category_id, name, color):
        """Update a category"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE categories
            SET name = ?, color = ?
            WHERE id = ?
        """, (name, color, category_id))
        self.conn.commit()
    
    def delete_category(self, category_id):
        """Delete a category"""
        cursor = self.conn.cursor()
        
        # Get category name
        cursor.execute("SELECT name FROM categories WHERE id = ?", (category_id,))
        row = cursor.fetchone()
        if not row:
            return
        
        category_name = row['name']
        
        # Update sessions to Uncategorized
        cursor.execute("""
            UPDATE sessions
            SET category = 'Uncategorized'
            WHERE category = ?
        """, (category_name,))
        
        # Delete category
        cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        self.conn.commit()
    
    # Settings methods
    def get_settings(self):
        """Get all settings"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT key, value FROM settings")
        settings = {}
        for row in cursor.fetchall():
            settings[row['key']] = json.loads(row['value'])
        return settings
    
    def get_setting(self, key, default=None):
        """Get a single setting"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM settings WHERE key = ?", (key,))
        row = cursor.fetchone()
        if row:
            return json.loads(row['value'])
        return default
    
    def set_setting(self, key, value):
        """Set a setting"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO settings (key, value)
            VALUES (?, ?)
        """, (key, json.dumps(value)))
        self.conn.commit()
    
    def close(self):
        """Close database connection"""
        self.conn.close()
