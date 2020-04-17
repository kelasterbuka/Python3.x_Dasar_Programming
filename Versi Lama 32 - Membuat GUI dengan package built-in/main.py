import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="aku ditekan ^_^")
    label2.pack()


label = tkinter.Label(main_window, text="halo, saya adalah \n GUI sederhana dengan \n menggunakan python")
tombol = tkinter.Button(main_window, text="tekan akuh", command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()