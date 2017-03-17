class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        '''
        Inserting text in the document.
        '''
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor += 1

    def delete(self):
        '''
        Deletes text from the document.

        '''
        del self.characters[self.cursor.position]

    def save(self):
        '''
        Writes down text in the document and saves it.
        '''
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    def forward(self):
        '''
        Moves cursor forward.
        '''
        self.cursor += 1

    def back(self):
        '''
        Moves cursor back.
        '''
        self.cursor -= 1

    @property
    def string(self):
        return ''.join(self.characters)

class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        '''
        The position changes forward.
        '''
        self.position += 1

    def back(self):
        '''
        The position changes to back.
        '''
        self.position -= 1

    def home(self):
        '''
         Moves the cursor to the beginning.
        '''
        while self.document.characters[self.position-1] != '\n':
            self.position -= 1
            if self.position == 0:
                break
    def end(self):
        '''
        Moves the cursor to the end.
        '''
        while self.position < len(self.document.characters) and self.document.characters[self.position] != '\n':
            self.position += 1

class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        '''
        Returns to string
        '''
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character