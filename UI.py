# Include PyQt5 tool kit
# Include sumy Automatic text summarizer

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk


# Install nlktk punkt
# nltk.download('punkt')

# Using a class for UI and summarizer
class Summarizer(QWidget):

    # Declaring
    def __init__(self):
        super().__init__()

        self.layout = None
        self.label = None
        self.input_text = None
        self.summarize_button = None
        self.output_text = None

        self.init_ui()

    # initializing UI
    def init_ui(self):

        # Main window
        self.setGeometry(800, 800, 800, 800)
        self.setWindowTitle('Text Summarizer')
        self.layout = QVBoxLayout()

        # Input text box
        self.input_text = QPlainTextEdit()
        self.input_text.insertPlainText("Enter your text here...")
        self.input_text.resize(50, 50)
        self.layout.addWidget(self.input_text)

        # Push Button
        self.summarize_button = QPushButton("Summarize")
        self.layout.addWidget(self.summarize_button)

        # Text Output
        self.output_text = QPlainTextEdit()
        self.output_text.insertPlainText("Summarized text...")
        self.output_text.setReadOnly(True)
        self.output_text.resize(50, 50)
        self.layout.addWidget(self.output_text)

        self.setLayout(self.layout)

        self.summarize_button.clicked.connect(self.summarize)

    # Show UI
    def run(self):
        self.show()

    # Summarizer
    def summarize(self):
        txt = self.input_text.toPlainText()
        print(txt)

        parser = None

        # Testing summarizer and checking for errors
        try:
            parser = PlaintextParser.from_string(txt, Tokenizer("english"))
            print("summarizing")
            summarizer = LexRankSummarizer()
            print("summarizing")
            summary = summarizer(parser.document, 4)
            self.output_text.clear()
            for sentence in summary:
                print(sentence)
                self.output_text.insertPlainText(str(sentence))
        except Exception as err:
            print("ERROR: " + str(err))
        finally:
            print("finally")
