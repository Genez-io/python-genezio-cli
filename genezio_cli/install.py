from setuptools import setup
from setuptools.command.install import install
import subprocess
import sys

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        try:
            # Verify if Node.js is installed
            subprocess.run(['node', '--version'], check=True, capture_output=True)
            
            # Install genezio globally through npm
            print("Installing genezio CLI through npm...")
            subprocess.run(['npm', 'install', '-g', 'genezio'], check=True)
            
            print("Genezio CLI has been successfully installed!")
            
        except subprocess.CalledProcessError as e:
            print("Error: Node.js is required but not found. Please install Node.js first.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred during installation: {str(e)}", file=sys.stderr)
            sys.exit(1)

setup(
    cmdclass={
        'install': PostInstallCommand,
    },
) 