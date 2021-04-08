import random
from AA_Tree import AATree
import time
import matplotlib.pyplot as plt


def gen_tests(n):
    # generates 10 tests of size n with name "test{n}_{cnt}.txt" in folder tests
    for i in range(10):
        f = open("tests/test" + str(n) + "_" + str(i+1) + ".txt", "w")
        f.write(str(n) + "\n")
        cur_list = []
        for j in range(n):
            cur_list.append(j+1)

        random.shuffle(cur_list)
        for x in cur_list:
            f.write(str(x) + " ")

        f.write("\n")

        random.shuffle(cur_list)
        for x in cur_list:
            f.write(str(x) + " ")

        f.close()

        if n == 10000000:
            break


def execute_tests(n):
    with open("results.txt","a") as f_out:
        f_out.write("n = " + str(n) + "\n")

        for i in range(10):
            with open("tests/test" + str(n) + "_" + str(i+1) + ".txt", "r") as f_in:
                temp_n = int(f_in.readline())
                to_add_list = f_in.readline().split()
                to_remove_list = f_in.readline().split()

                start = time.process_time()

                tree = AATree()

                for x in to_add_list:
                    tree.insert(x)

                for x in to_remove_list:
                    tree.remove(x)

                end = time.process_time()

                f_out.write(str(end-start) + " ")

            if n == 10000000:
                break

        f_out.write("\n\n")





# p = 10
# while p <= 1000000:
#     # gen_tests(p)
#     execute_tests(p)
#     p *= 10


n = [10, 100, 1000, 10000, 100000, 1000000]
mean_time = [0.0001121, 0.0023358, 0.0327708, 0.421958, 5.9872299, 85.3782082]
mean_time_scaled = []
for i in range(6):
    mean_time_scaled.append(mean_time[i]/n[i])

plt.plot(n, mean_time_scaled)
plt.savefig("results.png")
# plt.show()






