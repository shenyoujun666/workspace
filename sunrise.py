from manimlib import *

class SunRise_Second_Version(Scene):
    def construct(self):
        #坐标系（用于调整位置、排版<可注释掉>）
        """         axes = Axes()
        axes.add_coordinate_labels()
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        """
         #标题部分
        author = Text("--By CCHEN", font=".PingFang SC", color=WHITE, font_size=30)
        title = Text("海上日出", font=".PingFang SC", color=BLUE, font_size=100)
        subtitle = Text("--刍议圆与直线的位置关系--", font=".PingFang SC", color="#E6E6E6", font_size=30)
        tool = Text("Tools: ManimGL、Python", font=".PingFang SC", color=WHITE, font_size=30)

        title.move_to(UP * 1)
        author.move_to(title.get_center())
        author.shift(DOWN * 2+RIGHT * 1)
        tool.move_to(author.get_center())
        tool.shift(DOWN * 0.5+LEFT * 1+RIGHT * 0.1)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(Write(tool),Write(author))
        self.wait(4)

        self.play(FadeOut(tool),FadeOut(author),FadeOut(subtitle),FadeOut(title))

        #主题部分
        #初始化
        line = Line([-6, 0, 0], [6, 0, 0])

        circle = Circle(radius=1, color=ORANGE) 

        circle.move_to([-1,-2,0])
        
        circle_center = Dot(circle.get_center(),radius=0.05)

        circle_radius_text = Text("r") 

        line_circle_dist = Line(start=[-1,0,0],end=circle.get_center())
        line_circle_dist_text = Text(f"l={line_circle_dist.get_length():.2f}")
        line_circle_dist_text.move_to(line_circle_dist.get_center())
        line_circle_dist_text.shift(LEFT * 1)

        
        radius_dot = Dot(circle.point_from_proportion(2),radius=0.05)
        radius = DashedLine(start=circle_center,end=radius_dot)
        circle_radius_text.move_to(radius.get_center())
        circle_radius_text.shift(UP * 0.2)

        circle_staus1_text1 = Text("此时，圆与直线无交点", font=".PingFang SC", color=BLUE, font_size=35)
        circle_staus1_text2 = Text("我们称此时圆的状态为“相离”", font=".PingFang SC", color=BLUE,font_size=35)
        circle_staus1_text1.move_to(circle.get_center())
        circle_staus1_text1.shift(RIGHT * 3.5)
        circle_staus1_text1.shift(UP * 0.5)
        circle_staus1_text2.move_to(circle_staus1_text1.get_center())
        circle_staus1_text2.shift(DOWN * 0.5)


        #动画1
        #画出直线
        self.play(Write(line))  
        
        start_text_1 = Text("这是一条直线", font=".PingFang SC", color=BLUE, font_size=35)
        start_text_1.move_to(line.get_center())
        start_text_1.shift(UP * 2)

        self.play(Write(start_text_1))
        self.play(start_text_1.animate.shift(UP * 0.5))

        start_text_2 = Text("下面，让我们画一个圆", font=".PingFang SC", color=BLUE, font_size=35)
        start_text_2.move_to(start_text_1.get_center())
        start_text_2.shift(DOWN * 0.5)

        self.play(Write(start_text_2))


        #画出圆形
        self.play(Write(circle_center))        
        self.play(Write(circle))
        self.play(start_text_1.animate.shift(UP * 0.5),start_text_2.animate.shift(UP * 0.5))

        start_text_3 = Text("接下来，我们作出这个圆的半径，和其与直线的距离", font=".PingFang SC", color=BLUE, font_size=35)
        start_text_3.move_to(start_text_2.get_center())
        start_text_3.shift(DOWN * 0.5)

        self.play(Write(start_text_3))

        self.play(Write(line_circle_dist),Write(line_circle_dist_text),Write(radius_dot),Write(radius),Write(circle_radius_text))
        self.wait()
        self.play(FadeOut(start_text_3),FadeOut(start_text_1),FadeOut(start_text_2))
        self.play(Write(circle_staus1_text1))
        self.play(Write(circle_staus1_text2))
        self.wait(2)

        self.play(FadeOut(circle_staus1_text1,shift=DOWN),FadeOut(circle_staus1_text2,shift=DOWN),FadeOut(line_circle_dist_text,shift=DOWN),FadeOut(line_circle_dist,shift=DOWN))
        
        start_staus2_text1 = Text("接下来，我们将直线和圆的位置进行变换", font=".PingFang SC", color=BLUE, font_size=35)
        start_staus2_text1.move_to(start_text_2.get_center())

        self.play(Write(start_staus2_text1))

        #变换至相切状态
        animations_1 = [
            ApplyMethod(circle.shift, RIGHT*1+UP*1),
            ApplyMethod(circle_center.shift, RIGHT*1+UP*1),
            ApplyMethod(radius_dot.shift, RIGHT*1+UP*1),
            ApplyMethod(radius.shift, RIGHT*1+UP*1),
            ApplyMethod(circle_radius_text.shift, RIGHT*1+UP*1),
        ]
        group_animation_1 = AnimationGroup(*animations_1)
        self.play(group_animation_1)
        self.play(FadeOut(start_staus2_text1))

        line_circle_dist = Line(start=circle.get_center(),end=[0,0,0])
        line_circle_dist_text = Text(f"l={line_circle_dist.get_length():.2f}")
        line_circle_dist_text.move_to(line_circle_dist.get_center())
        line_circle_dist_text.shift(LEFT * 1)

        circle_staus2_text1 = Text("此时，圆与直线有一个交点", font=".PingFang SC", color=BLUE, font_size=35)
        circle_staus2_text2 = Text("我们称此时圆与直线的关系为“相切”", font=".PingFang SC", color=BLUE,font_size=35)
        circle_staus2_text1.move_to(circle.get_center())
        circle_staus2_text1.shift(RIGHT * 3.5)
        circle_staus2_text1.shift(UP * 0.5)
        circle_staus2_text2.move_to(circle_staus2_text1.get_center())
        circle_staus2_text2.shift(DOWN * 0.5)

        dot_staus2_1 = Dot([0,0,0],radius=0.05)
        dot_staus2_1.set_color(YELLOW)

        self.play(Write(line_circle_dist),Write(line_circle_dist_text))
        self.play(Write(circle_staus2_text1))
        self.play(Write(dot_staus2_1))
        self.play(Write(circle_staus2_text2))
        self.wait(2)
        self.play(FadeOut(circle_staus2_text1,shift=DOWN),FadeOut(circle_staus2_text2,shift=DOWN),FadeOut(line_circle_dist_text,shift=DOWN),FadeOut(line_circle_dist,shift=DOWN),FadeOut(dot_staus2_1))

        circle_staus3_text1 = Text("此时，圆与直线有交点", font=".PingFang SC", color=BLUE, font_size=35)
        circle_staus3_text2 = Text("不难发现，这时圆的交点有两个", font=".PingFang SC", color=BLUE, font_size=35)
        circle_staus3_text3 = Text("我们称此时圆与直线的关系为“相交”", font=".PingFang SC", color=BLUE,font_size=35)
        circle_staus3_text1.move_to(circle.get_center())
        circle_staus3_text1.shift(RIGHT * 3.5)
        circle_staus3_text1.shift(UP * 3)
        circle_staus3_text2.move_to(circle_staus3_text1.get_center())
        circle_staus3_text2.shift(DOWN * 0.5)
        circle_staus3_text3.move_to(circle_staus3_text2.get_center())
        circle_staus3_text3.shift(DOWN * 0.5)

        dot_staus3_1 = Dot([-1,0,0],radius=0.05)
        dot_staus3_2 = Dot([1,0,0],radius=0.05)
        dot_staus3_1.set_color(YELLOW)
        dot_staus3_2.set_color(YELLOW)

        line_circle_dist = Line(start=[1,0,0],end=[1,0,0])
        line_circle_dist_text = Text(f"l={line_circle_dist.get_length():.2f}")
        line_circle_dist_text.move_to(line_circle_dist.get_center())
        line_circle_dist_text.shift(LEFT * 1)


        animations_2 = [
            ApplyMethod(circle.shift, UP*1),
            ApplyMethod(circle_center.shift, UP*1),
            ApplyMethod(radius_dot.shift, UP*1),
            ApplyMethod(radius.shift, UP*1),
            ApplyMethod(circle_radius_text.shift, UP*1),
        ]
        group_animation_2 = AnimationGroup(*animations_2)
        self.play(group_animation_2)

        self.play(Write(line_circle_dist),Write(line_circle_dist_text))
        self.play(line_circle_dist_text.animate.shift(LEFT * 2 + UP * 0.5))
        self.play(Write(circle_staus3_text1))
        self.play(Write(circle_staus3_text2))
        self.play(Write(circle_staus3_text3))
        self.play(Write(dot_staus3_1),Write(dot_staus3_2))
        self.wait(2)

        self.play(FadeOut(circle_staus3_text1,shift=DOWN),FadeOut(circle_staus3_text2,shift=DOWN),FadeOut(circle_staus3_text3,shift=DOWN),FadeOut(line_circle_dist_text,shift=DOWN),FadeOut(line_circle_dist,shift=DOWN),FadeOut(dot_staus3_1,shift=DOWN),FadeOut(dot_staus3_2,shift=DOWN))   

        animations_3 = [
            ApplyMethod(circle.shift, UP*1+RIGHT*1),
            ApplyMethod(circle_center.shift, UP*1+RIGHT*1),
            ApplyMethod(radius_dot.shift, UP*1+RIGHT*1),
            ApplyMethod(radius.shift, UP*1+RIGHT*1),
            ApplyMethod(circle_radius_text.shift, UP*1+RIGHT*1),
        ]
        group_animation_3 = AnimationGroup(*animations_3)
        self.play(group_animation_3)   

        line_circle_dist = Line(start=[1,1,0],end=[1,0,0])
        line_circle_dist_text = Text(f"l={line_circle_dist.get_length():.2f}")
        line_circle_dist_text.move_to(line_circle_dist.get_center())
        line_circle_dist_text.shift(LEFT * 1)
        line_circle_dist_text.shift(UP * 1)

        circle_staus4_text1 = Text("当然，我们还能继续下去", font=".PingFang SC", color=BLUE, font_size=35)
        circle_staus4_text1.move_to(circle.get_center())
        circle_staus4_text1.shift(RIGHT * 3.5)
        circle_staus4_text2 = Text("位置关系：相切", font=".PingFang SC", color=BLUE, font_size=35)
        circle_staus4_text2.move_to(circle_staus4_text1.get_center())
        circle_staus4_text2.shift(DOWN * 0.5)

        self.play(Write(circle_staus4_text1),Write(line_circle_dist))
        self.play(Write(line_circle_dist_text))
        self.play(Write(circle_staus4_text2))
        self.wait()
        self.play(FadeOut(circle_staus4_text2,shift=DOWN),FadeOut(line_circle_dist_text,shift=DOWN),FadeOut(line_circle_dist,shift=DOWN))

        circle_staus_5_text1 = Text("位置关系：相离", font=".PingFang SC", color=BLUE, font_size=35)
        circle_staus_5_text1.move_to(circle_staus4_text2.get_center())

        animations_4 = [
            ApplyMethod(circle.shift, UP*1+RIGHT*1),
            ApplyMethod(circle_center.shift, UP*1+RIGHT*1),
            ApplyMethod(radius_dot.shift, UP*1+RIGHT*1),
            ApplyMethod(radius.shift, UP*1+RIGHT*1),
            ApplyMethod(circle_radius_text.shift, UP*1+RIGHT*1),
        ]
        group_animation_4 = AnimationGroup(*animations_4)
        self.play(group_animation_4)   

        line_circle_dist = Line(start=[2,2,0],end=[2,0,0])
        line_circle_dist_text = Text(f"l={line_circle_dist.get_length():.2f}")
        line_circle_dist_text.move_to(line_circle_dist.get_center())
        line_circle_dist_text.shift(LEFT * 1)
        line_circle_dist_text.shift(UP * 1)

        self.play(Write(circle_staus_5_text1))
        self.play(Write(line_circle_dist))
        self.play(Write(line_circle_dist_text))
        self.wait()

        self.play(FadeOut(circle_staus_5_text1,shift=DOWN),FadeOut(line_circle_dist_text,shift=DOWN),FadeOut(line_circle_dist,shift=DOWN))

        animations_5 = [
            ApplyMethod(circle.shift, UP*1),
            ApplyMethod(circle_center.shift, UP*1),
            ApplyMethod(radius_dot.shift, UP*1),
            ApplyMethod(radius.shift, UP*1),
            ApplyMethod(circle_radius_text.shift, UP*1),
        ]
        group_animation_5 = AnimationGroup(*animations_5)
        self.play(group_animation_5) 

        circle_staus_6_text1 = Text("圆的状态：相离", font=".PingFang SC", color=BLUE, font_size=35)
        circle_staus_6_text1.move_to(circle_staus4_text2.get_center())

        self.play(Write(circle_staus_6_text1))
        self.wait()

        self.play(FadeOut(circle_staus_6_text1,shift=DOWN),FadeOut(circle_staus4_text1,shift=DOWN),FadeOut(circle),FadeOut(circle_center),FadeOut(radius_dot),FadeOut(radius),FadeOut(circle_radius_text),FadeOut(line))
        self.wait()

        #part_2
        part_2_text_1 = Text("不知道大家有没有发现", font=".PingFang SC", color=BLUE, font_size=35)
        part_2_text_1.shift(UP * 1)
        self.play(Write(part_2_text_1))

        part_2_text_2 = Text("其实我在每个动画里都添加了半径、圆心到直线的距离", font=".PingFang SC", color=BLUE, font_size=35)
        part_2_text_2.move_to(part_2_text_1.get_center())
        self.play(Write(part_2_text_2),part_2_text_1.animate.shift(UP * 0.5))

        part_2_text_3 = Text("让我们来回顾看看", font=".PingFang SC", color=BLUE, font_size=35)
        part_2_text_3.move_to(part_2_text_2.get_center())
        self.play(part_2_text_2.animate.shift(UP * 0.5),part_2_text_1.animate.shift(UP * 0.5))
        self.play(Write(part_2_text_3))

        self.wait()

        self.play(FadeOut(part_2_text_1,shift=DOWN),FadeOut(part_2_text_2,shift=DOWN))
        self.play(part_2_text_3.animate.shift(DOWN * 1))
        self.wait()

        self.play(FadeOut(part_2_text_3,shift=DOWN))

        #表格
        text1 = Text("圆的状态", font=".PingFang SC", color=WHITE, font_size=40)
        text2 = Text("l 圆心到直线距离", font=".PingFang SC", color=WHITE, font_size=40)
        text3 = Text("r 圆半径", font=".PingFang SC", color=WHITE, font_size=40)
        text4 = Text("l与r数量关系", font=".PingFang SC", color=WHITE, font_size=40)
        text5 = Text("相离", font=".PingFang SC", color=WHITE, font_size=40)
        text6 = Text("l=2", font=".PingFang SC", color=WHITE, font_size=40)
        text7 = Text("r=1", font=".PingFang SC", color=WHITE, font_size=40)
        text8 = Text("l>r", font=".PingFang SC", color=WHITE, font_size=40)
        text9 = Text("相切", font=".PingFang SC", color=WHITE, font_size=40)
        text10 = Text("l=1", font=".PingFang SC", color=WHITE, font_size=40)
        text11 = Text("r=1", font=".PingFang SC", color=WHITE, font_size=40)
        text12 = Text("l=r", font=".PingFang SC", color=WHITE, font_size=40)
        text13 = Text("相交", font=".PingFang SC", color=WHITE, font_size=40)
        text14 = Text("l=0", font=".PingFang SC", color=WHITE, font_size=40)
        text15 = Text("r=1", font=".PingFang SC", color=WHITE, font_size=40)
        text16 = Text("l<r", font=".PingFang SC", color=WHITE, font_size=40)

        text1.move_to([-5,3.5,0])
        text2.move_to([-2.5,3.5,0])
        text3.move_to([0.5,3.5,0])
        text4.move_to([3.5,3.5,0])

        text5.move_to([-5,2,0])
        text6.move_to([-2.5,2,0])
        text7.move_to([0.5,2,0])
        text8.move_to([3.5,2,0])

        text9.move_to([-5,0,0])
        text10.move_to([-2.5,0,0])
        text11.move_to([0.5,0,0])
        text12.move_to([3.5,0,0])

        text13.move_to([-5,-2,0])
        text14.move_to([-2.5,-2,0])
        text15.move_to([0.5,-2,0])
        text16.move_to([3.5,-2,0])

        self.play(Write(text1),Write(text2),Write(text3),Write(text4),Write(text5),Write(text6),Write(text7),Write(text8),Write(text9),Write(text10),Write(text11),Write(text12),Write(text13),Write(text14),Write(text15),Write(text16))

        animations_6 = [
            ApplyMethod(text1.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text2.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text3.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text4.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text5.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text6.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text7.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text8.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text9.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text10.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text11.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text12.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text13.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text14.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text15.shift, DOWN*0.5+RIGHT*0.5),
            ApplyMethod(text16.shift, DOWN*0.5+RIGHT*0.5),
        ]
        group_animation_6 = AnimationGroup(*animations_6)
        self.play(group_animation_6) 
        self.wait(5)
        self.play(FadeOut(text1,shift=DOWN),FadeOut(text2,shift=DOWN),FadeOut(text3,shift=DOWN),FadeOut(text4,shift=DOWN),FadeOut(text5,shift=DOWN),FadeOut(text6,shift=DOWN),FadeOut(text7,shift=DOWN),FadeOut(text8,shift=DOWN),FadeOut(text9,shift=DOWN),FadeOut(text10,shift=DOWN),FadeOut(text11,shift=DOWN),FadeOut(text12,shift=DOWN),FadeOut(text13,shift=DOWN),FadeOut(text14,shift=DOWN),FadeOut(text15,shift=DOWN),FadeOut(text16,shift=DOWN))

        text_last_1 = Text("这样，我们就能得出：", font=".PingFang SC", color=BLUE, font_size=35)
        text_last_2 = Text("一般地，", font=".PingFang SC", color=BLUE, font_size=40)
        text_last_3 = Text("当直线与圆有两个交点时，叫做直线与圆相交；", font=".PingFang SC", color=BLUE, font_size=35)
        text_last_4 = Text("当直线与圆有唯一公共点时，叫做直线与圆相切；", font=".PingFang SC", color=BLUE, font_size=35)
        text_last_5 = Text("当直线与圆没有公共点时，叫做直线与圆相离。", font=".PingFang SC", color=BLUE, font_size=35)

        text_last_1.move_to([0,1,0])

        text_last_2.move_to(text_last_1.get_center())
        text_last_2.shift(DOWN * 0.5)

        text_last_3.move_to(text_last_2.get_center())
        text_last_3.shift(DOWN * 0.5)

        text_last_4.move_to(text_last_3.get_center())
        text_last_4.shift(DOWN * 0.5)

        text_last_5.move_to(text_last_4.get_center())
        text_last_5.shift(DOWN * 0.5)

        self.play(Write(text_last_1))
        self.play(text_last_1.animate.shift(UP * 1),run_time=2)
        self.play(Write(text_last_2))

        self.play(Write(text_last_3),Write(text_last_4),Write(text_last_5),run_time=5)
        self.wait(5)

        self.play(FadeOut(text_last_1),FadeOut(text_last_2),FadeOut(text_last_3),FadeOut(text_last_4),FadeOut(text_last_5))

        text_last2_1 = Text("当然，直线与圆的位置关系还有以下定理：", font=".PingFang SC", color=WHITE, font_size=40)
        text_last2_2 = Text("如果⊙O半径为r,圆心O到直线l的距离为d，那么，", font=".PingFang SC", color=BLUE, font_size=35)
        text_last2_3 = Text("当d < r，直线l与 ⊙O 相交；", font=".PingFang SC", color=BLUE, font_size=35)
        text_last2_4 = Text("当d = r，直线l与 ⊙O 相切；", font=".PingFang SC", color=BLUE, font_size=35)
        text_last2_5 = Text("当d > r，直线l与 ⊙O 相离。", font=".PingFang SC", color=BLUE, font_size=35)

        text_last2_1.move_to(text_last_1.get_center())

        text_last2_2.move_to(text_last_2.get_center())

        text_last2_3.move_to(text_last_3.get_center())

        text_last2_4.move_to(text_last_4.get_center())

        text_last2_5.move_to(text_last_5.get_center())

        self.play(Write(text_last2_1))
        self.play(Write(text_last2_2))
        self.play(Write(text_last2_3),Write(text_last2_4),Write(text_last2_5),run_time=5)
        self.wait(5)

        self.play(FadeOut(text_last2_1),FadeOut(text_last2_2),FadeOut(text_last2_3),FadeOut(text_last2_4),FadeOut(text_last2_5))


        text_last_3_1 = Text("其实，我们也可以将这个圆想象成一个太阳", font=".PingFang SC", color=WHITE, font_size=40)
        text_last_3_2 = Text("那么我们就可以得到……", font=".PingFang SC", color=BLUE, font_size=35)

        text_last_3_3 = Text("戴上耳机，欣赏数学的美", font=".PingFang SC", color=GREY, font_size=20)
        text_last_3_1.shift(UP * 1)
        text_last_3_2.move_to(text_last_3_1.get_center())
        text_last_3_2.shift(DOWN * 0.5)
        text_Ending = Text("The End.", font=".PingFang SC", color=WHITE, font_size=50)
        text_last_3_3.move_to(text_last_3_2.get_center())
        text_last_3_3.shift(DOWN * 0.5)

        self.play(Write(text_last_3_1),Write(text_last_3_2))
        self.play(Write(text_last_3_3),FadeOut(text_last_3_1),FadeOut(text_last_3_2),text_last_3_3.animate.shift(UP * 2),run_time=4)
        self.play(FadeOut(text_last_3_3))

        line = Line([-6, 0, 0], [6, 0, 0])

        circle = Circle(radius=1, color=ORANGE) 

        circle.move_to([-1,-2,0])
        
        circle_center = Dot(circle.get_center(),radius=0.05)

        circle_radius_text = Text("r") 

        radius_dot = Dot(circle.point_from_proportion(2),radius=0.05)
        radius = DashedLine(start=circle_center,end=radius_dot)
        circle_radius_text.move_to(radius.get_center())
        circle_radius_text.shift(UP * 0.2)

        text__0 = Text("圆的状态：", font="PingFang SC Regular", color=BLUE, font_size=40)        
        text__1 = Text("圆的状态：相离", font="PingFang SC Regular", color=BLUE, font_size=40)
        text__2 = Text("圆的状态：相切", font="PingFang SC Regular", color=BLUE, font_size=40)
        text__3 = Text("圆的状态：相交", font="PingFang SC Regular", color=BLUE, font_size=40)

        text__0.move_to([4,-3,0])
        text__1.move_to([4,-3,0])
        text__2.move_to([4,-3,0])
        text__3.move_to([4,-3,0])

        self.play(Write(circle),Write(circle_center),Write(circle_radius_text),Write(radius),Write(radius_dot),Write(line),run_time=2)
        self.play(ReplacementTransform(text__0, text__1))
        self.wait()
        animations_1 = [
            ApplyMethod(circle.shift, RIGHT*1+UP*1),
            ApplyMethod(circle_center.shift, RIGHT*1+UP*1),
            ApplyMethod(radius_dot.shift, RIGHT*1+UP*1),
            ApplyMethod(radius.shift, RIGHT*1+UP*1),
            ApplyMethod(circle_radius_text.shift, RIGHT*1+UP*1),
        ]
        group_animation_1 = AnimationGroup(*animations_1)

        self.play(group_animation_1)
        self.play(ReplacementTransform(text__1, text__2))
        self.wait()

        animations_2 = [
            ApplyMethod(circle.shift, UP*1),
            ApplyMethod(circle_center.shift, UP*1),
            ApplyMethod(radius_dot.shift, UP*1),
            ApplyMethod(radius.shift, UP*1),
            ApplyMethod(circle_radius_text.shift, UP*1),
        ]
        group_animation_2 = AnimationGroup(*animations_2)

        self.play(group_animation_2,ReplacementTransform(text__2, text__3))
        self.wait()

        animations_3 = [
            ApplyMethod(circle.shift, UP*1+RIGHT*1),
            ApplyMethod(circle_center.shift, UP*1+RIGHT*1),
            ApplyMethod(radius_dot.shift, UP*1+RIGHT*1),
            ApplyMethod(radius.shift, UP*1+RIGHT*1),
            ApplyMethod(circle_radius_text.shift, UP*1+RIGHT*1),
        ]
        group_animation_3 = AnimationGroup(*animations_3)

        self.play(group_animation_3,ReplacementTransform(text__3, text__1))  
        self.wait()

        animations_4 = [
            ApplyMethod(circle.shift, UP*1+RIGHT*1),
            ApplyMethod(circle_center.shift, UP*1+RIGHT*1),
            ApplyMethod(radius_dot.shift, UP*1+RIGHT*1),
            ApplyMethod(radius.shift, UP*1+RIGHT*1),
            ApplyMethod(circle_radius_text.shift, UP*1+RIGHT*1),
        ]
        group_animation_4 = AnimationGroup(*animations_4)

        self.play(group_animation_4,ReplacementTransform(text__1, text__0))   
        self.wait()

        animations_5 = [
            ApplyMethod(circle.shift, UP*1),
            ApplyMethod(circle_center.shift, UP*1),
            ApplyMethod(radius_dot.shift, UP*1),
            ApplyMethod(radius.shift, UP*1),
            ApplyMethod(circle_radius_text.shift, UP*1),
        ]
        group_animation_5 = AnimationGroup(*animations_5)

        self.play(group_animation_5) 
        self.wait(5)
        
        self.play(FadeOut(circle),FadeOut(circle_center),FadeOut(circle_radius_text),FadeOut(radius),FadeOut(radius_dot),FadeOut(line),FadeOut(text__0),run_time=2)

        text_Ending_2 = Text("Created By 周锦辰", font=".PingFang SC", color=WHITE, font_size=50)

        self.play(Write(text_Ending),run_time=4)

        self.wait(2)
        self.play(text_Ending.animate.shift(UP*1),Write(text_Ending_2))

        self.wait(5)

        self.wait(10)