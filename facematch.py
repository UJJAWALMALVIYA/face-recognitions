import face_recognition

image_of_bill = face_recognition.load_image_file('./img/known/bill.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

unknown_image = face_recognition.load_image_file('./img/unknown/download.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]


results = face_recognition.compare_faces([bill_face_encoding],unknown_face_encoding)

if results[0]:
    print('This is bill gates')
else:
    print("This is not bill gates")