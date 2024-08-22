from fastbook import *

urls = search_images_ddg('bird photos', max_images=1)
len(urls), urls[0]

dest = Path('bird.jpg')
if not dest.exists(): download_url(urls[0], dest, show_progress=False)
im = Image.open(dest)
im.to_thumb(256,256)

searches = 'forest', 'bird'
path = Path('bird_or_not')

if not path.exists():
    for o in searches:
        dest =(path/o)
        dest.mkdir(exist_ok=True)
        results = search_images_ddg(f'{o} photo')
        download_images(dest, urls=results[:200])
        resize_images(dest, max_size=400, dest=dest)


failed = verify_images(get_image_files(path))
failed.map(Path.unlink)

dls = DataBlock(
    blocks = (ImageBlock, CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192, method='squish')]
).dataloaders(path)

dls.show_batch(max_n=6)