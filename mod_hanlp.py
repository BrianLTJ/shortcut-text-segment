from typing import List
import hanlp

class HanlpModel:
    def __init__(self):
        self.tokenizer = hanlp.load('LARGE_ALBERT_BASE')
        self.pipeline = hanlp.pipeline() \
            .append(hanlp.utils.rules.split_sentence, output_key="sentences") \
            .append(self.tokenizer, output_key="tokens")
        
    def first_run(self):
        """handles first run operations.
            model file (if needed) should be downloaded here.
        """
    def segment(self, text: str) -> List[str]:
        """segment given text.
            text: the text content to be split.

            return: list of str.
        """
        ret = []
        return ret
