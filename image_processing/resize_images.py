""" 
python resize_images.py --raw-dir "C:/Users/css120804/Desktop/Video/Videos to images/pc" --save-dir "C:/Users/css120804/Desktop/images" --ext jpg --target-size "(800, 600)"


python resize_images.py --raw-dir "D:/2020-21/yolov5/YOLO_visualbot/image_processing/OutputDump" --save-dir "D:/2020-21/yolov5/YOLO_visualbot/image_processing/images" --ext jpg --target-size "(800, 600)"

Developed by: Ashish Kumar
"""
import argparse
import os
import glob
import cv2
from PIL import Image
from tqdm import tqdm

def main(raw_dir,save_dir,ext,target_size,convert=0):
    """ To resize the images """
    try:
        msg = "--target-size must be a tuple of 2 integers"
        assert isinstance(target_size, tuple) and len(target_size) == 2, msg
        fnames = glob.glob(os.path.join(raw_dir, "*.{}".format(ext)))
        os.makedirs(save_dir, exist_ok=True)
        print("{} files to resize from directory `{}` to target size:{}".format(len(fnames), raw_dir, target_size))
        for i, fname in tqdm(enumerate(fnames)):
            print(".", end="", flush=True)
            img = cv2.imread(fname)
            img_small = cv2.resize(img, target_size)
            new_fname = "{}.{}".format("Resized_"+str(i), ext)
            small_fname = os.path.join(save_dir, new_fname)
            cv2.imwrite(small_fname, img_small)
            if convert==1:
                im1=Image.open(small_fname)
                im1.save(small_fname.split(ext)[0]+'jpg')

        print("\nDone resizing {} files.\nSaved to directory: `{}`".format(len(fnames), save_dir))
    except Exception as ex:
        print('Exception:',ex)
def converter(path):
    im1 = Image.open(r'path where the PNG is stored\file name.png')
    im1.save(r'path where the JPG will be stored\new file name.jpg')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize raw images to uniformed target size.")
    parser.add_argument("--raw-dir",help="Directory path to raw images.",default="./data/raw",type=str,)
    parser.add_argument("--save-dir",help="Directory path to save resized images.",default="./data/images",type=str,)
    parser.add_argument("--ext", help="Raw image files extension to resize.", default="jpg", type=str)
    parser.add_argument("--target-size",help="Target size to resize as a tuple of 2 integers.",default="(800, 600)",type=str,)
    parser.add_argument("--convert",help="Convert file to jpg",default=0,type=int,)
    args = parser.parse_args()

    main(raw_dir=args.raw_dir,save_dir = args.save_dir,ext= args.ext,target_size= eval(args.target_size),convert=args.convert)