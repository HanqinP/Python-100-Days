import pygame

def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置尺寸大小
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    x,y = 50, 50
    
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 设置窗体背景色
        screen.fill((242,242,242))
        # 绘制一个圆（参数分别是：屏幕，颜色，圆心，半径，0表示填充圆）
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)

        # 刷新当前窗口（渲染窗口将绘制的图像显现出来）
        pygame.display.flip()
        # 每隔50毫秒改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()