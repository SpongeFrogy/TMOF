import os 
import re 
import shutil
import json

# Path to the script 
PATH = os.path.dirname(os.path.realpath(__file__))

# Path to the cifs folder
DATABASE_PATH = os.path.join(PATH, 'database')
CIFS_PATH = os.path.join(DATABASE_PATH, 'cifs')

def remove_special_characters(input_string):
    # This pattern matches any character that is not a word character
    pattern = re.compile('[^a-zA-Z0-9\.]+')
    return pattern.sub('', input_string)

def cif_folder_for_zeopp():
    # Copy all cifs folder to new folder in PATH but without special characters in name of cif files
    # Create new folder
    NEW_CIFS_PATH = os.path.join(PATH, 'cifs')
    if not os.path.exists(NEW_CIFS_PATH):
        os.mkdir(NEW_CIFS_PATH)

    # Create json for names mapping
    names_mapping = {}

    # Copy all cifs
    for folders in os.listdir(CIFS_PATH):
        for cif in os.listdir(os.path.join(CIFS_PATH, folders)):
            # Check if cif file
            if cif.endswith('.cif'):
                print('Before cif name: ', cif)
                # Remove special characters
                new_cif_name = remove_special_characters(cif)
                print('After cif name: ', new_cif_name)
                # Copy
                shutil.copy(os.path.join(CIFS_PATH, folders, cif), os.path.join(NEW_CIFS_PATH, new_cif_name))
                # Add to json
                names_mapping[cif] = new_cif_name
    
    # Save json
    with open(os.path.join(PATH, 'names_mapping.json'), 'w') as f:
        json.dump(names_mapping, f)

            
if __name__ == '__main__':
    cif_folder_for_zeopp()
        