# pyiconlibrary
A class that uses icons.yaml to allow a user to load
any icon in the google material icons library.
To pick an icon, simply find the icon you want on 
https://fonts.google.com/icons

```
The yaml file contains all 48dp icons.
name = The lowercase version of the icon name found at the link
        (verify that it is the same with a seach through the icons.yml file)
colors = [black, white]
icon_types = [outlined, round, sharp, twotone, normal]
size = [1x, 2x] (optional, default = 2x)

Example: 
lib = IconLibrary()
img = lib.get_icon(color="black", name="add_alert", icon_type="outlined")
Loading selected icon: 
{'color': 'black', 
'name': 'add_alert', 
'path': 'png/alert/add_alert/materialiconsoutlined/48dp/1x/outline_add_alert_black_48dp.png', 
'size': '1x', 
'type': 
'outlined', 
'used': False}
```


## Getting started

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
To install this package, in the main directory run:
```shell
make install_poetry
make install_depends
pip install .

```

To modify the package:

Prerequisites
```shell
# install poetry if you do n
curl -sSL https://install.python-poetry.org | python3 -

# Check if installation worked
poetry --version

# Update if needed:
poetry self update

# Add poetry to your bash completion file:
poetry completions bash >> ~/.bash_completion
source ~/.bash_completion


# Useful info (do NOT run now) If you want to build a python package from scratch using poetry:
mkdir nameofpythonpackage
cd nameofpythonpackage
poetry new .
```

Now that we have installed Poetry, we can install the dependencies on your system. 
Poetry will automatically create a virtual environment and install depends
based on the pyproject.toml. We will also install pre-commit hooks to locally check 
format and import sorting.

```shell
poetry install
# Enter the poetry shell and install all pre-commit hooks
poetry shell
pre-commit install
pre-commit run --all-files

```
## Support
Contact philip.mai@accenture.com for support.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
Icons were sourced from https://github.com/google/material-design-icons. I added white versions of all the black pngs

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
