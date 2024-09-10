import sys, os, dotenv
from openai import OpenAI

dotenv.load_dotenv()

key = os.getenv("OPENAI_API_KEY")
print(key)
client = OpenAI(api_key=key)
languageCodeNames = {
    'en': 'English',
    'pt': 'Portuguese',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh': 'Chinese',
    'ru': 'Russian'

}


def translate_file(input_file, output_file, lang):

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
        print(text)

    translated = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You translate the readME of a project to {}. Please, don't translate urls or project names".format(languageCodeNames[lang])},
            {"role": "user", "content": text}
        ]
    ).choices[0].message.content

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated)

if __name__ == "__main__":
    input_file = sys.argv[1]
    language = sys.argv[2]

    translate_file(input_file, f'README.{language}.md', language)
