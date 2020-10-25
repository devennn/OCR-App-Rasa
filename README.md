# OCR App Rasa
OCR Appa rasa chatbot

## Train Model

```python -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose```

## Run Model 

```python nlu_model.py```

## Reference 
- https://medium.com/@itsromiljain/build-a-conversational-chatbot-with-rasa-stack-and-python-rasa-nlu-b79dfbe59491
- https://legacy-docs.rasa.com/docs/nlu/python/