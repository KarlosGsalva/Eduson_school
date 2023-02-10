from PIL import Image

im = Image.open('python_avatar.png')
size = (300, 200)

# change size
out = im.resize(size)
out.save('python_avatar_resize.jpg')

# rotate picture
r_out = im.rotate(45)
r_out.save('python_avatar_rot.jpg')
