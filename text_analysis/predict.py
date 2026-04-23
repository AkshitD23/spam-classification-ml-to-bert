from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import sys

tokenizer = AutoTokenizer.from_pretrained("./bert_model")
model = AutoModelForSequenceClassification.from_pretrained("./bert_model")

def predict(text):
    inputs = tokenizer(text,truncation = True, padding = True, return_tensors ="pt")
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits,dim = 1)
    return "spam" if torch.argmax(probs).item() == 1 else "ham"

if len(sys.argv) > 1:
    text = " ".join(sys.argv[1:])
else:
    text = input("Enter message: ")

print("Prediction:", predict(text))