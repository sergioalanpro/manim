from manim import *


class IntroTexto(Scene):
    def construct(self):
        monodtext = Text("Ecuacion de monod")
        self.play(Write(monodtext))
        self.wait(1)
        equationtext = MathTex("\\mu=\\mu_{\max } \\frac{[S]}{K_s+[S]}")
        self.play(Transform(monodtext, equationtext))
        self.play(monodtext.animate.to_edge(UP)) 
        paratext = Text("Parametros a modificar para ver el comportamiento").scale(0.5)
        paratext.shift(UP*0.8)
        self.play(Write(paratext))
        kstext = MathTex("\mu").scale(1.5)
        kstext.shift(RIGHT)
        kstext.set_color(YELLOW)
        mtext = MathTex("K_s").scale(1.5)
        mtext.shift(LEFT)
        mtext.set_color(YELLOW)
        self.play(Write(mtext))
        self.play(Write(kstext))
        self.wait(1)
        self.play(FadeOut(mtext, kstext, paratext, monodtext))
    
    
        self.plot_ks_variation(with_fade_in=True)
        self.wait(1)
        self.fade_out_all()
    
        self.plot_mu_max_variation(with_fade_in=True)
        self.wait(1)
        self.fade_out_all()

        #Texto final
        gracias = Text("@mathbioscience")
        self.play(Write(gracias))
        self.wait(3)

    def plot_ks_variation(self, with_fade_in=False):  
        ks_text = MathTex("Parametro \\ K_s")
        ks_text.set_color(YELLOW)
        ks_text.shift(UP*2.5)
        ks_text.scale(0.8)
        self.play(Write(ks_text))
     
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(
            x_label="S \\ (Concentracion \\ de \\ sustrato)",
            y_label="\mu \\ (Velocidad \\ de \\ crecimiento)"
        )
        
        mu_max = 1
        K_s_values = [0.1, 0.5, 1.0]
        colors = [BLUE, GREEN, RED]
        legends = [MathTex(f"K_s = {ks}", font_size=35) for ks in K_s_values]

        def monod(S, K_s):
            return mu_max * S / (K_s + S)

        t = ValueTracker(0)
        graphs, dots, legend_texts = [], [], []

        for i, K_s in enumerate(K_s_values):
            graph = ax.plot(lambda S: monod(S, K_s), color=colors[i], x_range=[0, 10])
            graphs.append(graph)
    
            dot = Dot(ax.c2p(0, monod(0, K_s)), color=colors[i])
            dot.add_updater(lambda d, K_s=K_s: d.move_to(ax.c2p(t.get_value(), monod(t.get_value(), K_s))))
            dots.append(dot)
    
            legend = legends[i].set_color(colors[i])
            legend_texts.append(legend)


        legend_group = VGroup(*legend_texts).arrange(DOWN, aligned_edge=LEFT).to_corner(UR, buff=0.5)

        if with_fade_in: 
            self.play(FadeIn(ax, labels, *graphs, *dots, legend_group))
        else:
            self.add(ax, labels, *graphs, *dots, legend_group)

        self.play(t.animate.set_value(10), run_time=5, rate_func=linear)
        #self.wait(1)
        
        self.play(FadeOut(ks_text))

    def plot_mu_max_variation(self, with_fade_in=False):
    
        mumax_text = MathTex("Parametro \\ \mu_{max}")
        mumax_text.set_color(YELLOW)
        mumax_text.scale(0.85)
        mumax_text.shift(UP*2.5)
        self.play(Write(mumax_text))
        
    
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(
            x_label="S \\ (Concentracion \\ de \\ sustrato)",
            y_label="\mu \\ (Velocidad \\ de \\ crecimiento)"
        )
     
        K_s = 0.5
        mu_max_values = [0.2, 0.5, 1]
        colors = [BLUE, GREEN, RED]
        legends = [MathTex(f"\\mu_{{\\max}} = {mu}", font_size=35) for mu in mu_max_values]  

      
        def monod(S, mu_max, K_s):
            return mu_max * S / (K_s + S)
      
        t = ValueTracker(0)
        graphs, dots, legend_texts = [], [], []

        for i, mu_max in enumerate(mu_max_values):
   
            graph = ax.plot(lambda S: monod(S, mu_max, K_s), color=colors[i], x_range=[0, 10])
            graphs.append(graph)

   
            dot = Dot(ax.c2p(0, monod(0, mu_max, K_s)), color=colors[i])
            dot.add_updater(lambda d, mu_max=mu_max: d.move_to(ax.c2p(t.get_value(), monod(t.get_value(), mu_max, K_s))))
            dots.append(dot)

          
            legend = legends[i].set_color(colors[i])
            legend_texts.append(legend)

    
        legend_group = VGroup(*legend_texts).arrange(DOWN, aligned_edge=LEFT).to_corner(UR, buff=0.5)

        if with_fade_in:
            self.play(FadeIn(ax, labels, *graphs, *dots, legend_group))
        else:
            self.add(ax, labels, *graphs, *dots, legend_group)

        self.play(t.animate.set_value(10), run_time=5, rate_func=linear)
        #self.wait(1)
      
        self.play(FadeOut(mumax_text))

    def fade_out_all(self):
        """Desvanece todos los elementos de la escena."""
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])