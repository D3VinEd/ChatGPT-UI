import openai
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

ENGINE = config['OPENAI-API']['Engine']
TEMPERATURE = float(config['OPENAI-API']['Temperature'])
MAX_TOKENS = int(config['OPENAI-API']['MaxTokens'])
API_KEY = config['OPENAI-API']['APIKey']


def api_request(prompt):
    openai.api_key = API_KEY
    completions = openai.Completion.create(
        engine=ENGINE,
        prompt=prompt,
        max_tokens=MAX_TOKENS,
        n=1,
        stop=None,
        temperature=TEMPERATURE,
        # Temperature ist ein Parameter in OpenAI Completion, der die Intensität der Exploration bestimmt. Je höher
        # die Temperatur, desto mehr wird das Modell neue, unerforschte Wege erkunden, um eine bessere Lösung zu
        # finden. Eine niedrigere Temperatur erhöht die Explorationsintensität nicht und führt zu einer stärkeren
        # Exploitation des vorhandenen Wissens.
    )
    message = completions.choices[0].text
    # print(completions.choices)
    return message
