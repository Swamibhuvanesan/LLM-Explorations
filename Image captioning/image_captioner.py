from transformers import pipeline

captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
result = captioner("img//shark.jpg", max_new_tokens=50)
print(result)
