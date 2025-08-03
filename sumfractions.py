from manim import *

class Sf(Scene):
    def construct(self):
        
        text = Text("Suma de Fracciones")
       
        self.play(Write(text))  
        
        self.play(text.animate.to_edge(UP))
        self.wait(1)

        
        frac = MathTex(r"\frac{a}{b}", "+" , r"\frac{c}{d}" , "=", r"\frac{ad + bc}{bd}")
        self.play(Write(frac[:3]))
        self.wait(1)

       
        a_part = frac[0][0] 
        framebox_a = SurroundingRectangle(a_part, buff=0.1).set_color(RED)
        self.play(a_part.animate.set_color(RED))
        self.play(Create(framebox_a))
       
        d_part = frac[2][2]  
        framebox_d = SurroundingRectangle(d_part, buff=0.1).set_color(RED)
        self.play(d_part.animate.set_color(RED))
        self.play(Create(framebox_d))
        
        # AD
        a_position = frac[0][0].get_center()
        d_position = frac[2][2].get_center()
        line_ad = Line(a_position, d_position, color=YELLOW)
        self.play(Create(line_ad))
        self.play(Write(frac[3:])) 
        ad_part = frac[4][:2]  
        ad_postion = ad_part.get_center()
        line_ad2 = Line(d_position, ad_postion, color=YELLOW)
        self.play(Create(line_ad2))
        self.play(ad_part.animate.set_color(RED))
        framebox_ad = SurroundingRectangle(ad_part, buff=0.1).set_color(RED)
        self.play(Create(framebox_ad))
        self.wait(1)
        self.play(FadeOut(framebox_a), FadeOut(framebox_d), FadeOut(framebox_ad), FadeOut(line_ad), FadeOut(line_ad2))

        #BC
        b_part = frac[0][2] 
        framebox_b = SurroundingRectangle(b_part, buff=0.1).set_color(BLUE)
        self.play(b_part.animate.set_color(BLUE))
        self.play(Create(framebox_b))
        c_part = frac[2][0]  
        framebox_c = SurroundingRectangle(c_part, buff=0.1).set_color(BLUE)
        self.play(c_part.animate.set_color(BLUE))
        self.play(Create(framebox_c))
        b_position = b_part.get_center()
        c_position = c_part.get_center()
        line_bc = Line(b_position, c_position, color=YELLOW)
        self.play(Create(line_bc))  
        bc_part = frac[4][3:5]
        bc_postion = bc_part.get_center()
        line_cbc = Line(c_position, bc_postion, color=YELLOW)
        self.play(Create(line_cbc))
        self.play(bc_part.animate.set_color(BLUE))
        framebox_bc = SurroundingRectangle(bc_part, buff=0.1).set_color(BLUE)
        self.play(Create(framebox_bc))
        self.wait(1)
        self.play(FadeOut(framebox_b), FadeOut(framebox_c), FadeOut(framebox_bc), FadeOut(line_bc), FadeOut(line_cbc))

        #BD
        framebox_b = SurroundingRectangle(b_part, buff=0.1).set_color(GREEN)
        self.play(b_part.animate.set_color(GREEN))
        self.play(Create(framebox_b))
        framebox_d = SurroundingRectangle(d_part, buff=0.1).set_color(GREEN)
        self.play(d_part.animate.set_color(GREEN))
        self.play(Create(framebox_d))
        line_bd = Line(b_position, d_position, color=YELLOW)
        self.play(Create(line_bd))
        bd_position = frac[4][6].get_center()
        line_dbd = Line(d_position, bd_position, color=YELLOW)
        self.play(Create(line_dbd))    
        framebox_bd = SurroundingRectangle(frac[4][6:], buff=0.1).set_color(GREEN)
        self.play(frac[4][6:].animate.set_color(GREEN))
        self.play(Create(framebox_bd))
        self.wait(1)

        self.play(FadeOut(framebox_b), FadeOut(framebox_d), FadeOut(framebox_bd), FadeOut(line_bd), FadeOut(line_dbd))
        self.wait(2)




        





        
        
