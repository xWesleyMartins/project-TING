from typing import List
from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue: List = []

    def __len__(self) -> int:
        return len(self.queue)

    def enqueue(self, value: any) -> None:
        self.queue.append(value)

    def dequeue(self) -> any:
        return self.queue.pop(0)

    def search(self, index: int) -> any:
        if not (0 <= index < len(self.queue)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
