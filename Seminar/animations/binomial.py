from manim import *
import numpy as np

from binomial_config import Config


class Binomial(Scene):
    def shuffle_set(self, set):
        random_permutation = np.random.permutation(len(set) - 1)
        for i in range(len(set) - 1):
            set[i + 1].target.move_to(set[random_permutation[i] + 1])

    def construct(self):
        # tex template stuff
        tex_template = TexTemplate()
        tex_template.add_to_preamble(
            r"\usepackage[czech,english]{babel}", True)
        tex_template.add_to_preamble(r"\usepackage{mathtools}")

        self.next_section("Intro Text", skip_animations=True)

        intro_text = MathTex(
            "U_k(", "X", ")", r"\coloneqq", r"\#", r"\{", "(", "x_1", ",",
            "x_2", ",", "x_3", ")", r"\in", "X", r"^3", r"\mid", "x_1", ",",
            "x_2", ",", "x_3", r"\text{ navzájem různé}", r"\}",
            substrings_to_isolate=["X", "x_1", "x_2", "x_3"],
            tex_to_color_map={
                "X": Config.Color.X_COLOR,
                "x_1": Config.Color.K_TUPLE_COLOR,
                "x_2": Config.Color.K_TUPLE_COLOR,
                "x_3": Config.Color.K_TUPLE_COLOR
            },
            tex_template=tex_template
        )
        self.play(Write(intro_text))

        self.wait(2)
        self.next_section("Creating the set X...", skip_animations=True)

        # random elements trackers
        elem_labels = [intro_text[7], intro_text[9], intro_text[11]]
        for label in elem_labels:
            label.save_state()

        # the set X
        X = VGroup(
            MathTex("X", color=Config.Color.X_COLOR),
            *[
                Dot(color=Config.Color.X_COLOR) for _ in range(6)
            ]
        ).arrange(DOWN, buff=0.75).shift(3 * RIGHT)

        # choose random 3 elements from X
        random_permutation = np.random.permutation(6)
        chosen_elements = VGroup(*[
            X[random_permutation[i] + 1]
            for i in range(3)
        ])

        # animating it all together
        text_anim = AnimationGroup(
            *[FadeOut(intro_text[i]) for i in range(len(intro_text))
              if i not in [7, 9, 11]]
        )
        dots_anim = AnimationGroup(*list(map(DrawBorderThenFill, X[1:])))
        self.play(AnimationGroup(
            text_anim,
            dots_anim,
            Write(X[0]),
            lag_ratio=0.4
        ))

        # move x_1, x_2, x_3 to the chosen elements
        self.play(*[
            elem_labels[i].animate.next_to(chosen_elements[i], RIGHT)
            for i in range(3)
        ], *[
            chosen_elements[i].animate.set_color(Config.Color.K_TUPLE_COLOR)
            for i in range(3)
        ])

        # add updaters to the labels
        for i in range(3):
            elem_labels[i].add_updater(
                lambda m, i=i: m.next_to(chosen_elements[i], RIGHT)
            )

        self.next_section("Creating a set of 3 elements...",
                          skip_animations=True)

        A = VGroup(
            Tex(r"$A$", color=Config.Color.A_COLOR),
            *[Dot(color=Config.Color.A_COLOR) for _ in range(3)]
        ).arrange(DOWN, buff=0.75).shift(3 * LEFT).align_to(X, UP)

        A_labels = VGroup(*[
            Tex(rf"${i + 1}$",
                color=Config.Color.A_COLOR).next_to(A[i + 1], LEFT)
            for i in range(3)
        ])

        labels_anim = AnimationGroup(*[Write(A_labels[i]) for i in range(3)])
        dots_anim = AnimationGroup(*list(map(DrawBorderThenFill, A[1:])))
        self.play(AnimationGroup(
            dots_anim,
            AnimationGroup(Write(A[0]), labels_anim),
            lag_ratio=0.4
        ))

        self.next_section("Creating arrows A -> X...", skip_animations=True)
        arrows = VGroup(*[
            Arrow(start=A[i + 1].get_center(),
                  end=chosen_elements[i].get_center(),
                  color=Config.Color.ARROW_COLOR,
                  tip_length=0.25,
                  stroke_width=3)
            for i in range(3)
        ])

        self.play(*list(map(GrowArrow, arrows)))

        # add updaters to the arrows
        for i in range(3):
            arrows[i].add_updater(
                lambda ar, i=i: ar.become(
                    Arrow(start=A[i + 1].get_center(),
                          end=chosen_elements[i].get_center(),
                          color=Config.Color.ARROW_COLOR,
                          tip_length=0.25,
                          stroke_width=3
                          )
                )
            )
        self.wait(2)

        self.next_section("Randomly permuting X...", skip_animations=False)

        # generate targets for elements of X to shuffle to
        for element in X[1:]:
            element.generate_target()

        # shuffle the elements of X repeatedly
        for _ in range(5):
            self.shuffle_set(X)

            # animate the shuffle
            self.play(*list(map(MoveToTarget, X[1:])))
            self.wait(1)

        self.wait(2)
