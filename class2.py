class Save(object):

    y = 3

    def __init__(self,y=1):
        print('Save=')

    def save(self):
        return 'save2'

    def x(self):
        return 'Save-x'


class Delete(object):

    x = 1
    y = 2

    def delete(self):
        return self.save()


    def x(self):
        return 'Delete-x'

    def __init__(self):
        print('delete=')


class Main(Save,Delete):

    def __init__(self,*args):
        super(Main,self).__init__(2)
        # super(Delete,self).__init__(2)
        super(Save,self).__init__()

    def test(self):
        print(super(Main,self).x())
        print(super(Save,self).x())

    def test2(self):
        return self.delete()



main = Main()
main.test()
# print(main.test2())
# print(main.__class__.mro().index())