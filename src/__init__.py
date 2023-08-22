import sys

if 'src' not in sys.path:
    import os
    src_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(src_path)