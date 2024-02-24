import sys

if len(sys.argv) < 2:
    sys.exit("Too few argument")
elif len(sys.argv) > 2:
    sys.exit("Too many argument")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)