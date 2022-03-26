""" This file is used to test IBM Watson translation services """
#import json
import os
from ibm_watson                         import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators  import IAMAuthenticator
from dotenv                             import load_dotenv

load_dotenv()

apikey              = os.environ['apikey']
url                 = os.environ['url']
authenticator       = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ This method is used to translate english text to french """
    return translate(text=english_text, from_language='en', to_language='fr')

def french_to_english(french_text):
    """ This method is used to translate french text to english """
    return translate(text=french_text, from_language='fr', to_language='en')

def translate(text, from_language, to_language):
    """ This method is used to translate text from one language to another """
    if text is not None:
        model = from_language + '-' + to_language
        result = language_translator.translate(text=text, model_id=model).get_result()
        translation = result["translations"][0]["translation"]
        return translation
    return None
