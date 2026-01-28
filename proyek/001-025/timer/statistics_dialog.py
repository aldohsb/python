"""
Statistics Dialog
Dialog for viewing and editing timer statistics
"""

from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QComboBox, QHeaderView, QMessageBox, QSpinBox,
                             QTabWidget, QWidget, QGroupBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from datetime import datetime, timedelta


class StatisticsDialog(QDialog):
    """Statistics dialog for viewing and editing timer data"""
    
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.init_ui()
        self.load_statistics()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Statistics")
        self.setMinimumSize(800, 600)
        
        layout = QVBoxLayout()
        
        # Create tabs
        tabs = QTabWidget()
        tabs.addTab(self.create_sessions_tab(), "Sessions")
        tabs.addTab(self.create_summary_tab(), "Summary")
        
        layout.addWidget(tabs)
        
        # Close button
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)
        button_layout.addWidget(close_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def create_sessions_tab(self):
        """Create sessions tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Filters
        filter_layout = QHBoxLayout()
        
        filter_layout.addWidget(QLabel("Category:"))
        self.category_filter = QComboBox()
        self.category_filter.addItem("All Categories", None)
        for cat in self.db.get_categories():
            self.category_filter.addItem(cat['name'], cat['name'])
        self.category_filter.currentIndexChanged.connect(self.load_sessions)
        filter_layout.addWidget(self.category_filter)
        
        filter_layout.addWidget(QLabel("Days:"))
        self.days_filter = QSpinBox()
        self.days_filter.setRange(1, 365)
        self.days_filter.setValue(30)
        self.days_filter.valueChanged.connect(self.load_sessions)
        filter_layout.addWidget(self.days_filter)
        
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.load_sessions)
        filter_layout.addWidget(refresh_button)
        
        filter_layout.addStretch()
        layout.addLayout(filter_layout)
        
        # Sessions table
        self.sessions_table = QTableWidget()
        self.sessions_table.setColumnCount(6)
        self.sessions_table.setHorizontalHeaderLabels([
            "ID", "Category", "Duration", "Start Time", "End Time", "Actions"
        ])
        self.sessions_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.sessions_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.sessions_table.setSelectionBehavior(QTableWidget.SelectRows)
        
        layout.addWidget(self.sessions_table)
        
        widget.setLayout(layout)
        return widget
    
    def create_summary_tab(self):
        """Create summary tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Summary by category
        summary_group = QGroupBox("Total Time by Category")
        summary_layout = QVBoxLayout()
        
        self.summary_table = QTableWidget()
        self.summary_table.setColumnCount(4)
        self.summary_table.setHorizontalHeaderLabels([
            "Category", "Sessions", "Total Time", "Average Time"
        ])
        self.summary_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.summary_table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        summary_layout.addWidget(self.summary_table)
        summary_group.setLayout(summary_layout)
        
        layout.addWidget(summary_group)
        
        widget.setLayout(layout)
        return widget
    
    def load_statistics(self):
        """Load all statistics"""
        self.load_sessions()
        self.load_summary()
    
    def load_sessions(self):
        """Load sessions into table"""
        # Get filter values
        category = self.category_filter.currentData()
        days = self.days_filter.value()
        start_date = (datetime.now() - timedelta(days=days)).date().isoformat()
        
        # Get sessions
        sessions = self.db.get_sessions(category=category, start_date=start_date)
        
        # Populate table
        self.sessions_table.setRowCount(len(sessions))
        
        for row, session in enumerate(sessions):
            # ID
            id_item = QTableWidgetItem(str(session['id']))
            id_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.sessions_table.setItem(row, 0, id_item)
            
            # Category
            category_item = QTableWidgetItem(session['category'])
            category_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.sessions_table.setItem(row, 1, category_item)
            
            # Duration
            duration = self.format_duration(session['duration'])
            duration_item = QTableWidgetItem(duration)
            duration_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.sessions_table.setItem(row, 2, duration_item)
            
            # Start time
            start_time = datetime.fromisoformat(session['start_time']).strftime("%Y-%m-%d %H:%M:%S")
            start_item = QTableWidgetItem(start_time)
            start_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.sessions_table.setItem(row, 3, start_item)
            
            # End time
            end_time = datetime.fromisoformat(session['end_time']).strftime("%Y-%m-%d %H:%M:%S")
            end_item = QTableWidgetItem(end_time)
            end_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.sessions_table.setItem(row, 4, end_item)
            
            # Actions
            actions_widget = QWidget()
            actions_layout = QHBoxLayout()
            actions_layout.setContentsMargins(5, 2, 5, 2)
            
            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(lambda checked, s=session: self.edit_session(s))
            actions_layout.addWidget(edit_button)
            
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda checked, s=session: self.delete_session(s))
            actions_layout.addWidget(delete_button)
            
            actions_widget.setLayout(actions_layout)
            self.sessions_table.setCellWidget(row, 5, actions_widget)
    
    def load_summary(self):
        """Load summary statistics"""
        stats = self.db.get_total_statistics()
        
        self.summary_table.setRowCount(len(stats))
        
        for row, stat in enumerate(stats):
            # Category
            self.summary_table.setItem(row, 0, QTableWidgetItem(stat['category']))
            
            # Session count
            self.summary_table.setItem(row, 1, QTableWidgetItem(str(stat['session_count'])))
            
            # Total duration
            total_time = self.format_duration(stat['total_duration'])
            self.summary_table.setItem(row, 2, QTableWidgetItem(total_time))
            
            # Average duration
            avg_time = self.format_duration(int(stat['avg_duration']))
            self.summary_table.setItem(row, 3, QTableWidgetItem(avg_time))
    
    def edit_session(self, session):
        """Edit a session"""
        from PyQt5.QtWidgets import QInputDialog
        
        # Get current duration in HH:MM:SS format
        current_duration = self.format_duration(session['duration'])
        
        # Ask for new duration
        new_duration_str, ok = QInputDialog.getText(
            self,
            "Edit Session",
            "Enter new duration (HH:MM:SS):",
            text=current_duration
        )
        
        if ok and new_duration_str:
            try:
                # Parse duration
                parts = new_duration_str.split(':')
                hours = int(parts[0])
                minutes = int(parts[1])
                seconds = int(parts[2])
                
                new_duration = hours * 3600 + minutes * 60 + seconds
                
                # Update in database
                self.db.update_session(session['id'], new_duration)
                
                # Reload
                self.load_statistics()
                
                QMessageBox.information(self, "Success", "Session updated successfully!")
            except (ValueError, IndexError):
                QMessageBox.warning(self, "Error", "Invalid duration format. Use HH:MM:SS")
    
    def delete_session(self, session):
        """Delete a session"""
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete this session?\n\nCategory: {session['category']}\nDuration: {self.format_duration(session['duration'])}",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.db.delete_session(session['id'])
            self.load_statistics()
            QMessageBox.information(self, "Success", "Session deleted successfully!")
    
    @staticmethod
    def format_duration(seconds):
        """Format duration in seconds to HH:MM:SS"""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
