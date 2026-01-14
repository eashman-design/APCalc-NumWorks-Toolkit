"""
Derivative Toolkit for AP Calculus AB

Educational Goal:
This script provides a rule-based derivative toolkit that teaches students
standard differentiation rules through step-by-step explanations. Each
computation shows the rule applied, the resulting derivative, and a
conceptual interpretation of what the derivative represents.

Supported Rules:
- Power Rule: f(x) = a * x^n
- Sum/Difference Rule: two-term polynomials only
- Trigonometric: sin(x), cos(x), tan(x)
- Exponential/Logarithmic: e^x, ln(x)
- Chain Rule: restricted to linear (ax+b) or power (x^n) inner functions

Optional point evaluation allows students to compute the derivative value
at a specific x and understand it as the instantaneous rate of change.
"""

import math


# =============================================================================
# FORMATTING HELPERS
# =============================================================================

def format_coef(c, is_first=True, show_one=False):
    """Format a coefficient for display."""
    if c == 0:
        return "0"
    if is_first:
        if c == 1 and not show_one:
            return ""
        if c == -1 and not show_one:
            return "-"
        return str(c) if c == int(c) else str(c)
    else:
        # Not first term: show + or -
        if c == 1 and not show_one:
            return " + "
        if c == -1 and not show_one:
            return " - "
        if c > 0:
            return " + " + (str(int(c)) if c == int(c) else str(c))
        else:
            return " - " + (str(int(abs(c))) if c == int(c) else str(abs(c)))


def format_power_term(coef, exp, is_first=True):
    """Format a single power term a*x^n."""
    if coef == 0:
        return "0" if is_first else ""

    c_str = format_coef(coef, is_first, show_one=(exp == 0))

    if exp == 0:
        # Constant term
        if is_first:
            return str(int(coef)) if coef == int(coef) else str(coef)
        else:
            return c_str
    elif exp == 1:
        return c_str + "x"
    else:
        exp_str = str(int(exp)) if exp == int(exp) else str(exp)
        return c_str + "x^" + exp_str


def get_float(prompt):
    """Get a float from user input with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number.")


def get_int(prompt):
    """Get an integer from user input with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter an integer.")


def ask_evaluate():
    """Ask if user wants to evaluate at a point."""
    print()
    resp = input("Evaluate at x-value? (y/n): ")
    return resp.lower() == 'y'


def show_evaluation(deriv_func, deriv_str):
    """Evaluate derivative at a specific point."""
    x = get_float("Enter x-value: ")
    try:
        val = deriv_func(x)
        print()
        print("EVALUATION:")
        print("  f'(" + str(x) + ") = " + str(val))
        print()
        print("INTERPRETATION:")
        print("  At x = " + str(x) + ", the slope of")
        print("  the tangent line is " + str(val) + ".")
        print("  This is the instantaneous rate")
        print("  of change of f at that point.")
    except (ValueError, ZeroDivisionError) as e:
        print("Cannot evaluate: " + str(e))


# =============================================================================
# POWER RULE: f(x) = a * x^n
# =============================================================================

def power_rule():
    """
    Power Rule derivative.
    f(x) = a * x^n  =>  f'(x) = a * n * x^(n-1)
    """
    print()
    print("=== POWER RULE ===")
    print("f(x) = a * x^n")
    print()

    a = get_float("Enter coefficient a: ")
    n = get_float("Enter exponent n: ")

    # Compute derivative coefficients
    # f'(x) = a*n * x^(n-1)
    deriv_coef = a * n
    deriv_exp = n - 1

    # Format original function
    f_str = format_power_term(a, n, is_first=True)
    if f_str == "":
        f_str = "x^" + str(n)

    # Format derivative
    if deriv_coef == 0:
        deriv_str = "0"
    else:
        deriv_str = format_power_term(deriv_coef, deriv_exp, is_first=True)
        if deriv_str == "":
            deriv_str = "1"

    print()
    print("STEPS:")
    print("  1. Identify: f(x) = " + f_str)
    print("  2. Power Rule states:")
    print("     d/dx[x^n] = n * x^(n-1)")
    print("  3. With coefficient a:")
    print("     d/dx[a*x^n] = a*n * x^(n-1)")
    print("  4. Substituting a=" + str(a) + ", n=" + str(n) + ":")
    print("     f'(x) = " + str(a) + "*" + str(n) + " * x^(" + str(n) + "-1)")
    print("     f'(x) = " + str(deriv_coef) + " * x^" + str(deriv_exp))

    print()
    print("RESULT:")
    print("  f'(x) = " + deriv_str)

    print()
    print("INTERPRETATION:")
    print("  The derivative " + deriv_str + " gives the")
    print("  slope of the tangent line to f(x)")
    print("  at any point x. It represents the")
    print("  instantaneous rate of change of f.")

    # Optional evaluation
    if ask_evaluate():
        def deriv_func(x):
            if deriv_exp < 0 and x == 0:
                raise ValueError("undefined at x=0")
            return deriv_coef * (x ** deriv_exp)
        show_evaluation(deriv_func, deriv_str)


# =============================================================================
# SUM/DIFFERENCE RULE: EXACTLY TWO TERMS
# f(x) = a1*x^n1 + a2*x^n2
# =============================================================================

def sum_difference_rule():
    """
    Sum/Difference Rule for exactly two power terms.
    f(x) = a1*x^n1 + a2*x^n2
    f'(x) = a1*n1*x^(n1-1) + a2*n2*x^(n2-1)
    """
    print()
    print("=== SUM/DIFFERENCE RULE ===")
    print("Two-term polynomial:")
    print("f(x) = a1*x^n1 + a2*x^n2")
    print()
    print("Enter Term 1 (a1 * x^n1):")
    a1 = get_float("  Coefficient a1: ")
    n1 = get_float("  Exponent n1: ")

    print()
    print("Enter Term 2 (a2 * x^n2):")
    print("  (Use negative a2 for subtraction)")
    a2 = get_float("  Coefficient a2: ")
    n2 = get_float("  Exponent n2: ")

    # Compute derivative of each term using power rule
    # Term 1: d/dx[a1*x^n1] = a1*n1*x^(n1-1)
    d1_coef = a1 * n1
    d1_exp = n1 - 1

    # Term 2: d/dx[a2*x^n2] = a2*n2*x^(n2-1)
    d2_coef = a2 * n2
    d2_exp = n2 - 1

    # Format original function
    term1_str = format_power_term(a1, n1, is_first=True)
    term2_str = format_power_term(a2, n2, is_first=False)
    f_str = term1_str + term2_str

    # Format derivative terms
    d1_str = format_power_term(d1_coef, d1_exp, is_first=True)
    d2_str = format_power_term(d2_coef, d2_exp, is_first=False)

    # Handle zero cases
    if d1_coef == 0 and d2_coef == 0:
        deriv_str = "0"
    elif d1_coef == 0:
        deriv_str = format_power_term(d2_coef, d2_exp, is_first=True)
    elif d2_coef == 0:
        deriv_str = d1_str
    else:
        deriv_str = d1_str + d2_str

    if deriv_str == "":
        deriv_str = "0"

    print()
    print("STEPS:")
    print("  1. Identify: f(x) = " + f_str)
    print()
    print("  2. Sum/Difference Rule states:")
    print("     d/dx[f + g] = f' + g'")
    print("     Derivatives distribute over +/-")
    print()
    print("  3. Apply Power Rule to each term:")
    print()
    print("     Term 1: d/dx[" + term1_str + "]")
    print("       = " + str(a1) + "*" + str(n1) + "*x^(" + str(n1) + "-1)")
    print("       = " + format_power_term(d1_coef, d1_exp, True))
    print()
    print("     Term 2: d/dx[" + format_power_term(a2, n2, True) + "]")
    print("       = " + str(a2) + "*" + str(n2) + "*x^(" + str(n2) + "-1)")
    print("       = " + format_power_term(d2_coef, d2_exp, True))
    print()
    print("  4. Combine the derivatives:")

    print()
    print("RESULT:")
    print("  f'(x) = " + deriv_str)

    print()
    print("INTERPRETATION:")
    print("  The derivative of a sum (or difference)")
    print("  equals the sum (or difference) of the")
    print("  derivatives. Each term is differentiated")
    print("  independently using the Power Rule.")
    print("  The result gives the slope of f(x)")
    print("  at any point x.")

    # Optional evaluation
    if ask_evaluate():
        def deriv_func(x):
            val1 = d1_coef * (x ** d1_exp) if d1_coef != 0 else 0
            val2 = d2_coef * (x ** d2_exp) if d2_coef != 0 else 0
            return val1 + val2
        show_evaluation(deriv_func, deriv_str)


# =============================================================================
# TRIGONOMETRIC DERIVATIVES: sin(x), cos(x), tan(x)
# =============================================================================

def trig_derivative():
    """
    Trigonometric derivatives.
    d/dx[sin(x)] = cos(x)
    d/dx[cos(x)] = -sin(x)
    d/dx[tan(x)] = sec^2(x)
    """
    print()
    print("=== TRIGONOMETRIC DERIVATIVES ===")
    print()
    print("Select function:")
    print("  1. sin(x)")
    print("  2. cos(x)")
    print("  3. tan(x)")
    print()

    choice = get_int("Enter choice (1-3): ")

    if choice == 1:
        # d/dx[sin(x)] = cos(x)
        f_str = "sin(x)"
        deriv_str = "cos(x)"
        rule_text = "d/dx[sin(x)] = cos(x)"

        def deriv_func(x):
            return math.cos(x)

        interp = "The derivative of sin(x) is cos(x).\n" \
                 "  When sin(x) is increasing, cos(x) > 0.\n" \
                 "  When sin(x) is decreasing, cos(x) < 0.\n" \
                 "  At max/min of sin, cos(x) = 0."

    elif choice == 2:
        # d/dx[cos(x)] = -sin(x)
        f_str = "cos(x)"
        deriv_str = "-sin(x)"
        rule_text = "d/dx[cos(x)] = -sin(x)"

        def deriv_func(x):
            return -math.sin(x)

        interp = "The derivative of cos(x) is -sin(x).\n" \
                 "  The negative sign reflects that\n" \
                 "  cos decreases when sin is positive\n" \
                 "  (in the first quadrant)."

    elif choice == 3:
        # d/dx[tan(x)] = sec^2(x)
        f_str = "tan(x)"
        deriv_str = "sec^2(x)"
        rule_text = "d/dx[tan(x)] = sec^2(x)"

        def deriv_func(x):
            c = math.cos(x)
            if abs(c) < 1e-10:
                raise ValueError("undefined (asymptote)")
            return 1 / (c * c)

        interp = "The derivative of tan(x) is sec^2(x).\n" \
                 "  Since sec^2(x) is always positive,\n" \
                 "  tan(x) is always increasing on\n" \
                 "  its domain (between asymptotes)."

    else:
        print("Invalid choice.")
        return

    print()
    print("STEPS:")
    print("  1. Identify: f(x) = " + f_str)
    print("  2. Trig derivative rule:")
    print("     " + rule_text)
    print("  3. Apply directly:")
    print("     f'(x) = " + deriv_str)

    print()
    print("RESULT:")
    print("  f'(x) = " + deriv_str)

    print()
    print("INTERPRETATION:")
    print("  " + interp)

    # Optional evaluation
    if ask_evaluate():
        show_evaluation(deriv_func, deriv_str)


# =============================================================================
# EXPONENTIAL AND LOGARITHMIC DERIVATIVES: e^x, ln(x)
# =============================================================================

def exp_log_derivative():
    """
    Exponential and logarithmic derivatives.
    d/dx[e^x] = e^x
    d/dx[ln(x)] = 1/x
    """
    print()
    print("=== EXPONENTIAL / LOGARITHMIC ===")
    print()
    print("Select function:")
    print("  1. e^x")
    print("  2. ln(x)")
    print()

    choice = get_int("Enter choice (1-2): ")

    if choice == 1:
        # d/dx[e^x] = e^x
        f_str = "e^x"
        deriv_str = "e^x"
        rule_text = "d/dx[e^x] = e^x"

        def deriv_func(x):
            return math.exp(x)

        interp = "The derivative of e^x is itself!\n" \
                 "  This unique property makes e^x\n" \
                 "  fundamental in calculus. The rate\n" \
                 "  of growth equals the current value."

    elif choice == 2:
        # d/dx[ln(x)] = 1/x
        f_str = "ln(x)"
        deriv_str = "1/x"
        rule_text = "d/dx[ln(x)] = 1/x"

        def deriv_func(x):
            if x <= 0:
                raise ValueError("ln undefined for x <= 0")
            return 1 / x

        interp = "The derivative of ln(x) is 1/x.\n" \
                 "  For x > 0, this is always positive,\n" \
                 "  so ln(x) is always increasing.\n" \
                 "  The slope decreases as x grows."

    else:
        print("Invalid choice.")
        return

    print()
    print("STEPS:")
    print("  1. Identify: f(x) = " + f_str)
    print("  2. Standard derivative rule:")
    print("     " + rule_text)
    print("  3. Apply directly:")
    print("     f'(x) = " + deriv_str)

    print()
    print("RESULT:")
    print("  f'(x) = " + deriv_str)

    print()
    print("INTERPRETATION:")
    print("  " + interp)

    # Optional evaluation
    if ask_evaluate():
        show_evaluation(deriv_func, deriv_str)


# =============================================================================
# CHAIN RULE (RESTRICTED)
# Outer: power, trig, exp, log
# Inner: linear (ax+b) or power (x^n) only
# =============================================================================

def chain_rule():
    """
    Chain Rule with restricted inner functions.
    f(g(x)) => f'(g(x)) * g'(x)

    Inner functions allowed:
      - Linear: g(x) = ax + b
      - Power: g(x) = x^n

    Outer functions allowed:
      - Power: u^m
      - Trig: sin(u), cos(u), tan(u)
      - Exponential: e^u
      - Logarithmic: ln(u)
    """
    print()
    print("=== CHAIN RULE ===")
    print("f(g(x)) => f'(g(x)) * g'(x)")
    print()

    # Select outer function
    print("Select OUTER function f(u):")
    print("  1. u^m (power)")
    print("  2. sin(u)")
    print("  3. cos(u)")
    print("  4. tan(u)")
    print("  5. e^u")
    print("  6. ln(u)")
    print()
    outer = get_int("Enter choice (1-6): ")

    if outer < 1 or outer > 6:
        print("Invalid choice.")
        return

    # Get power exponent if needed
    m = None
    if outer == 1:
        m = get_float("Enter exponent m: ")

    print()
    # Select inner function
    print("Select INNER function g(x):")
    print("  1. Linear: ax + b")
    print("  2. Power: x^n")
    print()
    inner = get_int("Enter choice (1-2): ")

    if inner < 1 or inner > 2:
        print("Invalid choice.")
        return

    # Get inner function parameters
    if inner == 1:
        # Linear: g(x) = ax + b
        a = get_float("Enter a (coefficient of x): ")
        b = get_float("Enter b (constant): ")

        # g(x) = ax + b
        # g'(x) = a
        def g(x):
            return a * x + b

        def g_prime(x):
            return a

        g_prime_val = a  # constant

        # Format g(x)
        if b == 0:
            if a == 1:
                g_str = "x"
            elif a == -1:
                g_str = "-x"
            else:
                g_str = str(a) + "x"
        else:
            if a == 1:
                a_str = "x"
            elif a == -1:
                a_str = "-x"
            else:
                a_str = str(a) + "x"

            if b > 0:
                g_str = a_str + " + " + str(b)
            else:
                g_str = a_str + " - " + str(abs(b))

        g_prime_str = str(a)
        inner_type = "linear"

    else:
        # Power: g(x) = x^n
        n = get_float("Enter exponent n: ")

        # g(x) = x^n
        # g'(x) = n * x^(n-1)
        def g(x):
            return x ** n

        def g_prime(x):
            return n * (x ** (n - 1))

        g_str = "x^" + str(n)
        g_prime_str = str(n) + "*x^" + str(n - 1)
        inner_type = "power"
        # Store n for later
        g_prime_val = None  # not constant

    # Build outer function and its derivative
    if outer == 1:
        # Power: f(u) = u^m, f'(u) = m*u^(m-1)
        f_of_u = "u^" + str(m)
        f_prime_of_u = str(m) + "*u^" + str(m - 1)

        def f(u):
            return u ** m

        def f_prime(u):
            return m * (u ** (m - 1))

        outer_type = "power"

    elif outer == 2:
        # sin(u)
        f_of_u = "sin(u)"
        f_prime_of_u = "cos(u)"

        def f(u):
            return math.sin(u)

        def f_prime(u):
            return math.cos(u)

        outer_type = "sin"

    elif outer == 3:
        # cos(u)
        f_of_u = "cos(u)"
        f_prime_of_u = "-sin(u)"

        def f(u):
            return math.cos(u)

        def f_prime(u):
            return -math.sin(u)

        outer_type = "cos"

    elif outer == 4:
        # tan(u)
        f_of_u = "tan(u)"
        f_prime_of_u = "sec^2(u)"

        def f(u):
            return math.tan(u)

        def f_prime(u):
            c = math.cos(u)
            if abs(c) < 1e-10:
                raise ValueError("undefined (asymptote)")
            return 1 / (c * c)

        outer_type = "tan"

    elif outer == 5:
        # e^u
        f_of_u = "e^u"
        f_prime_of_u = "e^u"

        def f(u):
            return math.exp(u)

        def f_prime(u):
            return math.exp(u)

        outer_type = "exp"

    else:  # outer == 6
        # ln(u)
        f_of_u = "ln(u)"
        f_prime_of_u = "1/u"

        def f(u):
            if u <= 0:
                raise ValueError("ln undefined for u <= 0")
            return math.log(u)

        def f_prime(u):
            if u <= 0:
                raise ValueError("ln undefined for u <= 0")
            return 1 / u

        outer_type = "ln"

    # Compose: F(x) = f(g(x))
    f_composed = f_of_u.replace("u", "(" + g_str + ")")

    # Derivative: F'(x) = f'(g(x)) * g'(x)
    f_prime_at_g = f_prime_of_u.replace("u", "(" + g_str + ")")

    # Build the derivative string
    deriv_str = f_prime_at_g + " * " + g_prime_str

    # Simplify for linear inner function with constant g'(x) = a
    if inner == 1:  # linear
        # g'(x) = a, so we can simplify
        if a == 1:
            deriv_str = f_prime_at_g
        elif a == -1:
            # Multiply by -1
            if outer_type == "cos":
                deriv_str = "sin(" + g_str + ")"
            else:
                deriv_str = "-" + f_prime_at_g
        else:
            deriv_str = str(a) + " * " + f_prime_at_g

    print()
    print("STEPS:")
    print("  1. Identify composite function:")
    print("     F(x) = " + f_composed)
    print()
    print("  2. Outer function: f(u) = " + f_of_u)
    print("     Inner function: g(x) = " + g_str)
    print()
    print("  3. Chain Rule states:")
    print("     d/dx[f(g(x))] = f'(g(x)) * g'(x)")
    print()
    print("  4. Find f'(u):")
    print("     f'(u) = " + f_prime_of_u)
    print()
    print("  5. Find g'(x):")
    print("     g'(x) = " + g_prime_str)
    print()
    print("  6. Apply Chain Rule:")
    print("     F'(x) = f'(g(x)) * g'(x)")
    print("     F'(x) = " + f_prime_at_g + " * " + g_prime_str)

    print()
    print("RESULT:")
    print("  F'(x) = " + deriv_str)

    print()
    print("INTERPRETATION:")
    print("  The Chain Rule decomposes the rate of")
    print("  change of a composition into the product")
    print("  of two rates: how fast the outer function")
    print("  changes with respect to the inner (f'),")
    print("  times how fast the inner changes with")
    print("  respect to x (g'). This is the 'chain'")
    print("  connecting the derivatives.")

    # Optional evaluation
    if ask_evaluate():
        def deriv_func(x):
            u = g(x)
            return f_prime(u) * g_prime(x)
        show_evaluation(deriv_func, deriv_str)


# =============================================================================
# MAIN MENU
# =============================================================================

def main():
    """Main menu loop for Derivative Toolkit."""
    while True:
        print()
        print("================================")
        print("  DERIVATIVE TOOLKIT")
        print("  AP Calculus AB")
        print("================================")
        print()
        print("Select an option:")
        print("  1. Power Rule")
        print("  2. Sum/Difference (two-term)")
        print("  3. Trigonometric")
        print("  4. Exponential / Logarithmic")
        print("  5. Chain Rule")
        print("  6. Exit")
        print()

        choice = get_int("Enter choice (1-6): ")

        if choice == 1:
            power_rule()
        elif choice == 2:
            sum_difference_rule()
        elif choice == 3:
            trig_derivative()
        elif choice == 4:
            exp_log_derivative()
        elif choice == 5:
            chain_rule()
        elif choice == 6:
            print()
            print("Exiting Derivative Toolkit.")
            print("Keep practicing calculus!")
            break
        else:
            print("Invalid choice. Enter 1-6.")


# Entry point
if __name__ == "__main__":
    main()
