class Operation:

    def __init__(self, id_operation, date, state, amount, code, description, to, from_=None):
        self.id_operation = id_operation
        self.date = date
        self.state = state
        self.amount = amount
        self.code = code
        self.description = description
        self.to = to
        self.from_ = from_

    def get_date(self) -> None:
        """Преобразовать дату в нужный вид"""
        date = self.date[8:10] + self.date[4:8] + self.date[:4]
        self.date = date.replace('-', '.')

    def encode_to(self) -> None:
        """Кодировка получателя"""
        if self.to.startswith('Счет'):
            self.to = 'Счет **' + self.to[-4:]
        else:
            self.to = self.to[:-12] + ' ' + self.to[-12:-10] + '**' + ' **** ' + self.to[-4:]

    def encode_from(self) -> None:
        """Кодировка отправителя"""
        if self.from_ is not None:
            if self.from_.startswith('Счет'):
                self.from_ = 'Счет **' + self.from_[-4:]
            else:
                self.from_ = self.from_[:-12] + ' ' + self.from_[-12:-10] + '**' + ' **** ' + self.from_[-4:]

    def beautiful_output(self) -> str:
        """Вывод в требуемом виде"""
        return f"""
                {self.date}   {self.description}
                {self.to}  ->  {self.from_ if self.from_ else ''}
                {self.amount}  {self.code}
                """

    def __str__(self):
        """Красивый вывод"""
        return f'{self.id_operation}    {self.date}    {self.state}   ' \
               f'{self.amount}    {self.code}    {self.description}   ' \
               f'{self.to}    {self.from_}'
