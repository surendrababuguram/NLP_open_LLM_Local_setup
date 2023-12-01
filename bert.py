from transformers import BertTokenizer, BertModel


Models = ['bert-base-cased',
          'bert-large-uncased',
          'bert-base-uncased',
          'bert-large-cased'
          ]

for model in Models:

    # Download BERT model to the specified cache directory
    tokenizer = BertTokenizer.from_pretrained(model)
    BERTmodel = BertModel.from_pretrained(model)
    # BERT Model
    tokenizer_BERT =  tokenizer.save_pretrained("/opt/"+model)
    model_Bert = BERTmodel.save_pretrained("/opt/"+model)
