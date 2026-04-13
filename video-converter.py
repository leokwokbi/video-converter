import moviepy.editor as mp
import os

def batch_convert_folder():
    # Get the directory where this script is currently located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define input and output directories
    input_dir = os.path.join(script_dir, 'input')
    output_dir = os.path.join(script_dir, 'output')
    
    # Create directories if they don't exist
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    # List all files in the input directory
    files = os.listdir(input_dir)
    
    # Filter for mp4 files (case-insensitive)
    mp4_files = [f for f in files if f.lower().endswith('.mp4')]
    
    if not mp4_files:
        print(f"No MP4 files found in the 'input' folder: {input_dir}")
        print("Please place your MP4 files in the 'input' folder and run again.")
        return

    print(f"Found {len(mp4_files)} MP4 file(s) in 'input' folder. Starting conversion...\n")

    for filename in mp4_files:
        try:
            # Construct the full file paths
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + ".mp3"
            output_path = os.path.join(output_dir, output_filename)
            
            # Process the file
            video = mp.VideoFileClip(input_path)
            video.audio.write_audiofile(output_path)
            video.close()
            
            print(f"✓ Converted: {filename} → output/{output_filename}\n")
            
        except Exception as e:
            print(f"Error converting {filename}: {e}")

    print(f"All conversions complete! MP3 files saved in: {output_dir}")

if __name__ == "__main__":
    batch_convert_folder()