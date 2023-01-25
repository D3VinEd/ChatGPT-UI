import openai
import configparser


def api_request(prompt):
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    engine = config['OPENAI-API']['engine']
    temperature = float(config['OPENAI-API']['temperature'])
    max_tokens = int(config['OPENAI-API']['maxtokens'])
    api_key = config['OPENAI-API']['apikey']
    openai.api_key = api_key
    completions = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
        # Temperature ist ein Parameter in OpenAI Completion, der die Intensität der Exploration bestimmt. Je höher
        # die Temperatur, desto mehr wird das Modell neue, unerforschte Wege erkunden, um eine bessere Lösung zu
        # finden. Eine niedrigere Temperatur erhöht die Explorationsintensität nicht und führt zu einer stärkeren
        # Exploitation des vorhandenen Wissens.
    )
    return completions.choices[0].text
