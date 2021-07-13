import xml.etree.ElementTree as ET
import sys, requests, os

print("\n\t-- Bilgi:   Erisime Acik AWS S3 Bucketlerindeki Dosyalari/Dizinleri Listeler --")
try:
    aws_url = sys.argv[1]
    r = requests.get("https://s3.amazonaws.com/"+str(aws_url)+"/")
    if(r.status_code == 200  and r.headers["Content-Type"]=='application/xml'):
        root = ET.fromstring(r.content)
        for i in range(len(root)):
            for attr in range(len(root[i])):
                if("key" in str(root[i][attr]).lower()):
                    content = str(root[i][attr].text)
                    if(str(content).endswith("/")):
                        print("\n [*] Yol: ",content)
                    else:
                        if("/" in content):
                            print("          ",content)  
                        else:
                            print("\n [*] Yol: ",content)

    else:
        print(" [X] Muhtemelen Forbidden: %s %s " % (str(r.status_code),str(r.reason)))
except Exception as e:
    print(" [X] Hata VAR: %s " % str(e))
