# Syntax: open(filename, mode, buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file = open("example.txt", "r", encoding="utf-8")

# Modes:
# 'r' = read (default)
# 'w' = write (overwrite)
# 'a' = append
# 'x' = create new
# 'b' = binary mode
# 't' = text mode (default)
# '+' = read/write
# Example: "r+", "w+", "a+"

# ⿢ Closing Files
file.close()  # manual
# Recommended: Context manager auto-closes
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()

# ⿣ Reading Files
with open("example.txt", "r") as file:
    all_text = file.read()        # Read all content
    first_line = file.readline()  # Read single line
    lines = file.readlines()      # Read all lines into list

# Iterate line by line efficiently
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read with size
with open("example.txt", "r") as file:
    chunk = file.read(1024)  # Read 1024 chars

# ⿤ Writing Files
with open("example.txt", "w") as file:
    file.write("Hello World\n")  # Overwrite
with open("example.txt", "a") as file:
    file.write("Append this line\n")
lines = ["Line 1\n", "Line 2\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)

# ⿥ File Pointer / Cursor
with open("example.txt", "r") as file:
    print(file.tell())  # Cursor position
    file.seek(0)        # Move cursor to start

# ⿦ Binary Files
with open("image.png", "rb") as file:
    data = file.read()
with open("image_copy.png", "wb") as file:
    file.write(data)

# ⿧ Random Access & Seek
with open("example.txt", "r+") as file:
    file.seek(5)          # Move cursor
    file.write("INSERT")  # Overwrites from cursor position
    file.seek(0)
    print(file.read())

# ⿨ Exception Handling
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print("I/O error:", e)

# ⿩ Working with Paths: pathlib (modern & recommended)
from pathlib import Path
file_path = Path("example.txt")
print(file_path.exists())
file_path.write_text("Pathlib write\n", encoding="utf-8")
print(file_path.read_text(encoding="utf-8"))

# ⿡⿠ Temporary Files
import tempfile
with tempfile.TemporaryFile(mode="w+t") as tmp:
    tmp.write("Temporary data\n")
    tmp.seek(0)
    print(tmp.read())

# ⿡⿡ JSON File Handling
import json
data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
with open("data.json", "r") as f:
    loaded_data = json.load(f)

# ⿡⿢ CSV File Handling
import csv
rows = [["Name", "Age"], ["Bob", 25], ["Alice", 30]]
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ⿡⿣ File Metadata & OS Utilities
import os
print(os.path.exists("example.txt"))
print(os.path.getsize("example.txt"))
print(os.path.abspath("example.txt"))
print(os.listdir("."))  # List files in directory
os.rename("old.txt", "new.txt")
os.remove("new.txt")

# ⿡⿤ File Compression (gzip)
import gzip
with gzip.open("compressed.txt.gz", "wt") as f:
    f.write("Compressed data\n")
with gzip.open("compressed.txt.gz", "rt") as f:
    print(f.read())

# ⿡⿥ Efficient Reading for Large Files
with open("large_file.txt", "r") as file:
    for line in file:
        process(line)  # Replace with actual processing

# ⿡⿦ Advanced: Memory Mapping
import mmap
with open("example.txt", "r+") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(mm.readline())
    mm.close()

