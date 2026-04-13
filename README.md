# Video to Audio Converter

A simple Python script that batch converts MP4 video files to MP3 audio files using MoviePy.

## Overview

This tool automatically scans an `input` folder for MP4 files and extracts their audio tracks, saving them as MP3 files in an `output` folder. Perfect for extracting audio from video recordings, creating podcast episodes from video content, or reducing file sizes.

## Features

- 🎬 **Batch Processing** - Converts all MP4 files at once
- 📁 **Organized Structure** - Separate `input` and `output` folders
- 🔄 **Automatic Discovery** - No need to manually specify input files
- 📝 **Case-Insensitive** - Finds files with `.mp4`, `.MP4`, `.Mp4`, etc.
- 🚀 **Auto-Create Folders** - Creates input/output directories if missing
- ⚠️ **Error Handling** - Continues processing remaining files if one fails
- 📊 **Progress Feedback** - Real-time status updates during conversion

## Requirements

- Python 3.6 or higher
- MoviePy library

## Installation

1. Clone or download this repository
2. Install the required dependency:

```bash
pip install moviepy
```

## Usage

1. Place your MP4 files in the `input` folder (the script will create this folder automatically on first run)
2. Run the script:

```bash
python video-converter.py
```

3. The script will:
   - Scan for all MP4 files in the `input` folder
   - Convert each video to MP3 format
   - Save the MP3 files in the `output` folder with the same base filename

### Example

```
Project Structure:
video-converter/
├── video-converter.py
├── input/
│   ├── meeting-recording.mp4
│   └── presentation.mp4
└── output/
    ├── meeting-recording.mp3  ← Converted!
    └── presentation.mp3        ← Converted!
```

## How It Works

1. **Creates Folders** - Automatically creates `input` and `output` directories if they don't exist
2. **Scans Input Folder** - Lists all files in the `input` directory
3. **Filters MP4 Files** - Identifies video files (case-insensitive)
4. **Extracts Audio** - Uses MoviePy to extract audio tracks
5. **Saves as MP3** - Writes audio to the `output` folder
6. **Cleans Up** - Properly closes video objects to free memory

## Error Handling

If a conversion fails for any file, the script will:
- Print an error message with the filename and error details
- Continue processing the remaining files
- Complete the batch operation

## Technical Details

- **Library**: MoviePy (built on FFmpeg)
- **Input Format**: MP4 video files
- **Output Format**: MP3 audio files
- **Audio Quality**: Default MoviePy settings (typically 128 kbps)

## Limitations

- Only processes MP4 files (other video formats not supported)
- Requires sufficient disk space for output files
- Processing time depends on video length and system performance

## Troubleshooting

### "No MP4 files found"
- Ensure MP4 files are in the `input` folder
- Check file extensions are `.mp4` (or case variants)
- The script will create the `input` folder automatically if it doesn't exist

### "Error converting [filename]"
- Verify the video file is not corrupted
- Ensure the video contains an audio track
- Check you have write permissions in the directory

### MoviePy Installation Issues
If you encounter issues installing MoviePy:
```bash
pip install --upgrade pip
pip install moviepy
```

## License

This project is open source and available for personal and commercial use.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.