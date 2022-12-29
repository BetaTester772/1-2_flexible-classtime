# import numpy for math and matplotlib.pyplot for graph
import matplotlib.pyplot as plt
import numpy as np

L = 1  # 상자의 길이


def W(x, n):  # wave function
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)


def waveFunction():  # 파동함수
    x = np.linspace(0, L, 1000)  # 0부터 L까지 1000개의 점을 생성
    colors = ['b', 'g', 'r']  # 파란색, 초록색, 빨간색
    for n in range(1, 4):  # 1부터 3까지 반복
        plt.plot(x, W(x, n) + n * 3, colors[n - 1])  # 파동 함수 파란색, 초록색, 빨간색으로 그래프를 그림
    plt.gca().axes.xaxis.set_visible(False)  # x축 숨김
    plt.gca().axes.yaxis.set_visible(False)  # y축 숨김
    plt.title('Wave functions')  # 그래프 제목
    plt.legend(['n=1', 'n=2', 'n=3'])  # 범례
    for n in range(1, 4):
        plt.axhline(n * 3, color='lightgray', linestyle='--', linewidth=2)  # 가로선
    plt.show()  # 그래프 출력


def probabilityDensity():  # 확률밀도함수
    x = np.linspace(0, L, 1000)  # 0부터 L까지 1000개의 점을 생성
    colors = ['b', 'g', 'r']  # 파란색, 초록색, 빨간색
    for n in range(1, 4):  # 1부터 3까지 반복
        plt.plot(x, W(x, n) ** 2 + n * 3, colors[n - 1])  # 확률밀도 함수(파동함수 ^ 2) 파란색, 초록색, 빨간색으로 그래프를 그림
    plt.gca().axes.xaxis.set_visible(False)  # x축 숨김
    plt.gca().axes.yaxis.set_visible(False)  # y축 숨김
    plt.title('Probability density')  # 그래프 제목
    plt.legend(['n=1', 'n=2', 'n=3'])  # 범례
    for n in range(1, 4):
        plt.axhline(n * 3, color='lightgray', linestyle='--', linewidth=2)  # 가로선
    plt.show()  # 그래프 출력


if __name__ == '__main__':  # wave_function_and_probability_density.py를 실행할 때만 실행
    waveFunction()  # 파동함수 그래프 출력
    print('waveFunction() done')  # waveFunction() 함수가 끝났음을 출력
    probabilityDensity()  # 확률밀도함수 그래프 출력
    print('probabilityDensity() done')  # probabilityDensity() 함수가 끝났음을 출력
