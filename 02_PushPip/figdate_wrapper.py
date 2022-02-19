import venv
import os
import shutil
import subprocess
import tempfile

temp_dir = tempfile.mkdtemp()
venv.create(temp_dir, with_pip=True)
subprocess.run([os.path.join(temp_dir, 'bin', 'pip3'),'install', 'pyfiglet'], capture_output=True)
subprocess.run([os.path.join(temp_dir, 'bin', 'python3'), '-m', 'figdate'])
shutil.rmtree(temp_dir)
