import os
import subprocess
import random

if __name__ == '__main__':
    def createFiles(n, p, g):
        for i in range(n):
            with open(f"person{i}.py", 'w') as f:
                for j in range(0, n):
                    if j != i:
                        f.write(f"import person{j}\n")
        with open("Public.py", "w")as f:
            f.write(
                f"prime={p}\ngroup={g}")
        return

    def writeData(n, p, g):
        for i in range(n):
            if i != n-1:
                with open(f"person{i}.py", "a") as f:
                    k = random.randint(1, p)
                    f.write(
                        f"import subprocess\nimport threading\nimport Public\nclass Self:\n\tdef __init__(self):\n\t\tself.e={k}\ns=Self()\nlock=threading.Lock()\nwith open('Public.py','a') as f:\n\tf.write('ge{i}={g**k}')\nlock.acquire()\ntry:\n\tprint(subprocess.check_output(['python', f'person{(i+1)%n}']))\nfinally:\n\tlock.release()\npg=Public.g{(i-1)%n}\npn=Public.g{(i+1)%n}\nr=((pg/pn)**s.e)%{p}\nwith open('Public.py','a') as f:\n\tf.write('r{i}=r')\nkey=pg**({n}*s.e)\nfor i in range(0,{n}):\n\tkey*=Public.r{(i-1)%n}\nprint(key)")
                    print(2)
            else:
                with open(f"person{i}.py", "a") as f:
                    k = random.randint(1, p)
                    f.write(
                        f"import subprocess\nimport threading\nimport Public\nclass Self:\n\tdef __init__(self):\n\t\tself.e={k}\ns=Self()\nlock=threading.Lock()\nwith open('Public.py','a') as f:\n\tf.write('ge{i}={g**k}')\npg=Public.g{(i-1)%n}\npn=Public.g{(i+1)%n}\nr=((pg/pn)**s.e)%{p}\nwith open('Public.py','a') as f:\n\tf.write('r{i}=r')\nkey=pg**({n}*s.e)\nfor i in range(0,{n}):\n\tkey*=Public.r{(i-1)%n}\nprint(key)")
    n = int(input("Enter number of users"))
    p = int(input("Enter the prime number"))
    g = int(input("Enter the primitive root of prime"))
    createFiles(n, p, g)
    writeData(n, p, g)
    for i in range(n):
        print(subprocess.check_output(["python", f"person{i}"]))
