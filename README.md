# Extract Unicode Ranges from Font File

This is a lightweight GUI-based Python tool that allows you to extract and compress all used Unicode code points from a given `.ttf` or `.otf` font file. The result is saved as a range-compressed text file like:

```
0000-007F,00A0,00AB,00BB,00D7,00F7,060C,060D,...
```

---

## 🔧 Requirements

- **Python 3.8+** (Recommended: 64-bit)
- **pip** (Python package manager)
- OS: Windows / Linux / macOS

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nsediq/unicode-font-extractor.git
cd unicode-font-extractor
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate.bat     # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you're not using `requirements.txt`, install manually:

```bash
pip install fonttools
```

> `tkinter` is included with standard Python distributions. If it's missing, install via OS package manager (Linux) or re-install Python with GUI options.

---

## 🚀 Running the Program

To launch the tool:

```bash
python extract_unicode_gui.py
```

A window will appear where you can:

1. Select a font file (`.ttf` / `.otf`)
2. Extract Unicode code points
3. Save the compressed Unicode range list as `.txt`

---

## 💡 Features

- GUI interface (no command-line required)
- Supports all Unicode fonts with CMAP tables
- Output in compact range format
- Unicode-safe UTF-8 export

---

## 🧪 Example

Given a font that includes:
```
U+0627 (ARABIC LETTER ALEF), U+0628 (ARABIC LETTER BEH), U+062A (ARABIC LETTER TEH), U+062B
```

The output will be:
```
0627-0628,062A-062B
```

---

## 🖼️ Screenshot

> _(Optional: Add a screenshot of the GUI interface here if you like)_

---

## 🧰 Development Notes

- Python GUI built with `tkinter`
- Font parsing via `fontTools.ttLib.TTFont`
- Cross-platform support (Windows, Linux, macOS)

---

## 🗜️ Optional: Build as Standalone `.exe`

To build a Windows `.exe` version:

```bash
pip install pyinstaller

pyinstaller --noconsole --onefile extract_unicode_gui.py
```

The resulting `.exe` will be located in the `dist/` folder.

---

## 📁 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🤝 Contributions

Pull requests and suggestions are welcome! Please open an issue or submit a PR.

---

## 🔗 Author

Made by [Nader Sediq] • [nader.sediq@gmail.com]
