import vtk

# *************柱体****************
# 生成一个球体
sphere = vtk.vtkSphereSource()
# 半径
sphere.SetRadius(1.0)
# 设置经纬面点
sphere.SetThetaResolution(360)
sphere.SetPhiResolution(360)

print(f"半径:{sphere.GetRadius()},分辨率：{sphere.GetThetaResolution ()}")

# 读取 bmp 背景图片
bmpReader = vtk.vtkPNGReader()
bmpReader.SetFileName("img.png")
# 纹理
texture = vtk.vtkTexture()
# 数据接口联通纹理
texture.SetInputConnection(bmpReader.GetOutputPort())
# 插入纹理
texture.InterpolateOn()
textureMapToSphere = vtk.vtkTextureMapToSphere()
textureMapToSphere.SetInputConnection(sphere.GetOutputPort())

# 映射,将输入的数据转换为几何图元(点、线、多边形)进行渲染
sphereMapper = vtk.vtkPolyDataMapper()
# 设置 VTK 可视化管线的输入数据接口，对应的可视化管线输出数据的接口为 GetOutputPort()
sphereMapper.SetInputConnection(textureMapToSphere.GetOutputPort())

sphereActor = vtk.vtkActor()
print(f"位置:{sphereActor.GetPosition()}")
# 绘制对象添加映射器，设置定义Actor几何形状的Mapper
sphereActor.SetMapper(sphereMapper)
# 设置纹理属性
sphereActor.SetTexture(texture)

# 绘制器，负责管理场景的渲染过程。
# 组成场景的所有对象包括Prop，照相机(Camera)和光照(Light)都被集中在一个vtkRenderer对象中。
# 一个vtkRenderWindow中可以有多个vtkRenderer对象，而这些vtkRenderer可以渲染在窗口中不同的矩形区域中(即视口)，或者覆盖整个窗口区域。
renderer = vtk.vtkRenderer()
# 绘制窗口,将操作系统与VTK渲染引擎连接到一起
renWin = vtk.vtkRenderWindow()
# 绘制窗口添加绘制器,加入 vtkRenderer 对象
renWin.AddRenderer(renderer)
# 交互器,提供平台独立的响应鼠标、键盘和时钟事件的交互机制
i_ren = vtk.vtkRenderWindowInteractor()
# 交互器绑定绘制窗口,设置渲染窗口，消息是通过渲染窗口捕获到的，所以必须要给交互器对象设置渲染窗口
i_ren.SetRenderWindow(renWin)
# 为处理窗口事件做准备，交互器工作之前必须先调用这个方法进行初始化
i_ren.Initialize()

# 绘制器添加对象，添加vtkProp类型的对象到渲染场景中
renderer.AddActor(sphereActor)
# 绘制器设置背景，设置渲染场景的背景颜色
renderer.SetBackground(0.25,0.41,0.88)
print("Renderer bg:",renderer.GetBackground())
# SetBackground2()用于设置渐变的另外一种颜色
renderer.SetBackground2(0.7,0.7,0.7)
# 打开背景颜色渐变效果，相当于调用方法 GradientBackgroundOn()
renderer.SetGradientBackground(1)

# 绘制窗口内所有绘制器同步渲染绘制
renWin.Render()
# 设置窗口的大小，以像素为单位
renWin.SetSize(800,600)
renWin.SetWindowName("Project2")

print("Window size:",renWin.GetSize())

# 开始进入事件响应循环，交互器处于等待状态，等待用户交互事件的发生
i_ren.Start()
