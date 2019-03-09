# OpenTTD-OBM

A repository for the development of a python program for generating an '.obm' file for the use in music packs for the game
OpenTTD.

## Files
- README.md: this readme
- opendttd_obm_generator.py: OBMData class module.
- OBM_generator_GUI.py: 

## Dependencies
- Standard library for Python 3.6.2.
- OpenTTD

## Installation
Download the opendttd_obm_generator.py and OBM_generator_GUI.py files into the same directory.

## Usage
1. Run OBM_generator_GUI.py.
2. Enter the metadata information into the Name, Shortname, Version, Description, and Origin entry fields 
3. Import .mid, .midi, or .gm files by clicking the "IMPORT..." button then choosing the directory where the files are located.
4. Click on either the "THEME", "OLD STYLE", "NEW STYLE", or "EZY STREET" button.
5. Type the display name of the song being added in the Name entry field above the "THEME" button.
6. In the "TRACK LIST" box either single click the filename of the track you wish to add then click the "ADD >>" button, or double click the filename.
7. To remove a track from the selected style, in the "PROGRAM -" box either single click the filename then click the "<< REMOVE" button, or double click the filename.
8. When finished adding tracks to each style, click the "SAVE OBM" button in the bottom right corner.