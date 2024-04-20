import subprocess, msvcrt, time

# Geçici .bat dosyası oluşturur ve işlem sonunda siler. (Geçici batch dosyası içerisine yazılacak kodlar batchScript değişkenine atanmıştır)
def runBatchCode():
    # Batch kodlarını içeren dize
    batchScript = '''
    @echo off
    chcp 65001 > nul
    echo Yüklenecek uygulamalar (Google Chrome, VLC Media Player, Adobe Acrober Reader, Whatsapp, Winrar)
    timeout /t 2 > nul
    cls

    echo Google Chrome Yükleniyor
    winget install Google.Chrome
    timeout /t 3 > nul
    cls

    echo VLC Media Player Yükleniyor
    winget install VideoLAN.VLC
    timeout /t 3 > nul
    cls

    echo Adobe Acrober Reader Yükleniyor
    winget install XPDP273C0XHQH2
    timeout /t 3 > nul
    cls

    echo Whatsapp Yükleniyor
    winget install WhatsApp.WhatsApp
    timeout /t 3  > nul
    cls

    echo Winrar Yükleniyor
    winget install RARLab.WinRAR
    timeout /t 3 > nul
    cls

    echo Tüm uygulamalar başarıyla yüklendi.
    '''

    # Geçici bir bat dosyası oluşturur
    with open("basic_programs.bat", "w", encoding="utf-8") as file:
        file.write(batchScript)
    
    # Oluşturulan geçici dosyayı çalıştırır
    subprocess.run("basic_programs.bat", shell=True, encoding="utf-8")

    # Oluşturulan geçici dosyayı siler
    subprocess.run("del basic_programs.bat", shell=True, encoding="utf-8"
    )

# Yükleme işlemine başlamak için girilen tuş kontrolünü yapar
def keyControl():
    # Kullanıcıya bilgilendirme mesajları göster
    print("ÖNEMLİ!!!\nBu uygulamayı kullanmadan önce Windows işletim sistemi güncellemelerini yaptığınızdan emin olunuz!\nAksi halde yükleme işlemi yapılmayacaktır.")
    print("Devam etmek için Enter tuşuna, çıkmak için ESC tuşuna basın.")

    while True:
        key = msvcrt.getch()  # Kullanıcının bastığı tuşu alır

        if key == b'\x1b':  # ESC tuşuna basıldıysa (ESC'nin ASCII değeri: 27)
            print("Çıkış yapılıyor...")
            time.sleep(3)  # 3 saniye bekleyerek programdan çıkar
            break

        elif key == b'\r':  # Enter (Return) tuşuna basıldıysa (Enter'ın ASCII değeri: 13)
            print("Devam ediliyor...")
            runBatchCode()  # Yükleme fonksiyonunu çağırır.

            print("Çıkış yapılıyor...")
            time.sleep(3)  # 3 saniye bekleyerek programdan çıkar
            break
        else:
            print("Sadece Enter veya ESC tuşları kabul edilmektedir.")

keyControl()
