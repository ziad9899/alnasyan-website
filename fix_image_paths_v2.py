#!/usr/bin/env python3.11
import os
import re

def fix_paths_in_file(filepath, is_in_subdir_logical):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        if is_in_subdir_logical:
            # HTML attributes
            content = content.replace('src="../images/', 'src="../')
            content = content.replace('data-image-src="../images/', 'data-image-src="../')
            content = content.replace('xlink:href="../images/', 'xlink:href="../')
            
            content = content.replace('src="images/', 'src="../')
            content = content.replace('data-image-src="images/', 'data-image-src="../')
            content = content.replace('xlink:href="images/', 'xlink:href="../')
            content = content.replace('"logo": "images/', '"logo": "../') # JSON-LD
            content = content.replace('href="images/', 'href="../') # Other hrefs

            # CSS url() patterns
            content = re.sub(r'url\s*\(\s*["\"]?\s*\.\./images/', 'url("../', content)
            content = re.sub(r'url\s*\(\s*["\"]?\s*images/', 'url("../', content)

        else: # Root files (or CSS files in root)
            # HTML attributes
            content = content.replace('src="images/', 'src="')
            content = content.replace('data-image-src="images/', 'data-image-src="')
            content = content.replace('xlink:href="images/', 'xlink:href="')
            content = content.replace('"logo": "images/', '"logo": "') # JSON-LD
            content = content.replace('href="images/', 'href="') # Other hrefs

            # CSS url() patterns
            content = re.sub(r'url\s*\(\s*["\"]?\s*images/', 'url("', content)
            # Specific inline style cases (less critical if re.sub is robust)
            content = content.replace('style="background-image: url(images/', 'style="background-image: url(')
            content = content.replace('style="background-image: url("images/', 'style="background-image: url("')
            content = content.replace("style=\"background-image: url('images/", "style=\"background-image: url('")

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Processed and modified: {filepath}")
        else:
            print(f"Processed (no changes needed, or patterns not found): {filepath}")
            
    except Exception as e:
        print(f"Error processing file {filepath}: {str(e)}")

files_to_process = {
    "index.html": False, "Home.html": False,
    "Page-1.html": False, "Page-2.html": False, "Page-3.html": False, "Page-4.html": False, "Page-5.html": False,
    "nicepage.css": False,
    "index.css": False,
    "Page-1.css": False, "Page-2.css": False, "Page-3.css": False, "Page-4.css": False, "Page-5.css": False,
    "intlTelInput.css": False,
    "Post-Template.css": False, 
    "Blog-Template.css": False, 
    "post-1.html": True, "post-2.html": True, "post-3.html": True, "post-4.html": True, "post-5.html": True,
    "post.html": True,
    "blog.html": True
}

base_path = "/home/ubuntu/upload/"

all_provided_files = [
    "Post-Template.css", "Page-5.html", "Page-5.css", "Page-4.html", "Page-4.css", 
    "Page-3.html", "Page-3.css", "Page-2.html", "Page-2.css", "Page-1.html", "Page-1.css",
    "nicepage.js", "nicepage.css", "jquery.js", "index.html", "index.css", "Home.html",
    "Blog-Template.css", "utils.js", "intlTelInput.min.js", "intlTelInput.css",
    "post-5.html", "post-4.html", "post-3.html", "post-2.html", "post-1.html", "post.html",
    "blog.json", "blog.html"
]

for f_name in all_provided_files:
    if f_name.endswith(('.html', '.css')):
        if f_name not in files_to_process:
            if (('post' in f_name or 'blog' in f_name) and f_name.endswith(".html")):
                 files_to_process[f_name] = True
            else:
                 files_to_process[f_name] = False

for filename, is_subdir_logical_file in files_to_process.items():
    file_full_path = os.path.join(base_path, filename)
    if os.path.exists(file_full_path):
        fix_paths_in_file(file_full_path, is_subdir_logical_file)
    else:
        if not (filename.endswith(".js") or filename.endswith(".json")):
             print(f"File not found, skipping: {file_full_path}")

print("All relevant files processed by script.")

