from app.multimodal.ocr import extract_text_from_image

text = extract_text_from_image("sample_input/sample_image.png")

print("Extracted Text:")
print(text)