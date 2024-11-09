# Texture Atlas Generator
This tool allows you to generate texture atlases from a set of images. Simply drag and drop your images into the interface, adjust your output settings and hit "Generate Atlas." The tool will then pack your images into a single texture atlas. You can download the stand-alone and run it directly (atlas_yool.exe) or run the Python script directly by downloading all the files and executing atals_tool.py. In this case, you will need to install the following libraries: PIL, PyQt5.

 ![ShowCase](https://github.com/user-attachments/assets/7022664e-3d2b-48a3-bcb4-815e6c9fb322)



## Actions
### Drag and Drop Images
- You can drag and drop image files directly onto the slots in the grid. Simply drag an image from your file explorer and drop it into any of the available slots to add it to your atlas.
- Once an image is added, you can see a preview of the image inside the slot. The tool will automatically resize the images to fit the grid, but if needed, you can adjust the size in the settings.
### Right-Click to Remove Images
- If you want to remove an image from a slot, simply right-click on the image preview inside a slot. This will clear the image and reset the slot, allowing you to replace it with a new image if needed.
### Adjust Grid Size
- Use the dropdown menu to select the desired grid size for your atlas (e.g., 2x2, 4x4). This will automatically update the layout of the slots in the grid, creating the correct number of image slots based on your selection.
### Slot Layout
- The grid layout updates automatically based on the number of slots specified in the grid size selection. You can add or remove images by interacting with individual slots.
### Clear Grid
- If you want to remove all images from the grid and start fresh, simply click the Clear button. This will clear all the image slots, and you can begin adding new images again.

## More
- The tool supports TGA, PNG, and other common image formats for input. However you can only output in TGA or PNG.
- Make sure the images you add are all the same size or have sizes that are compatible with each other to ensure proper packing. The tool will automatically adjust if needed, but consistent sizes help prevent layout issues.
- To see all possible actions hit the "Help" button.
