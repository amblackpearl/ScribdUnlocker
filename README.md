# ScribdUnlocker

A desktop application that unlocks Scribd document previews, allowing users to access content directly through their browser.

## Features

- **Simple Interface**: Paste a Scribd link and unlock with one click
- **Automatic Browser Launch**: Opens the unlocked document directly in your default browser
- **Lightweight**: Minimal system resource usage

## Preview

![ScribdUnlocker Preview](https://github.com/user-attachments/assets/0dbf7d3b-29ae-4b64-a07b-3f2553c6861a)

*Application interface showing the Scribd link input field and unlock button*

## Technical Details

- **Language**: Python
- **GUI Framework**: Tkinter (Python's standard GUI toolkit)
- **Packaging**: PyInstaller for creating standalone executables

## Installation

### Download Executable
1. Navigate to the `/dist` folder in this repository
2. Download the appropriate executable for your operating system
3. Run the executable directly (no installation required)

*Note: The application is currently distributed via direct download from the `/dist` folder as we establish automated release workflows.*

## Usage

1. Launch `ScribdUnlocker.exe` (Windows) or the appropriate executable for your OS
2. Copy a Scribd document URL (e.g., `https://www.scribd.com/document/...`)
3. Paste the URL into the application
4. Click the **"Unlock"** button
5. The document will automatically open in your default web browser

## Project Structure
```
ScribdUnlocker/
├── dist/ # Compiled executables
├── src/ # Source code (if applicable)
├── README.md # This file
└── (other project files)
```

## Development

This project is built with Python and uses:
- **Tkinter** for the graphical user interface
- **PyInstaller** for packaging into standalone executables
- **Standard Python libraries** for URL processing and browser control

## Limitations

- Requires an active internet connection
- Functionality depends on Scribd's current website structure
- Only unlocks document previews as permitted by Scribd's terms of service

## Disclaimer

This tool is intended for educational purposes and to access content that is legally available for preview. Users are responsible for complying with Scribd's Terms of Service and respecting copyright laws.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

[Specify your license here - e.g., MIT, GPL, etc.]

## Support

For issues or questions:
- Open an issue on [GitHub](https://github.com/amblackpearl/ScribdUnlocker/issues)
- Ensure you provide the Scribd URL and describe the problem in detail
