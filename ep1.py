from fastbook import *

urls = search_images_ddg('bird photos', max_images=1)
len(urls), urls[0]

dest = Path('bird.jpg')
if not dest.exists(): download_url[0], dest, show_progress=False
im = Image.open(dest)
im.to_thumb(256,256)