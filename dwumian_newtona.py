from manim import *



class PodzbioryZbioruPrzyklad(Scene):
    def construct(self):
        zbior = MathTex(r"\{a,b,c\}")
        podzbiory = MathTex(r"\{\emptyset,\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\},\{a,b,c\}\}")

        podzbiory.next_to(zbior, DOWN)

        self.play(Write(zbior))
        self.wait()
        self.play(zbior.animate.shift(2 * UP))
        self.wait()
        self.play(Write(podzbiory))

        liczba_elementow = MathTex(r"3")
        liczba_podzbiorow = MathTex(r"8")

        ramka_zbior = SurroundingRectangle(zbior, buff=0.1)
        ramka_podzbiory = SurroundingRectangle(podzbiory, buff=0.1)

        liczba_elementow.next_to(zbior, 2 * RIGHT).set_color(YELLOW).scale(1.5)
        liczba_podzbiorow.next_to(podzbiory, 2 * RIGHT).set_color(YELLOW).scale(1.5)

        self.wait()
        self.play(Create(ramka_zbior))
        self.play(Write(liczba_elementow))
        self.wait()
        self.play(Create(ramka_podzbiory))
        self.play(Write(liczba_podzbiorow)) 
        


class PodzbioryZbioruPrzejscieDoWiekszego(Scene):
    def construct(self):
        zbior = MathTex(r"\{1,2,3,4,\ldots,n\}")
        podzbiory = [
            MathTex("\{", "\emptyset", "\}"),
            MathTex("\{", "1", "\}"),
            MathTex(r"\{", "1", ",", "2", ",", "3", "\}"),
            MathTex(r"\vdots"),
            MathTex(r"\{", "1", ",", "2", ",", "3", ",", "4", ",", "\ldots", ",", "n", "\}"),
        ]
        
        self.play(Write(zbior))
        self.play(zbior.animate.shift(4 * LEFT))

        self.wyswietl_podzbiory(podzbiory, pozycja_poczatkowa=4 * RIGHT + 1.5 * UP)

        zbior2 = MathTex(r"\{", "1", ",", "2", ",", "3", ",", "4", ",", "\ldots", ",", "n", ",", "n+1", "\}").shift(4 * LEFT)
        # todo: TransformMatchingTex
        self.play(Transform(zbior, zbior2))

    def wyswietl_podzbiory(self, podzbiory, pozycja_poczatkowa):
        podzbiory[0].shift(pozycja_poczatkowa)
        self.play(Write(podzbiory[0]))

        for poprzedni_podzbior, podzbior in zip(podzbiory, podzbiory[1:]):
            podzbior.next_to(poprzedni_podzbior, DOWN)
            self.play(Write(podzbior))


