import requests
import pydub
import io

# define function to read in sound file
def get_audio_from_url(url):
  """Lấy audio từ một URL."""
  response = requests.get(url,verify=False)
  audio_data = response.content
  return audio_data

def convert_audio_to_16khz(audio_data):
  """Chuyển đổi audio thành định dạng 16kHz."""
  audio_format = pydub.AudioSegment.from_file(io.BytesIO(audio_data))
  audio_format = audio_format.set_frame_rate(16000)
  return audio_format

def split_audio_into_clips(audio_format, clip_duration_seconds):
  """Chia audio thành các clip nhỏ hơn."""
  clips = []
  start_time = 0
  while start_time < audio_format.duration_seconds:
    end_time = min(start_time + clip_duration_seconds, audio_format.duration_seconds)
    clip = audio_format[start_time:end_time]
    clips.append(clip)
    start_time = end_time
  return clips

