class Sotr:
    def __init__(self, first, second, pay=None):
        self.first = first
        self.second = second
        self.full = first + ' ' + second
        self.pay = pay
        self.email = first + '.' + second + '@company.com'
        self.company = 'Sosisosiza5$'

    def fullname_data(self):
        return '{} {} {} {}'.format(self.first, self.second, str(self.pay), self.company)
    def bool_company(self, company):
        """твоя ли это компания"""
        if self.company == company:
            return 'Yes'
        else:
            return 'No'



sotr_1 = Sotr('Corey', 'Jhon', 60)
sotr_2 = Sotr('Kate', 'Don', 1021)
sotr_3 = Sotr('Loli', 'Name', 4000)



class PC(Sotr):
    """Компьютеры сотрудников"""
    def __init__(self, CPU, GPU, password, first, second, pay):
        super().__init__(first, second, pay)
        self.CPU = CPU
        self.GPU = GPU
        self.password = password
pc_1 = PC('Intel Core i5 12100F', 'RX6600xt', 'lolimolly', 'Cory', 'Jhon', 60)

print(pc_1.first)

