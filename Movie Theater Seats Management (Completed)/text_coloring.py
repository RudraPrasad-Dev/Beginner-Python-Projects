# ANSI escape codes for text color

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
orange = '\033[38;2;255;165;0m'
pink = '\033[38;2;255;105;180m'
end = '\033[0m'  # Reset to default color

def color_text(text, color):
    return f'{color}{text}{end}'

# Example usage
if __name__ == '__main__':
    print(color_text('This is red text', red))
    print(color_text('This is green text', green))
    print(color_text('This is yellow text', yellow))
    print(color_text('This is blue text', blue))
