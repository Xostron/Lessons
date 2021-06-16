import time

unnecessary = ("the", "and", "was", "were", "not", 'did', 'will', 'had', 'have', 'has',
               'all', 'that', 'this', 'with', 'for', 'from', 'are', 'she', 'they', 'his',
               'then', 'than', 'york',)


class Collect:
    def __init__(self):
        self.stat = {}
        self.word = ''

    def collections(self, file_name):
        with open(file_name, 'r', encoding='cp1251') as file:
            self.word = ""
            for line in file:
                for char in line:
                    if 90 >= ord(char) >= 65 or 122 >= ord(char) >= 97:
                        self.word += char
                    elif len(self.word) > 2 and not self.word in unnecessary:
                        if self.word in self.stat:
                            self.stat[self.word] += 1
                        else:
                            self.stat[self.word] = 1
                        self.word = ""
                    elif len(self.word) <= 2:
                        self.word = ""
                    else:
                        self.word = ""
                    self.word = self.word.lower()
            self.collect = list(self.stat.items())
            self.collect.sort(key=lambda x: x[1], reverse=True)
            self.resultTop = [i[0] for i in self.collect]
        return self.resultTop


mark = Collect()
file_name = input("ведите путь книги: \n")
started_at = time.time()  # ====================
try:
    result = mark.collections(file_name)
except FileNotFoundError:
    result = []
ended_at = time.time()  # ====================
elapsed = round(ended_at - started_at, 6)  # ====================
print(result[:100])
print(elapsed)


