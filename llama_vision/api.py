from huggingface_hub import InferenceClient
from PIL import Image
from base64 import b64encode
import tkinter as tk
from tkinter import filedialog

client = InferenceClient(api_key="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") # login

# Get user input
user_messages = input('Message Llama 3.2 Vi: ')
# Get image path
root = tk.Tk()
root.withdraw() 
image_path = filedialog.askopenfilename(
    title="Select a File",
    filetypes=[("Text Files", "*.jpeg")]
)
print(f'Image path: {image_path}')

# Formating
with open(image_path, "rb") as image_file:
    base64_image = b64encode(image_file.read()).decode("utf-8")


# Pass to api
messages = [
	{
		"role": "user",
		"content": [
			{
				"type": "text",
				"text": f"{user_messages}"
			},
			{
				"type": "image_url",
				"image_url": {
					"url": f"data:image/jpeg;base64,{base64_image}"
				}
			}
		]
	}
]

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct", 
	messages=messages, 
	max_tokens=500
)

# print(completion.choices[0].message)
print('-'*50)
print(completion.choices[0].message.content)
print('='*50)