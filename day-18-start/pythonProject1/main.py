import turtle
from turtle import Turtle, Screen
import random
#this is how you import stuff using an alia. You may want to use an alias if the name of a module is long
#import turtle as t
#tim = t.Turtle()

#if you uncomment the line below and click on the red bulb you will be prompted to install a module that
#does not come in the python standard library
#import heroes
turtle.colormode(255)
tim = Turtle()
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Fuchsia", "Aqua", "Lime"]
directions = [0, 90, 180, 270, -90, -180, -270]
#-90, -180, -270

# numSides = 3
# while numSides < 10:
#     tim.color(random.choice(colors))
#     for i in range(numSides):
#         tim.forward(100)
#         tim.right(360/numSides)
#     numSides += 1


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
tim.speed("fastest")
# for i in range(100):
#     angle = random.choice(directions)
#     tim.color(random_color())
#     tim.setheading(angle)
#     tim.forward(25)

num_circles = 100
for i in range(num_circles):
    tim.color(random_color())
    tim.circle(100,360,50)
    tim.left(360/num_circles)

tim_orientation = tim.heading()
















screen = Screen()
screen.exitonclick()



import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AwqConfig

model_id = "hugging-quants/Meta-Llama-3.1-405B-Instruct-AWQ-INT4"
quantization_config = AwqConfig(
    bits=4,
    fuse_max_seq_len=512, # Note: Update this as per your use-case
    do_fuse=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
  model_id,
  torch_dtype=torch.float16,
  low_cpu_mem_usage=True,
  device_map="auto",
  quantization_config=quantization_config
)

prompt = [
  {"role": "system", "content": "You are a helpful assistant, that responds as a pirate."},
  {"role": "user", "content": "What's Deep Learning?"},
]
inputs = tokenizer.apply_chat_template(
  prompt,
  tokenize=True,
  add_generation_prompt=True,
  return_tensors="pt",
  return_dict=True,
).to("cuda")

outputs = model.generate(**inputs, do_sample=True, max_new_tokens=256)
print(tokenizer.batch_decode(outputs[:, inputs['input_ids'].shape[1]:], skip_special_tokens=True)[0])

