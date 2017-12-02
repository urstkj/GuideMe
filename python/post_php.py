import requests


class PostPHP:

    def __init__(self, id, name, exp, city, languages):
        self.id = id
        self.name = name
        self.exp = exp
        self.city = city
        self.languages = languages
        self.filename = "face_" + str(id) + ".npy"

    def post(self):
        url = "http://localhost/add_guide.php"
        r = requests.post(url, data={'id': self.id,
                                     'name': self.name,
                                     'exp': self.exp,
                                     'city':self.city,
                                     'languages':self.languages,
                                     'filename' : self.filename})
        print (r.status_code)
        print (r.text)


if __name__ == '__main__':
    p = PostPHP(100, "Yash", "6", "Ahmedabad", "Hindi,English")
    p.post()


