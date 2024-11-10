import time
import json
from dotenv import load_dotenv

import subprocess
import re
import os
import google.generativeai as genai
import cv2
from logging import *
from prompts import *

FRAME_PREFIX = "_frame"
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

#Make directory for saving additional media
def create_frame_output_dir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


#Extract Python Code and the Class for Manim
def extract_code_blocks(text):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)

    class_name = r"class (.*?)\("
    class_match = re.findall(class_name, text, re.DOTALL)

    return matches, class_match


#Extracts Frame From Video
def extract_frame_from_video(video_path, output_dir='frames/'):
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)

  cap = cv2.VideoCapture(video_path)

  fps = cap.get(cv2.CAP_PROP_FPS)

  frame_count = 0
  output_index = 0

  while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
          break

      if frame_count % int(fps) == 0:
          frame_filename = os.path.join(output_dir, f'frame_00:{output_index}.jpg')
          cv2.imwrite(frame_filename, frame)
          print(f'Saved: {frame_filename}')
          output_index += 1

      frame_count += 1

  cap.release()
  print('Done extracting frames!')


#File Class to Store Response From Gemini and the Timestamp

class Files:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.timestamp = file_path.split('_')[1]
        self.response = None

    def set_file_response(self, response):
        self.response = response

    def get_info(self):
        return self.timestamp, self.response
    

#Write into a Python file the manim script
def create_python_file(response):
    code_blocks = extract_code_blocks(response.text)[0]
    for block in code_blocks:
        code = block.strip()
    filename = f"manim_script"

    with open(f"{filename}.py", 'w') as file:
        file.write(code)
    return filename

def make_request(prompt, files):
    request = [prompt]
    for file in files:

        request.append(file.get_info()[0])
        request.append(file.get_info()[1])
    print(request)
    return request


#Make a request with new prompt to revise the video and the frames from video
def make_request(prompt, files):
    request = [prompt]
    for file in files:

        request.append(file.get_info()[0])
        request.append(file.get_info()[1])
    return request


#Interacts with Gemini with a chat session

def send_message_with_retries(chat, request, max_retries=3):
    retry_wait = 60  
    for attempt in range(max_retries):
        try:
            response = chat.send_message(request)
            return response
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(retry_wait)
            retry_wait *= 2 
    raise Exception("Max retries exceeded")


#Sets the Gemini Model
def GetModel(api_key):
  genai.configure(api_key=api_key)
  generation_config = {
    "temperature": 1,
    "top_p": 0.9, 
    "top_k": 40,
    "response_mime_type": "text/plain",
  }
  model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-002",
    generation_config=generation_config,
  )
  return model


#Makes the Manim Animation, Tries to fix any issue with Gemini looking through the Frames.
def make_animation(topic):
  try:
      

    prompt = ANIMATION_PROMPT.format(problem=topic)

    model = GetModel(api_key)

    chat_session = model.start_chat(
        history=[]
    )

    attempted_1 = 0
    completed = False
    next_prompt = prompt


    #--------------- Completed First Raw Video Animation ---------------#

    while (attempted_1 < 5 and not completed):
            response = send_message_with_retries(chat_session, next_prompt)

            filename = create_python_file(response)
            class_name = extract_code_blocks(response.text)[1][0]

            command = f"manim -pql {filename}.py {class_name} --disable_caching"

            result = subprocess.run(command, shell=True,
                                    capture_output=True, text=True)

            if result.returncode == 0:
                completed = True
                print('Video animated successfully.')
            else:
                print('Failed. Trying Again!')
                attempted_1 += 1
                error_prompt = ERROR_PROMPT.format(error=result.stderr)
                next_prompt = "\n\n" + error_prompt


            if not completed and attempted_1 ==5:
                print("Failed to generate a successful output even after 5 attempts.")
                raise Exception("Failed to generate a successful output even after 5 attempts.")


    #---------------- Revising The Animated Video------------------#

    frame_extraction_directory = 'frames/'

    with open(f"{filename}.py", 'r') as file:
        initial_code = file.read()

    extract_frame_from_video(f'media/videos/manim_script/480p15/{class_name}.mp4')

    files = os.listdir(frame_extraction_directory)
    files = sorted(files)

    video_duration = len(files)

    prompt = REVISION_PROMPT.format(video_duration=video_duration, initial_code=initial_code
    )

    uploaded_files = []

    for file in files:
        file_class = Files(file)
        response = genai.upload_file(frame_extraction_directory+file)
        file_class.set_file_response(response)

        uploaded_files.append(file_class)

    request = make_request(prompt, uploaded_files)  


    completed = False
    attempted = 0

    while (attempted < 5 and not completed):
            response = send_message_with_retries(chat_session, request)

            filename = create_python_file(response)
            class_name = extract_code_blocks(response.text)[1][0]

            command = f"manim -pql {filename}.py {class_name} --disable_caching"

            result = subprocess.run(command, shell=True,
                                    capture_output=True, text=True)

            if result.returncode == 0:
                completed = True
                print('Video Revised successfully.')
            else:
                print('Failed. Revising Again!')
                attempted += 1
                error_prompt = ERROR_PROMPT.format(error=result.stderr)
                next_prompt = "\n" + error_prompt


            if not completed and attempted ==5:
                print("Failed to generate a successful output even after 5 attempts.")
                raise Exception("Failed to generate a successful output even after 5 attempts.")
            if attempted_1 >1:
                break
  except:
      pass
  
  for i in os.listdir(frame_extraction_directory):
      os.remove(frame_extraction_directory+i)
  

  all_videos_path = 'media/videos/manim_script/480p15/'
  print(os.listdir(all_videos_path))

  print(all_videos_path+class_name)

  file_video = all_videos_path + class_name + '.mp4'

  if os.path.exists(file_video):
      return file_video
  else:
      return 'No File Generated.png'
  