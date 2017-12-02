import requests
import base64

class PostPHP:

    def __init__(self, id, name, exp, city, languages):
        self.id = id
        self.name = name
        self.exp = exp
        self.city = city
        self.languages = languages
        self.npy = "npy/face_" + str(id) + ".npy"
        self.img = "png/face_" + str(id) + ".png"

    def b64(self, filelocation):
        with open(filelocation, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string

    def post(self):
        url = "http://35.154.83.186/guideme/add_guide.php"
        r = requests.post(url, data={'id': self.id,
                                     'name': self.name,
                                     'exp': self.exp,
                                     'city':self.city,
                                     'languages':self.languages,
                                     'npy' : self.b64(self.npy),
                                     'png' : self.b64(self.img)})
        print (r.status_code)
        print (r.text)


if __name__ == '__main__':
    p = PostPHP(100, "Yash", "6", "Ahmedabad", "Hindi,English")
    p.post()


