import tkinter as tk
from tkinter import filedialog, messagebox
from fontTools.ttLib import TTFont

def compress_unicode_ranges(unicodes):
    unicodes = sorted(set(unicodes))
    if not unicodes:
        return ""
    ranges = []
    start = end = unicodes[0]

    for code in unicodes[1:]:
        if code == end + 1:
            end = code
        else:
            if start == end:
                ranges.append(f"{start:04X}")
            else:
                ranges.append(f"{start:04X}-{end:04X}")
            start = end = code

    if start == end:
        ranges.append(f"{start:04X}")
    else:
        ranges.append(f"{start:04X}-{end:04X}")

    return ",".join(ranges)

def extract_unicode_from_font(font_path):
    font = TTFont(font_path)
    unicodes = []
    for table in font['cmap'].tables:
        unicodes.extend(table.cmap.keys())
    return unicodes

def select_font_file():
    font_path = filedialog.askopenfilename(
        title="Select a font file",
        filetypes=[("Font Files", "*.ttf *.otf")]
    )
    if not font_path:
        return

    try:
        codes = extract_unicode_from_font(font_path)
        compressed = compress_unicode_ranges(codes)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read font file:\n{e}")
        return

    output_path = filedialog.asksaveasfilename(
        title="Save output as...",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if output_path:
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(compressed)
            messagebox.showinfo("Success", f"Unicode list saved to:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Save Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Extract Unicode Ranges from Font File")
root.geometry("400x150")
root.resizable(False, False)

btn = tk.Button(root, text="Select Font File and Extract Unicode Ranges", command=select_font_file, font=("Segoe UI", 11))
btn.pack(expand=True, pady=40)

root.mainloop()
