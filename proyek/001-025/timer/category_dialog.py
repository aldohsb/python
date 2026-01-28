"""
Category Dialog
Dialog for selecting and managing timer categories
"""

from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QListWidget, QListWidgetItem,
                             QLineEdit, QColorDialog, QMessageBox, QInputDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush


class CategoryDialog(QDialog):
    """Dialog for selecting and managing categories"""
    
    def __init__(self, db, current_category, parent=None):
        super().__init__(parent)
        self.db = db
        self.selected_category = current_category
        self.init_ui()
        self.load_categories()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Select Category")
        self.setMinimumSize(400, 500)
        
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Select a category for your timer:")
        title.setStyleSheet("font-weight: bold; font-size: 12pt;")
        layout.addWidget(title)
        
        # Category list
        self.category_list = QListWidget()
        self.category_list.itemDoubleClicked.connect(self.select_category)
        layout.addWidget(self.category_list)
        
        # Management buttons
        manage_layout = QHBoxLayout()
        
        add_button = QPushButton("Add New")
        add_button.clicked.connect(self.add_category)
        manage_layout.addWidget(add_button)
        
        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(self.edit_category)
        manage_layout.addWidget(edit_button)
        
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_category)
        manage_layout.addWidget(delete_button)
        
        layout.addLayout(manage_layout)
        
        # Action buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        select_button = QPushButton("Select")
        select_button.clicked.connect(self.select_category_button)
        select_button.setDefault(True)
        button_layout.addWidget(select_button)
        
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def load_categories(self):
        """Load categories into list"""
        self.category_list.clear()
        
        categories = self.db.get_categories()
        
        for cat in categories:
            item = QListWidgetItem(cat['name'])
            item.setData(Qt.UserRole, cat)
            
            # Set color
            color = QColor(cat['color'])
            item.setBackground(QBrush(color.lighter(160)))
            item.setForeground(QBrush(QColor(0, 0, 0)))
            
            # Highlight current category
            if cat['name'] == self.selected_category:
                item.setSelected(True)
            
            self.category_list.addItem(item)
    
    def select_category(self, item):
        """Select category on double click"""
        cat_data = item.data(Qt.UserRole)
        self.selected_category = cat_data['name']
        self.accept()
    
    def select_category_button(self):
        """Select category on button click"""
        current_item = self.category_list.currentItem()
        if current_item:
            cat_data = current_item.data(Qt.UserRole)
            self.selected_category = cat_data['name']
            self.accept()
        else:
            QMessageBox.warning(self, "Warning", "Please select a category!")
    
    def add_category(self):
        """Add a new category"""
        # Get category name
        name, ok = QInputDialog.getText(
            self,
            "Add Category",
            "Category name:"
        )
        
        if not ok or not name:
            return
        
        # Get color
        color = QColorDialog.getColor(QColor("#3366FF"), self, "Select Color")
        
        if not color.isValid():
            return
        
        # Add to database
        category_id = self.db.add_category(name, color.name())
        
        if category_id:
            self.load_categories()
            QMessageBox.information(self, "Success", f"Category '{name}' added successfully!")
        else:
            QMessageBox.warning(self, "Error", "Category already exists!")
    
    def edit_category(self):
        """Edit selected category"""
        current_item = self.category_list.currentItem()
        
        if not current_item:
            QMessageBox.warning(self, "Warning", "Please select a category to edit!")
            return
        
        cat_data = current_item.data(Qt.UserRole)
        
        # Don't allow editing Uncategorized
        if cat_data['name'] == "Uncategorized":
            QMessageBox.warning(self, "Warning", "Cannot edit the Uncategorized category!")
            return
        
        # Get new name
        name, ok = QInputDialog.getText(
            self,
            "Edit Category",
            "Category name:",
            text=cat_data['name']
        )
        
        if not ok or not name:
            return
        
        # Get new color
        color = QColorDialog.getColor(QColor(cat_data['color']), self, "Select Color")
        
        if not color.isValid():
            return
        
        # Update in database
        self.db.update_category(cat_data['id'], name, color.name())
        self.load_categories()
        
        QMessageBox.information(self, "Success", f"Category '{name}' updated successfully!")
    
    def delete_category(self):
        """Delete selected category"""
        current_item = self.category_list.currentItem()
        
        if not current_item:
            QMessageBox.warning(self, "Warning", "Please select a category to delete!")
            return
        
        cat_data = current_item.data(Qt.UserRole)
        
        # Don't allow deleting Uncategorized
        if cat_data['name'] == "Uncategorized":
            QMessageBox.warning(self, "Warning", "Cannot delete the Uncategorized category!")
            return
        
        # Confirm deletion
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete the category '{cat_data['name']}'?\n\nAll sessions in this category will be moved to 'Uncategorized'.",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.db.delete_category(cat_data['id'])
            self.load_categories()
            QMessageBox.information(self, "Success", f"Category '{cat_data['name']}' deleted successfully!")
