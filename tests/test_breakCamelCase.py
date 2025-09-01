import pytest
from challenges.breakCamelCase import breakCamelCase

def test_single_word():
    assert breakCamelCase('word') == 'word'

@pytest.mark.parametrize('sentence', [
    'several normal words',
    'more words',
    'space separated'
])
def test_multiple_non_camel_words(sentence):
   assert breakCamelCase(sentence) == sentence

def test_camel_case_word():
    assert breakCamelCase('camelCase') == 'camel Case'

def test_sentence_with_camelCase():
    assert breakCamelCase('Camel case isThebest') == 'Camel case is Thebest'

def test_multi_camel_word():
    assert breakCamelCase('breakCamelCase') == 'break Camel Case'

def test_multi_camel_word_sentence():
    assert breakCamelCase('breakCamelCase torpedo assassinsCreed') == 'break Camel Case torpedo assassins Creed'