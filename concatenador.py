#####################
# This script will merge .txt files that find in the same folder
# into one file.
#####################

import os

# Reading all the files in the folder
all_files = os.listdir()

# Turning the previous reading into a list and filtering only .txt
txt_files = list(filter(lambda x: x[-4:] == ".txt", all_files))

# print(txt_files)

# Creating a file in write mode and using a loop to fill it, 
# the output file name can be changed in the next line
with open("fusion-liq-elec.txt","w") as resultado:
    for archivos in txt_files: # Looping the txt_files
        with open(archivos) as contenido:  # Opening the txt_files
            resultado.write(contenido.read()) # Writing what is read on the final file
        resultado.write("\n") # Insert the next content in a new line