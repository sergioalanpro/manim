from manim import *

class ConfiguracionElectronicaCloro(Scene):
    def construct(self):

        titulo = Text("Configuración Electrónica del Cloro").scale(0.8).to_edge(UP)
        self.play(Write(titulo))

        config_electro = MathTex(
            "1s^2", ", ", "2s^2", ", ", "2p^6", ", ", "3s^2", ", ", "3p^5"
        ).scale(0.8).next_to(titulo, DOWN, buff=1)
        self.play(Write(config_electro))
        self.wait(1)

    
        subniveles = [
            ("1s", 2),
            ("2s", 2),
            ("2p", 6),
            ("3s", 2),
            ("3p", 5)
        ]

        orbitales = VGroup()
        for i, (label, electrones) in enumerate(subniveles):
            grupo = VGroup()

            etiqueta = Text(label).scale(0.5)  
            grupo.add(etiqueta)

            #orbitales
            for e in range(electrones):
                espin = Arrow(
                    start=UP if e % 2 == 0 else DOWN,
                    end=ORIGIN,
                    buff=0,
                    color=WHITE if e % 2 == 0 else WHITE
                ).scale(0.3)  # Flechas más pequeñas
                espin.next_to(etiqueta, RIGHT, buff=0.15 + 0.15 * (e // 2))
                grupo.add(espin)

            grupo.arrange(RIGHT, buff=0.4)
            grupo.shift(DOWN * (i + 0.5)) 
            orbitales.add(grupo)

        orbitales.move_to(ORIGIN).scale(0.8)  
        self.play(config_electro.animate.shift(UP))
        self.play(Write(orbitales))
        self.wait(2)


        self.play(FadeOut(titulo,config_electro))
        self.play(orbitales.animate.scale(0.85).to_edge(LEFT))


        #####################################LAS ANIM


        # nucleo
        nucleo = Circle(radius=0.5, color=GRAY).set_fill(GRAY_BROWN, opacity=0.5)
        protones = MathTex("Z = 17").scale(0.6).move_to(nucleo.get_center())
        #neutrones = MathTex("18n").scale(0.6).next_to(protones, DOWN, buff=0.1)
        

        # niveles de energia
        def agregar_nivel(radio, color, electrones):
            nivel = Circle(radius=radio, color=color) 
            nivel_electrones = VGroup()

            for j in range(electrones):
                angulo = j * TAU / electrones
                electron = Dot(radius=0.1, color=WHITE).move_to(
                    nivel.point_at_angle(angulo)
                )
                nivel_electrones.add(electron)

            self.play(Create(nivel), FadeIn(nivel_electrones))
            return VGroup(nivel, nivel_electrones)
        

        modelo_titulo = Text("Modelo Atómico").scale(0.8).to_edge(UP)
        self.play(Write(modelo_titulo))

        self.play(FadeIn(nucleo), Write(protones))


        nivel_1 = VGroup(orbitales[0], orbitales[0])  
        framebox1 = SurroundingRectangle(nivel_1, buff=0.1).set_color(RED)  
        self.play(Create(framebox1))
        #self.wait(2)

        agregar_nivel(1, RED, 2)   
        self.wait(2)

    
        nivel_2 = VGroup(orbitales[1], orbitales[2])  
        framebox2 = SurroundingRectangle(nivel_2, buff=0.1).set_color(PINK)  
        self.play(Create(framebox2))
        #self.wait(2)

        agregar_nivel(2, PINK, 8) 
        self.wait(2)

        nivel_3 = VGroup(orbitales[3], orbitales[4])  
        framebox3 = SurroundingRectangle(nivel_3, buff=0.1).set_color(GREEN)  
        self.play(Create(framebox3))
        #self.wait(2)

        agregar_nivel(3, GREEN, 7)
        self.wait(3)

        #self.play(FadeOut(nucleo, protones, neutrones, modelo_titulo))

        self.fade_out_all()


        final_text = Text("@mathbioscience").scale(0.8)
        self.play(Write(final_text))
        self.wait(2)


    def fade_out_all(self):
        """Desvanece todos los elementos de la escena."""
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])
