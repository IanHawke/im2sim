import argparse

import libxmp
from libxmp import XMPFiles, XMPMeta
from libxmp.utils import file_to_dict
import ast

import subprocess
import os
import glob

def get_image(filename):
    xmp = file_to_dict(filename)
    dc = xmp[libxmp.consts.XMP_NS_DC]
    docker_image = None
    for name, value, d in dc:
        if name.find('creator') >= 0:
            if value.find('im2sim') >= 0:
                d = ast.literal_eval(value)
                docker_image = d['im2sim']
    print('Pulling docker image {}'.format(docker_image))
    return subprocess.call('docker pull {}'.format(docker_image), shell=True)

def tag_images(docker_image):
    subprocess.call(['mkdir', '-p', 'figures'])
    subprocess.call("docker run --rm -v {}/figures:/figures "
    "{} make figures".format(os.getcwd(), docker_image), shell=True)

    figures = glob.glob('{}/figures/*.png'.format(os.getcwd()))
    for filename in figures:
        xmpfile = XMPFiles(file_path=filename, open_forupdate=True)
        xmp = xmpfile.get_xmp()
        if xmp == None:
            xmp = XMPMeta()
        xmp.append_array_item(libxmp.consts.XMP_NS_DC, 'creator', '{{ "im2sim" : "{}" }}'.format(docker_image), {'prop_array_is_ordered': True, 'prop_value_is_array': True})
        xmpfile.put_xmp(xmp)
        xmpfile.close_file()

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
