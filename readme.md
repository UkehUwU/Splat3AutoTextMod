# Splat3AutoTextMod

**ATTENTION:** This is still a work is progress. The script doesn't work yet.

## Table of contents
txt

## Overview
This script is designed to automate the process of modifying text within Splatoon 3, making it easier for users to customize the in-game text to their preferences. Whether you want to change the language, tweak dialogues, or experiment with translations, this script can help you achieve your desired modifications.

The script achieves this by iterating through every in-game dialogue and applying specific modifications as defined in its functions.

## Getting Started

### Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system. [Download page](https://www.python.org/downloads/). I'll be using 3.11.5. You will need at least basic knowledge on how to use Python.

### File Structure
To get started with Splat3AutoTextMod, organize your project's file structure as follows:
```
/baseFolder
│
├── Splat3AutoTextMod
│ ├── main.py
│ ├── requirements.txt
│ ├── modifyText.py
│ └── readme.md
│
├── original
│ ├── ... (original game files)
```

- `/baseFolder`: This is your project's main directory. You can name it however you want.
- `Splat3AutoTextMod`: This folder contains the script and necessary files. This is also the Git repository you will be cloning.
  - `main.py`: The main script file for Splat3AutoTextMod.
  - `requirements.txt`: A list of Python dependencies required for the script.
  - `modifyTetx.py`: This file contains the function that will be iterated through every string.
  - `readme.md`: This file.
- `original`: Place your original game files in this directory.

Another folders and files will be automatically created by the script.

## How to use
I'll assume you've already cloned this repository in your machine and ordered everything as shown in the [File structure section](#file-structure).

1. **Dump Your Game Data:**
   - Start by obtaining access to the game's data. This can be done using a modified Nintendo Switch or an emulator like Yuzu. Here, we'll walk you through using Yuzu for simplicity.
   - Right-click on the game and select `Dump RomFS` → `Dump RomFS`. Yuzu will perform this process, and a folder will open containing the game's content.

2. **Navigate to the Appropriate Directory:**
   - Inside the dumped game content, you'll find various directories. For text modifications, we need to access the text files.
   - Navigate to the following directory: `0100C2500FC20000/romfs/Mals`. In this location, you'll encounter numerous files, each containing the game's text in different languages.
   
3. **Copy Your Desired Language File:**
   - Depending on your preferences, choose the language file that corresponds to your desired modifications. Each file is labeled with a two-digit code representing the region and language.
   - For instance, if you want to modify the Spanish text in the European version of Splatoon 3 with the 5.1 update, look for a file named `EUes.Product.500.sarc.zs`.
   - Copy that file to `/baseFolder/original`. There must only be one translation file at the same time.

4. **Edit the `modifyText.py` function:**
   - In order to achieve your desired result, you'll need to modify `modifyText.py`. This file contains a function that processes every single text from the game.
   - More information in [How to edit the `modifyText.py` function](#how-to-edit-the-modifyText-py-function).

5. **Execute the script:**
   - Before executing the script, run on your terminal inside this folder `pip install -r requirements.txt` to install the dependencies.
   - To finally execute the script, run `python main.py` on your terminal, inside this folder.
   - Make sure everything is in order before running the script.
   - This may take a while considering the amount of text present on the game and the modifications you want to perform.

6. **It's done!**
   - If everything worked as excepted, you should have in `/baseFolder/modification` the modified file. The name will be the same as the original.
   - To use it in your game, follow the instruction on [How to add the modification in your game](#how-to-add-the-modification-in-your-game).

## How to edit the `modifyText.py` function
txt

## How to add the modification in your game
To see your modifications in the game, you will need to create a mod. It's actually simpler than you may think, but before creating one, let me explain how they work.

### How mods work
Your emulator or CFW (custom firmware) will provide you a mod folder for every game. Inside that folder, you can add as many mods as you want (or as many as your Switch/PC can handle). Every mod is inside its own folder, which can have any name you want, for organization purposes. The emulator/CFW replaces the content of the original game with the content inside every mod folder when the game is executed, it doesn't modify the ROM of the game. Obviously, every mod does not contain the whole game, it only contains the modified files.

Here's an example of how to structure your mod folder:
```
/modName
│
├── romfs
│ ├── UI
│ │ ├── Icon
│ │ │ ├── Badge
│ │ │ │ ├── Badge_CatalogueLevel_Lv00.bntx.zs
```
In this example, the `modName` folder is your mod's name, and you can choose any name that makes sense to you. Inside it, the `romfs` directory mirrors the structure of the original game. In this case, it's modifying a badge. To further understanding, I recommend you to analyze the game's structure and compare it with some mods using [Switch Toolbox](https://github.com/KillzXGaming/Switch-Toolbox).

### How to create yours
In this specific case, you will need to follow these steps:
1. Create a new folder in your emulator or CFW's mod directory. You can name it whatever you like, but it's often helpful to give it a name that corresponds to your mod.
2. Inside that folder, create the following structure: `/romfs/Mals`.
3. Copy the file that the script generated inside that folder. Don't rename it.

When you launch the game with the mod enabled, it will replace the game's original files with the ones in your mod folder. This way, you'll see your modifications in the game without altering the original game files.

### How to share them
If you want to share you creations, you can do it through pages like [GameBanana](https://gamebanana.com). Each page will have its own guidelines, so make sure to read and follow them.

## How the script works
txt

## Additional Information

### What is a `.sarc` file?
A SARC file is an archive format known as "Sead ARChived Resource" used in various Nintendo 3DS, Wii U, and Switch games. These files store game data resource files, including images, textures, levels, and objects. The modding and Homebrew communities often modify SARC files to make alterations to gameplay and game content.

Learn more about SARC files: [FileInfo](https://fileinfo.com/extension/sarc)

### What is a `.msbt` file?
An MSBT file contains information about how text is displayed in various games for several Nintendo consoles, such as 3DS, Switch, Wii, and Wii U. It stores information about dialogs that appear during the game, such as the actual text, the appearance of the dialog, the character attributed with the dialog, and when the dialog appears.

Learn more about MSBT files: [FileInfo](https://fileinfo.com/extension/msbt)

### What is zstd?
Zstd, short for "Zstandard," is a high-performance compression algorithm and format. It is commonly used in various applications and game development to efficiently compress and decompress data. In the context of Splatoon 3 the game assets use zstd compression to reduce the size of files while maintaining their integrity.

Learn more about zstd compression: [Official page](http://facebook.github.io/zstd/)

## License
This code is provided under the GNU GPL v3 license. It is attached in this repository, and you can read it [here](./LICENSE) or [online](https://www.gnu.org/licenses/gpl-3.0.html#license-text).

## Contribution
If you would like to contribute to this project, feel free to fork the repository and submit pull requests. We welcome contributions from the community to make this tool better.