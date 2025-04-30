# 🎵 AI Music Composer

An AI-powered music generation application using Meta's MusicGen model and Streamlit interface.

## 📋 Overview

This application allows users to generate music by specifying:
- Genre (pop, jazz, classical, rock, lofi, electronic)
- Mood (happy, sad, chill, epic, romantic)
- Tempo (slow, mid, fast)

The app uses Meta's MusicGen model to generate 10-second music clips based on these parameters.

## 🔧 System Requirements

### Hardware Requirements
- **CPU**: Modern multi-core processor (Intel i5/i7 or AMD equivalent)
- **RAM**: Minimum 8GB, Recommended 16GB
- **Storage**: At least 5GB free space
- **GPU**: Optional but recommended for faster generation
  - NVIDIA GPU with CUDA support (4GB+ VRAM)
  - If no GPU, will run on CPU mode (slower)

### Software Requirements
- Python 3.9 or higher
- Windows/Linux/MacOS
- Required build tools:
  - CMake (3.10 or higher)
  - C++ build tools
    - Windows: Visual Studio Build Tools with "Desktop development with C++"
    - Linux: gcc and g++
    - MacOS: Xcode Command Line Tools

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone [repository-url]
   cd ai-music-composer
   ```

2. **Install build dependencies (Windows):**
   - Download and install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
   - Select "Desktop development with C++"
   - Download and install [CMake](https://cmake.org/download/)
   - Add CMake to system PATH during installation

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

1. **Start the application:**
   ```bash
   streamlit run main.py
   ```

2. **Using the interface:**
   - Select your desired genre from the dropdown
   - Choose the mood for your music
   - Pick the tempo
   - Click "Generate Music" button
   - Wait for generation (can take 1-2 minutes)
   - Use the download button to save your generated music

## 📁 Project Structure

```
ai-music-composer/
├── main.py           # Main application file
├── requirements.txt  # Python dependencies
├── README.md        # Documentation
└── musicgen_outputs/ # Generated music files (created on first run)
```

## ⚠️ Known Issues and Limitations

1. **Installation Complexity:**
   - Requires specific build tools and system dependencies
   - May encounter build errors if prerequisites are not met

2. **Resource Usage:**
   - High memory usage during generation
   - GPU mode requires significant VRAM
   - CPU mode is significantly slower

3. **Generation Time:**
   - Each generation takes 1-2 minutes
   - First run downloads the model (~1GB)

## 🔍 Troubleshooting

1. **Build Errors:**
   - Ensure all build tools are installed
   - Try running in a new terminal after installing tools
   - Check system PATH includes CMake

2. **Memory Issues:**
   - Close other applications
   - Switch to CPU mode if GPU memory is insufficient
   - Reduce other GPU-intensive tasks

3. **Generation Failures:**
   - Check internet connection for first run
   - Ensure enough disk space for model download
   - Try restarting the application

## 📝 Dependencies

- streamlit
- torch (2.7.0)
- torchaudio (2.7.0)
- audiocraft (from Meta's repository)

## 🔒 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

[Add contribution guidelines if applicable]

## 📧 Contact

[Add your contact information if desired]
