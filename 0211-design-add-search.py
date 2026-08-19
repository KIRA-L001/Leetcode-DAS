class WordDictionary:
    def __init__(self): self.d = {}
    def addWord(self, word: str) -> None:
        self.d.setdefault(len(word), []).append(word)
    def search(self, word: str) -> bool:
        import re
        pat = re.compile('^' + word + '$')
        return any(pat.match(w) for w in self.d.get(len(word), []))
