import openai

def get_car_ai_comments(model, brand, year):
    prompt = '''
        Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Foque nas especificações técnicas desse modelo.
    '''

    openai.api_key = 'sk-proj-aFckrE06NunOfvWSyIqLT3BlbkFJHVGKmCvwGvFP6H6BlZTj'
    prompt = prompt.format(brand, model, year)
    response = openai.Completion.create(
        model='gpt-3.5-turbo',
        prompt=prompt,
        max_tokens=1000
    )
    return response['choices'][0]['text']