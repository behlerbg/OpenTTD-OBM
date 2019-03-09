#! python3
# openttd_obm_generator.py
# Generates a .obm file for use by OpenTTD from a directory
# Brett Behler 12.20.2018

import hashlib
import os
import shutil


class OBMData(object):
    """Does these things.
    
    Instance Variables:
        

    Methods:
        
    """
    def __init__(self,
            name='New OBM',
            shortname='XXXX',
            version='*',
            description='*',
            origin='*'):
        """Instantiate and return OBMData object.

        Keyword Arguments:
            name:(str) -- The name for metadata.
            shortname:(str) -- The shortname for metadata.
            version:(str) -- The music pack version number.
            description:(str) -- Short description for music pack.
            origin:(str) -- URL for music pack download.

        Returns:
            OBMData object.

        Raises:
            None
        """

        # self.read_directory()
        self.meta_data = {
            'name': name,
            'shortname': shortname,
            'version': version,
            'description': description,
            'origin': origin}

        self.theme = []
        self.old_style = []
        self.new_style = []
        self.ezy_street = []
        self.tracks = []
        self.music_dir = ''
        self.destination_dir = ''

    def combine_styles(self):
        self.tracks.extend(self.theme)
        self.tracks.extend(self.old_style)
        self.tracks.extend(self.new_style)
        self.tracks.extend(self.ezy_street)

    def md5(self, fname):
        """Do this. Return that.
        
        Arguments:
            
        
        Keyword Arguments:
            
        
        Returns:
            
        
        Raises:
            
        """
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def write_text(self):
        """Do this. Return that.
        
        Arguments:
            
        
        Keyword Arguments:
            
        
        Returns:
            
        
        Raises:
            
        """
        self.obm_meta_text = [
                '[metadata]',
                'name = ' + self.meta_data['name'],
                'shortname = ' + self.meta_data['shortname'],
                'version = ' + self.meta_data['version'],
                'description = ' + self.meta_data['description'],
                '\n']
        self.obm_files_text = ['[files]']
        self.obm_md5s_text = ['[md5s]']
        self.obm_names_text = ['[names]']
        self.obm_origin_text = '[origin]\n' + self.meta_data['origin']

        for track in self.theme:
            self.obm_files_text.append('theme = ' + track)
            self.obm_md5s_text.append(track + ' = '
                                     + self.md5(os.path.join(self.music_dir, 
                                                             track)))
            self.obm_names_text.append(track + ' = ' + track)

        for i in range(10):
            try:
                track = self.old_style[i]
                self.obm_files_text.append('old_' + str(i) + ' = ' + track)
                self.obm_md5s_text.append(track + ' = '
                                        + self.md5(os.path.join(self.music_dir, 
                                                             track)))
                self.obm_names_text.append(track + ' = ' + track)
            except IndexError:
                self.obm_files_text.append('old_' + str(i) + ' = ')

        for i in range(10):
            try:
                track = self.new_style[i]
                self.obm_files_text.append('new_' + str(i) + ' = ' + track)
                self.obm_md5s_text.append(track + ' = '
                                        + self.md5(os.path.join(self.music_dir, 
                                                             track)))
                self.obm_names_text.append(track + ' = ' + track)
            except IndexError:
                self.obm_files_text.append('new_' + str(i) + ' = ')

        for i in range(10):
            try:
                track = self.ezy_street[i]
                self.obm_files_text.append('ezy_' + str(i) + ' = ' + track)
                self.obm_md5s_text.append(track + ' = '
                                        + self.md5(os.path.join(self.music_dir, 
                                                             track)))
                self.obm_names_text.append(track + ' = ' + track)
            except IndexError:
                self.obm_files_text.append('ezy_' + str(i) + ' = ')

    def create_file(self, obm_dir, music_dir):
        """Do this. Return that.
        
        Arguments:
            
        
        Keyword Arguments:
            
        
        Returns:
            
        
        Raises:
            
        """
        self.music_dir = music_dir
        self.destination_dir = obm_dir
        if obm_dir != music_dir:
            self.combine_styles()
            for track in self.tracks:
                shutil.copy2(os.path.join(music_dir, track), obm_dir)
        self.write_text()
        with open(os.path.join(obm_dir, self.meta_data['name'] + '.obm'),
                 'w') as obm_file:
            obm_file.write('\n'.join(self.obm_meta_text))
            obm_file.write('\n'.join(self.obm_files_text))
            obm_file.write('\n\n')
            obm_file.write('\n'.join(self.obm_md5s_text))
            obm_file.write('\n\n')
            obm_file.write('\n'.join(self.obm_names_text))
            obm_file.write('\n\n')
            obm_file.write(self.obm_origin_text)


if __name__ == '__main__':
    print('A class for tracking and formatting data into the OBM format.')
