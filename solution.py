import pandas as pd
import numpy as np


chat_id = 704471350

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    a1 = x_success
    a2 = y_success
    b1 = x_cnt
    b2 = y_cnt
    S = a1+a2+b1+b2

    f_11 = ((a1+a2)*(a1+b1))/S
    f_12 = ((a1+a2)*(a2+b2))/S
    f_21 = ((b1+b2)*(a1+b1))/S
    f_22 = ((b1+b2)*(a2+b2))/S

    chi2 = ( ((a1-f_11)**2)/f_11 ) + ( ((a2-f_12)**2)/f_12 ) + ( ((b1-f_21)**2)/f_21 ) + ( ((b2-f_22)**2)/f_22 )

    chi2_crit = 5.412
    if chi2 < chi2_crit:
      res = False
    else:
      res = True

    return res
