from flask import Flask, render_template, request
import os
from superres.utils import load_image, save_image, upsample_nearest
from superres.operators import DegradationOperator
from superres.regularizers import L2Regularizer, HuberRegularizer
from superres.gd import GradientDescentSR

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/superresolution", methods=["POST"])
def superresolution():
    file = request.files["image"]
    path = "static/results/input.png"
    file.save(path)

    b = load_image(path)

    reg_type = request.form["regularizer"]
    lam = float(request.form["lambda"])
    delta = float(request.form["delta"])
    lr = float(request.form["lr"])
    iters = int(request.form["iters"])
    s = int(request.form["s"])

    op = DegradationOperator(sigma=1, s=s)

    if reg_type == "l2":
        reg = L2Regularizer()
    else:
        reg = HuberRegularizer(delta)

    x0 = upsample_nearest(b, s)

    solver = GradientDescentSR(op.A, op.AT, reg, lr, lam, iters)
    x_final, _ = solver.solve(b, x0)

    out_path = "static/results/result.png"
    save_image(x_final, out_path)

    return render_template(
        "result.html",
        input_path=path,
        output_path=out_path,
        params=request.form
    )

if __name__ == "__main__":
    app.run(debug=True)
