def translate(sentence, model, tokenizer):
    
    translated_tokens = model.generate(**tokenizer.prepare_seq2seq_batch([sentence], return_tensors="pt"))
    translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated_tokens]
    
    return translated_text