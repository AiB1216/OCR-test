from paddlex import create_pipeline
pipeline = create_pipeline(pipeline='OCR', 
                           paddlex_config='custom_ocr.yaml', 
                           model_dir="./pad_model")
print("ok")