import gradio as gr
import openai

openai.api_key = "OPEN-AI API KEY HERE"

def greet(text):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Who won the world series in 2020?"},
      {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
      {"role": "user", "content": f"{text}"}
      ]
    )
    return completion.choices[0].message.content


iface = gr.Interface(fn=greet, inputs="text", outputs="text", title="ChatGPT-3.5-turbo-model", theme="dark", layout="vertical")

iface.launch()
