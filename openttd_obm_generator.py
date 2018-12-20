#! python3
## openttd_obm_generator.py
## Generates a .obm file for use by OpenTTD from a directory
## Brett Behler 12.20.2018

import hashlib, os

class OBM_File(object):
    def __init__(self):
        self.read_directory()

    def md5(self, fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def read_directory(self):
        # get list of valid midi files in current directory
        self.name = os.path.split(os.getcwd())[-1]
        self.tracks = [f for f in os.listdir('.') if os.path.isfile(f) and f[-4:] == '.mid']


    def create_file(self):
        with open(self.name+'.obm', 'w') as obm_file:
            self.write_obm_metadata(obm_file)
            self.write_obm_data(obm_file)


    def write_obm_metadata(self, file_obj):
        text = [
                '[metadata]', 
                'name = ' + self.name,
                'shortname = '+ self.name[:4].upper(),
                'version = *',
                'description = *',
                '\n'
                ]
        file_obj.write('\n'.join(text))

    def write_obm_data(self, file_obj):
        obm_files_text = ['[files]']
        obm_md5s_text = ['[md5s]']
        obm_names_text = ['[names]']
        for track in self.tracks:
            i = self.tracks.index(track)
            if i == 0:
                prefix = 'theme'
            elif i < 11:
                prefix = 'old_' + str(i-1)
            elif i < 21:
                prefix = 'new_' + str(i-1 % 10)
            else:
                prefix = 'ezy_' + str(i-1 % 10)
            prefix += ' = '
            obm_files_text.append(prefix + track)
            obm_md5s_text.append(track + ' = ' + self.md5(track))
            # file naming convention XX_track_title_name.mid where XX is the numerical track number
            obm_names_text.append(track + ' = ' + ' '.join(track[3:-4].split('_')).title())
        if len(obm_files_text) - 1 < 31:
            start = len(obm_files_text) - 1
            for i in range(start, 33):
                if i == 0:
                    prefix = 'theme'
                elif i < 11:
                    prefix = 'old_' + str(i-1)
                elif i < 21:
                    prefix = 'new_' + str(i-1 % 10)
                else:
                    prefix = 'ezy_' + str(i-1 % 10)
                prefix += ' = '
                obm_files_text.append(prefix)
        file_obj.write('\n'.join(obm_files_text))
        file_obj.write('\n\n')
        file_obj.write('\n'.join(obm_md5s_text))
        file_obj.write('\n\n')
        file_obj.write('\n'.join(obm_names_text))
        file_obj.write('\n\n')
        file_obj.write('\n'.join(['[origin]', 'default = *']))

if __name__ == '__main__':
    gen_obm = OBM_File()
    gen_obm.create_file()
