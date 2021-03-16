#! /bin/python3

#
#    @author  : Maxime Chretien (MixLeNain)
#    @mail    : mchretien@linuxmail.org
#    @project : LowTechSite
#    @summary : A script generating light web pages from markdown files
#    @version : 1.0
#

import markdown as md
import os
import shutil
from PIL import Image
import hitherdither

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) + "/"
SOURCE_DIR = BASE_DIR + "source/"
OUTPUT_DIR = BASE_DIR + "output/"

TITLE_APPEND = " - WebSiteName"

HEADER = SOURCE_DIR + "header.html"

FOOTER = SOURCE_DIR + "footer.html"

# Get HTML header and footer
with open(HEADER, 'r') as of:
    header_text = of.read()

with open(FOOTER, 'r') as of:
    footer_text = of.read()

# Sort files from source directory
files = os.listdir(SOURCE_DIR)
md_files = []
css_files = []

for f in files:
    if f.endswith(".md"):
        md_files.append(os.path.splitext(f)[0])
    elif f.endswith(".css"):
        css_files.append(f)

# Generate HTML files from Markdown files
for f in md_files:
    with open(SOURCE_DIR + f + '.md', 'r') as of:
        title, text = of.read().split('\n', 1)
        html = md.markdown(text, extensions=["tables", "nl2br", "fenced_code"])

    with open(OUTPUT_DIR + f + '.html', 'w') as of:
        of.write(header_text.replace("TITLE", title + TITLE_APPEND))
        of.write(html)
        of.write(footer_text)

# Copy CSS files to output folder
for f in css_files:
    shutil.copy(SOURCE_DIR + f, OUTPUT_DIR)

# Generate dithered images from source images
images = os.listdir(SOURCE_DIR + "images")

for i in images:
    img = Image.open(SOURCE_DIR + "images/" + i).convert('RGB')
    img.thumbnail((800,800), Image.LANCZOS)

    palette = hitherdither.palette.Palette([(25,25,25), (75,75,75),(125,125,125),(175,175,175),(225,225,225),(250,250,250)])
    threshold = [96, 96, 96]

    img_dithered = hitherdither.ordered.bayer.bayer_dithering(img, palette, threshold, order=8)
    img_dithered.save(OUTPUT_DIR + "images/" + os.path.splitext(i)[0] + ".png", optimize=True)

# Copy high resolution images to output folder
highres_images = os.listdir(SOURCE_DIR + "highres_images")

for i in highres_images:
    shutil.copy(SOURCE_DIR + "highres_images/" + i, OUTPUT_DIR + "highres_images/")

# Copy download files to output folder
downloads = os.listdir(SOURCE_DIR + "downloads")

for d in downloads:
    shutil.copy(SOURCE_DIR + "downloads/" + d, OUTPUT_DIR + "downloads/")
