class Article:

    def __init__(self, name, author, title, descrip, link, img, date):
        self.__newspaper = name
        self.__author = author
        self.__title = title
        self.__description = descrip
        self.__link = link
        self.__urlImage = img
        self.__published = date

    def set_newspaper(self, val):
        if type(val) == str:
            self.__newspaper = val
        else:
            print('AttributeError')

    def set_author(self, val):
        if type(val) == str:
            self.__author = val
        else:
            print('AttributeError')

    def set_title(self, val):
        if type(val) == str:
            self.__title = val
        else:
            print('AttributeError')

    def set_description(self, val):
        if type(val) == str:
            self.__description = val
        else:
            print('AttributeError')

    def set_link(self, val):
        if type(val) == str:
            self.__link = val
        else:
            print('AttributeError')

    def set_urlImage(self, val):
        if type(val) == str:
            self.__urlImage = val
        else:
            print('AttributeError')

    def set_published(self, val):
        if type(val) == str:
            self.__published = val
        else:
            print('AttributeError')

    def get_newspaper(self):
        return self.__newspaper

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_description(self):
        return self.__description

    def get_link(self):
        return self.__link

    def get_urlImage(self):
        return self.__urlImage

    def get_published(self):
        return self.__published


    def __str__(self):
        return 'Bienvenu sur {}\n' \
               'Voici les nouvelles du jour: \n' \
               'Auteur: {}\n' \
               'Publié le {}\n' \
               'Sujet: {}\n' \
               'Résumé: {} \n'\
               'image: {}\n'\
               'lien: {}'.format(self.__newspaper, self.__author, self.__published[0:10], self.__title, self.__description, self.__urlImage, self.__link)