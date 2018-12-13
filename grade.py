def grade_marks(marks):
    if isinstance(marks, list):

        for mark in marks:
            if mark >= 90 and mark <= 100:
                print("your mark {} is Excellent".format(mark))
            elif mark >= 70 and mark <= 89:
                print("your mark {} is very good".format(mark))
            elif mark >= 60 and mark <= 69:
                print("your mark {} is good".format(mark))
            elif mark >= 40 and mark <= 59:
                print("your mark {} is poor".format(mark))
            elif mark >= 20 and mark <= 39:
                print("your mark {} is very poor".format(mark))
            else:
                print("repeat")
    else:
        print("Marks must be a list")


grade_marks([23, 4, 5, 6, 64, 90, 67, 98, 45, 23, 67, 78, 89])
