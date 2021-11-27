import base64 
print("""
---------------------------------------------------------
web site : https://farukdeveloper.online
github : github.com/hawk-unity/
youtube : HAWK DEFACER 
instagram : faruk.developer 
---------------------------------------------------------

1 - Şifrele =0

2 - Çöz =0
""")

hello = input("Seçenek seç -> ")
if hello == "1" : 
    message = input("Şifrelencek Metin => ")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(f"şifre -> {base64_message}")
if hello == "2" : 
    base64_string = input("Çözülecek ifade => ")
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    print(f"Çözülmüş ifade -> : {sample_string}")
