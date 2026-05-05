# https://www.scaler.com/academy/mentee-dashboard/class/417082/assignment/problems/25986?navref=cl_tt_nv

import numpy as np
import pandas as pd


def class_priors(df):
    # We assume the column name for labels is 'author' based on the problem context

    # Finding number of EAP entries
    eap = len(df[df['author'] == 'EAP'])

    # Finding number of HPL entries
    hpl = len(df[df['author'] == 'HPL'])

    # Finding number of MWS entries
    mws = len(df[df['author'] == 'MWS'])

    # Total number of entries in the dataset
    total_entries = len(df)

    # Class Prior for EAP (count of EAP / total)
    class_prior_eap = eap / total_entries

    # Class Prior for HPL (count of HPL / total)
    class_prior_hpl = hpl / total_entries

    # Class Prior for MWS (count of MWS / total)
    class_prior_mws = mws / total_entries

    return (class_prior_eap, class_prior_hpl, class_prior_mws)