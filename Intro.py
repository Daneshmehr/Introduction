#!/usr/bin/python

class Daneshmehr:

    def __init__(self):
        self.name = "Daneshmehr"
        self.researcher = True
        self.developer = True
        self.languages = ["en_US", "es_MX"]

    def say_Hello(self):
        print("I'm glad you read my intro! Please also visit my Scholar Google at https://scholar.google.com/citations?user=6kT3gHsAAAAJ&hl=en")


me = Daneshmehr()
me.say_Hello()
