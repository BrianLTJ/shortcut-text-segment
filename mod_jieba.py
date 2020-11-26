from typing import List
import jieba

class JiebaModel:
    def __init__(self):
        pass
        
    def first_run(self):
        """handles first run operations.
            model file (if needed) should be downloaded here.
        """
        pass
    def segment(self, text: str) -> List[str]:
        """segment given text.
            text: the text content to be split.

            return: list of str.
        """
        ret = jieba.cut(text)
        return list(ret)
