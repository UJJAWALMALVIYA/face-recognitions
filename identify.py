import face_recognition
from PIL import Image,ImageDraw

image_of_bill = face_recognition.load_image_file('./img/known/bill.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

image_of_Elonmusk = face_recognition.load_image_file('./img/known/Elonmusk.jpg')
Elonmusk_face_encoding = face_recognition.face_encodings(image_of_Elonmusk)[0]

image_of_Steve = face_recognition.load_image_file('./img/known/Steve.jpg')
Steve_face_encoding = face_recognition.face_encodings(image_of_Steve)[0]



known_face_encoding =[
    bill_face_encoding,
    Elonmusk_face_encoding,
    Steve_face_encoding
]
    
    

known_face_names =[
    "Bill Gates",
    "Elon Musk",
    "Steve jobs"
    
]


test_image = face_recognition.load_image_file('./img/groups/bill_steve.jpg')

face_locations= face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image= Image.fromarray(test_image)

draw= ImageDraw.Draw(pil_image)

for(top,right,bottom,left),face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encoding, face_encoding)

    name ="unknown person"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    

    #draw box
    draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))
    
    text_width,text_height =draw.textsize(name)
    draw.rectangle(((left,bottom - text_height - 10),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
    draw.text((left +6, bottom - text_height -5),name , fill=(255,255,255,255))


del draw


pil_image.show()

pil_image.save('identify.jpg')
