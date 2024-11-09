# atlas_ui.py
from PyQt5.QtWidgets import (QWidget, QComboBox, QLineEdit, QLabel, 
                             QPushButton, QFileDialog, QVBoxLayout, 
                             QGridLayout, QApplication, QSizePolicy, 
                             QFrame, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QDragEnterEvent, QDropEvent
import sys

class DraggableLabel(QLabel):
    """Custom label widget to support drag-and-drop and right-click deletion."""
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setFrameShape(QFrame.Box) 

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            file_path = event.mimeData().urls()[0].toLocalFile()
            pixmap = QPixmap(file_path).scaled(100, 100, Qt.KeepAspectRatio)
            self.setPixmap(pixmap)
            self.setProperty("image_path", file_path)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.clear()
            self.setProperty("image_path", None) 


class AtlasUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid_size_label = QLabel("Grid Size:")
        self.grid_size_combo = QComboBox()
        self.grid_size_combo.addItems(["2x2", "4x4"])
        self.grid_size_combo.currentIndexChanged.connect(self.update_slots)

        self.output_size_label = QLabel("Output Size:")
        self.output_size_combo = QComboBox()
        self.output_size_combo.addItems(["512x512", "1024x1024", "2048x2048", "4096x4096"])
        self.file_format_label = QLabel("File Format:")
        self.file_format_combo = QComboBox()
        self.file_format_combo.addItems(["TGA","PNG"])

        self.texture_name_label = QLabel("Texture Name:")
        self.texture_name_input = QLineEdit()
        self.save_path_label = QLabel("Save Path:")
        self.save_path_input = QLineEdit()
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_save_path)

        self.slot_layout = QGridLayout()
        self.slots = []

        self.generate_button = QPushButton("Generate Atlas")
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_slots)

        self.help_button = QPushButton("Help")
        self.help_button.clicked.connect(self.show_help)

        layout = QVBoxLayout()
        layout.addWidget(self.grid_size_label)
        layout.addWidget(self.grid_size_combo)
        layout.addWidget(self.output_size_label)
        layout.addWidget(self.output_size_combo)
        layout.addWidget(self.texture_name_label)
        layout.addWidget(self.texture_name_input)
        layout.addWidget(self.save_path_label)
        layout.addWidget(self.save_path_input)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.file_format_label)
        layout.addWidget(self.file_format_combo)
        layout.addLayout(self.slot_layout)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.help_button)
        
        self.setLayout(layout)
        self.setWindowTitle("Atlas Texture Generator")
        self.update_slots() 
        self.show()

    def update_slots(self):
        """Update the slots layout based on the selected grid size."""
        for i in reversed(range(self.slot_layout.count())):
            widget = self.slot_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        self.slots.clear()

        grid_text = self.grid_size_combo.currentText().split("x")
        rows, cols = int(grid_text[0]), int(grid_text[1])
        for row in range(rows):
            for col in range(cols):
                slot = DraggableLabel()
                slot.setFixedSize(100, 100)
                self.slot_layout.addWidget(slot, row, col)
                self.slots.append(slot)

    def browse_save_path(self):
        save_path = QFileDialog.getExistingDirectory(self, "Select Save Folder")
        if save_path:
            self.save_path_input.setText(save_path)

    def clear_slots(self):
        """Clear all images in the slots."""
        for slot in self.slots:
            slot.clear()
            slot.setProperty("image_path", None) 

    def show_help(self):
        """Show help information in a message box."""
        help_message = (
            "<b>Available Actions:</b><ul>"
            "<li>Drag and drop an image file into a slot to add it.</li>"
            "<li>Right-click on a slot to remove the image.</li>"
            "<li>Click 'Clear' to remove all images from the grid.</li>"
            "<li>Use 'Generate Atlas' to export the texture atlas.</li>"
            "</ul>"
        )
        QMessageBox.information(self, "Help", help_message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AtlasUI()
    sys.exit(app.exec_())
