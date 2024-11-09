from PIL import Image
import os

class AtlasGenerator:
    def __init__(self, grid_size, output_size, texture_slots, texture_name, save_path, file_format):
        self.grid_size = grid_size  
        self.output_size = output_size  
        self.texture_slots = texture_slots  
        self.texture_name = texture_name
        self.save_path = save_path
        self.file_format = file_format 

    def generate_atlas(self):
        atlas_image = Image.new("RGBA", self.output_size)
        slot_width = self.output_size[0] // self.grid_size[1]
        slot_height = self.output_size[1] // self.grid_size[0]

        for idx, slot in enumerate(self.texture_slots):
            image_path = slot.property("image_path")
            if image_path:
                row = idx // self.grid_size[1]
                col = idx % self.grid_size[1]

                texture = Image.open(image_path)
                texture = texture.resize((slot_width, slot_height))

                x = col * slot_width
                y = row * slot_height
                atlas_image.paste(texture, (x, y))


        save_filename = f"{self.texture_name}.{self.file_format.lower()}"
        atlas_image.save(os.path.join(self.save_path, save_filename), self.file_format)
