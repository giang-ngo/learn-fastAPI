class Enemy:

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight!')

    def walf_forward(self):
        print(f'{self.__type_of_enemy} di chuyển gần tới bạn.')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')

    def special_attack(self):
        print('Kẻ địch không có đòn tấn công đặc biệt')
