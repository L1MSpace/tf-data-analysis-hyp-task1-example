from math import sqrt
from scipy.stats import norm

chat_id = 704471350

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:

    a1 = x_success
    b1 = x_cnt
    a2 = y_success
    b2 = y_cnt
    frac_a1b1 = a1 / b1
    frac_a2b2 = a2 / b2

    stan_error = sqrt( (frac_a1b1 * (1-frac_a1b1)/b1) + (frac_a2b2 * (1-frac_a2b2)/b2) )

    z_test = (frac_a2b2 - frac_a1b1) / stan_error
    z_crit = norm.ppf(1 - 0.02)
    res = z_test > z_crit

    return res
