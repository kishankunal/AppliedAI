#https://www.scaler.com/academy/mentee-dashboard/class/424891/assignment/problems/253595?navref=cl_tt_nv

def find_elbow(wcss_values):
    k = len(wcss_values)

    if k <= 2:
        return 1

    max_drop = -1

    elbow_index = 0

    for i in range(k-1):
        current_drop = wcss_values[i] - wcss_values[i+1]
        if current_drop > max_drop:
            max_drop = current_drop
            elbow_index = i

    return elbow_index+1