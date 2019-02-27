#!/usr/bin/env python3
""" The master faceswap.py script """
# 0.download准备招聘
#   python ~/project/piglab/machinelearning/lib/download_image.py
# 1.extract提取
#   python faceswap.py extract -i ./data/photo/huangrong/ -o ./data/extract/huangrong/
#   python faceswap.py extract -i ./data/photo/guojing/ -o ./data/extract/guojing/
#   python faceswap.py extract -i ./data/photo/zhu/ -o ./data/extract/zhu/
#   python faceswap.py extract -i ./data/photo/yan/ -o ./data/extract/yan/
# 2.train训练   (AB参数：模型用于输入A，输出B)
#   python faceswap.py train -A ./data/extract/huangrong/ -B ./data/extract/zhu/ -m ./models/huangrong2zhu/ -p
#   python faceswap.py train -A ./data/extract/guojing/ -B ./data/extract/yan/ -m ./models/guojing2yan/ -p
# 3.convert替换
#   python faceswap.py convert -i ./data/test/ -o ./data/output/ -m ./models/huangrong2zhu/

import sys
import lib.cli as cli

if sys.version_info[0] < 3:
    raise Exception("This program requires at least python3.2")
if sys.version_info[0] == 3 and sys.version_info[1] < 2:
    raise Exception("This program requires at least python3.2")


def bad_args(args):
    """ Print help on bad arguments """
    PARSER.print_help()
    exit(0)


if __name__ == "__main__":
    PARSER = cli.FullHelpArgumentParser()
    SUBPARSER = PARSER.add_subparsers()
    EXTRACT = cli.ExtractArgs(SUBPARSER,
                              "extract",
                              "Extract the faces from pictures")
    TRAIN = cli.TrainArgs(SUBPARSER,
                          "train",
                          "This command trains the model for the two faces A and B")
    CONVERT = cli.ConvertArgs(SUBPARSER,
                              "convert",
                              "Convert a source image to a new one with the face swapped")
    GUI = cli.GuiArgs(SUBPARSER,
                      "gui",
                      "Launch the Faceswap Graphical User Interface")
    PARSER.set_defaults(func=bad_args)
    ARGUMENTS = PARSER.parse_args()
    ARGUMENTS.func(ARGUMENTS)
