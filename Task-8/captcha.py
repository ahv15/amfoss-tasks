from PIL import Image
import pytesseract
image= Image.open("test.png")
text=pytesseract.image_to_string(image, lang="eng")
no1=int(text[0])
no2=int(text[-1])
ans=no1+no2
print(ans)

