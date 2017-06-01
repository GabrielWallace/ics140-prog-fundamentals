def calc_areas():
    rec_1_len = eval(input("Please Enter the length of the first rectangle: "))
    rec_1_wid = eval(input("Please Enter the width of the first rectangle: "))

    rec_2_len = eval(input("Please Enter the length of the s rectangle: "))
    rec_2_wid = eval(input("Please Enter the length of the first rectangle: "))

    rec_one_area = rec_1_len * rec_1_wid
    rec_two_area = rec_2_len * rec_2_wid

    if rec_one_area <= 0 or rec_two_area <= 0:
        print("Negative values and zeros not allowed.  Please try again.")
        calc_areas()
    if rec_one_area > rec_two_area:
        print("Rectangle One has a greater area", rec_one_area)
    elif rec_one_area == rec_two_area:
        print("The areas of the rectangles are equal", rec_one_area, rec_two_area)
    else:
        print("Rectangle Two has a greater area", rec_two_area)
calc_areas()