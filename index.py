import moviepy.editor as mp

# set the video path and audio threshold based on your needs
video_path = 'P7.mp4'
audio_threshold = 0 
duration = 0

video = mp.VideoFileClip(video_path)

for t in range(int(video.duration)):
    audio_volume = video.audio.subclip(t, t+1).max_volume()
    if audio_volume > audio_threshold:
        duration += 1

hours = duration // 3600
minutes = (duration % 3600) // 60
seconds = duration % 60

print(f"Audio length with volume above {audio_threshold} dB: {hours:02d}:{minutes:02d}:{seconds:02d}")