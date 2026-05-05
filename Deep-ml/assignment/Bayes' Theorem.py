# https://www.scaler.com/academy/mentee-dashboard/class/417082/homework/problems/14813?navref=cl_tt_nv

import numpy as np


def solve(prior, positive_covid, positive_not_covid):
    # Convert string inputs to floats as requested
    p_covid = float(prior)
    p_pos_given_covid = float(positive_covid)
    p_pos_given_not_covid = float(positive_not_covid)

    # 1. Calculate the probability of NOT having covid: P(~covid)
    p_not_covid = 1 - p_covid

    # 2. Calculate the numerator: P(positive|covid) * P(covid)
    numerator = p_pos_given_covid * p_covid

    # 3. Calculate total probability of testing positive: P(positive)
    # P(pos) = [P(pos|covid) * P(covid)] + [P(pos|~covid) * P(~covid)]
    p_positive = numerator + (p_pos_given_not_covid * p_not_covid)

    # 4. Apply Bayes' Theorem
    ans = numerator / p_positive

    # Return the answer rounded to three decimal places using numpy
    return np.round(ans, 3)

# Example usage based on sample input:
# solve("0.6", "0.9", "0.1") -> returns 0.931