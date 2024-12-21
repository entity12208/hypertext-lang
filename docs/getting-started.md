# Getting Started with Hypertext (.ht)

## Table of Contents
1. [Installation](#installation)
2. [Development Environment Setup](#development-environment-setup)
3. [Core Concepts](#core-concepts)
4. [First Program](#your-first-program)
5. [Web Integration](#web-integration)
6. [Common Patterns](#common-patterns)
7. [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites
- C++ compiler (GCC 7+ or Clang 6+)
- CMake 3.15+
- Python 3.8+
- Git

### Step-by-Step Installation

#### Linux
```bash
# Install dependencies (Ubuntu/Debian)
sudo apt update
sudo apt install build-essential cmake python3 python3-pip git

# Clone and build Hypertext
git clone https://github.com/entity12208/hypertext-lang
cd hypertext-lang
./tools/build.py --build-type Release

# Install system-wide
sudo make install
```
#### macOS
```bash
# Install dependencies using Homebrew
brew install cmake python git

# Clone and build Hypertext
git clone https://github.com/entity12208/hypertext-lang
cd hypertext-lang
./tools/build.py --build-type Release

# Install system-wide
sudo make install
```
#### Windows
```PowerShell
# Install dependencies (using Chocolatey)
choco install cmake python git visualstudio2022-workload-vctools

# Clone and build Hypertext
git clone https://github.com/entity12208/hypertext-lang
cd hypertext-lang
python tools/build.py --build-type Release

# Add to PATH (run as Administrator)
setx PATH "%PATH%;C:\Program Files\Hypertext\bin"
```
## Development Environment Setup
### VS Code Setup
1. Install VS Code
2. Install the Hypertext Extension:
- Open VS Code
- Press Ctrl+P (Windows/Linux) or Cmd+P (macOS)
- Type: ext install hypertext-lang
### Configuration
```JSON
// .vscode/settings.json
{
    "hypertext.path": "/usr/local/bin/ht",
    "hypertext.formatOnSave": true,
    "hypertext.lintOnSave": true,
    "editor.tabSize": 4
}
```
## Core Concepts
### 1. Variables and Types
```ht
# Type inference (recommended)
let name = "Hypertext"
let age = 25
let price = 19.99
let isActive = true

# Explicit typing
string title: "Hello"
int count: 0
float value: 3.14
bool flag: false

# Constants
const PI = 3.14159
const API_URL = "https://api.example.com"
```
### 2. Functions
```ht
# Basic function
func greet(name: string) -> string {
    return "Hello, ${name}!"
}

# Multiple parameters with type inference
func calculate(x, y) {
    return x * y + 100
}

# Async function
async func fetchData(url: string) -> Response {
    return await http.get(url)
}
```
### 3. Control Flow
```ht
# If statements
if age >= 18 {
    print("Adult")
} else if age >= 13 {
    print("Teenager")
} else {
    print("Child")
}

# Loops
for i in range(5) {
    print(i)
}

while condition {
    # do something
}
```
## Your First Program
Create a new file `hello.ht`:
```ht
# hello.ht - Your first Hypertext program

func main() {
    # Get user input
    print("What's your name?")
    let name = input()
    
    # Greet the user
    print("Hello, ${name}!")
    
    # Basic calculation
    let numbers = [1, 2, 3, 4, 5]
    let sum = 0
    
    for num in numbers {
        sum += num
    }
    
    print("Sum of numbers: ${sum}")
}
```
Run your program:
`ht hello.ht`
## Web Integration
### Simple Web Server
```ht
import { http } from "web"

func main() {
    let server = http.createServer()
    
    server.get("/", (req, res) => {
        res.send("Hello from Hypertext!")
    })
    
    server.listen(3000, () => {
        print("Server running at http://localhost:3000")
    })
}
```
### HTTP Client
```ht
import { http } from "web"

async func fetchUserData(userId: string) {
    try {
        let response = await http.get(
            "https://api.example.com/users/${userId}"
        )
        
        if response.ok {
            let user = response.json()
            print("User: ${user.name}")
        }
    } catch (error) {
        print("Error: ${error.message}")
    }
}
```
## Common Patterns
### Error Handling
```ht
func divideNumbers(a: int, b: int) -> float {
    try {
        if b == 0 {
            throw Error("Division by zero")
        }
        return a / b
    } catch (error) {
        print("Error: ${error.message}")
        return 0
    }
}
```
### Working with Files
```ht
func readConfig() {
    try {
        let file = File.open("config.json", "r")
        let content = file.readAll()
        let config = JSON.parse(content)
        return config
    } catch (error) {
        print("Could not read config: ${error.message}")
        return null
    } finally {
        file.close()
    }
}
```
## Troubleshooting
### Common Issues and Solutions
1. **Command not found**

```bash
# Add to PATH
export PATH="$PATH:/usr/local/bin"
```
2. **Compilation Errors**

- Check compiler version
- Verify all dependencies are installed
- Run with debug flag: `ht --debug your_file.ht`
3. **Missing Libraries**

```bash
# Install development tools
sudo apt install build-essential
./tools/build.py --rebuild
```
### Getting Help
* Visit our GitHub Issues
* Join our Discussion Forum
* Check the FAQ
## Next Steps
- Explore the Tutorial Series
- Read the Language Reference
- Try the Web Development Guide
- Contribute to Hypertext
Remember: The best way to learn Hypertext is by writing code! Start with small programs and gradually build more complex applications as you become comfortable with the language features.
