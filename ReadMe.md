# LowTechSite

This is a python script that helps creating lightweight static websites from Markdown files.  
It has been built for a website that aims to be solar powered.

## Main features
 - Convert Markdown to HTML
 - Convert images to low resolution [dithered](https://en.wikipedia.org/wiki/Dither) images

## Repository structure
```
.
generate.py
|
|-- source/		# Where you put the Markdown and CSS files (also where you modify header.html and footer.html)
|  |
|  |-- images/		# Where you put the images that will be dithered
|  |
|  |-- highres_images/	# Where you put the images you don't want to be dithered
|  |
|  --- downloads/	# Where you put files that will be available to download from the site
|
--- output/		# Where the script puts the HTML and CSS files
   |
   |-- images/		# Where the script puts the dithered images
   |
   |-- highres_images/	# Where the script copy the images from source/highres_images
   |
   --- downloads/	# Where the script copy the files from source/downloads
```

## ToDo
 - **Incremental build support**  
	For now the script builds the whole website each time which becomes time consumming when the website is huge
 - **Multi-Language support**  
	Or in a more general way, subfolder support for Markdown files

## Licence
This project is licensed under GPLv3 License. See [LICENSE](LICENSE)
