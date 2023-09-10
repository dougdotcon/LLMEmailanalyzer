# llm_trainer.py

from langchain import LLMChain, PromptTemplate, HuggingFaceHub
import json

def train_llm(emails):
    # Criando um template de prompt para treinamento
    template = """Question: {question}\nAnswer: """
    prompt = PromptTemplate(template=template, input_variables=['question'])
    
    # Usando um modelo do Hugging Face Hub como exemplo
    hub_llm = HuggingFaceHub(repo_id='google/flan-t5-xl', model_kwargs={'temperature':1e-10})
    
    # Criando uma cadeia com o template e o modelo
    llm_chain = LLMChain(prompt=prompt, llm=hub_llm)
    
    # Treinando o modelo (isso é um exemplo simplificado, pode ser necessário ajustar conforme a documentação)
    for email in emails:
        question = email['body']  # Supondo que o corpo do e-mail seja a questão
        llm_chain.run(question)
    
    # Salvando o modelo treinado (isso é um exemplo, pode ser necessário ajustar conforme a documentação)
    llm_chain.save('../models/llm_model')
    
    return llm_chain

if __name__ == '__main__':
    # Carregando e-mails processados (isso é apenas um exemplo, você pode ajustar conforme necessário)
    with open('../data/processed_data/emails.json', 'r') as file:
        emails = json.load(file)
    
    train_llm(emails)
