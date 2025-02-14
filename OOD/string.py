class TextEditor():
    def __init__(self, text):
        self.text = list(text)
        self.cursor = 0
    def move_forward(self, n):
        self.cursor = min(self.cursor + n, len(self.text)-1)
        print(f"Moved forward to position {self.cursor}")
    def move_backward(self, n):
        self.cursor = max(self.cursor - n, 0)
        print(f"Moved backward to position {self.cursor}")
    def replace(self, c):
        print(f"Replacing '{self.text[self.cursor]}' at position {self.cursor} with '{c}'")
        self.text[self.cursor] = c
    def get_text(self):
        return ''.join(self.text)
class Operation():
    def execute(self, editor: TextEditor):
        raise NotImplementedError("This method should be overridden in subclasses.")
class MoveForward(Operation):
    def __init__(self, n):
        self.n = n
    def execute(self, editor: TextEditor):
        editor.move_forward(self.n)
class MoveBackward(Operation):
    def __init__(self, n):
        self.n = n
    def execute(self, editor: TextEditor):
        editor.move_backward(self.n)
class Replace(Operation):
    def __init__(self, char):
        self.char = char
    def execute(self, editor: TextEditor):
        editor.replace(self.char)
def parse_operations(op_string):
    ops = []
    i = 0
    while i < len(op_string):
        op = op_string[i]
        i += 1
        # For 'F' (forward) and 'B' (backward), we expect a number following
        if op in ('F', 'B'):
            num_str = ""
            while i < len(op_string) and op_string[i].isdigit():
                num_str += op_string[i]
                i += 1
            n = int(num_str)
            if op == 'F':
                ops.append(MoveForward(n))
            else:
                ops.append(MoveBackward(n))
        # For 'R' (replace), we assume the next character is the replacement
        elif op == 'R':
            if i < len(op_string):
                replacement_char = op_string[i]
                i += 1
                ops.append(Replace(replacement_char))
            else:
                raise ValueError("Replace operation requires a character.")
        else:
            raise ValueError(f"Unknown operation: {op}")
    return ops

# Example usage:
if __name__ == "__main__":
    original_text = "abcdefghijklmn"
    editor = TextEditor(original_text)
    # Operation string: F2B1F5Rw (move forward 2, back 1, forward 5, replace with 'w')
    op_string = "F2B1F5Rw"
    operations = parse_operations(op_string)
    
    for op in operations:
        op.execute(editor)
    
    print("Final text:", editor.get_text())
