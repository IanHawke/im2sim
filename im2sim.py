import argparse

import PIL
from PIL import Image
import subprocess
import os
import glob

def get_image(filename):
    p = Image.open(filename)
    docker_image = p.info['im2sim_image']
    return subprocess.call('docker pull {}'.format(docker_image), shell=True)
    print('Pulled docker image {}'.format(docker_image))

def tag_images(docker_image):
    subprocess.call(['mkdir', '-p', 'figures'])
    subprocess.call("docker run -v {}/figures:/figures "
    "{} make figures".format(os.getcwd(), docker_image), shell=True)

    figures = glob.glob('{}/figures/*.png'.format(os.getcwd()))
    for filename in figures:
        p = Image.open(filename)
        info = PIL.PngImagePlugin.PngInfo()
        info.add_text('im2sim_image', docker_image)
        p.save(filename, pnginfo = info)

    return None

parser = argparse.ArgumentParser()
parser.add_argument("action", help="'pull', 'tag'")
parser.add_argument("object", help="Figure file (if pulling)"
                                   " or docker container (if tagging)")
args = parser.parse_args()

print("Action {}, Object {}".format(args.action, args.object))

if args.action == 'pull':
    get_image(args.object)
elif args.action == 'tag':
    tag_images(args.object)
else:
    print("Action must be either 'pull' or 'tag'.")
