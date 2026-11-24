from src.connect_class import AeroplanesAPI
from src.plane_class import Aeroplane
from src.saver_class import JSONSaver

# Получение информации о самолетах с opensky-network.org


# Пример работы контструктора класса с одним самолетом
aeroplane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)

# Сохранение информации в файл
json_saver = JSONSaver()
json_saver.add_aeroplane(aeroplane)
json_saver.delete_aeroplane(aeroplane)


def filter_aeroplanes(aeroplanes, filter_words):
    filtered_planes = []
    for plane in aeroplanes:
        if plane.origin_country in filter_words:
            filtered_planes.append(plane)
    return filtered_planes


def quick_sort(aeroplanes, lo, hi):
    if lo >= hi:
        return aeroplanes
    op = hi
    i = lo
    for j in range(lo, hi):
        if aeroplanes[j].baro_altitude is None:
            continue
        if (
            aeroplanes[op].baro_altitude is None
            or aeroplanes[j].baro_altitude > aeroplanes[op].baro_altitude
        ):
            aeroplanes[j], aeroplanes[i] = aeroplanes[i], aeroplanes[j]
            i += 1
    aeroplanes[i], aeroplanes[hi] = aeroplanes[hi], aeroplanes[i]
    quick_sort(aeroplanes, lo, i - 1)
    quick_sort(aeroplanes, i + 1, hi)
    return aeroplanes


def sort_aeroplanes(aeroplanes):
    return quick_sort(aeroplanes, 0, len(aeroplanes) - 1)


def get_aeroplanes_by_altitude(aeroplanes, altitude):
    altitude_range = list(map(float, str(altitude).split(" - ")))
    filtered_aeroplanes = []
    for aeroplane in aeroplanes:
        if altitude_range[0] <= aeroplane.velocity <= altitude_range[1]:
            filtered_aeroplanes.append(aeroplane)
    return filtered_aeroplanes


def get_top_aeroplanes(sorted_aeroplanes, top_n):
    if top_n == 0:
        raise ValueError("Количество не может быть меньше единицы")
    return sorted_aeroplanes[:top_n]


def print_aeroplanes(aeroplanes):
    for aeroplane in aeroplanes:
        print(aeroplane)


# Функция для взаимодействия с пользователем
def user_interaction():
    country = input("Введите название страны: ")
    top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    filter_words = input(
        "Введите названия стран для фильтрации по стране регистрации: "
    ).split()
    altitude_range = input("Введите диапазон высот полета: ")  # Пример: 100000 - 150000
    api = AeroplanesAPI(country)
    aeroplanes = api.get_aeroplanes()
    aeroplanes_list = Aeroplane.cast_to_object_list(aeroplanes)
    filtered_aeroplanes = filter_aeroplanes(aeroplanes_list, filter_words)

    ranged_aeroplanes = get_aeroplanes_by_altitude(filtered_aeroplanes, altitude_range)

    sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
    top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
    print_aeroplanes(top_aeroplanes)

if __file__ == "__main__":
    user_interaction()
