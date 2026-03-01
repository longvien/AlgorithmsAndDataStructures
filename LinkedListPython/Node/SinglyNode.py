from typing import override
class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    @override
    def __str__(self) -> str:
        return self.value
