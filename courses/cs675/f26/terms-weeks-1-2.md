# CS 675 · Weeks 1–2 · Terms and notions to go over

Instructor checklist for a live session with section 1B1, covering Modules 1–3 of the
[Machine Learning notes](https://ikoutis.github.io/mlnotes/). Week 1 carries Modules 1 and 2;
Week 2 carries Module 3. Section numbers point into the notes. Terms in **bold** are the ones a
student should be able to define in a sentence; the indented lines say what to say about them.

Interactive companions for the session: [The loss landscape](loss-landscape.html) and
[A batch stands in for the data](batches.html).

---

## Module 1 — Introduction to Machine Learning

- **Supervised learning** (§1.2) — data comes with labels; the task is to predict the label of a new point.
  - **Classification** — the label is categorical (a colour, a species). **Regression** — the label is a number.
    The only difference is *what kind of thing* is predicted.
- **Data as points** (§1.3) — every object is a vector of numbers; the number of coordinates is the **dimension** *d*.
  - Iris: 150 points, 4 dimensions, 3 classes. A 28×28 image: one point in 784 dimensions.
  - Most data cannot be drawn; linear algebra is the language that handles any *d* the same way.
- **Notation** (§1.4) — point *i* is the row vector *x*⁽ⁱ⁾; the **data matrix** *X* is *n* × *d* (one row per point,
  one column per **attribute / feature**); the **label vector** *y* has one entry per point.
- **Hypothesis / model** — a candidate "law" that explains the data (Newton's law is a regression model on
  [*m*₁, *m*₂, *r*]). Learning = choosing among hypotheses using data (§1.6).
- **Learned bias vs learning bias** (§1.5) — learned bias comes from the data seen (the word "doctor");
  **learning (inductive) bias** is a built-in constraint of the algorithm that makes learning possible and
  causes characteristic errors (optical illusions).

## Module 2 — k-Nearest Neighbors and basic ML notions

- **Memory-based learning** (§2.1) — predict for a new object by recalling similar stored objects.
- **Distance as inverse similarity** (§2.2) — small distance = high similarity.
  - **Euclidean** (ℓ₂), **Manhattan** (ℓ₁), the **Minkowski** ℓₚ family; the choice is a design decision.
  - **Kernel** — a function that turns a distance into a similarity; the **Gaussian kernel**
    exp(−‖x−x′‖² / 2σ²) is the standard example. (Quiz: kernels measure *similarity*, not distance.)
- **k-Nearest Neighbors** (§2.4) — find the *k* closest training points; predict the **majority label**.
  Variant: weight votes by inverse distance.
- **Hyperparameter** (§2.5) — a setting fixed *before* learning that changes which algorithm you get:
  *k*, the distance, the voting rule. Contrast with **parameters**, which learning sets (Module 3).
  - The notes' word "hyperalgorithm": one recipe, many algorithms, one per hyperparameter setting.
- **Train / test split** (§2.6) — hold out a random **test set** as a proxy for unseen data; the rest is the
  **training set**. (A **validation set** will be added later.) `train_test_split`, `stratify`, `random_state`.
- **Overfitting, underfitting, generalization** (§2.7)
  - *k* = 1 is perfect on training data and fragile on new data → **overfitting**; one mislabelled point
    poisons a whole region.
  - Very large *k* ignores the data → **underfitting**.
  - Moving *k* is moving the **learning bias**; the goal is to **generalize**.
- **Decision regions and decision boundary** (§2.11) — visualized by *querying the classifier on a grid of
  points and colouring each* (quiz question). `plot_decision_regions`.
- **Feature scaling** (§2.10, motivated in §3.7.2) — `StandardScaler`: subtract the mean, divide by the
  standard deviation, fit on the training set only.
- **Efficiency** (§2.8) — naive kNN reads the whole memory per query: O(*d n*) time; special data structures
  give O(*d* log *n*) queries after expensive preprocessing. ML algorithms have computational costs too.
- **scikit-learn habits** (§2.9–2.12) — `fit` / `predict`; "the manual is your friend".
- **kNN regression** (§2.12) — predict the (distance-weighted) **average** of the neighbours' values;
  many algorithms have both a classification and a regression version.

## Module 3 — Linear regression, gradient descent, feature engineering

### The model and the loss
- **Parametric learning** (§3.1) — assume a form, here the line **y = ax + b**; the **parameters** *a*, *b*
  are what learning must find. The equation is an infinite family of hypotheses.
- **Error / residual** eᵢ = |f(Xᵢ) − yᵢ| (§3.2); the **loss function** aggregates the errors over the data set.
- **Mean squared error (MSE)** L(a, b) = (1/n) Σ eᵢ² — the loss depends only on *a*, *b* once the data is fixed.
- **Why MSE** (§3.2.1) — the surface L(a, b) is **convex**: one minimum, no other dips; it is **smooth**
  (differentiable). **Level sets**: the curves where L is constant.
  → *Demo: The loss landscape, "Toy line".*

### Gradient descent
- **Derivative as a rate of change**; its **sign** says whether the function is rising (§3.3.1).
- **Update rule** x ← x − ρ·f′(x); **step size / learning rate ρ**.
  Exercise from the notes: what happens for ρ too small, too large, ρ = 1 on y = x²?
- **Partial derivative** (§3.3.2) — the rate of change along one axis with the others held fixed.
- **Gradient** and **gradient descent in several variables** (§3.3.3) — one update per parameter;
  together they move in the direction of steepest descent.
  → *Demo: the black arrow is −∇L; "step downhill" applies the update rule.*
- **GD as a learning algorithm** (§3.4) — learn from mistakes, repeat; ρ as how fast one adapts.
- **The update rules for MSE** (§3.5):
  a ← a − ρ Σⱼ (ŷⱼ − yⱼ) Xⱼ,  b ← b − ρ Σⱼ (ŷⱼ − yⱼ), with ŷⱼ = aXⱼ + b the current prediction.
  Point out where each factor comes from (chain rule on eⱼ²).
- **Hyperplane** (§3.6) — the line's analogue in *d* dimensions: y = b + x·wᵀ; **intercept** *b*,
  **weight vector** *w*; each weight has the same update rule, using its own coordinate.

### Running it
- **Epoch** (§3.7) — one pass over the whole data set; **nepochs** is a hyperparameter.
- **Random initialization** and **`random_state`** — reproducibility of randomness.
- **The optimizer is a hyperparameter** — gradient descent is one of several ways to minimize the loss
  (quiz question).
- **Batch / batch size k** (§3.7.1) — shuffle the data, cut it into n/k batches, one update per batch with
  the *same* update rule on *fewer points*. A batch is a **proxy** for the whole data set.
  → *Demo: A batch stands in for the data, view 1: a batch's own best line vs the all-days line.*
- **Stochastic (mini-batch) gradient descent** — the resulting algorithm; **SGD** proper is k = 1.
  - The output depends on the order/shuffle of the points (quiz: order matters for SGD, not for full GD).
  - More updates per epoch, each noisier; slower per epoch, often fewer epochs.
  → *Demo, view 2: red arrow = the step the batch chose, black arrow = the step all the data would take.*
- **Feature scaling for faster learning** (§3.7.2) — standardize each attribute (μᵢ, σᵢ); it reshapes the
  loss landscape so one step size works along every axis.
  → *Demo: The loss landscape, "Newark, raw °F" vs "Newark, scaled" — same bowl, one is a razor valley.*

### Evaluating and extending
- **Loss on the test set** is not expected to be smaller than on the training set (quiz question).
- **Coefficient of determination R²** (§3.8) = 1 − SE_model / SE_base, where the **baseline model** predicts
  mean(y). Scale-invariant; 1 is perfect, 0 is the baseline, negative is worse than the baseline.
- **Outliers** and **RANSAC** (§3.9) — sample n′ points, fit, count **inliers** under a loss threshold θ,
  accept if more than n″, refit on the inliers.
- **Feature engineering** (§3.10) — add transformed features so a linear model can fit non-linear data
  (moving averages and bands on the S&P index).
- **Polynomial regression** (§3.11) — add the monomials (x₁², x₁x₂, …); quadratic regression *is* linear
  regression on the enlarged point x̃. Cost: more features.

---

## Suggested flow for the session (≈75 min)

1. **Warm-up on vocabulary** (10 min) — supervised / classification vs regression / X, y, d, n /
   hyperparameter vs parameter. Ask for kNN examples of each.
2. **kNN and generalization** (10 min) — k = 1 memorizes; large k ignores; test set as proxy.
3. **The loss surface** (15 min) — open *The loss landscape*, toy line. Show level sets, the two slopes,
   fog on: "this is all gradient descent ever knows". Step downhill with three step sizes.
4. **The batch idea** (25 min) — open *A batch stands in for the data*. View 1: k = 4, 64, 1024, the cloud
   shrinks. View 2: k = 1 vs k = 64 vs all, arrows and the loss curve; epoch as one pass.
   Connect to the pseudocode in §3.7.1 line by line.
5. **Scaling** (10 min) — back to the landscape, Newark raw vs scaled; why standardize.
6. **Quiz Q03 debrief** (5 min) — order of points (GD vs SGD), optimizer as hyperparameter, test loss.
