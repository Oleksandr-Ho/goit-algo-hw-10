import random
import scipy.integrate as spi

# Функція, яку інтегруємо
def f(x):
    return x ** 2

def monte_carlo_integration(f, a, b, y_max, num_points, num_experiments):
    """Виконує серію експериментів методом Монте-Карло для обчислення інтеграла."""
    total_area = 0
    
    for _ in range(num_experiments):
        points_under_curve = 0
        for _ in range(num_points):
            random_x = random.uniform(a, b)
            random_y = random.uniform(0, y_max)
            if random_y <= f(random_x):
                points_under_curve += 1
        
        # Розрахунок площі за методом Монте-Карло для одного експерименту
        area_under_curve = (points_under_curve / num_points) * (b - a) * y_max
        total_area += area_under_curve
    
    # Обчислення середньої площі за всіма експериментами
    average_area = total_area / num_experiments
    return average_area

# Параметри інтегрування та експерименту
a = 0  # Нижня межа інтегрування
b = 2  # Верхня межа інтегрування
y_max = f(b)  # Максимальне значення функції на інтервалі
# num_points = 15000  # Кількість випадкових точок в одному експерименті
# num_experiments = 100  # Кількість експериментів

num_points = 1500  # Кількість випадкових точок в одному експерименті
num_experiments = 10  # Кількість експериментів

# Виконання серії експериментів методом Монте-Карло
average_integral = monte_carlo_integration(f, a, b, y_max, num_points, num_experiments)

# Обчислення точного значення інтеграла за допомогою функції quad
integral_quad, _ = spi.quad(f, a, b)

print(f"Середнє значення інтеграла методом Монте-Карло: {average_integral}")
print(f"Точне значення інтеграла за допомогою функції quad: {integral_quad}")


