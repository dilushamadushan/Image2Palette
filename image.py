from tkinter import Tk, filedialog
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
from PIL import Image
import os

def get_image_path():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    root.destroy()
    if not file_path:
        raise FileNotFoundError("No image file selected.")
    return file_path

image_path = get_image_path()

if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found: {image_path}")

image = mpimg.imread(image_path)
w, h, d = image.shape
pixels = image.reshape((w * h, d))

n_colors = 10  
kmeans = KMeans(n_clusters=n_colors, random_state=42)
labels = kmeans.fit_predict(pixels)
palette = np.uint8(kmeans.cluster_centers_)

counts = np.bincount(labels)
percentages = counts / counts.sum()

sorted_indices = np.argsort(-percentages)
sorted_palette = palette[sorted_indices]
sorted_percentages = percentages[sorted_indices]

def plot_color_palette(colors, percentages):
    """Plot color palette with percentages."""
    fig, ax = plt.subplots(figsize=(8, 2))
    start = 0
    for i in range(len(colors)):
        end = start + percentages[i]
        ax.add_patch(plt.Rectangle((start, 0), end - start, 1,
                                   color=colors[i] / 255))
        start = end
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title("Dominant Colors with Percentage")
    plt.show()

plt.figure(figsize=(6, 6))
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')
plt.show()

plot_color_palette(sorted_palette, sorted_percentages)

def save_palette_image(colors, file_path="palette.png"):
    palette_img = np.zeros((50, len(colors) * 50, 3), dtype=np.uint8)
    for i, color in enumerate(colors):
        palette_img[:, i*50:(i+1)*50, :] = color
    Image.fromarray(palette_img).save(file_path)
    print(f"Palette saved to {file_path}")

save_palette_image(sorted_palette)
