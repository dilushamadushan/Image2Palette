# 🎨 Image Color Palette Extractor

This Python project allows you to **extract the dominant colors** from an image using **KMeans clustering**. It displays the original image, shows a color palette with each color's percentage, and saves the palette to a PNG file.

## 🚀 Features

- 🖼️ Interactive file picker to select any image
- 🎨 Extracts top N dominant colors using KMeans clustering
- 📊 Displays color palette sorted by dominance
- 💾 Saves palette image as `palette.png`
- 📈 Shows color percentage visually

## 📦 Installation

### 1. Clone the repository
```bash
https://github.com/dilushamadushan/Image2Palette.git
```

### 2. Install dependencies
Install the required Python packages using pip:

```bash
pip install matplotlib numpy scikit-learn pillow
```

## 🖥️ Usage

1. Run the script using:
```bash
python image.py
```

2. A file dialog will open. Select an image file (.jpg, .png, .bmp, etc.).

3. The script will:
   - Display the original image
   - Show a horizontal color palette of the most dominant colors
   - Save the color palette to `palette.png`

## 🧪 Example Output

- **Original Image**: Displayed in a popup window
- **Color Palette**: Shows a horizontal bar with colors sized by percentage
- **Saved File**: `palette.png` – color blocks for the top N colors

## ⭐ Show your support

Give a ⭐️ if this project helped you!
