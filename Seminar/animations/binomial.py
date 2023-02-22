from manim import *
import numpy as np
from itertools import permutations

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
            r"\usepackage[utf8]{inputenc}", True)
        tex_template.add_to_preamble(
            r"\usepackage[T1]{fontenc}", True)
        tex_template.add_to_preamble(
            r"\usepackage[czech,english]{babel}", True)
        tex_template.add_to_preamble(r"\usepackage{mathtools}")

        self.next_section("Intro Text", skip_animations=False)

        intro_text = MathTex(
            "U_3(", "X", ")", r"\coloneqq", r"\#", r"\{", "(", "x_1", ",",
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
        self.next_section("Creating the set X...", skip_animations=False)

        # random elements trackers
        elem_labels = VGroup(*[intro_text[7], intro_text[9], intro_text[11]])
        elem_labels.save_state()

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
                          skip_animations=False)

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

        self.next_section("Creating arrows A -> X...", skip_animations=False)
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
        for _ in range(3):
            self.shuffle_set(X)

            # animate the shuffle
            self.play(*list(map(MoveToTarget, X[1:])))
            self.wait(2)

        self.next_section("Calculating U_3(X)...", skip_animations=False)

        # returning intro text to its original state and fading out A, X
        arrows.clear_updaters()
        elem_labels.clear_updaters()
        self.play(
            *[FadeOut(mob) for mob in [A, X, arrows, A_labels]],
            Restore(elem_labels),
            *[FadeIn(intro_text[i]) for i in range(len(intro_text))
              if i not in [7, 9, 11]]
        )

        # text about injective funcs
        injective_text = MathTex(
            r"= \text{počet prostých funkcí } \{1, 2, 3\} \to", "X",
            substrings_to_isolate="X",
            tex_to_color_map={
                "X": Config.Color.X_COLOR
            },
            tex_template=tex_template
        ).next_to(intro_text, DOWN, buff=0.5).align_to(intro_text[3], LEFT)

        self.play(Write(injective_text))

        intro_text.add(injective_text)

        # text calculating injective funcs
        calc_text = MathTex(
            r"= \prod_{i=0}^{3 - 1} \#", "X", " - i.",
            substrings_to_isolate="X",
            tex_to_color_map={
                "X": Config.Color.X_COLOR
            },
            tex_template=tex_template
        ).next_to(intro_text, DOWN, buff=0.5).align_to(intro_text[3], LEFT)

        self.wait(1)

        self.play(Write(calc_text))

        intro_text.add(calc_text)

        self.wait(2)

        self.next_section("Choosing k elements from X", skip_animations=False)
        # fading everything out
        self.play(FadeOut(intro_text))

        # create X as a rectangular grid
        X = VGroup(
            MathTex("X", color=Config.Color.X_COLOR_ENDGAME),
            Rectangle(color=Config.Color.X_COLOR_ENDGAME,
                      fill_opacity=0, width=6, height=1),
        ).arrange(DOWN).shift(2 * UP)

        X_bars = VGroup(*[Line(
            start=X[1].get_corner(UP + LEFT) + (i + 1) * RIGHT,
            end=X[1].get_corner(DOWN + LEFT) + (i + 1) * RIGHT,
            color=Config.Color.X_COLOR_ENDGAME,
            stroke_width=3)
            for i in range(5)
        ])

        self.play(Write(X[0]), Create(X[1]), Create(X_bars))

        self.wait(1)

        # create rects for three random elements from X
        random_permutation = np.random.permutation(6)
        rectangles = VGroup(*[
            Rectangle(
                fill_color=Config.Color.RECT_COLORS[i], height=1, width=1,
                stroke_opacity=0, fill_opacity=0.5).align_to(
                    X[1].get_corner(UP + LEFT), UP + LEFT)
            .shift(random_permutation[i] * RIGHT)
            for i in range(3)
        ])
        self.play(FadeIn(rectangles))

        self.wait(1)
        self.next_section("Permutations of rects...", skip_animations=False)

        all_rects = VGroup()
        # first perm
        rectangles.generate_target()
        rectangles.target.arrange(RIGHT, buff=0.15).move_to(
            DOWN + 4 * LEFT).set_fill(opacity=1)

        self.play(MoveToTarget(rectangles), run_time=1)
        all_rects.add(rectangles)

        # other perms
        perms = list(permutations([0, 1, 2]))
        for j, perm in enumerate(perms[1:]):
            new_rects = rectangles.copy()
            new_rects.move_to(all_rects[-1].get_center())
            new_rects.set_fill(opacity=0)
            for i in range(3):
                new_rects[i].generate_target()
                new_rects[i].target.move_to(
                    new_rects[perm[i]]).set_fill(opacity=1)
                if j != 2:
                    new_rects[i].target.shift(4 * RIGHT)
                else:
                    new_rects[i].target.shift(8 * LEFT + 2 * DOWN)
            all_rects.add(new_rects)

            self.play(*list(map(MoveToTarget, new_rects)), run_time=1)
            self.wait(0.5)

        self.next_section("Counting perms...", skip_animations=False)
        self.play(X.animate.shift(1.5 * DOWN), all_rects.animate.shift(
            0.5 * DOWN), X_bars.animate.shift(1.5 * DOWN))
        final_text = MathTex(
            "U_3(", "X", ") = ", r"{\#", "X", r"\choose 3}"
        ).shift(3 * UP)
        final_text_addendum = MathTex(
            r"\; \cdot \; 3!"
        ).next_to(final_text, RIGHT, buff=0.2)

        self.play(Write(final_text))
        self.wait(1)
        self.play(Write(final_text_addendum))

        self.wait(2)
