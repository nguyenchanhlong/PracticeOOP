import random

# who go fisrt
lst = [1,2]
rand = random.choice(lst)

# The all space number in the caro table
lst_space = [1,2,3,4,5,6,7,8,9]
lst2 = [1,2,3,4,5,6,7,8,9]
# List the number User choice
lst_u = []
# List the number Boot choice
lst_b = []

lst_r_u = []
lst_r_b = []

# List of Rule
common_elements_u = {}
common_elements_b = {}
lst_r_u_u = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
lst_r_b_b = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]


class BC:
    def __init__(self):
        self.user = None
        self.boot = None
    def main(self):
        while True:
            if rand == 1:
                print('User first')
                for element in range(len(lst_space)):
                    self.user = int(input(f'Please input your choice with the number{lst_space}: '))
                    self.boot = random.choice(lst_space)
                    print('User choice space: ',self.user)
                    lst_u.append(self.user)
                    lst_b.append(self.boot)
                    if self.boot != self.user:
                        print('Boot choice space: ',self.boot)
                    for i in lst_space:
                        if i == self.user:
                            lst_space.remove(self.user)
                    if self.boot == self.user:
                        if lst_space == []:
                            print('None')
                            break
                        else:
                            self.boot = random.choice(lst_space)
                        print('Boot choice space:',self.boot)
                    for j in lst_space:
                        if j == self.boot:
                            lst_space.remove(self.boot)
            else:
                print('Boot first')
                for element in range(len(lst_space)):
                    self.boot = random.choice(lst_space)
                    lst_b.append(self.boot)
                    print('Boot choice space: ',self.boot)
                    for j in lst_space:
                        if j == self.boot:
                            lst_space.remove(self.boot)
                    if lst_space == []:
                        print('None')
                        break
                    self.user = int(input(f'Please input your choice with the number{lst_space}: '))
                    lst_u.append(self.user)
                    print('User choice space: ',self.user)
                    for i in lst_space:
                        if i == self.user:
                            lst_space.remove(self.user)
                    if self.boot != self.user:
                        for i in lst_space:
                            if i == self.user:
                                lst_space.remove(self.user)
                    if self.boot == self.user:
                        self.boot = random.choice(lst_space)
                        print('Boot choice space: ',self.boot)
            break
        
class Rules:
    def find_common_elements(self,list1, list2):
        return [item for item in list1 if item in list2]
    def start(self):
        for results in lst2:
            for result in lst_u:
                if results == result:
                    lst_r_u.append(results)
        for results in lst2:
            for result in lst_b:
                if results == result:
                    lst_r_b.append(results)


        for i, lst in enumerate(lst_r_u_u, start=1):
            common_elements_u[f"lst_r_u{i}"] = [item for item in lst if item in lst_r_u]
        # Find the list(s) with the most common elements
        max_common_u = max(common_elements_u, key=lambda k: len(common_elements_u[k]))

        for i, lst in enumerate(lst_r_b_b, start=1):
            common_elements_b[f"lst_r_b{i}"] = [item for item in lst if item in lst_r_b]
        # Find the list(s) with the most common elements
        max_common_b = max(common_elements_b, key=lambda k: len(common_elements_b[k]))
        while True:
            if len(common_elements_u[max_common_u]) == 3:
                print(f"User is the winner with common elements: {common_elements_u[max_common_u]}")
                break
            elif len(common_elements_b[max_common_b]) == 3:
                print(f"Boot is the winner with common elements: {common_elements_b[max_common_b]}")
                break
            break

if __name__ == '__main__':
    b = BC()
    b.main()
    start = Rules()
    start.start()