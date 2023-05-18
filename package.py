# worst code that people have ever seen in the world

import shutil

if __name__ == '__main__':
    shutil.copytree('extension/css', 'prepacked/v2/css', dirs_exist_ok=True)
    shutil.copytree('extension/css', 'prepacked/v3/css', dirs_exist_ok=True)
    shutil.copytree('extension/icons', 'prepacked/v2/icons', dirs_exist_ok=True)
    shutil.copytree('extension/icons', 'prepacked/v3/icons', dirs_exist_ok=True)
    shutil.copyfile('extension/manifest_v2.json', 'prepacked/v2/manifest.json')
    shutil.copyfile('extension/manifest_v3.json', 'prepacked/v3/manifest.json')
    shutil.make_archive('packed/v2/no_link', 'zip', 'prepacked/v2')
    shutil.make_archive('packed/v3/no_link', 'zip', 'prepacked/v3')