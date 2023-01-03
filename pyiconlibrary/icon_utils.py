"""
 Copyright 2022 Philip Mai - philip.mai@accenture.com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
import tkinter as tk

import customtkinter
import wand
import wand.image
import yaml
from PIL import Image


class IconLibrary:
    """A class that uses icons.yaml to allow a user to load
    any icon in the google material icons library.
    To pick an icon, simply find the icon you want on
    https://fonts.google.com/icons

    The yaml file contains all 48dp icons.
    name = The lowercase version of the icon name found at the link
    colors = [black, white]
    icon_types = [outlined, round, sharp, twotone, normal]
    size = [1x, 2x]

    Example:
    lib = IconLibrary()
    img = lib.get_icon(color="black", name="add_alert", icon_type="outlined")
    Loading selected icon:
    {'name': 'add_alert',
    'path': 'alert/add_alert/materialiconsoutlined/48dp/2x/outline_add_alert_black_48dp.png',
    'type': 'outlined',
    'used': False}

    """

    def __init__(self):
        """This will load icons.yml. This file should be in the main directory"""
        with open("icons.yml", "r") as f:
            self.icons = yaml.safe_load(f)
        self.path = "pyiconlibrary"
        self.icon_types = ["outlined", "round", "sharp", "twotone", "normal"]
        self.colors = ["black", "white"]
        self.sizes = ["1x", "2x"]
        self.return_types_info = ["color", "name", "path", "size", "type", "used", "info"]
        self.return_types_img = ["CTkImage", "PIL.Image"]
        print(self.path)

    def check_parameters(self, color, icon_type, size, width, height):
        if color not in self.colors:
            print("Error: this color does not exist in the icon library ->", color)
            print("Valid colors are: ", self.colors)
            return False
        if icon_type not in self.icon_types:
            print("Error: this icon_type does not exist in the icon library ->", icon_type)
            print("Valid types are: ", self.icon_types)
            return False
        if size not in self.sizes:
            print("Error: this size of icon does not exist in the icon library ->", size)
            print("Valid sizes are: ", self.sizes)
            return False
        if width < 1 or height < 1:
            print("Error: negative sizes don't exist ->", size)
            return False

    def get_icon(
        self, color, name, icon_type, size="2x", width=20, height=20, return_type="CTkImage"
    ):
        """_summary_
            Getter for icons that returns an image object or info about the icon.
        Args:
            color (str): [black, white]
            name (str): The lowercase version of the icon name
            icon_type (str): [outlined, round, sharp, twotone, normal]
            size (str): (str, optional) [1x, 2x]. Defaults to 2x
            width (int, optional): Width of image returned. Defaults to 20.
            height (int, optional): Height of image returned. Defaults to 20.
            return_type (str, optional) Type of info to be returned.
                Can be information: ["color", "name", "path", "size", "type", "used", "info"]
                Can be an image object: ["CTkImage", "PIL.Image"]
                Defaults to customtkinter.CTkImage object
        Returns:
            Image object or information based on return_type
        """
        if not self.check_parameters(
            color=color, icon_type=icon_type, size=size, width=width, height=height
        ):
            return

        # Checking if only info is needed
        if return_type in self.return_types_info:
            if return_type == "info":
                return self.icons[size][color][icon_type][name]
            else:
                return self.icons[size][color][icon_type][name][return_type]
        else:
            print("Valid return types are: ", self.return_types_info)

        # Loading image
        icon_path = self.icons[size][color][icon_type][name]["path"]
        icon_path = os.path.join(self.path, icon_path)
        print("Loading selected icon: ")
        print("{'size':'" + size + "', 'color': '" + color + "',")
        print(self.icons[size][color][icon_type][name], "}")
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((width, height))
        print(icon_image)

        # Checking type of image to return
        if return_type == "CTkImage":
            return customtkinter.CTkImage(icon_image)
        elif return_type == "PIL.Image":
            return icon_image
        else:
            print("Error: invalid return_type ->", return_type)
            print("Valid return types are: ", self.return_types_img)


def icon_svg_2_png_crop(svg_file, out_file="temp.png"):
    # file = open("resources/icons/Settings.svg")
    file = open(svg_file)
    with wand.image.Image(
        blob=file.read().encode("utf-8"), format="svg", background=wand.color.Color("transparent")
    ) as image:
        # with wand.image.Image( blob=file.read().encode('utf-8'), format="svg") as image:
        print(image.size)
        image.crop(140, 90, width=220, height=220)
        png_image = image.make_blob("png")
        with open(out_file, "wb") as out:
            out.write(png_image)


def svg_2_png_mass(
    svg_list="resources/icons/icon_list_svg.txt", png_list="resources/icons/icon_list_png.txt"
):
    # svg_files = glob.glob("resources/icons/*.svg")
    svg_files = open(svg_list).read().split("\n")
    png_files = open(png_list).read().split("\n")
    f = list(zip(svg_files, png_files))
    for (svg, png) in f:
        # print(svg,png)
        icon_svg_2_png_crop(svg, png)


def white(L, R):
    # print(L)
    img = Image.open(L)
    img = img.convert("RGBA")
    r, g, b, a = img.split()
    r = g = b = r.point(lambda i: 0 if i > 0 else 255)
    img = Image.merge("RGBA", (r, g, b, a))
    img.save(R)


def black(L, R):
    # print(L)
    img = Image.open(L)
    img = img.convert("RGBA")
    r, g, b, a = img.split()
    r = g = b = r.point(lambda i: 0)
    img = Image.merge("RGBA", (r, g, b, a))
    img.save(R)


def png_black2white_mass(black_files="listOfFiles.txt", white_files="listOfFiles_white.txt"):
    # svg_files = glob.glob("resources/icons/*.svg")
    left_files = open(black_files).read().split("\n")
    right_files = open(white_files).read().split("\n")
    f = list(zip(left_files, right_files))
    print(f)
    for (l, r) in f:
        print(l + r)
        white(l, r)


def png_white2black_mass(
    black_files="resources/icons/icon_list_png.txt",
    white_files="resources/icons/icon_list_png_white.txt",
):
    # svg_files = glob.glob("resources/icons/*.svg")
    right_files = open(black_files).read().split("\n")
    left_files = open(white_files).read().split("\n")
    f = list(zip(left_files, right_files))
    print(f)
    for (l, r) in f:
        print(l + r)
        black(l, r)


def generate_icon_yaml(white, black):
    all = {"1x": {}, "2x": {}}
    all["1x"] = {"white": {}, "black": {}}
    all["2x"] = {"white": {}, "black": {}}
    all["1x"]["white"] = {"outlined": {}, "round": {}, "sharp": {}, "twotone": {}, "normal": {}}
    all["1x"]["black"] = {"outlined": {}, "round": {}, "sharp": {}, "twotone": {}, "normal": {}}
    all["2x"]["white"] = {"outlined": {}, "round": {}, "sharp": {}, "twotone": {}, "normal": {}}
    all["2x"]["black"] = {"outlined": {}, "round": {}, "sharp": {}, "twotone": {}, "normal": {}}

    files = [white, black]
    colors = ["white", "black"]
    for file, color in zip(files, colors):
        print(file, color)
        with open(file, "r") as f:
            image_paths = f.read().split("\n")

        for path in image_paths:
            # Determine color from path
            # color = "black" if "_black" in path else "white"
            size = "2x" if "2x" in path else "1x"
            icon_type = "normal"
            if "outlined" in path:
                icon_type = "outlined"
            elif "round" in path:
                icon_type = "round"
            elif "sharp" in path:
                icon_type = "sharp"
            elif "twotone" in path:
                icon_type = "twotone"
            # Extract icon name and create dict with image data
            filename = os.path.basename(path)
            icon = filename.split("_" + color + "_")[0]
            icon = icon[icon.find("_") + 1 :]
            entry = {}
            entry["path"] = "png/" + path
            entry["used"] = False
            entry["type"] = icon_type
            entry["name"] = icon
            entry["size"] = size
            entry["color"] = color
            # print(entry)
            all[size][color][icon_type][icon] = entry
    # Write icon data to yaml file
    with open("icons.yml", "w") as f:
        yaml.dump(all, f)


def remake_icon_yaml():
    generate_icon_yaml(white="listOfFiles_white.txt", black="listOfFiles_black.txt")


# remake_icon_yaml()
# png_white2black_mass()
# png_black2white_mass()
# white = "listOfFiles_white.txt"
# black = "listOfFiles_black.txt"
