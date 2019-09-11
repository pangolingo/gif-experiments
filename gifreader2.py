import subprocess
import re
import binascii
import PIL
from PIL import Image

image_path = "script_k.gif"

im = Image.open(image_path)
dimensions = im.size

# dimensions = subprocess.check_output(["convert", image_path + "[0]", "-format", "%wx%h","info:-"])
# dimensions = dimensions.decode("utf-8").split("x")
# dimensions = [int(i) for i in dimensions]
print(dimensions)

num_frames = 0
try:
    while 1:
        num_frames += 1
        im.seek(im.tell()+1)
        # im.show()
        # do something to im
except EOFError:
    pass # end of sequence

print(num_frames)


frames = []

for i in range(num_frames):
    frame_arg = "[" + str(i) + "]"
    # frame_rgb_bytes = subprocess.check_output(["convert", "-dispose", "background","-coalesce", "-compress", "none", image_path + frame_arg, "rgba:-"])
    frame_rgb_bytes = subprocess.check_output(["convert", "-coalesce", "-compress", "none", image_path + frame_arg, "rgba:-"])
    frame_img = PIL.Image.frombytes("RGBA", dimensions, frame_rgb_bytes)
    frames.append(frame_img)
    frame_img.show()
    print(frame_rgb_bytes.hex())
    frame_img.save("export/x-" + str(i) + ".png", "PNG")

# alternative to all this:
# use imagemagick to split & resize the file
# then just load each frame
# http://www.imagemagick.org/Usage/anim_basics/


# out = subprocess.check_output(["convert", "-coalesce", "-compress", "none", image_path, "txt:-"])
# out = subprocess.check_output(["convert", "-coalesce", "-compress", "none", image_path, "rgb:-"])
# out = out.decode("utf-8") 
# out = int.from_bytes(out, byteorder='big')

# group the raw rgb bytes into a group per frame
# n = num_frames * dimensions[0] * dimensions[1]
# frames = [out[i:i+n] for i in range(0, len(out), n)]

# frame = PIL.Image.frombytes("RGB", (8,8), frames[2])

# frame.show()

# out = out.hex()

# out = out.splitlines()
# n = 6
# out = [out[i:i+n] for i in range(0, len(out), n)]

# frames = re.split("^# ImageMagick pixel enumeration.+$", out, flags=re.MULTILINE)
# print(frames[2])
# print(out)
# print(type(str(out)))