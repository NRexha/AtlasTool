from PyQt5.QtWidgets import QApplication
from atlas_ui import AtlasUI
from atlas_logic import AtlasGenerator
import sys

class AtlasApp(AtlasUI):
    def __init__(self):
        super().__init__()
        self.generate_button.clicked.connect(self.create_atlas)

    def create_atlas(self):
        grid_size_text = self.grid_size_combo.currentText().split("x")
        grid_size = (int(grid_size_text[0]), int(grid_size_text[1]))

        output_size_text = self.output_size_combo.currentText().split("x")
        output_size = (int(output_size_text[0]), int(output_size_text[1]))

        file_format = self.file_format_combo.currentText()

        texture_name = self.texture_name_input.text()
        save_path = self.save_path_input.text()

        generator = AtlasGenerator(grid_size, output_size, self.slots, texture_name, save_path, file_format)
        generator.generate_atlas()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    atlas_app = AtlasApp()
    sys.exit(app.exec_())
