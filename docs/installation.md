# Installing Hypertext Programming Language

**Current Version:** 0.1.0 (Development)
**Last Updated:** 2024-12-21

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Quick Installation](#quick-installation)
3. [Detailed Installation by Platform](#detailed-installation-by-platform)
4. [Build from Source](#build-from-source)
5. [Package Manager Installation](#package-manager-installation)
6. [Docker Installation](#docker-installation)
7. [Development Tools](#development-tools)
8. [Verification](#verification)
9. [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements
- **CPU:** Any x64 processor
- **RAM:** 2GB minimum, 4GB recommended
- **Disk Space:** 500MB
- **Operating System:**
  - Linux: Ubuntu 20.04+, Fedora 34+, or equivalent
  - macOS: 11.0 (Big Sur) or later
  - Windows: Windows 10 version 1909 or later

### Required Dependencies
- C++ compiler (GCC 7+, Clang 6+, or MSVC 2019+)
- CMake 3.15 or later
- Python 3.8 or later
- Git 2.25 or later

## Quick Installation

### Linux (Ubuntu/Debian)
```bash
# Add Hypertext repository
curl -fsSL https://hypertext-lang.org/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hypertext-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hypertext-archive-keyring.gpg] https://repo.hypertext-lang.org/apt stable main" | sudo tee /etc/apt/sources.list.d/hypertext.list

# Install Hypertext
sudo apt update
sudo apt install hypertext
```
### macOS
```bash
# Using Homebrew
brew tap hypertext-lang/hypertext
brew install hypertext
```
#### Windows
```PowerShell
# Using Chocolatey
choco install hypertext
```
## Detailed Installation by Platform
### Linux
**Ubuntu/Debian**
```bash
# Install dependencies
sudo apt update
sudo apt install -y build-essential cmake python3 python3-pip git

# Clone repository
git clone https://github.com/entity12208/hypertext-lang
cd hypertext-lang

# Build and install
./tools/build.py --build-type Release
sudo make install
```
**Fedora/RHEL**
```bash
# Install dependencies
sudo dnf groupinstall "Development Tools"
sudo dnf install cmake python3 python3-pip git

# Clone and build
git clone https://github.com/entity12208/hypertext-lang
cd hypertext-lang
./tools/build.py --build-type Release
sudo make install
```
**Arch Linux**
```bash
# Using AUR helper (yay)
yay -S hypertext-lang-git

# Or manual installation
git clone https://github.com/entity12208/hypertext-lang
cd hypertext-lang
makepkg -si
```
### macOS
**Using Homebrew (Recommended)**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Hypertext
brew tap hypertext-lang/hypertext
brew install hypertext
```
**Manual Installation**
```bash
# Install dependencies
brew install cmake python git

# Clone and build
git clone https://github.com/entity12208/hypertext-lang
cd hypertext-lang
./tools/build.py --build-type Release
sudo make install
```
### Windows
**Using Chocolatey (Recommended)**
```PowerShell
# Install Chocolatey if not already installed
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install Hypertext
choco install hypertext
```
**Manual Installation**
```PowerShell
# Install Visual Studio Build Tools
winget install Microsoft.VisualStudio.2022.BuildTools

# Install other dependencies
winget install Kitware.CMake
winget install Python.Python.3.11
winget install Git.Git

# Clone repository
git clone https://github.com/entity12208/hypertext-lang
cd hypertext-lang

# Build
python tools/build.py --build-type Release

# Add to PATH (run as Administrator)
setx PATH "%PATH%;C:\Program Files\Hypertext\bin"
```
## Build from Source
```bash
# Clone repository
git clone https://github.com/entity12208/hypertext-lang
cd hypertext-lang

# Create build directory
mkdir build
cd build

# Configure
cmake .. -DCMAKE_BUILD_TYPE=Release

# Build
cmake --build . -j$(nproc)

# Install
sudo cmake --install .
```
## Package Manager Installation
### npm (Node.js)
`npm install -g hypertext-lang`
### pip (Python)
`pip install hypertext-lang`

## Docker Installation
```bash
# Pull official image
docker pull hypertext/hypertext-lang:latest

# Run container
docker run -it hypertext/hypertext-lang:latest

# Or build from Dockerfile
git clone https://github.com/entity12208/hypertext-lang
cd hypertext-lang
docker build -t hypertext-lang .
```
## Development Tools
### VS Code Extension
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Hypertext Language"
4. Click Install
### JetBrains Plugin
1. Open your JetBrains IDE
2. Go to Settings → Plugins
3. Search for "Hypertext"
4. Click Install
## Verification
After installation, verify the setup:

```bash
# Check version
ht --version

# Run test program
echo 'print("Hello, Hypertext!")' > test.ht
ht test.ht
```
## Troubleshooting
### Common Issues
**Command Not Found**
```bash
# Add to PATH
export PATH="$PATH:/usr/local/bin"
```
**Missing Dependencies**
```bash
# Ubuntu/Debian
sudo apt install --fix-missing

# macOS
brew doctor
brew update && brew upgrade

# Windows
choco upgrade all
Build Errors
bash
# Clean build
rm -rf build/
./tools/build.py --clean --rebuild
```
## Getting Help
Check our [GitHub Issues](https://github.com/entity12208/hypertext-lang/issues)
Read the FAQ
