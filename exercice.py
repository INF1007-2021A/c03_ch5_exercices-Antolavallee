#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0: 
        number *= -1 
    return number 


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    full_name = []
    for characters in (prefixes):
        full_name.append(characters + suffixe)
        
    return full_name


def prime_integer_summation() -> int:
    total = 0 
    list_prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
    for number in range(0, len(list_prime)):    
        total = total + list_prime[number]
    return total


def factorial(number: int) -> int:
    facto = 1
    for i in range(1, number + 1):
       facto = facto * i 
    return facto 


def use_continue() -> None:
    variable = 11 
    while variable > 0:
        variable -= 1 
        if variable == 5: 
            continue
        print(variable)
        


def verify_ages(groups: List[List[int]]) -> List[bool]:
    boolean_list = []
    index_integer = 0
    for index_list in groups: 
        if len(index_list) > 10 or len(index_list) <= 3: 
            boolean_list.append(False)
            continue
        if len(boolean_list) == index_integer:
            for age_groups in index_list: 
                if age_groups == 25: 
                    boolean_list.append(True)
                    break
        if len(boolean_list) == index_integer:
            for age_groups in index_list: 
                if age_groups < 18: 
                    boolean_list.append(False)
                    break
        if len(boolean_list) == index_integer:
            for age_groups in index_list:
                if age_groups > 70 or age_groups == 50:
                    boolean_list.append(False)
                    break
        else: 
            boolean_list.append(True)
        index_integer += 1 
    return boolean_list


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
