"""
Minimalist Timer Application
Main application file with timer display, system tray, and core functionality
"""

import sys
import json
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QSystemTrayIcon, 
                             QMenu, QAction, QWidget, QVBoxLayout)
from PyQt5.QtCore import QTimer, Qt, QPoint
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter, QColor
from pynput import keyboard
import ctypes
from ctypes import wintypes

from database import Database
from settings_dialog import SettingsDialog
from statistics_dialog import StatisticsDialog
from category_dialog import CategoryDialog


class IdleDetector:
    """Detect user inactivity on Windows"""
    
    def __init__(self):
        self.last_input_info = wintypes.LASTINPUTINFO()
        self.last_input_info.cbSize = ctypes.sizeof(self.last_input_info)
    
    def get_idle_duration(self):
        """Get idle time in seconds"""
        ctypes.windll.user32.GetLastInputInfo(ctypes.byref(self.last_input_info))
        millis = ctypes.windll.kernel32.GetTickCount() - self.last_input_info.dwTime
        return millis / 1000.0


class TimerWindow(QMainWindow):
    """Main timer window - displays only the timer"""
    
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.idle_detector = IdleDetector()
        
        # Timer state
        self.elapsed_seconds = 0
        self.is_running = False
        self.current_category = "Uncategorized"
        self.session_start = None
        
        # Load settings
        self.load_settings()
        
        # Setup UI
        self.init_ui()
        
        # Setup timers
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        
        self.idle_check_timer = QTimer()
        self.idle_check_timer.timeout.connect(self.check_idle)
        self.idle_check_timer.start(1000)  # Check every second
        
        # Setup system tray
        self.setup_tray()
        
        # Setup global hotkeys
        self.setup_hotkeys()
        
        # Make window draggable
        self.dragging = False
        self.drag_position = QPoint()
    
    def load_settings(self):
        """Load settings from database"""
        settings = self.db.get_settings()
        self.idle_threshold = settings.get('idle_threshold', 60)
        self.transparency = settings.get('transparency', 0.8)
        self.font_size = settings.get('font_size', 72)
        self.pause_hotkey = settings.get('pause_hotkey', '<ctrl>+<alt>+p')
        self.reset_hotkey = settings.get('reset_hotkey', '<ctrl>+<alt>+r')
    
    def init_ui(self):
        """Initialize the user interface"""
        # Window properties
        self.setWindowFlags(
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint | 
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(self.transparency)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Timer label
        self.timer_label = QLabel("00:00:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", self.font_size, QFont.Bold)
        self.timer_label.setFont(font)
        self.timer_label.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 150); padding: 20px; border-radius: 10px;")
        
        layout.addWidget(self.timer_label)
        central_widget.setLayout(layout)
        
        # Window size and position
        self.resize(400, 200)
        self.center_window()
    
    def center_window(self):
        """Center window on screen"""
        screen = QApplication.desktop().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def setup_tray(self):
        """Setup system tray icon and menu"""
        # Create icon
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setBrush(QColor(100, 100, 255))
        painter.drawEllipse(4, 4, 56, 56)
        painter.end()
        
        icon = QIcon(pixmap)
        
        # Create tray icon
        self.tray_icon = QSystemTrayIcon(icon, self)
        
        # Create menu
        menu = QMenu()
        
        # Start/Pause action
        self.start_pause_action = QAction("Start", self)
        self.start_pause_action.triggered.connect(self.toggle_timer)
        menu.addAction(self.start_pause_action)
        
        # Reset action
        reset_action = QAction("Reset", self)
        reset_action.triggered.connect(self.reset_timer)
        menu.addAction(reset_action)
        
        menu.addSeparator()
        
        # Category action
        category_action = QAction("Select Category", self)
        category_action.triggered.connect(self.show_category_dialog)
        menu.addAction(category_action)
        
        menu.addSeparator()
        
        # Statistics action
        stats_action = QAction("Statistics", self)
        stats_action.triggered.connect(self.show_statistics)
        menu.addAction(stats_action)
        
        # Settings action
        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.show_settings)
        menu.addAction(settings_action)
        
        menu.addSeparator()
        
        # Show/Hide action
        show_hide_action = QAction("Show/Hide Timer", self)
        show_hide_action.triggered.connect(self.toggle_visibility)
        menu.addAction(show_hide_action)
        
        # Exit action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.quit_application)
        menu.addAction(exit_action)
        
        self.tray_icon.setContextMenu(menu)
        self.tray_icon.show()
        
        # Double click to show/hide
        self.tray_icon.activated.connect(self.tray_activated)
    
    def tray_activated(self, reason):
        """Handle tray icon activation"""
        if reason == QSystemTrayIcon.DoubleClick:
            self.toggle_visibility()
    
    def setup_hotkeys(self):
        """Setup global keyboard shortcuts"""
        self.hotkey_listener = keyboard.GlobalHotKeys({
            self.pause_hotkey: self.toggle_timer,
            self.reset_hotkey: self.reset_timer,
        })
        self.hotkey_listener.start()
    
    def toggle_timer(self):
        """Start or pause the timer"""
        if self.is_running:
            self.pause_timer()
        else:
            self.start_timer()
    
    def start_timer(self):
        """Start the timer"""
        if not self.is_running:
            self.is_running = True
            self.session_start = datetime.now()
            self.timer.start(1000)  # Update every second
            self.start_pause_action.setText("Pause")
            self.update_display()
    
    def pause_timer(self):
        """Pause the timer"""
        if self.is_running:
            self.is_running = False
            self.timer.stop()
            self.start_pause_action.setText("Resume")
            self.save_session()
    
    def reset_timer(self):
        """Reset the timer"""
        was_running = self.is_running
        if was_running:
            self.save_session()
        
        self.is_running = False
        self.elapsed_seconds = 0
        self.session_start = None
        self.timer.stop()
        self.start_pause_action.setText("Start")
        self.update_display()
    
    def update_timer(self):
        """Update timer every second"""
        if self.is_running:
            self.elapsed_seconds += 1
            self.update_display()
    
    def update_display(self):
        """Update the timer display"""
        hours = self.elapsed_seconds // 3600
        minutes = (self.elapsed_seconds % 3600) // 60
        seconds = self.elapsed_seconds % 60
        
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.timer_label.setText(time_str)
        
        # Update tray tooltip
        status = "Running" if self.is_running else "Paused"
        self.tray_icon.setToolTip(f"Timer: {time_str} - {status}\nCategory: {self.current_category}")
    
    def check_idle(self):
        """Check for user inactivity"""
        if self.is_running:
            idle_time = self.idle_detector.get_idle_duration()
            if idle_time > self.idle_threshold:
                self.pause_timer()
                self.tray_icon.showMessage(
                    "Timer Paused",
                    f"Timer paused due to {int(idle_time)}s of inactivity",
                    QSystemTrayIcon.Information,
                    2000
                )
    
    def save_session(self):
        """Save current session to database"""
        if self.session_start and self.elapsed_seconds > 0:
            self.db.add_session(
                category=self.current_category,
                duration=self.elapsed_seconds,
                start_time=self.session_start,
                end_time=datetime.now()
            )
    
    def show_category_dialog(self):
        """Show category selection dialog"""
        dialog = CategoryDialog(self.db, self.current_category, self)
        if dialog.exec_():
            self.current_category = dialog.selected_category
            self.tray_icon.showMessage(
                "Category Changed",
                f"Current category: {self.current_category}",
                QSystemTrayIcon.Information,
                2000
            )
    
    def show_statistics(self):
        """Show statistics dialog"""
        dialog = StatisticsDialog(self.db, self)
        dialog.exec_()
    
    def show_settings(self):
        """Show settings dialog"""
        dialog = SettingsDialog(self.db, self)
        if dialog.exec_():
            self.load_settings()
            self.apply_settings()
    
    def apply_settings(self):
        """Apply settings to the window"""
        self.setWindowOpacity(self.transparency)
        font = QFont("Arial", self.font_size, QFont.Bold)
        self.timer_label.setFont(font)
        
        # Restart hotkey listener with new hotkeys
        self.hotkey_listener.stop()
        self.setup_hotkeys()
    
    def toggle_visibility(self):
        """Toggle window visibility"""
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.raise_()
            self.activateWindow()
    
    def quit_application(self):
        """Quit the application"""
        if self.is_running:
            self.save_session()
        self.hotkey_listener.stop()
        QApplication.quit()
    
    # Mouse events for dragging
    def mousePressEvent(self, event):
        """Handle mouse press for dragging"""
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        """Handle mouse move for dragging"""
        if self.dragging:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release"""
        self.dragging = False
    
    def closeEvent(self, event):
        """Handle window close event"""
        event.ignore()
        self.hide()


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    
    window = TimerWindow()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
