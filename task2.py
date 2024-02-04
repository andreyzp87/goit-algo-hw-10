import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x: float) -> float:
    return 2 * x ** 2 + 6 * x + 10


def monte_carlo(f: callable(float), a: float, b: float, n: int) -> float:
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, f(b), n)

    inside_count = np.sum(y <= f(x))
    full_area = (b - a) * max(f(b), f(a))

    return full_area * inside_count / n


def show_chart(f: callable(float), a: float, b: float):
    # Створення діапазону значень для x
    x = np.linspace(0, 4, 400)
    y = f(x)
    # Створення графіка
    fig, ax = plt.subplots()
    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)
    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = 2x^2 +6x +10 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


if __name__ == '__main__':
    a = 1
    b = 3

    result, error = spi.quad(f, a, b)

    print("Інтеграл: ", result)

    area = monte_carlo(f, a, b, 1000000)
    print("Площа під графіком: ", area)

    show_chart(f, a, b)
