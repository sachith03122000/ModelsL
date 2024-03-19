from transformers import GPT2LMHeadModel, GPT2Tokenizer
from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

@app.task
def generate_text(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    max_length = len(input_ids[0]) + 50  # Adjust as needed
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    text_output = tokenizer.decode(output[0], skip_special_tokens=True)
    return text_output
