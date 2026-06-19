def say_hello():                        #начальное приветствие
    print("What is your name?")
    name = input()
    print(f"Hello, {name}, what is next?")

def create_shopping_list():                 #создание списка покупок
    n = 0       #счётчик заполняемолсти списка
    count = 0   #количество покупок в списке
    shop_list = []
    flag = False
    while not flag:     #ввод количества покупок
        print("Enter the number of purchases: ")
        try:
            count = int(input())
            if count > 0:        #если количество целое и неотрицательное
                flag = True
            else:        #если введено 0 или меньше
                print(f"Number should be positive!")
        except ValueError:
            print(f"Wrong enter, try again")

    while n != count:
        print(f"Enter price of your {n+1} purchase: ")
        try:
            item = float(input())
            if item > 0:        #если ценник не отрицательный
                shop_list.append(item)
                n += 1
            else:
                print("Price should be positive!")
        except ValueError:
            print(f"Wrong enter, try again")
    print("Done!")
    return shop_list

def create_settings():          #начальные параметры скидок
    settings_dict = {"price_limit": 0, "min_price": 0, "percent": 0}
    flags = [False,False,False]        #флаги корректного заполнения каждого значения
    while not flags[0]:
        print("Enter maximum purchase price limit:")
        try:
            settings_dict["price_limit"] = int(input())
            if settings_dict["price_limit"] < 0:
                print("Wrong input!")
            else:
                flags[0] = True     #limit больше нуля, первый флаг выполнен
        except ValueError:
            print("Wrong input")

    while not flags[1]:
        print("Enter the minimum price to receive a discount:")
        try:
            settings_dict["min_price"] = int(input())
            if settings_dict["min_price"] < 0:
                print("Wrong input, price should be positive!")
            else:
                flags[1] = True     #минимальный ценник положительный -> второй флаг выполнен
        except ValueError:
            print("Wrong input")

    while not flags[2]:
        print("What percentage is the discount?:")
        try:
            settings_dict["percent"] = int(input())
            if settings_dict["percent"] < 0 or settings_dict["percent"] > 100:
                print("Wrong input, percentage should be from 0 to 100")
            else:
                flags[2] = True     #корректный процентаж -> выполненный третий флаг
        except ValueError:
            print("Wrong input!")

    print("Done!")
    return settings_dict

def make_stat(settings_dict, shopping_list):   #финальные подсчёты
    stat_dict = {"total_price": sum(shopping_list), "final_price": 0,      #общая стоимость до скидок, стоимость после скидок
                 "discount_items": 0, "final_benefit": 0,                  #товаров со скидкой, общая скидка
                 "all_items": len(shopping_list), "above_limit": 0,        #всего покупок, выше заданного лимита
                 "average_check": 0, "max_check": max(shopping_list),      #средний чек, максимальный чек без скидок
                 "items": shopping_list}                                   #список всех покупок
    for i in range(len(shopping_list)):

        if shopping_list[i] > settings_dict["min_price"]:        #если ценник выше скидочного порога
            stat_dict["discount_items"] += 1                     #+1 к товарам попавшим под скидку
            stat_dict["final_benefit"] += (shopping_list[i] / 100) * settings_dict["percent"]   #+ общей скидке

        if shopping_list[i] > settings_dict["price_limit"]:
            stat_dict["above_limit"] += 1  # +1 в список покупок выше лимита (без учёта скидок)

    stat_dict["final_price"] = stat_dict["total_price"] - stat_dict["final_benefit"]   # общая стоимость после скидок
    stat_dict["average_check"] = stat_dict["total_price"] / len(shopping_list)          #средний чек
    return stat_dict

def show_stat(stat_dict, settings_dict):
    print(f'Number of purchases: {stat_dict["all_items"]}')
    print(f"Prices: {(stat_dict["items"])}")
    print(f'Most expensive purchase: {stat_dict["max_check"]}')
    print(f'Average check: {stat_dict["average_check"]}')
    print(f'Price limit: {settings_dict["price_limit"]}')
    print(f"Purchases above the limit: {stat_dict["above_limit"]}")
    print(f"Total price: {stat_dict["total_price"]}")
    print(f"Purchases at a discount: {stat_dict["discount_items"]}")
    print(f"Minimal price to get the discount: {settings_dict["min_price"]}")
    print(f"Benefit: {stat_dict["final_benefit"]}")
    print(f"Final price: {stat_dict["final_price"]}")

def choice(live_stat, live_shopping_list, live_settings, is_working):       #выбор в основном меню
    print("1.Create purchases list")
    print("2.Change settings")
    print("3.Show statistic")
    print("0.Exit")
    try:
        n = int(input())
        if n == 1:
            live_shopping_list = create_shopping_list()
        elif n == 2:
            live_settings = create_settings()
        elif n == 3:
            if live_settings == {} or live_shopping_list == []:
                print("Nothing to be done!")
            else:
                live_stat = make_stat(live_settings,live_shopping_list)
                show_stat(live_stat,live_settings)

        elif n == 0:
            is_working = False
        else:
            print("Wrong enter!")

    except ValueError:
        print("Wrong enter")

    return live_stat, live_shopping_list, live_settings, is_working


def main():
    live_stat = {}
    live_shopping_list = []
    live_settings = {}
    is_working = True
    say_hello()
    while is_working:
        live_stat, live_shopping_list, live_settings, is_working = choice(
            live_stat, live_shopping_list, live_settings, is_working
        )


if __name__ == "__main__":      #точка входа
    main()
