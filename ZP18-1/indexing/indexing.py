import random


class IndexText:
    lines = None
    indexes = None
    def __init__(self, text_file):
        self.indexes = {}
        with open(text_file) as f:
            data = f.read().split('.')
            self.lines = {i:line for i, line in enumerate(data)}
        for i, line in self.lines.items():
            self.index(i,line)

    def index(self,line_id, line:str):
        line = line.strip()
        words = [word for word in line.split(' ')]
        for word in words:
            index = self.indexes.get(word,[])
            index.append(line_id)
            self.indexes[word] = index

    def find(self, word):
        if word not in self.indexes:
            print("No sentences in the text contain this word.")
        else:
            for line_id in self.indexes[word]:
                print(line_id, self.lines[line_id])

def mock_text():
    get_lower = lambda :chr(random.randint(97, 112))
    get_upper = lambda :chr(random.randint(65, 90))
    with open('test.txt', 'w') as f:
        for _ in range(100_000):
            sentence = []
            for _ in range(random.randint(10,100)):
                word = []
                for _ in range(random.randint(1,10)):
                    word.append(random.choice([get_upper, get_lower])())
                sentence.append("".join(word))
            print(*sentence,'.',file=f)


# mock_text()
indexed = IndexText('test.txt')
print("Done")