def PointsCoverSorted(x_array):
    segments = []
    nb_points = len(x_array)
    i = 1

    while i <= nb_points:
        print(i)
        (l, r) = (x_array[i-1], x_array[i-1] +2)
        segments.append([l,r])
        i += 1                                           # if the following point is not covered by the segement
        while (i <= nb_points) and (x_array[i-1] <= r):  # if the following point is covered by the segment
            i += 1        
    
    return segments


if __name__ == '__main__':
    age_arr = map(float, input("Insert children ages in ascending order...").split())
    segments = PointsCoverSorted(age_arr)
    print("Children can be splitted into minimum {} groups of age range of 2: {}".format(len(segments), segments))
