import qrcode
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os

def qr_olusturucu():#Tkinter 
    
    root = tk.Tk()
    root.withdraw()

    try:
        
        url = simpledialog.askstring("Giriş", "QR Kod yapılacak web sitesi linkini girin:", 
                                     initialvalue="https://")
        
        if not url:
            print("İşlem iptal edildi.")
            return

        kayit_yolu = filedialog.asksaveasfilename(
            title="QR Kodu Nereye Kaydedelim?",
            defaultextension=".png",
            filetypes=[("PNG Dosyası", "*.png")],
            initialfile="websitesi_qr_kod"
        )

        if kayit_yolu:
            
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(url)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            
            img.save(kayit_yolu)
            
            messagebox.showinfo("Başarılı", f"QR Kod oluşturuldu ve kaydedildi:\n{kayit_yolu}")
            print(f"Başarılı: {kayit_yolu}")
        else:
            print("Kaydetme işlemi iptal edildi.")

    except Exception as e:
        messagebox.showerror("Hata", f"Bir sorun oluştu: {e}")
        print(f"Hata detayı: {e}")

    
    input("\nProgram bitti. Kapatmak için Enter'a basın...") #admin olmayan oturumlarda otomatik kapanmayı onlemek için'gereksiz'

if __name__ == "__main__":
    qr_olusturucu()