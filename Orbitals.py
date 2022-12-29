# Schrödinger equation
import matplotlib.pyplot as plt
import numpy as np

# Constants
a0 = 5.2917721092e-11
Z = 1
a = a0


# Wave function(n, l, ml)
def R_1_0_0(r):  # 1s
    return 2 * (Z / a) ** (3 / 2) * np.exp(-Z * r / a)


def R_2_0_0(r):  # 2s
    return 1 / (2 * (Z / a) ** (3 / 2)) * (2 - Z * r / a) * np.exp(-Z * r / (2 * a))


def R_2_1_0(r):  # 2p
    return 1 / 3 ** 1 / 2 * (2 * a) ** (3 / 2) * r / a * np.exp(-Z * r / (2 * a))


def R_3_0_0(r):  # 3s
    return 1 / (2 * (Z / a) ** (3 / 2)) * (18 - 9 * Z * r / a + Z ** 2 * r ** 2 / a ** 2) * np.exp(-Z * r / (3 * a))


def R_3_1_0(r):  # 3p
    return 1 / 3 ** 1 / 2 * (2 * a) ** (3 / 2) * r / a * (6 - Z * r / a) * np.exp(-Z * r / (3 * a))


def R_3_2_0(r):  # 3d
    return 1 / 3 ** 1 / 2 * (2 * a) ** (3 / 2) * r ** 2 / a ** 2 * np.exp(-Z * r / (3 * a))


def R_4_0_0(r):  # 4s
    return 1 / (2 * (Z / a) ** (3 / 2)) * (
            32 - 24 * Z * r / a + 6 * Z ** 2 * r ** 2 / a ** 2 - Z ** 3 * r ** 3 / a ** 3) * np.exp(
            -Z * r / (4 * a))


def R_4_1_0(r):  # 4p
    return 1 / 3 ** 1 / 2 * (2 * a) ** (3 / 2) * r / a * (12 - 6 * Z * r / a + Z ** 2 * r ** 2 / a ** 2) * np.exp(
            -Z * r / (4 * a))


def R_4_2_0(r):  # 4d
    return 1 / 3 ** 1 / 2 * (2 * a) ** (3 / 2) * r ** 2 / a ** 2 * (4 - Z * r / a) * np.exp(-Z * r / (4 * a))


def R_4_3_0(r):  # 4f
    return 1 / 3 ** 1 / 2 * (2 * a) ** (3 / 2) * r ** 3 / a ** 3 * np.exp(-Z * r / (4 * a))


def R_5_0_0(r):  # 5s
    return 1 / (2 * (Z / a) ** (3 / 2)) * (
            50 - 40 * Z * r / a + 12 * Z ** 2 * r ** 2 / a ** 2 - 2 * Z ** 3 * r ** 3 / a ** 3) * np.exp(
            -Z * r / (5 * a))


def R_5_1_0(r):  # 5p
    return 1 / 3 ** 1 / 2 * (2 * a) ** (3 / 2) * r / a * (20 - 12 * Z * r / a + 2 * Z ** 2 * r ** 2 / a ** 2) * np.exp(
            -Z * r / (5 * a))


def R_5_2_0(r):  # 5d
    return 1 / 3 ** 1 / 2 * (2 * a) ** (3 / 2) * r ** 2 / a ** 2 * (6 - 2 * Z * r / a) * np.exp(-Z * r / (5 * a))


def R_5_3_0(r):  # 5f
    return 1 / 3 ** 1 / 2 * (2 * a) ** (3 / 2) * r ** 3 / a ** 3 * (2 - Z * r / a) * np.exp(-Z * r / (5 * a))


def R_5_4_0(r):  # 5g
    return 1 / 3 ** 1 / 2 * (2 * a) ** (3 / 2) * r ** 4 / a ** 4 * np.exp(-Z * r / (5 * a))


# plot
def plotEach():  # 오비탈 각각 그리기
    r = np.linspace(0, a0 * 50, 1000)  # r 범위
    functions = [R_1_0_0, R_2_0_0, R_2_1_0, R_3_0_0, R_3_1_0, R_3_2_0, R_4_0_0, R_4_1_0, R_4_2_0, R_4_3_0, R_5_0_0,
                 R_5_1_0, R_5_2_0, R_5_3_0, R_5_4_0]  # 함수들
    print(len(functions))  # 함수 개수
    titles = ['1s', '2s', '2p', '3s', '3p', '3d', '4s', '4p', '4d', '4f', '5s', '5p', '5d', '5f',
              '5g']  # 오비탈 종류
    for f in functions:  # 함수 개수만큼 반복
        plt.plot(r, f(r))  # 그래프 그리기
        plt.title(titles[functions.index(f)])  # 오비탈 종류
        plt.show()  # 그래프 보여주기
        print(f)  # 함수 출력


def plotAll():  # 오비탈 한번에 그리기
    plt.figure(figsize=(16, 10))  # 그래프 크기
    r = np.linspace(0, a0 * 50, 1000)  # r 범위
    functions = [R_1_0_0, R_2_0_0, R_2_1_0, R_3_0_0, R_3_1_0, R_3_2_0, R_4_0_0, R_4_1_0, R_4_2_0, R_4_3_0, R_5_0_0,
                 R_5_1_0, R_5_2_0, R_5_3_0, R_5_4_0]  # 함수들
    print(len(functions))  # 함수 개수
    titles = ['1s', '2s', '2p', '3s', '3p', '3d', '4s', '4p', '4d', '4f', '5s', '5p', '5d', '5f',
              '5g']  # 오비탈 종류
    for f in functions:  # 함수 개수만큼 반복
        plt.subplot(3, 5, functions.index(f) + 1)  # 그래프 위치
        plt.plot(r, f(r))  # 그래프 그리기
        plt.title(titles[functions.index(f)])  # 오비탈 종류
        print(f)  # 함수 출력
    plt.show()  # 그래프 보여주기


if __name__ == '__main__':  # 메인 함수
    plotEach()  # 오비탈 각각 그리기
    print('plotEash() 완료')  # plotEash() 완료 출력
    plotAll()  # 오비탈 한번에 그리기
    print('plotAll() 완료')  # plotAll() 완료 출력
