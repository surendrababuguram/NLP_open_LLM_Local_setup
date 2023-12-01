# NLP_open_LLM_Local_setup
  #### Run all the files locally to store models locally
  
# Usage
  Models are stored in the `/opt` directory.

Here's an example:


# NLP Models

## T5 Models

### T5-Small
- **Description:** Pre-trained T5 model with a smaller architecture.
- **Model Path:** `/opt/t5-small`
- **Usage Example:**
  ```python
  from transformers import T5ForConditionalGeneration, T5Tokenizer
  model_name = "/opt/t5-small"
  model = T5ForConditionalGeneration.from_pretrained(model_name)
  tokenizer = T5Tokenizer.from_pretrained(model_name)
  ```

### T5-Base
- **Description:** Pre-trained T5 model with a base architecture.
- **Model Path:** `/opt/t5-base`
- **Usage Example:**
  ```python
  from transformers import T5ForConditionalGeneration, T5Tokenizer
  model_name = "/opt/t5-base"
  model = T5ForConditionalGeneration.from_pretrained(model_name)
  tokenizer = T5Tokenizer.from_pretrained(model_name)
  ```

### T5-Large
- **Description:** Pre-trained T5 model with a larger architecture.
- **Model Path:** `/opt/t5-large`
- **Usage Example:**
  ```python
  from transformers import T5ForConditionalGeneration, T5Tokenizer
  model_name = "/opt/t5-large"
  model = T5ForConditionalGeneration.from_pretrained(model_name)
  tokenizer = T5Tokenizer.from_pretrained(model_name)
  ```

## BERT Models

### BERT-Base-Uncased
- **Description:** Pre-trained BERT model with a base, uncased architecture.
- **Model Path:** `/opt/bert-base-uncased`
- **Usage Example:**
  ```python
  from transformers import BertForQuestionAnswering, BertTokenizer
  model_name = "/opt/bert-base-uncased"
  model = BertForQuestionAnswering.from_pretrained(model_name)
  tokenizer = BertTokenizer.from_pretrained(model_name)
  ```

### BERT-Base-Cased
- **Description:** Pre-trained BERT model with a base, cased architecture.
- **Model Path:** `/opt/bert-base-cased`
- **Usage Example:**
  ```python
  from transformers import BertForQuestionAnswering, BertTokenizer
  model_name = "/opt/bert-base-cased"
  model = BertForQuestionAnswering.from_pretrained(model_name)
  tokenizer = BertTokenizer.from_pretrained(model_name)
  ```

### BERT-Large-Uncased
- **Description:** Pre-trained BERT model with a large, uncased architecture.
- **Model Path:** `/opt/bert-large-uncased`
- **Usage Example:**
  ```python
  from transformers import BertForQuestionAnswering, BertTokenizer
  model_name = "/opt/bert-large-uncased"
  model = BertForQuestionAnswering.from_pretrained(model_name)
  tokenizer = BertTokenizer.from_pretrained(model_name)
  ```

### BERT-Large-Cased
- **Description:** Pre-trained BERT model with a large, cased architecture.
- **Model Path:** `/opt/bert-large-cased`
- **Usage Example:**
  ```python
  from transformers import BertForQuestionAnswering, BertTokenizer
  model_name = "/opt/bert-large-cased"
  model = BertForQuestionAnswering.from_pretrained(model_name)
  tokenizer = BertTokenizer.from_pretrained(model_name)
  ```
```

