def find_max_steel_blocks(A, B, C):
    """
    Находит максимальное количество блоков стали для меча в Майнкрафт
    
    Формула цены: Цена = A + B * N
    Ограничение: Цена <= C
    
    Args:
        A (int): Стоимость дерева для рукояти (изумруды)
        B (int): Стоимость одного блока стали (изумруды)  
        C (int): Максимальная цена, которую готовы заплатить жители (изумруды)
        
    Returns:
        int: Максимальное количество блоков стали или -1 если невозможно
    """
    
    if B <= 0:
        return float('inf') if A <= C else -1
    
    if A > C:
        return -1
    
    
    max_blocks = (C - A) // B 
    
    return max_blocks

def calculate_sword_price(A, B, N):
    """Вычисляет цену меча с N блоками стали"""
    return A + B * N

def optimize_sword_crafting(A, B, C, show_details=True):
    """
    Полный анализ оптимизации крафта мечей
    
    Returns:
        dict: Результаты анализа
    """
    
    max_blocks = find_max_steel_blocks(A, B, C)
    
    if show_details:
        print("⚔️  ОПТИМИЗАЦИЯ КРАФТА МЕЧЕЙ В МАЙНКРАФТ ⚔️")
        print("=" * 55)
        print(f"💰 Стоимость рукояти (A): {A} изумрудов")
        print(f"🔩 Стоимость блока стали (B): {B} изумрудов")
        print(f"💎 Максимальный бюджет жителей (C): {C} изумрудов")
        print()
        
        if max_blocks == -1:
            print("❌ РЕЗУЛЬТАТ: Жители не могут купить даже базовый меч!")
            print(f"   Базовая цена: {A} изумрудов > Бюджет: {C} изумрудов")
            return {'max_blocks': -1, 'max_price': 0, 'profit': 0}
        
        elif max_blocks == float('inf'):
            print("♾️  РЕЗУЛЬТАТ: Можно добавлять блоки стали бесконечно!")
            print("   (Блоки стали бесплатны или дают деньги)")
            return {'max_blocks': float('inf'), 'max_price': float('inf'), 'profit': float('inf')}
        
        else:
            max_price = calculate_sword_price(A, B, max_blocks)
            base_price = A
            
            print(f"✅ РЕЗУЛЬТАТ: Максимум {max_blocks} блоков стали")
            print(f"   Цена оптимального меча: {max_price} изумрудов")
            print(f"   Прибыль от улучшений: +{max_price - base_price} изумрудов")
            print()
            
            print("📊 ВАРИАНТЫ МЕЧЕЙ:")
            print("-" * 40)
            
            for n in range(min(max_blocks + 2, 6)):
                price = calculate_sword_price(A, B, n)
                affordable = "✅" if price <= C else "❌"
                if n == max_blocks:
                    status = f"{affordable} ОПТИМАЛЬНЫЙ"
                elif price > C:
                    status = f"{affordable} Слишком дорого"
                else:
                    status = f"{affordable} Можно улучшить"
                    
                print(f"  {n} блоков: {price} изумрудов {status}")
            
            if max_blocks >= 5:
                print("  ...")
                price = calculate_sword_price(A, B, max_blocks)
                print(f"  {max_blocks} блоков: {price} изумрудов ✅ ОПТИМАЛЬНЫЙ")
            
            return {
                'max_blocks': max_blocks, 
                'max_price': max_price, 
                'profit': max_price - base_price
            }

def test_multiple_scenarios():
    """Тестирует несколько сценариев крафта"""
    
    scenarios = [
        {"A": 10, "B": 5, "C": 50, "name": "Обычная деревня"},
        {"A": 15, "B": 3, "C": 30, "name": "Бедная деревня"},
        {"A": 5, "B": 10, "C": 100, "name": "Богатая деревня"},
        {"A": 20, "B": 8, "C": 15, "name": "Невозможная ситуация"},
        {"A": 10, "B": 0, "C": 50, "name": "Бесплатная сталь"},
    ]
    
    print("🏘️  АНАЛИЗ РАЗНЫХ ДЕРЕВЕНЬ")
    print("=" * 60)
    
    results = []
    
    for scenario in scenarios:
        print(f"\n🏠 {scenario['name']}:")
        print("-" * 30)
        
        result = optimize_sword_crafting(
            scenario["A"], 
            scenario["B"], 
            scenario["C"], 
            show_details=False
        )
        
        max_blocks = result['max_blocks']
        
        if max_blocks == -1:
            print("❌ Жители не могут купить даже базовый меч")
        elif max_blocks == float('inf'):
            print("♾️  Можно добавлять сталь бесконечно")
        else:
            max_price = result['max_price']
            profit = result['profit']
            print(f"✅ Максимум: {max_blocks} блоков стали")
            print(f"   Цена: {max_price} изумрудов (+{profit} к базовой)")
        
        results.append({**scenario, **result})
    
    return results

def interactive_calculator():
    """Интерактивный калькулятор для игроков"""
    
    print("🎮 ИНТЕРАКТИВНЫЙ КАЛЬКУЛЯТОР МЕЧЕЙ")
    print("=" * 40)
    print("Введите параметры для расчета оптимального меча:")
    
    try:
        A = int(input("💰 Стоимость рукояти (A): "))
        B = int(input("🔩 Стоимость блока стали (B): "))
        C = int(input("💎 Бюджет жителей (C): "))
        
        print()
        result = optimize_sword_crafting(A, B, C)
        return result
        
    except ValueError:
        print("❌ Ошибка: Введите корректные числа!")
        return None

def quick_formula(A, B, C):
    """
    Быстрый расчет по формуле без детального вывода
    
    Returns:
        int: Максимальное количество блоков стали
    """
    if A > C:
        return -1
    if B <= 0:
        return float('inf')
    return (C - A) // B

def minecraft_guide():
    """Практическое руководство для игроков Майнкрафт"""
    
    print("🎮 ГАЙД ПО ОПТИМИЗАЦИИ МЕЧЕЙ В МАЙНКРАФТ")
    print("=" * 50)
    print()
    print("📝 ФОРМУЛА ЦЕНЫ МЕЧА:")
    print("   Цена = A + B × N")
    print("   где:")
    print("   • A = стоимость дерева для рукояти")
    print("   • B = стоимость одного блока стали") 
    print("   • N = количество блоков стали")
    print("   • Ограничение: Цена ≤ C (бюджет жителей)")
    print()
    
    print("🧮 БЫСТРАЯ ФОРМУЛА:")
    print("   Максимум блоков = (C - A) ÷ B (округлить вниз)")
    print()
    
    print("⚠️  ОСОБЫЕ СЛУЧАИ:")
    print("   • Если A > C → жители не купят даже базовый меч")
    print("   • Если B = 0 → можно добавлять блоки бесплатно")
    print("   • Если (C - A) < B → только базовый меч без улучшений")
    print()
    
    print("💡 СТРАТЕГИИ:")
    print("   1. Всегда используйте максимум блоков стали")
    print("   2. Если A слишком велико - найдите более дешевое дерево")
    print("   3. Торгуйтесь с кузнецами за более дешевую сталь")
    print("   4. Ищите богатых жителей с большим бюджетом C")
    print()
    
    examples = [
        (10, 5, 50, "Стандартная ситуация"),
        (15, 3, 30, "Бедная деревня"),
        (5, 10, 100, "Богатая деревня"),
        (20, 8, 15, "Слишком дорого")
    ]
    
    print("📊 ПРИМЕРЫ РАСЧЕТОВ:")
    print("-" * 30)
    
    for A, B, C, desc in examples:
        max_blocks = quick_formula(A, B, C)
        if max_blocks == -1:
            result = "Невозможно"
        elif max_blocks == float('inf'):
            result = "Бесконечно"
        else:
            price = A + B * max_blocks
            result = f"{max_blocks} блоков ({price} изумрудов)"
        
        print(f"{desc}:")
        print(f"  A={A}, B={B}, C={C} → {result}")

minecraft_guide()
    
print("\n" + "="*60)
    

print("🔧 ДЕТАЛЬНЫЙ ПРИМЕР:")
optimize_sword_crafting(A=10, B=5, C=50)