stackSize = [10,10,10]
buffer = [None]*sum(stackSize)
stackPointer = [-1,-1,-1]  # указатели для отслеживания верхних элементов

def push(stackNum, value):
    global stackPointer
    global buffer
    global stackSize
    #Проверяем, есть ли пространство
    if (stackPointer[stackNum] >= stackSize[stackNum]):
        print("Недостаточно пространства.")
        return
    
    # Находим индекс верхнего элемента массива + 1, и увеличиваем указатель стека
    index = stackNum * stackSize[stackNum] + stackPointer[stackNum] + 1
    stackPointer[stackNum] += 1
    buffer[index] = value

def pop(stackNum):
    global stackSize
    global stackPointer
    if (stackPointer[stackNum] == -1):
        print("Попытка использовать пустой стек")
        return
    index = stackNum * stackSize[stackNum] + stackPointer[stackNum]
    stackPointer[stackNum] -= 1
    value = buffer[index]
    buffer[index] = None
    return value

def peek(stackNum):
    global stackSize
    index = stackNum * stackSize[stackNum] + stackPointer[stackNum]
    return buffer[index]

def isEmpty(stackNum):
    global stackPointer
    return stackPointer[stackNum] == 0
