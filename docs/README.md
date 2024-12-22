# Hypertext Documentation

![Hypertext Logo](assets/logo.png) *(Coming Soon)*

## Welcome to Hypertext!

Hypertext (.ht) is a modern programming language that combines the simplicity of Python, the flexibility of JavaScript, and the performance of C++, with built-in web capabilities.

## Documentation Sections

### 📚 Core Documentation
- [Getting Started Guide](getting-started.md)
- [Installation Guide](installation.md)
- [Language Tutorial](tutorial/README.md)
- [Language Reference](reference/README.md)

### 🌐 Web Development
- [Web Features Overview](web/README.md)
- [HTTP Client Guide](web/http-client.md)
- [WebSocket Guide](web/websocket.md)
- [DOM Manipulation](web/dom.md)

### 📦 Standard Library
- [Standard Library Reference](stdlib/README.md)
- [Core Modules](stdlib/core.md)
- [Web Modules](stdlib/web.md)
- [I/O Operations](stdlib/io.md)

### 🛠 Tools and Integration
- [VS Code Extension](tools/vscode.md)
- [Build System](tools/build.md)
- [Package Manager](tools/package.md)

### 👥 Community
- [Contributing Guide](contributing.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Style Guide](style-guide.md)

## Quick Start Example
```ht
# Hello World with web integration
import { http } from "web"

func main() {
    # Basic console output
    print("Hello, Hypertext!")
    
    # Simple HTTP request
    http.get("https://api.example.com/greet", (response) => {
        print(response.body)
    })
}
```
## Latest Release
Current Version: 0.1.0 (Development)

[📥 Download Latest Release](https://github.com/entity12208/hypertext-lang/releases)

## Community Links
[GitHub Repository](https://github.com/entity12208/hypertext-lang)
[Issue Tracker](https://github.com/entity12208/hypertext-lang/issues)
[Discussion Forum](https://github.com/entity12208/hypertext-lang/discussions)
