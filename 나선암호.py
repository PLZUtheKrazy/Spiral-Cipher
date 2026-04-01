import tkinter as tk
from tkinter import messagebox

# --- 소수 생성 ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(count):
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# --- 암호화 함수 ---
def spiral_prime_encrypt(text):
    primes = generate_primes(len(text))
    result = ""

    for i, ch in enumerate(text):
        if ch.isalpha():
            shift = primes[i] % 26

            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')

            new_char = chr((ord(ch) - base + shift) % 26 + base)
            result += new_char
        else:
            result += ch

    return result

# --- UI 기능 ---
def encrypt_text():
    input_text = entry.get("1.0", tk.END).strip()
    
    if not input_text:
        messagebox.showwarning("경고", "문장을 입력하세요!")
        return
    
    encrypted = spiral_prime_encrypt(input_text)
    
    output.delete("1.0", tk.END)
    output.insert(tk.END, encrypted)

# --- UI 구성 ---
root = tk.Tk()
root.title("나선 소수 암호 인코더")
root.geometry("500x400")

# 입력 라벨
tk.Label(root, text="암호화할 문장 입력").pack()

# 입력창
entry = tk.Text(root, height=5)
entry.pack(padx=10, pady=5)

# 버튼
tk.Button(root, text="암호화", command=encrypt_text).pack(pady=10)

# 출력 라벨
tk.Label(root, text="암호 결과").pack()

# 출력창
output = tk.Text(root, height=5)
output.pack(padx=10, pady=5)

# 실행
root.mainloop()