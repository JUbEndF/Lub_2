from tqdm import tqdm

def sort_puzirek(arrays: list) -> list:
    for i in tqdm(range(len(arrays)), desc="Запись результата валидации в файл", ncols=100):
        for j in range(len(arrays) - i - 1):
            if arrays[j].get("passport_series") > arrays[j + 1].get("passport_series"):
                arrays[j], arrays[j + 1] = arrays[j + 1], arrays[j]
    return arrays