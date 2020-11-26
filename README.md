# Shortcut text segment
This is the iOS shortcut tool 

## Short cut in iOS


## Backend server (this repo)

### Authorization
User ID + Secret

Generation of an access token:

The diff between local and server timestamp should remain in 60 seconds.

PassCode = SHA256("{UserID}.{Secret}.{Timestamp}")
Token = "{UserID.PassCode}"




### Change handling model
Default model: HanLP

All language model should be wrapped into a class with following functions.

```python
class LangModel:
    def __init__(self):
        pass
    def first_run(self):
        """handles first run operations.
            model file (if needed) should be downloaded here.
        """
    def segment(self, text: str) -> List[str]:
        """segment given text.
            text: the text content to be split.

            return: list of str.
        """
```
