from transformers import T5Model, BertModel

Models = ['small',
          'base',
          'large',
          '3b',
          '11b'
          ]

for model in Models:

    t5_model = T5Model.from_pretrained("t5-"+model)
    t5_model.save_pretrained("/opt/t5-"+model)
