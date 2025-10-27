class field:
    def __init__(self, height, width):
        self.height = height
        self.width = width



mainmap = field(16, 16)
print('☪' * (mainmap.width + 2))
for i in range(mainmap.height):
    print('☪' + '✡' * mainmap.width + '☪')
print('☪' * (mainmap.width + 2))
