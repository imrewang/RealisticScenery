# RealisticScenery
编程画一个真实感静态或动画景物

# 一、程序说明

## （一）基本思路

1. 生成一个球体

2. 读取背景图片

3. 插入纹理

4. 绘制对象添加映射器

5. 绘制窗口

6. 绘制窗口添加绘制器,加入对象

7. 交互器绑定绘制窗口,设置渲染窗口

8. 设置渲染场景的背景颜色

9. 绘制窗口内所有绘制器同步渲染绘制

10. 开始进入事件响应循环

## （二）说明

bmpReader.SetFileName("img.png")

img.png为球体纹理。

运行时，请将Project2.py和img.png放于同一工作目录下。

# 二、算法原理

视觉化工具函式库

Vtk，（visualization toolkit）是一个开源的免费软件系统，主要用于三维计算机图形学、图像处理和可视化。Vtk是在面向对象原理的基础上设计和实现的，它的内核是用C++构建的。
Visualization Toolkit 是一个用于可视化应用程序构造与运行的支撑环境，它是在三维函数库OpenGL 的基础上采用面向对象的设计方法发展起来的，它将我们在可视化开发过程中会经常遇到的细节屏蔽起来，并将一些常用的算法封装起来。

Visualization Toolkit 具有丰富的数据类型，支持对多种数据类型进行处理。其核心数据模型能够表示几乎所有与物理科学相关的现实世界问题，适合涉及有限差分和有限元解决方案的医学成像和工程工作。

Visualization Toolkit具有强大的三维图形功能。Visualization Toolkit 既支持基于体素Voxel-basedrendering 的体绘制Volume Rendering又保留了传统的面绘制，从而在极大的改善可视化效果的同时又可以充分利用现有的图形库和图形硬件。

# 三、运行截图

![run1](https://github.com/imrewang/RealisticScenery/blob/main/screenshot/run1.png?raw=true)

![run2](https://github.com/imrewang/RealisticScenery/blob/main/screenshot/run2.png?raw=true)

![run3](https://github.com/imrewang/RealisticScenery/blob/main/screenshot/run3.png?raw=true)


# 四、参考文献

vtk: https://vtk.org/

VTK 9.2.20221001 Documentation: https://vtk.org/doc/nightly/html/index.html

Python Examples: https://kitware.github.io/vtk-examples/site/Python/
