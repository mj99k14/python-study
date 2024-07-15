import sys
import os

module_path =os.getcwd()+'\qqwwee'
if module_path not in sys.path:
    sys.path.append(module_path)

import external_module

def main():
    greeting = external_module.greet("python user")
    print(greeting)

if __name__ == '__main__':
    main()
