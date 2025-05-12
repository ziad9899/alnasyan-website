#!/usr/bin/env python3.11
import os

def fix_paths_in_file(filepath, is_in_subdir_logical):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        if is_in_subdir_logical:
            # Order matters: replace '../images/' first, then 'images/'
            # ../images/path -> ../path (correct for images in root, referenced from subdir)
            content = content.replace('src="../images/', 'src="../')
            content = content.replace('data-image-src="../images/', 'data-image-src="../')
            content = content.replace('url(\"../images/', 'url(\"../') # For CSS url("../images/...")
            content = content.replace('url(\\'../images/
', 'url(\\'../
') # For CSS url('../images/...')
            content = content.replace('url(../images/', 'url(../')     # For CSS url(../images/...)
            content = content.replace('xlink:href="../images/', 'xlink:href="../')
            
            # images/path -> ../path (correct for images in root, referenced from subdir as if they were in subdir/images)
            content = content.replace('src="images/', 'src="../')
            content = content.replace('data-image-src="images/', 'data-image-src="../')
            content = content.replace('url(\"images/', 'url(\"../') # For CSS url("images/...")
            content = content.replace('url(\\'images/
', 'url(\\'../
') # For CSS url('images/...')
            content = content.replace('url(images/', 'url(../')     # For CSS url(images/...)
            content = content.replace('xlink:href="images/', 'xlink:href="../')
            content = content.replace('"logo": "images/', '"logo": "../') # For JSON-LD in sub-HTMLs
            content = content.replace('href="images/', 'href="../') # For other hrefs like <a href="images/...">

        else: # Root files (or CSS files in root)
            # images/path -> path
            content = content.replace('src="images/', 'src="')
            content = content.replace('data-image-src="images/', 'data-image-src="')
            content = content.replace('url(\"images/', 'url("')      # For CSS url("images/...")
            content = content.replace('url(\\'images/
', 'url(\\'
')      # For CSS url('images/...')
            content = content.replace('url(images/', 'url(')          # For CSS url(images/...)
            content = content.replace('xlink:href="images/', 'xlink:href="')
            content = content.replace('"logo": "images/', '"logo": "') # For JSON-LD in root HTMLs
            content = content.replace('href="images/', 'href="') # For other hrefs like <a href="images/...">
            # Removed special handling for inline styles, relying on general url() replacements
        
        # Corrected indentation for this block
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Processed and modified: {filepath}")
        else:
            print(f"Processed (no changes needed, or patterns not found): {filepath}")
            
    except Exception as e:
        print(f"Error processing file {filepath}: {str(e)}")

# List of files and their logical subdir status (True if the file ITSELF is in a logical subdir like 'blog/')
files_to_process = {
    "index.html": False,
    "Page-1.html": False, "Page-2.html": False, "Page-3.html": False, "Page-4.html": False, "Page-5.html": False,
    "nicepage.css": False,
    "index.css": False,
    "Page-1.css": False, "Page-2.css": False, "Page-3.css": False, "Page-4.css": False, "Page-5.css": False,
    "intlTelInput.css": False,
    "Post-Template.css": False, # It's in root, referenced by ../ from blog posts
    "Blog-Template.css": False, # It's in root, referenced by ../ from blog.html

    # These files are logically in 'blog/' subdirectory relative to root
    "post-1.html": True, "post-2.html": True, "post-3.html": True, "post-4.html": True, "post-5.html": True,
    "post.html": True,
    "blog.html": True
}

base_path = "/home/ubuntu/upload/"

for filename, is_subdir_logical_file in files_to_process.items():
    file_full_path = os.path.join(base_path, filename)
    if os.path.exists(file_full_path):
        fix_paths_in_file(file_full_path, is_subdir_logical_file)
    else:
        print(f"File not found, skipping: {file_full_path}")

print("All files processed by script.")

