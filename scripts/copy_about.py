import shutil
import os

src = './_site/site-description.html'
dst = './_includes/site-description.html'

print(shutil.copyfile(src, dst))

src = './about.md'
dst = './_posts/about.md'

print(shutil.copyfile(src, dst))