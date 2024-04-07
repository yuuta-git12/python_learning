class Word(object):
    def __init__(self, text) -> None:
        self.text = text
    
    def __str__(self) -> str:
        return 'これは__str__の表示テストです'

    def __len__(self):
        return len(self.text)
    
    def __add__(self, word):
        return self.text.lower() + word.text.lower()
    
    def __eq__(self, word):
        return self.text == word


w = Word('これはテストです')
w2 = Word('これはテストです')
print(w)
print(len(w))
print(w + w2)
print(w == w2)
print(id(w))
print(id(w2))
