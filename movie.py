import moviepy.editor as mp
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
import cv2

# Load the video clips
clip1 = mp.VideoFileClip('src/vid2.mp4')
clip2 = mp.VideoFileClip('src/vid1.mp4')

start_time = 0.0121
end_time = 0.0214

# Create a cropped subclip
clip = clip1.subclip(start_time, end_time)
clip_2= clip2.subclip(start_time, 4)
fade_duration = 1

# Apply the fade-in transition to the second clip
fadein_clip2 = clip_2.fx(fadeout, fade_duration)

# Apply the fade-out transition to the first clip
fadeout_clip1 = clip.fx(fadein, fade_duration)

# Concatenate the clips with the transitions
final_clip = mp.CompositeVideoClip([fadeout_clip1, fadein_clip2.set_start(3).crossfadein(1)])

for frame in final_clip.iter_frames(fps=final_clip.fps*5):
    frame = cv2.cvtColor(frame.astype('uint8'), cv2.COLOR_RGB2BGR)  # Convert to 8-bit depth
    cv2.imshow("Final Clip", frame)
    
    # Check for the 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()