import graphics as gr

window = gr.GraphWin('Russian game', 300, 300)

def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    gr.Line(gr.Point(*A))

my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))
my_rectangle.draw(window)
