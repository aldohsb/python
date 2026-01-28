"""
Settings Dialog
Dialog for configuring application settings
"""

from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QSpinBox, QSlider, QLineEdit,
                             QGroupBox, QFormLayout)
from PyQt5.QtCore import Qt


class SettingsDialog(QDialog):
    """Settings dialog for configuring timer preferences"""
    
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.settings = db.get_settings()
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Settings")
        self.setMinimumWidth(400)
        
        layout = QVBoxLayout()
        
        # Appearance settings
        appearance_group = QGroupBox("Appearance")
        appearance_layout = QFormLayout()
        
        # Font size
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setRange(24, 200)
        self.font_size_spin.setValue(self.settings.get('font_size', 72))
        self.font_size_spin.setSuffix(" pt")
        appearance_layout.addRow("Font Size:", self.font_size_spin)
        
        # Transparency
        transparency_layout = QHBoxLayout()
        self.transparency_slider = QSlider(Qt.Horizontal)
        self.transparency_slider.setRange(30, 100)
        self.transparency_slider.setValue(int(self.settings.get('transparency', 0.8) * 100))
        self.transparency_label = QLabel(f"{self.transparency_slider.value()}%")
        self.transparency_slider.valueChanged.connect(
            lambda v: self.transparency_label.setText(f"{v}%")
        )
        transparency_layout.addWidget(self.transparency_slider)
        transparency_layout.addWidget(self.transparency_label)
        appearance_layout.addRow("Transparency:", transparency_layout)
        
        appearance_group.setLayout(appearance_layout)
        layout.addWidget(appearance_group)
        
        # Behavior settings
        behavior_group = QGroupBox("Behavior")
        behavior_layout = QFormLayout()
        
        # Idle threshold
        self.idle_threshold_spin = QSpinBox()
        self.idle_threshold_spin.setRange(10, 600)
        self.idle_threshold_spin.setValue(self.settings.get('idle_threshold', 60))
        self.idle_threshold_spin.setSuffix(" seconds")
        behavior_layout.addRow("Idle Threshold:", self.idle_threshold_spin)
        
        behavior_group.setLayout(behavior_layout)
        layout.addWidget(behavior_group)
        
        # Hotkeys settings
        hotkeys_group = QGroupBox("Keyboard Shortcuts")
        hotkeys_layout = QFormLayout()
        
        # Pause hotkey
        self.pause_hotkey_edit = QLineEdit()
        self.pause_hotkey_edit.setText(self.settings.get('pause_hotkey', '<ctrl>+<alt>+p'))
        self.pause_hotkey_edit.setPlaceholderText("e.g., <ctrl>+<alt>+p")
        hotkeys_layout.addRow("Pause/Resume:", self.pause_hotkey_edit)
        
        # Reset hotkey
        self.reset_hotkey_edit = QLineEdit()
        self.reset_hotkey_edit.setText(self.settings.get('reset_hotkey', '<ctrl>+<alt>+r'))
        self.reset_hotkey_edit.setPlaceholderText("e.g., <ctrl>+<alt>+r")
        hotkeys_layout.addRow("Reset:", self.reset_hotkey_edit)
        
        # Hotkey help
        help_label = QLabel("Format: <ctrl>+<alt>+<key> or <ctrl>+<shift>+<key>")
        help_label.setStyleSheet("color: gray; font-size: 10px;")
        hotkeys_layout.addRow("", help_label)
        
        hotkeys_group.setLayout(hotkeys_layout)
        layout.addWidget(hotkeys_group)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_settings)
        
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(save_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def save_settings(self):
        """Save settings to database"""
        # Save each setting
        self.db.set_setting('font_size', self.font_size_spin.value())
        self.db.set_setting('transparency', self.transparency_slider.value() / 100.0)
        self.db.set_setting('idle_threshold', self.idle_threshold_spin.value())
        self.db.set_setting('pause_hotkey', self.pause_hotkey_edit.text())
        self.db.set_setting('reset_hotkey', self.reset_hotkey_edit.text())
        
        self.accept()
