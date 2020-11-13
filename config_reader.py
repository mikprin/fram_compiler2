import re

class Config:
    #Horizontal size
    word_size = 0
    #Vertical size
    num_words = 0
    #Output file name
    output_name = ""
    
    def __open_config(self, filename: str):
        f = open(filename, 'r')
        text = f.read()
        f.close()
        return text

    def __parse_config(self, config: str):
        reg = re.compile(r'^\s*([\d\w]+)\s*:\s*([\d\w\.]+)\s*$', flags=re.MULTILINE)
        matches = reg.findall(config)
        return matches
    
    def __apply_config(self, config):
        for i in config:
            key = i[0]
            value = i[1]
            if key == 'word_size':
                self.word_size = value
            if key == 'num_words':
                self.num_words = value
            if key == 'output_name':
                self.output_name = value

    def __init__(self, filename: str):
        config_text = self.__open_config(filename)
        matches = self.__parse_config(config_text)
        self.__apply_config(matches)

# Test
conf = Config("test.conf")
print(conf)