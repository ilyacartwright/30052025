class SortingHat:
    """Распределяющая шляпа Хогвартса"""
    
    def __init__(self):
        self.houses = {
            'Гриффиндор': {'main_skill': 'храбрость', 'priority': 1},
            'Когтевран': {'main_skill': 'ум', 'priority': 2}, 
            'Пуффендуй': {'main_skill': 'настойчивость', 'priority': 3},
            'Слизерин': {'main_skill': 'хитрость', 'priority': 4}
        }
        
        self.skills = {
            'храбрость': 0,
            'ум': 1, 
            'настойчивость': 2,
            'хитрость': 3
        }
    
    def calculate_house_score(self, student_skills, house_name):
        """
        Вычисляет суммарный балл студента для конкретного факультета
        
        Args:
            student_skills (list): [храбрость, ум, настойчивость, хитрость]
            house_name (str): Название факультета
            
        Returns:
            int: Суммарный балл с учетом удвоения основного навыка
        """
        main_skill = self.houses[house_name]['main_skill']
        main_skill_index = self.skills[main_skill]
        
        total_score = sum(student_skills) + student_skills[main_skill_index]
        
        return total_score
    
    def find_best_house(self, student_skills):
        """
        Определяет лучший факультет для студента
        
        Args:
            student_skills (list): [храбрость, ум, настойчивость, хитрость]
            
        Returns:
            str: Название факультета
        """
        house_scores = {}
        
        for house_name in self.houses:
            score = self.calculate_house_score(student_skills, house_name)
            house_scores[house_name] = score
        
        max_score = max(house_scores.values())
        
        best_houses = [house for house, score in house_scores.items() if score == max_score]
        
        if len(best_houses) > 1:
            best_houses.sort(key=lambda house: self.houses[house]['priority'])
        
        return best_houses[0]
    
    def sort_students(self, students):
        """
        Распределяет всех студентов по факультетам
        
        Args:
            students (list): Список кортежей (имя, [храбрость, ум, настойчивость, хитрость])
            
        Returns:
            dict: Словарь {факультет: [список студентов]}
        """
        result = {house: [] for house in self.houses}
        sorting_details = []
        
        for name, skills in students:
            house_scores = {}
            for house_name in self.houses:
                score = self.calculate_house_score(skills, house_name)
                house_scores[house_name] = score
            
            chosen_house = self.find_best_house(skills)
            result[chosen_house].append(name)
            
            sorting_details.append({
                'name': name,
                'skills': skills,
                'scores': house_scores,
                'chosen_house': chosen_house
            })
        
        return result, sorting_details
    
    def print_sorting_ceremony(self, students):
        """Проводит торжественную церемонию распределения"""
        print("🎩 ЦЕРЕМОНИЯ РАСПРЕДЕЛЕНИЯ В ХОГВАРТСЕ 🎩")
        print("=" * 60)
        
        sorted_houses, details = self.sort_students(students)
        
        for detail in details:
            print(f"\n👤 {detail['name']}")
            print(f"   Навыки: Храбрость={detail['skills'][0]}, Ум={detail['skills'][1]}, "
                  f"Настойчивость={detail['skills'][2]}, Хитрость={detail['skills'][3]}")
            print("   Баллы по факультетам:")
            
            for house, score in detail['scores'].items():
                main_skill = self.houses[house]['main_skill']
                print(f"     {house}: {score} (основной навык: {main_skill})")
            
            print(f"   🏰 РЕЗУЛЬТАТ: {detail['chosen_house']}!")
        
        print("\n" + "=" * 60)
        print("📊 ИТОГОВОЕ РАСПРЕДЕЛЕНИЕ:")
        print("=" * 60)
        
        for house, students_list in sorted_houses.items():
            print(f"\n🏛️  {house}: {len(students_list)} студентов")
            if students_list:
                for student in students_list:
                    print(f"    • {student}")
            else:
                print("    • (пусто)")
        
        return sorted_houses

def hogwarts_example():
    """Пример церемонии распределения"""
    
    hat = SortingHat()
    
    new_students = [
        ("Гарри Поттер", [9, 7, 8, 6]),
        ("Гермиона Грейнджер", [8, 10, 9, 7]),
        ("Рон Уизли", [8, 6, 7, 5]),
        ("Драко Малфой", [6, 8, 7, 9]),
        ("Полумна Лавгуд", [7, 9, 6, 8]),
        ("Седрик Диггори", [7, 8, 10, 6]),
        ("Невилл Долгопупс", [5, 6, 9, 4])
    ]
    
    return hat.print_sorting_ceremony(new_students)

def test_single_student(name, skills):
    """Тестирует распределение одного студента"""
    hat = SortingHat()
    
    print(f"🎓 Тестируем студента: {name}")
    print(f"Навыки: {skills}")
    
    house_scores = {}
    for house_name in hat.houses:
        score = hat.calculate_house_score(skills, house_name)
        house_scores[house_name] = score
        main_skill = hat.houses[house_name]['main_skill']
        print(f"{house_name}: {score} баллов (основной: {main_skill})")
    
    chosen_house = hat.find_best_house(skills)
    print(f"\n🏰 Результат: {chosen_house}!")
    
    return chosen_house

hogwarts_example()