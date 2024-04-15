from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch
import re
device = "cuda" 

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True, # Enables loading the model in 4-bit precision
    bnb_4bit_quant_type="nf4", # Specifies the quantization type
    bnb_4bit_use_double_quant=True, # Enables double quantization for better precision
)
# Loading the tokenizer
tokenizer = AutoTokenizer.from_pretrained("./Mistral-7B-Instruct-v0.2")
# Loading the model with BitsAndBytes configuration, and additional settings from Method-1
model = AutoModelForCausalLM.from_pretrained(
    "./Mistral-7B-Instruct-v0.2",
    torch_dtype=torch.float16, # Sets the tensor type to float16 for faster computation
    device_map="auto", # Automatically maps the model layers to the available devices
    trust_remote_code=True, # Allows the execution of remote code for custom model configurations
    #attn_implementation="flash_attention_2", # Uses a specific attention implementation optimized for performance
    quantization_config=bnb_config, # Applies the BitsAndBytes configuration
)
# Prepare the messages for encoding
# messages = [
#     {"role": "user", "content": "What is your favourite condiment?"},
#     {"role": "assistant", "content": "Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!"},
#     {"role": "user", "content": "Do you have mayonnaise recipes?"}
# ]

prompt_template = '''<s>[INST] just provide 'Yes' or 'No' for whether the following commit message is implementing performance optimization or not.
{commit_message} [/INST]</s>'''


sample_commit_message = "scsi: ufs: add debug counters for recoverable errors during runtime  There is no way to know how many times various UFS errors happened while system is running if we have successfully recovered from those errors. Those failures should be counted and inspected as they might be anomaly behavior of the driver and can impact performance. This change adds support to capture these failures statistics like how many times we have seen errors, and which type of errors.  To reset the counters: echo 1 > /sys/kernel/debug/ufs/err_stats  To print them out: cat /sys/kernel/debug/ufs/err_stats  Note: There is no need to enable them as they are never disabled. This error counters are something that we always would like to have."

generated_prompt = prompt_template.format(commit_message=sample_commit_message)

inputs = tokenizer.apply_chat_template(
            [{'role': 'user', 'content': generated_prompt}],
            return_tensors="pt"
        ).to(model.device)

outputs = model.generate(
        inputs, 
        max_new_tokens=5,
        do_sample=True)

# Encode the messages using the tokenizer
#encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt").to(device)
# Generate responses using the model
#generated_ids = model.generate(encodeds, max_new_tokens=5, do_sample=True)
#decoded = tokenizer.batch_decode(generated_ids)
# Print the generated response
#df['Mistral_result_cleaned']=df['Mistral_result'].apply(lambda x: re.search(r'\b(Yes|No)\b', x).group(0) if re.search(r'\b(Yes|No)\b', x) else None)

def parse_output(out):
    res = re.search(r'\b(Yes|No)\b', out)
    if res:
        return res.group(0)
    else:
        return None

value = parse_output(tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True))
with open('mistral.txt', 'w') as file:
    file.write(value)