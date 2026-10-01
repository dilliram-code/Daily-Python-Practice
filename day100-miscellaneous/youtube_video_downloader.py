import streamlit as st
import yt_dlp
import os

def download_video(video_url):
    # Configure options for 1080p video + best audio
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Saves inside a "downloads" folder
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        # Get the final merged filename path
        filename = ydl.prepare_filename(info)
        return filename

# Streamlit UI Setup
st.set_page_config(page_title="FHD YouTube Downloader", page_icon="🎥")
st.title("🎥 FHD YouTube Downloader")
st.write("Paste a YouTube link below to download the video in **1080p (FHD) with sound**.")

# Input Field
url = st.text_input("YouTube Video URL", placeholder="https://youtube.com...")

if url:
    if st.button("Process & Download Video", use_container_width=True):
        try:
            with st.spinner("📥 Fetching video and merging high-quality audio (this may take a moment)..."):
                # Run the download logic
                filepath = download_video(url)
                
            st.success("✅ Video successfully processed!")
            
            # Read file bytes to provide a local browser download button
            with open(filepath, "rb") as file:
                st.download_button(
                    label="💾 Save Video to Your Device",
                    data=file,
                    file_name=os.path.basename(filepath),
                    mime="video/mp4",
                    use_container_width=True
                )
                
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
