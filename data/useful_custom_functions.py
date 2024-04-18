from colorama import Fore, Style

class Message:
    def __init__(self, message, prefix=None, header_symbol = "-"):
        self.prefix = prefix
        self.message = message
        self.header_symbol = header_symbol
        self.header = ""
    
    def setHeader(self):
        prefix_length = len(self.prefix)+2 if self.prefix != None else 0
        self.header = f"{(len(self.message)+prefix_length)*self.header_symbol}"
        return self.header

    def setContent(self):
        content=self.message
        if self.prefix != None:
            content = f"{self.prefix}: {content}"
        return content

    def print(self):
        print(self.setHeader())
        print(self.setContent())
        print(self.setHeader())
        print(Style.RESET_ALL)

class InfoMessage(Message):
    def __init__(self, message, prefix="> INFO", header_symbol = "-"):
        super().__init__(message, prefix, header_symbol)
    def print(self):
        print(Fore.BLUE, end="")
        print(self.setHeader())
        print(self.setContent())
        print(self.setHeader())
        print(Style.RESET_ALL)

class ErrorMessage(Message):
    def __init__(self, message, prefix="! ERROR", header_symbol = "-"):
        super().__init__(message, prefix, header_symbol)
    def print(self):
        print(Fore.RED, end="")
        print(self.setHeader())
        print(self.setContent())
        print(self.setHeader())
        print(Style.RESET_ALL)