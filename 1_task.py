def find_correct_cipher(encrypted_message, cipher_methods):
    """
    Определяет правильный способ шифрования для врат Мории
    
    Args:
        encrypted_message (str): Зашифрованное сообщение над воротами
        cipher_methods (list): Список кортежей (название, m, n, t)
    
    Returns:
        str: Название правильного способа шифрования или None
    """
    
    for method_name, m, n, t in cipher_methods:
        if m < 1 or n > len(encrypted_message) or m > n:
            continue
            
        substring = encrypted_message[m-1:n]
        
        if t in substring:
            return method_name
    
    return None

def solve_moria_gates():
    encrypted_message = "SPEAKFRIENDANDENTER"
    
    cipher_methods = [
        ("Шифр гномов", 1, 5, "SPEAK"),
        ("Шифр эльфов", 6, 12, "FRIEND"), 
        ("Шифр орков", 10, 15, "ENEMY"),
        ("Шифр людей", 13, 18, "ENTER")
    ]
    
    result = find_correct_cipher(encrypted_message, cipher_methods)
    
    if result:
        print(f"Врата откроются! Использован: {result}")
        print("Слово-ключ найдено!")
    else:
        print("Ни один из известных способов не подходит...")
        print("Гендальфу придется искать другие варианты")
    
    return result

def check_all_methods(encrypted_message, cipher_methods):
    """Проверяет все методы и показывает детали"""
    print(f"Анализируем сообщение: '{encrypted_message}'")
    print("-" * 50)
    
    suitable_methods = []
    
    for method_name, m, n, t in cipher_methods:
        if m < 1 or n > len(encrypted_message) or m > n:
            print(f"{method_name}: Некорректные границы ({m}, {n})")
            continue
            
        substring = encrypted_message[m-1:n]
        contains_t = t in substring
        
        print(f"{method_name}:")
        print(f"  Позиции {m}-{n}: '{substring}'")
        print(f"  Ищем: '{t}' -> {'✓ НАЙДЕНО' if contains_t else '✗ не найдено'}")
        
        if contains_t:
            suitable_methods.append(method_name)
        print()
    
    return suitable_methods

solve_moria_gates()