import tkinter as tk
from tkinter import messagebox,scrolledtext
import random
import string

def generate_password(lenght, include_letters, include_digits, include_punctuation):
    characters=""
    if include_letters:
         characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation

    if not characters:
        return ""
    
    password = ''.join(random.choice(characters) for _ in range(lenght))
    return password

def generate_password_from_input(input_text, length):
    if not input_text:
        return ""
    password = ''.join(random.choice(input_text) for _ in range(length))
    return password

def generate_and_display_password():
    
    input_text = entry_input.get()
    if not input_text:
        messagebox.showerror("خطا", "لطفاً یک عدد مثبت وارد کنید.")
        return
    include_letters=var_letters.get()
    include_digits=var_digits.get()
    include_punctuation = var_punctuation.get()

    if not include_letters and not include_digits and not include_punctuation:
        messagebox.showerror("خطا", "لطفاً حداقل یک نوع کاراکتر را انتخاب کنید.")
        return
        
    length = 10

    password=generate_password_from_input(input_text,length)
    output_password_text.delete(1.0,tk.END)
    output_password_text.insert(tk.END,password)




root = tk.Tk()
root.title("تولید رمز عبور تصادفی")
root.geometry("400x200")

label_instruction = tk.Label(root, text="لطفاً طول پسورد را وارد کنید:")
label_instruction.pack(pady=10)

entry_input = tk.Entry(root, width=10, font=('Arial', 14))
entry_input.pack()

frame_options=tk.Frame(root)
frame_options.pack(pady=10)

var_letters=tk.BooleanVar(value=True)
chk_letters=tk.Checkbutton(frame_options,text='حروف (بزرگ و کوچک)',variable=var_letters)
chk_letters.grid(row=0,column=0,padx=5)

var_digits = tk.BooleanVar(value=True)
chk_digits=tk.Checkbutton(frame_options,text="اعداد", variable=var_digits)
chk_digits.grid(row=0,column=2,padx=5)

var_punctuation = tk.BooleanVar(value=True)
chk_punctuation = tk.Checkbutton(frame_options, text="نمادها", variable=var_punctuation)
chk_punctuation.grid(row=0, column=3, padx=5)


# دکمه برای تولید پسورد
btn_generate = tk.Button(root, text="تولید پسورد", command=generate_and_display_password)
btn_generate.pack(pady=10)


# جایگاه برای نمایش پسورد
output_password_label = tk.Label(root, text="رمز عبور تولید شده:", font=('Arial', 12))
output_password_label.pack()

output_password_text = scrolledtext.ScrolledText(root, width=40, height=3, font=('Arial', 12), wrap=tk.WORD)
output_password_text.pack(pady=5, padx=10)

# اجرای برنامه
root.mainloop()