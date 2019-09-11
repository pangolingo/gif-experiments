import os
from PIL import Image

def processImage(path):
    '''
    Iterate the GIF, extracting each frame.
    '''
    # mode = analyseImage(path)['mode']
    mode = 'full'
    
    im = Image.open(path)

    i = 0
    p = im.getpalette()
    last_frame = im.convert('RGBA')

    try:
        while True:
            # print("saving {} ({}) frame {}, {}, {}".format(path, mode, i, im.size, im.tile))
            
            '''
            If the GIF uses local colour tables, each frame will have its own palette.
            If not, we need to apply the global palette to the new frame.
            '''
            if not im.getpalette():
                print('using global palette')
                im.putpalette(p)

            # print(im.getpalette())
            
            new_frame = Image.new('RGBA', im.size)
            
            '''
            Is this file a "partial"-mode GIF where frames update a region of a different size to the entire image?
            If so, we need to construct the new frame by pasting it on top of the preceding frames.
            '''
            if mode == 'partial':
                new_frame.paste(last_frame)
            
            new_frame.paste(im, (0,0), im.convert('RGBA'))
            new_frame.save('export/%s-%d.png' % (''.join(os.path.basename(path).split('.')[:-1]), i), 'PNG')

            i += 1
            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass


def main():
    # processImage('rgb.gif')
    processImage('custom.gif')
    

if __name__ == "__main__":
    main()