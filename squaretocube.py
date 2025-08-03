from manim import *

class MetrosAMetrosCubicos(ThreeDScene):
    def construct(self):
        lineam1 = Line(start=LEFT, end=RIGHT).scale(1)
        self.play(Create(lineam1))

        label1 = MathTex("m").next_to(lineam1, DOWN).scale(1)
        #self.play(Write(label1))
        
        disttext = Text("Distancia").shift(LEFT*3.75, UP*3).scale(0.5)
        #self.play(Write(disttext))
        metros = MathTex("Metros").next_to(disttext, DOWN).scale(0.5)
        centimetros = MathTex("Centimetros").next_to(metros, DOWN).scale(0.5)
        kilom = MathTex("Kilometros").next_to(centimetros, DOWN).scale(0.5)
        milimetros = MathTex("Milimetros").next_to(kilom, DOWN).scale(0.5)

        self.play(Write(label1), Write(disttext))
        self.wait(1)
        self.play(Write(metros), Write(centimetros), Write(kilom), Write(milimetros))
        self.wait(2)

    
        lineam2 = Line(start=lineam1.get_end(), end=lineam1.get_end()+UP*2).scale(1)
        label2 = MathTex("m").next_to(lineam2)
        self.play(Create(lineam2))
        self.play(Write(label2))

        self.wait(1)


        op1 = label1.copy()
        op2 = label2.copy()

        self.play(op1.animate.move_to(lineam1.get_center() + UP + LEFT*0.5).scale(0.5))
        x = MathTex(r"\times").next_to(op1).scale(0.6)
        self.play(Write(x))
        self.play(op2.animate.next_to((x)).scale(0.5))
        self.wait(1)

        expr1 = VGroup(op1,x,op2)

        area = Text("Area").set_color(YELLOW).next_to(milimetros, DOWN).scale(0.5)

        #self.play(Write(area))

        area_label = MathTex("m^2").move_to(lineam1.get_center() + UP)
        self.play(Write(area), Transform(expr1, area_label))
        self.wait(2)
        
        lineam3 = Line(start=lineam2.get_end(), end=lineam2.get_end()+LEFT*2).scale(1)
        lineam4 = Line(start=lineam1.get_start(), end=lineam3.get_end())

        self.play(Create(lineam3), Create(lineam4))
        
        # Crear el cuadrado con relleno
        cuadrado = Polygon(
            lineam1.get_start(), lineam1.get_end(), 
            lineam2.get_end(), lineam3.get_end()
        )
        cuadrado.set_fill(YELLOW, opacity=0.3)
        self.play(FadeIn(cuadrado))

        metroscopy = metros.copy().next_to(area, DOWN)
        centimetroscopy = centimetros.copy().next_to(metroscopy, DOWN)
        kilomscopy = kilom.copy().next_to(centimetroscopy, DOWN)
        milimetroscopy = milimetros.copy().next_to(kilomscopy, DOWN)

        metroscopy.move_to(area.get_center() + DOWN*0.5).set_color(YELLOW_A)
        centimetroscopy.move_to(metroscopy.get_center() + DOWN*0.5).set_color(YELLOW_A)
        kilomscopy.move_to(centimetroscopy.get_center() + DOWN*0.5).set_color(YELLOW_A)
        milimetroscopy.move_to(kilomscopy.get_center() + DOWN*0.5).set_color(YELLOW_A)


        self.play(
            Transform(metros.copy(), metroscopy),
            Transform(centimetros.copy(), centimetroscopy),
            Transform(kilom.copy(), kilomscopy),
            Transform(milimetros.copy(), milimetroscopy)
        )
        #self.wait(1)

        m2 = MathTex("^2").next_to(metroscopy).shift(LEFT*0.2, UP*0.1).scale(0.5).set_color(YELLOW)
        c2 = MathTex("^2").next_to(centimetroscopy).shift(LEFT*0.2, UP*0.1).scale(0.5).set_color(YELLOW)
        k2 = MathTex("^2").next_to(kilomscopy).shift(LEFT*0.2, UP*0.1).scale(0.5).set_color(YELLOW)
        m12 = MathTex("^2").next_to(milimetroscopy).shift(LEFT* 0.2, UP*0.1).scale(0.5).set_color(YELLOW)
        self.play(Write(m2), Write(c2), Write(k2), Write(m12))



        # Mover la camara
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=3)
        
        profundidad = 1.5 * OUT
        
        lineam5 = Line(lineam1.get_start(), lineam1.get_start() + profundidad)
        lineam6 = Line(lineam1.get_end(), lineam1.get_end() + profundidad)
        lineam7 = Line(lineam3.get_end(), lineam3.get_end() + profundidad)
        lineam8 = Line(lineam2.get_end(), lineam2.get_end() + profundidad)

        self.play(Create(lineam8))
      
        label3 = MathTex("m").scale(0.8)
        self.add_fixed_in_frame_mobjects(label3)
        label3.move_to(lineam8.get_end() + RIGHT * 0.5 + DOWN * 0.3)
        self.play(Write(label3))
        
    
        mult_sign = MathTex(r"\times").scale(0.6).next_to(label3, RIGHT, buff=0.1)
        self.add_fixed_in_frame_mobjects(mult_sign)
        #mult_sign.next_to(label3, RIGHT, buff=0.1)
        self.play(Write(mult_sign))
        
    
        area_label_copy = area_label.copy()

        self.play(
            area_label_copy.animate
            .next_to(mult_sign, RIGHT, buff=0.2)
        )
        
  
        expression_group = VGroup(label3, mult_sign, area_label_copy)
        

        final_expr = MathTex("m^3").scale(0.8).move_to(expression_group.get_center())
        final_expr.rotate(PI/2, axis=RIGHT)
        final_expr.rotate(-PI/4, axis=UP)


        self.play(
            ReplacementTransform(expression_group, final_expr)
            )
        
    
        #self.play(
        #    final_expr.animate.move_to(lineam8.get_end() + 0.5 * OUT + RIGHT * 0.5)
        #)
        
        self.play(Create(lineam5), Create(lineam6), Create(lineam7))


        lineac1 = Line(lineam8.get_end(), lineam7.get_end())
        lineac2 = Line(lineam7.get_end(), lineam5.get_end())
        lineac3 = Line(lineam5.get_end(), lineam6.get_end())
        lineac4 = Line(lineam6.get_end(), lineam8.get_end())
        self.play(Create(lineac1), Create(lineac2), Create(lineac3), Create(lineac4))


   
        cara_frontal = cuadrado.copy()
        cara_superior = Polygon(
            lineam2.get_end(), lineam3.get_end(), 
            lineam7.get_end(), lineam8.get_end()
        ).set_fill(BLUE, opacity=0.5)
        cara_lateral = Polygon(
            lineam1.get_end(), lineam2.get_end(), 
            lineam8.get_end(), lineam6.get_end()
        ).set_fill(BLUE, opacity=0.5)
        cara_fondo = Polygon(
            lineam5.get_end(), lineam6.get_end(),
            lineam8.get_end(), lineam7.get_end()
        ).set_fill(BLUE, opacity=0.5)
        cara_inferior = Polygon(
            lineam6.get_end(), lineam5.get_end(),
            lineam1.get_start(), lineam1.get_end()
            ).set_fill(BLUE, opacity=0.5)
        
        
        self.play(FadeIn(cara_superior), FadeIn(cara_lateral), FadeIn(cara_fondo), FadeIn(cara_inferior), FadeIn(cara_frontal))
        
        self.wait(2)
