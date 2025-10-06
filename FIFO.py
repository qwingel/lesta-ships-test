# == Реализация циклического буфера FIFO  ==

# == Первая реализация ==
# == Циклический буфер на основе списка ==
#

class CircularBufferList:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive") # Возвращаем ValueError
        self.capacity = capacity        # Вместимость буфера
        self.buffer = [None] * capacity # Список заполняется None
        self.head = 0                   # Указатель на начало
        self.tail = 0                   # Указатель на конец
        self.size = 0                   # Количество элементов
        self.is_full = False            # Заполнен ли буфер
    
    # @func enqueue(self, item: any)
    # Метод добавляет элемент в бфуер
    # @param item - элемент, который добавляем в буфер
    # @return None
    def enqueue(self, item) -> None:
        if self.is_full:
            self.head = (self.head + 1) % self.capacity
        
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        
        if self.tail == self.head:
            self.is_full = True
        else:
            self.size = min(self.size + 1, self.capacity)
    
    # @func dequeue(self)
    # Метод удаляет элемент из буфера
    # @return None, если буфер пустой, иначе удаленный элемент
    def dequeue(self):
        if self.is_empty():
            return None
        
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        self.is_full = False
        
        return item
    
    # @func first(self)
    # Метод вовзращает первый элемент буфера
    # @return None, если буфер пустой, иначе первый элемент буфера
    def first(self):
        if self.is_empty():
            return None
        return self.buffer[self.head]
    
    # @func is_empty(self)
    # Метод проверяет пустой ли буфер
    # @return True, если буфер пустой, иначе False
    def is_empty(self) -> bool:
        return self.size == 0
    
    # @func is_full(self)
    # Метод проверяет полный ли буфер
    # @return True, если буфер полный, иначе False
    def is_full(self) -> bool:
        return self.is_full
    
    # @func get_size(self)
    # Стандартный геттер размера буфера
    # @return Размер буфера
    def get_size(self) -> int:
        return self.size
    
    # @func clear(self)
    # Метод очищает буфер
    # @return None
    def clear(self) -> None:
        self.buffer = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.is_full = False
    
    # @func __str__(self)
    # Стандартный tostring метод, представляющий наш класс в виде строки
    # @return Строку - представление нашего класса
    def __str__(self):
        items = []
        current = self.head
        for _ in range(self.size):
            items.append(str(self.buffer[current]))
            current = (current + 1) % self.capacity
        return f"CircularBuffer([{', '.join(items)}])"
    

# == Вторая реализация ==
# == Циклический буфер на основе deque ==
#
# == Все методы аналогичны и выполняют тот 
#    же функционал, что и в первой реализации ==
#

from collections import deque

class CircularBufferDeque:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity) # наш buffer - deque с maxlen = capacity
    
    def enqueue(self, item) -> None:
        self.buffer.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.buffer.popleft()
    
    def first(self):
        if self.is_empty():
            return None
        return self.buffer[0]
    
    def is_empty(self) -> bool:
        return len(self.buffer) == 0
    
    def is_full(self) -> bool:
        return len(self.buffer) == self.capacity
    
    def get_size(self) -> int:
        return len(self.buffer)
    
    def clear(self):
        self.buffer.clear()
    
    def __str__(self):
        return f"CircularBuffer({list(self.buffer)})"