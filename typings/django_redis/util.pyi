"""
This type stub file was generated by pyright.
"""

class CacheKey(str):
    """
    A stub string class that we can use to check if a key was created already.
    """
    def original_key(self) -> str:
        ...
    


def default_reverse_key(key: str) -> str:
    ...

