from transformers import T5ForConditionalGeneration, T5Tokenizer

# Download T5-small model and tokenizer
t5_model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# Save the model and tokenizer to the desired directory
t5_model.save_pretrained("/opt/t5-small")
tokenizer.save_pretrained("/opt/t5-small")

# Download T5-small model and tokenizer
t5_model = T5ForConditionalGeneration.from_pretrained("t5-base")
tokenizer = T5Tokenizer.from_pretrained("t5-base")

# Save the model and tokenizer to the desired directory
t5_model.save_pretrained("/opt/t5-base")
tokenizer.save_pretrained("/opt/t5-base")

# Download T5-small model and tokenizer
t5_model = T5ForConditionalGeneration.from_pretrained("t5-large")
tokenizer = T5Tokenizer.from_pretrained("t5-large")

# Save the model and tokenizer to the desired directory
t5_model.save_pretrained("/opt/t5-large")
tokenizer.save_pretrained("/opt/t5-large")
