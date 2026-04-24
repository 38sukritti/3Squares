import os

file_path = 'index_combined_final_v2.html'
if os.path.exists(file_path):
    # Read the file with UTF-16LE encoding
    with open(file_path, 'r', encoding='utf-16le') as f:
        content = f.read()
    
    # Replace all instances of cursor: none with cursor: auto
    new_content = content.replace('cursor: none', 'cursor: auto')
    
    # Write back
    with open(file_path, 'w', encoding='utf-16le') as f:
        f.write(new_content)
    print("Replaced cursor: none in index_combined_final_v2.html")
else:
    print("File not found")
